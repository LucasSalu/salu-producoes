import Lenis from 'lenis';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReduced) {
  const lenis = new Lenis({ lerp: 0.1, wheelMultiplier: 1 });
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });
  gsap.ticker.lagSmoothing(0);
}

function revealBlocks() {
  if (prefersReduced) return;

  document.querySelectorAll<HTMLElement>('[data-reveal]').forEach((el) => {
    gsap.fromTo(
      el,
      { y: 34, autoAlpha: 0 },
      {
        y: 0,
        autoAlpha: 1,
        duration: 0.95,
        ease: 'power3.out',
        scrollTrigger: { trigger: el, start: 'top 88%', once: true },
      },
    );
  });

  document.querySelectorAll<HTMLElement>('[data-reveal-group]').forEach((group) => {
    gsap.fromTo(
      group.children,
      { y: 26, autoAlpha: 0 },
      {
        y: 0,
        autoAlpha: 1,
        duration: 0.85,
        stagger: 0.06,
        ease: 'power3.out',
        scrollTrigger: { trigger: group, start: 'top 88%', once: true },
      },
    );
  });

  document.querySelectorAll<HTMLElement>('[data-parallax]').forEach((el) => {
    const parent = el.parentElement ?? el;
    gsap.fromTo(
      el,
      { yPercent: -3 },
      {
        yPercent: 3,
        ease: 'none',
        scrollTrigger: {
          trigger: parent,
          start: 'top bottom',
          end: 'bottom top',
          scrub: true,
        },
      },
    );
  });
}

function customCursor() {
  const cursor = document.getElementById('cursor');
  const fine = window.matchMedia('(pointer: fine)').matches;
  if (!cursor || prefersReduced || !fine) return;

  gsap.set(cursor, { xPercent: -50, yPercent: -50, x: -100, y: -100 });

  window.addEventListener('mousemove', (event) => {
    cursor.classList.add('is-visible');
    gsap.to(cursor, { x: event.clientX, y: event.clientY, duration: 0.16, ease: 'power2.out' });
  });

  document.querySelectorAll('a, button, summary').forEach((el) => {
    el.addEventListener('mouseenter', () => cursor.classList.add('is-active'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('is-active'));
  });

  document.querySelectorAll('a[data-pswp-width]').forEach((el) => {
    el.addEventListener('mouseenter', () => cursor.classList.add('is-view'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('is-view'));
  });
}

function pageTransitions() {
  if (prefersReduced) return;

  document.addEventListener('click', (event) => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const link = (event.target as Element).closest('a');
    if (!link) return;
    const href = link.getAttribute('href');
    if (!href || href.startsWith('#') || link.getAttribute('target') === '_blank') return;
    if (/^(https?:)?\/\//.test(href) || href.startsWith('mailto:')) return;

    event.preventDefault();
    document.body.classList.add('is-leaving');
    window.setTimeout(() => {
      window.location.href = href;
    }, 260);
  });

  window.addEventListener('pageshow', () => document.body.classList.remove('is-leaving'));
}

function headerState() {
  const header = document.getElementById('site-header');
  if (!header) return;
  const update = () => {
    header.classList.toggle('is-scrolled', window.scrollY > 40);
  };
  update();
  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('pageshow', update);
}

function mobileMenu() {
  const menu = document.querySelector('.mobile-menu');
  if (!(menu instanceof HTMLDetailsElement)) return;

  document.addEventListener('click', (event) => {
    if (menu.open && !menu.contains(event.target as Node)) {
      menu.open = false;
    }
  });

  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      menu.open = false;
    });
  });
}

const progress = document.getElementById('scroll-progress');
if (progress) {
  ScrollTrigger.create({
    start: 0,
    end: 'max',
    onUpdate: (self) => {
      progress.style.transform = `scaleX(${self.progress})`;
    },
  });
}

revealBlocks();
customCursor();
pageTransitions();
headerState();
mobileMenu();
