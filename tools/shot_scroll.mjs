import fs from 'node:fs';

const PORT = 9222;
const URL = process.argv[2] ?? 'http://127.0.0.1:4321/';
const OUT = process.argv[3] ?? 'C:\\dev\\deepseek\\salu_producoes\\selecao\\scroll.png';
const Y = Number(process.argv[4] ?? '1500');

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
await new Promise((r) => setTimeout(r, 3000));
await send('Runtime.evaluate', { expression: `window.scrollTo(0, ${Y})` });
await new Promise((r) => setTimeout(r, 1200));

const shot = await send('Page.captureScreenshot', { format: 'png' });
fs.writeFileSync(OUT, Buffer.from(shot.data, 'base64'));
console.log('capturado em y=' + Y, fs.statSync(OUT).size);
ws.close();
