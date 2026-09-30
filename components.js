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
      const swap = () => { const im = shots[i].querySelector('img') || shots[i]; big.src = im.dataset.full || im.currentSrc || im.src; big.alt = im.alt; count.textContent = `${i + 1} / ${shots.length}`; };
      dlg.open && document.startViewTransition && !reduceMotion ? document.startViewTransition(swap) : swap();
    };
    shots.forEach((el, k) => {
      el.addEventListener('click', () => { show(k); dlg.showModal(); });
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
    const params = new URLSearchParams(location.search);
    for (const name of ['prestation', 'personnes', 'style', 'message']) {
      const field = form.elements[name], value = params.get(name);
      if (!field || !value) continue;
      if (field.tagName === 'SELECT' && ![...field.options].some((o) => o.value === value)) continue;
      field.value = value.slice(0, 2000);
    }
    // Pas de date de mariage dans le passé.
    const day = form.querySelector('[type=date]');
    if (day) day.min = new Date().toISOString().slice(0, 10);
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('[type=submit]');
      if (form.action.includes('VOTRE_ID')) { status.textContent = this.dataset.wip; return; }
      btn.setAttribute('aria-busy', 'true');
      btn.disabled = true;
      try {
        const r = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
        if (!r.ok) throw new Error();
        form.reset();
        status.textContent = this.dataset.ok;
      } catch {
        status.textContent = this.dataset.err;
      } finally {
        btn.removeAttribute('aria-busy');
        btn.disabled = false;
      }
    });
  }
}

// Boutons − / + autour d'un champ nombre (estimateur et planning).
function wireSteppers(root, onChange) {
  root.querySelectorAll('.stepper').forEach((s) => {
    const input = s.querySelector('input');
    s.addEventListener('click', (e) => {
      const b = e.target.closest('[data-step]');
      if (!b) return;
      const v = Math.min(+input.max, Math.max(+input.min, (+input.value || 0) + +b.dataset.step));
      input.value = v;
      onChange();
    });
  });
  root.addEventListener('input', onChange);
  root.addEventListener('change', onChange);
}

const fill = (tpl, values) => tpl.replace(/\{(\w+)\}/g, (_, k) => values[k] ?? '');
const clampInput = (input) => Math.min(+input.max, Math.max(+input.min, Math.round(+input.value || 0)));

// <lyn-estimate> : total estimé en direct, et lien vers le devis pré-rempli.
class LynEstimate extends HTMLElement {
  connectedCallback() {
    // « 350 € » dans toutes les langues, comme dans le reste du site.
    const num = new Intl.NumberFormat(this.lang || 'fr', { maximumFractionDigits: 0 });
    const euro = { format: (v) => `${num.format(v)}\u00a0€` };
    const out = this.querySelector('output'), deposit = this.querySelector('.total small'), cta = this.querySelector('.btn');
    const proches = this.querySelector('#est-proches'), heures = this.querySelector('#est-retouches');
    const base = cta.getAttribute('href');
    const update = () => {
      const f = this.querySelector('[name=formule]:checked');
      const n = clampInput(proches), h = clampInput(heures);
      const total = +f.dataset.price + n * 70 + h * 60;
      out.textContent = fill(this.dataset.amount, { total: euro.format(total) });
      deposit.textContent = fill(this.dataset.deposit, { deposit: euro.format(Math.round(total * 0.3)) });
      const bride = f.value === 'mariee' || f.value === 'essai';
      const params = new URLSearchParams({
        prestation: f.value === 'essai' ? 'mariee' : f.value,
        personnes: Math.max(1, n + (bride ? 1 : 0)),
        message: fill(this.dataset.msg, { formule: f.nextElementSibling.textContent, n, h, total: euro.format(total) }),
      });
      cta.href = `${base}?${params}#devis`;
    };
    wireSteppers(this, update);
    update();
  }
}

// <lyn-dayplan> : planning de la matinée calculé à partir de l'heure de la cérémonie.
class LynDayplan extends HTMLElement {
  connectedCallback() {
    const time = new Intl.DateTimeFormat(this.lang || 'fr', { hour: '2-digit', minute: '2-digit' });
    const at = (min) => time.format(new Date(2026, 0, 1, Math.floor(min / 60), min % 60));
    const heure = this.querySelector('#tl-heure'), proches = this.querySelector('#tl-proches'), list = this.querySelector('.plan');
    const d = this.dataset;
    const update = () => {
      const [hh, mm] = (heure.value || '14:00').split(':').map(Number);
      const ceremony = hh * 60 + mm, ready = ceremony - 60, bride = ready - 75;
      const n = clampInput(proches);
      // Au-delà de cinq proches, une assistante maquille en même temps : deux personnes par créneau.
      const slots = [];
      if (n > 5) for (let i = 1; i <= n; i += 2) slots.push(i + 1 <= n ? fill(d.team, { a: i, b: i + 1 }) : fill(d.proche, { i }));
      else for (let i = 1; i <= n; i++) slots.push(fill(d.proche, { i }));
      const first = bride - slots.length * 45, arrive = first - 20;
      const rows = [[arrive, d.arrive], ...slots.map((s, k) => [first + k * 45, s]), [bride, d.bride], [ready, d.ready], [ceremony, d.cer]];
      list.replaceChildren(...rows.map(([m, label], k) => {
        const li = document.createElement('li');
        if (k === rows.length - 1) li.className = 'key';
        const t = document.createElement('time');
        t.textContent = at(m);
        li.append(t, document.createTextNode(label));
        return li;
      }));
      if (arrive < 7 * 60) {
        const li = document.createElement('li');
        li.className = 'warn';
        li.textContent = d.early;
        list.append(li);
      }
    };
    wireSteppers(this, update);
    update();
  }
}

