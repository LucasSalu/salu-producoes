import PhotoSwipeLightbox from 'photoswipe/lightbox';
import 'photoswipe/style.css';

const gallery = document.getElementById('galeria');
if (gallery) {
  const lightbox = new PhotoSwipeLightbox({
    gallery: '#galeria',
    children: 'a',
    pswpModule: () => import('photoswipe'),
    bgOpacity: 0.96,
    showHideAnimationType: 'fade',
    padding: { top: 40, bottom: 40, left: 16, right: 16 },
  });
  lightbox.init();
}
