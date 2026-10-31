import fs from 'node:fs';

const PORT = 9222;
const URL = process.argv[2] ?? 'http://127.0.0.1:4321/';
const OUT_PNG = process.argv[3] ?? 'C:\\dev\\deepseek\\salu_producoes\\selecao\\full.png';
const OUT_JSON = 'C:\\dev\\deepseek\\salu_producoes\\selecao\\positions.json';

const list = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json();
const page = list.find((t) => t.type === 'page');
if (!page) throw new Error('Nenhuma aba encontrada');

const ws = new WebSocket(page.webSocketDebuggerUrl);
let seq = 0;
const pending = new Map();

function send(method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = ++seq;
    pending.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });
}

ws.onmessage = (event) => {
  const msg = JSON.parse(event.data);
  if (msg.id && pending.has(msg.id)) {
    const { resolve, reject } = pending.get(msg.id);
    pending.delete(msg.id);
    if (msg.error) reject(new Error(JSON.stringify(msg.error)));
    else resolve(msg.result);
  }
};

await new Promise((resolve) => {
  ws.onopen = resolve;
});

await send('Page.enable');
await send('Runtime.enable');
await send('Emulation.setEmulatedMedia', {
  features: [{ name: 'prefers-reduced-motion', value: 'reduce' }],
});
await send('Emulation.setDeviceMetricsOverride', {
  width: 1440,
  height: 900,
  deviceScaleFactor: 1,
  mobile: false,
});
await send('Page.navigate', { url: URL });
await new Promise((r) => setTimeout(r, 3500));

const expr = `(() => {
  const ids = ['sobre','citacao','portfolio','pacotes','processo','faq','contato'];
  const out = {};
  for (const id of ids) {
    const el = document.getElementById(id);
    if (el) out[id] = Math.round(el.getBoundingClientRect().top + window.scrollY);
  }
  out.total = Math.round(document.body.scrollHeight);
  return JSON.stringify(out);
})()`;

const res = await send('Runtime.evaluate', { expression: expr, returnByValue: true });
const positions = JSON.parse(res.result.value);
fs.writeFileSync(OUT_JSON, JSON.stringify(positions, null, 1));

const shot = await send('Page.captureScreenshot', {
  format: 'png',
  captureBeyondViewport: true,
});
fs.writeFileSync(OUT_PNG, Buffer.from(shot.data, 'base64'));

console.log('total altura:', positions.total);
console.log('secoes:', JSON.stringify(positions));
console.log('png bytes:', fs.statSync(OUT_PNG).size);
ws.close();
