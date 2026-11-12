const siteUrl = (import.meta.env.SITE ?? 'https://salu-producoes.pages.dev').replace(/\/+$/, '');

export const SITE = {
  name: 'Salu Produções',
  title:
    'Salu Produções | Fotografia e Filme de Casamento em Paulínia e SP',
  description:
    'Fotografia e filme de casamento em Paulínia e todo o estado de São Paulo. Um registro honesto, bem conduzido e pensado para atravessar o tempo.',
  url: siteUrl,
  locale: 'pt-BR',
} as const;

export const CONTACT = {
  whatsapp: '5519993520172',
  whatsappDisplay: '(19) 99352-0172',
  whatsappMessage: 'Olá! Vi o site e quero um orçamento para meu casamento.',
  instagram: 'salu_producoes',
  city: 'Paulínia',
  state: 'SP',
  area: 'Paulínia e todo o estado de São Paulo',
} as const;

export const LINKS = {
  whatsapp: `https://wa.me/${CONTACT.whatsapp}?text=${encodeURIComponent(
    CONTACT.whatsappMessage,
  )}`,
  instagram: `https://instagram.com/${CONTACT.instagram}`,
} as const;

export const NAV = [
  { label: 'Portfólio', href: '/portfolio' },
  { label: 'Filmes', href: '/filmes' },
  { label: 'Pacotes', href: '/pacotes' },
  { label: 'Natal', href: '/natal' },
  { label: 'Sobre', href: '/sobre' },
] as const;
