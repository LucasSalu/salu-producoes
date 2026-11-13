import raw from '../data/selecionadas.json';

export interface Foto {
  n: number;
  w: number;
  h: number;
  portrait: boolean;
  variants: Record<string, string>;
}

export const fotos = raw as Foto[];

export function byNumber(n: number): Foto {
  const foto = fotos.find((f) => f.n === n);
  if (!foto) throw new Error(`Foto ${n} não encontrada na seleção`);
  return foto;
}

export function srcset(f: Foto): string {
  return Object.entries(f.variants)
    .sort((a, b) => Number(a[0]) - Number(b[0]))
    .map(([w, url]) => `${url} ${w}w`)
    .join(', ');
}

export function fallback(f: Foto, size = 960): string {
  const keys = Object.keys(f.variants)
    .map(Number)
    .sort((a, b) => a - b);
  const best = keys.find((k) => k >= size) ?? keys[keys.length - 1];
  return f.variants[best];
}

export function largest(f: Foto): string {
  const keys = Object.keys(f.variants)
    .map(Number)
    .sort((a, b) => b - a);
  return f.variants[keys[0]];
}

export function alt(f: Foto): string {
  return `Casamento registrado pela Salu Produções, foto ${String(f.n).padStart(3, '0')}`;
}