// <lyn-quiz> : trois questions, un style proposé, et le devis pré-rempli avec ce style.
class LynQuiz extends HTMLElement {
  connectedCallback() {
    // Dans une fenêtre (page Contact) ou directement dans la page (onglet « Mon style »).
    const dlg = this.querySelector('dialog'), box = dlg || this, step = box.querySelector('.quiz-step');
    const questions = [...box.querySelectorAll('[data-q]')], results = [...box.querySelectorAll('[data-result]')];
    let answers = [];
    const show = (k, focus = true) => {
      questions.forEach((q, i) => { q.hidden = i !== k; });
      results.forEach((r) => { r.hidden = true; });
      step.textContent = fill(this.dataset.step, { i: k + 1 });
      step.hidden = false;
      if (focus) questions[k].querySelector('button').focus();
    };
    const finish = () => {
      const count = {};
      answers.forEach((v) => { count[v] = (count[v] || 0) + 1; });
      // Trois réponses différentes : « sophistiqué », le style du milieu.
      const style = Object.keys(count).find((v) => count[v] >= 2) || 'sophistique';
      questions.forEach((q) => { q.hidden = true; });
      step.hidden = true;
      const r = results.find((x) => x.dataset.result === style);
      r.hidden = false;
      r.querySelector('.btn').focus();
    };
    if (dlg) {
      this.querySelector('[data-open]').addEventListener('click', () => { answers = []; show(0); dlg.showModal(); });
      dlg.querySelector('[data-close]').addEventListener('click', () => dlg.close());
    } else {
      show(0, false);
    }
    box.addEventListener('click', (e) => {
      if (dlg && e.target === dlg) return dlg.close();
      const answer = e.target.closest('[data-v]');
      if (answer) {
        answers.push(answer.dataset.v);
        return answers.length === questions.length ? finish() : show(answers.length);
      }
      if (e.target.closest('[data-again]')) { answers = []; show(0); return; }
      // Sur la page Contact, le résultat remplit directement le champ « Style ».
      const cta = e.target.closest('.result .btn'), select = this.closest('form')?.querySelector('[name=style]');
      if (cta && select && dlg) {
        e.preventDefault();
        select.value = cta.closest('[data-result]').dataset.result;
        dlg.close();
        select.focus();
      }
    });
  }
}

// <lyn-tabs> : onglets accessibles (clavier, adresse #onglet partageable). Sans JavaScript,
// les onglets restent des liens vers chaque partie de la page.
class LynTabs extends HTMLElement {
  connectedCallback() {
    const tabs = [...this.querySelectorAll('[role=tab]')];
    const panels = tabs.map((t) => this.querySelector(`#${t.getAttribute('aria-controls')}`));
    const select = (i, { focus = false, push = true } = {}) => {
      const swap = () => tabs.forEach((t, k) => {
        const on = k === i;
        t.setAttribute('aria-selected', on);
        t.tabIndex = on ? 0 : -1;
        panels[k].hidden = !on;
      });
      document.startViewTransition && !reduceMotion && push ? document.startViewTransition(swap) : swap();
      if (focus) tabs[i].focus();
      if (push) history.replaceState(null, '', `#${panels[i].id}`);
    };
    const fromHash = () => Math.max(0, panels.findIndex((p) => `#${p.id}` === location.hash));
    this.addEventListener('click', (e) => {
      const t = e.target.closest('[role=tab]');
      if (!t) return;
      e.preventDefault();
      select(tabs.indexOf(t));
    });
    this.querySelector('[role=tablist]').addEventListener('keydown', (e) => {
      const i = tabs.indexOf(document.activeElement);
      const next = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
      if (i < 0 || next === undefined) return;
      e.preventDefault();
      select((next + tabs.length) % tabs.length, { focus: true });
    });
    addEventListener('hashchange', () => select(fromHash(), { push: false }));
    select(fromHash(), { push: false });
    // Arrivée directe sur un onglet (ex. prestations.html#budget) : on montre la barre d'onglets.
    if (location.hash && panels.some((p) => `#${p.id}` === location.hash)) this.scrollIntoView({ block: 'start' });
  }
}

customElements.define('lyn-tabs', LynTabs);
customElements.define('lyn-estimate', LynEstimate);
customElements.define('lyn-dayplan', LynDayplan);
customElements.define('lyn-quiz', LynQuiz);
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
