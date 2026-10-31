// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// Troque a URL abaixo pelo domínio final (ou defina a variável SITE_URL no Cloudflare)
const site = process.env.SITE_URL ?? 'https://salu-producoes.pages.dev';

export default defineConfig({
  site,
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
