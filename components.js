// Composants web du site Maison de Lyn (Custom Elements natifs, sans dépendance).

const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

// <lyn-lightbox> : visionneuse plein écran pour toutes les images [data-lightbox] de la page.
class LynLightbox extends HTMLElement {
  connectedCallback() {
    const shots = [...document.querySelectorAll('[data-lightbox]')];
    if (!shots.length) return;
    const close = this.getAttribute('label-close') || 'Fermer';
    const prev = this.getAttribute('label-prev') || 'Photo précédente';
    const next = this.getAttribute('label-next') || 'Photo suivante';
    this.innerHTML = `
      <dialog class="lightbox" aria-label="Photo">
        <img alt="">
        <button class="lb-close" aria-label="${close}">×</button>
        <button class="lb-prev" aria-label="${prev}">‹</button>
        <button class="lb-next" aria-label="${next}">›</button>
        <p class="lb-count" aria-live="polite"></p>
      </dialog>`;
    const dlg = this.querySelector('dialog'), big = dlg.querySelector('img'), count = dlg.querySelector('.lb-count');
    let i = 0, x0 = null;
    const show = (k) => {
      i = (k + shots.length) % shots.length;
      const swap = () => { big.src = shots[i].currentSrc || shots[i].src; big.alt = shots[i].alt; count.textContent = `${i + 1} / ${shots.length}`; };
      dlg.open && document.startViewTransition && !reduceMotion ? document.startViewTransition(swap) : swap();
    };
    shots.forEach((el, k) => {
      el.tabIndex = 0;
      el.setAttribute('role', 'button');
      const open = () => { show(k); dlg.showModal(); };
      el.addEventListener('click', open);
      el.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
    });
    dlg.querySelector('.lb-close').onclick = () => dlg.close();
    dlg.querySelector('.lb-prev').onclick = () => show(i - 1);
    dlg.querySelector('.lb-next').onclick = () => show(i + 1);
    dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
    dlg.addEventListener('keydown', (e) => { if (e.key === 'ArrowLeft') show(i - 1); if (e.key === 'ArrowRight') show(i + 1); });
    dlg.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
    dlg.addEventListener('touchend', (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 40) show(dx < 0 ? i + 1 : i - 1);
      x0 = null;
    });
  }
}

// <lyn-book-button> : bouton « Prendre rendez-vous » flottant sur mobile,
// visible après le premier écran et masqué quand le pied de page arrive.
class LynBookButton extends HTMLElement {
  connectedCallback() {
    const footer = document.querySelector('footer');
    let pastHero = false, atFooter = false;
    const update = () => this.toggleAttribute('visible', pastHero && !atFooter);
    addEventListener('scroll', () => { pastHero = scrollY > innerHeight * 0.6; update(); }, { passive: true });
    if (footer && 'IntersectionObserver' in window) {
      new IntersectionObserver(([e]) => { atFooter = e.isIntersecting; update(); }).observe(footer);
    }
  }
}

// <lyn-quote-form> : envoie le formulaire de devis sans recharger la page.
class LynQuoteForm extends HTMLElement {
  connectedCallback() {
    const form = this.querySelector('form'), status = this.querySelector('[role=status]');
    if (!form) return;
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('[type=submit]');
      if (form.action.includes('VOTRE_ID')) { status.textContent = this.dataset.wip; return; }
      btn.setAttribute('aria-busy', 'true');
      try {
        const r = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
        if (!r.ok) throw new Error();
        form.reset();
        status.textContent = this.dataset.ok;
      } catch {
        status.textContent = this.dataset.err;
      } finally {
        btn.removeAttribute('aria-busy');
      }
    });
  }
}

customElements.define('lyn-lightbox', LynLightbox);
customElements.define('lyn-book-button', LynBookButton);
customElements.define('lyn-quote-form', LynQuoteForm);

// Apparitions au défilement : pris en charge en CSS (animation-timeline) quand le
// navigateur le permet ; sinon, repli sur IntersectionObserver.
if (!CSS.supports('animation-timeline: view()') && 'IntersectionObserver' in window) {
  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }), { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach((el) => io.observe(el));
} else {
  document.querySelectorAll('.reveal').forEach((el) => el.classList.add('in'));
}
