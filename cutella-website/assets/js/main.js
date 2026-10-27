/* Cutella site behaviour: shared header/footer, menus, search, carousels, tabs, recipes, products */
(function () {
  const D = window.CUTELLA;
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const icon = {
    chev: '<svg viewBox="0 0 12 8" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 1l5 5 5-5"/></svg>',
    search: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
    menu: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    arrow: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    left: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M15 6l-6 6 6 6"/></svg>',
    fb: '<svg viewBox="0 0 24 24"><path d="M14 8h3V4h-3c-2.8 0-4 1.7-4 4.3V10H7v4h3v8h4v-8h3l1-4h-4V8.6c0-.4.3-.6.6-.6z"/></svg>',
    ig: '<svg viewBox="0 0 24 24"><path d="M12 7.3A4.7 4.7 0 1 0 12 16.7 4.7 4.7 0 0 0 12 7.3zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm4.9-8.9a1.1 1.1 0 1 0 0 2.2 1.1 1.1 0 0 0 0-2.2zM21 7.5c-.1-1.5-.4-2.8-1.5-3.9S17.1 2.1 15.6 2C14 2 10 2 8.4 2 6.9 2.1 5.6 2.4 4.5 3.5S3.1 5.9 3 7.4C3 9 3 13 3 14.6c.1 1.5.4 2.8 1.5 3.9s2.4 1.4 3.9 1.5c1.6.1 5.6.1 7.2 0 1.5-.1 2.8-.4 3.9-1.5s1.4-2.4 1.5-3.9c.1-1.6.1-5.6 0-7.1zm-2 8.8a3 3 0 0 1-1.7 1.7c-1.2.5-4 .4-5.3.4s-4.1.1-5.3-.4A3 3 0 0 1 5 16.3c-.5-1.2-.4-4-.4-5.3s-.1-4.1.4-5.3A3 3 0 0 1 6.7 4c1.2-.5 4-.4 5.3-.4s4.1-.1 5.3.4A3 3 0 0 1 19 5.7c.5 1.2.4 4 .4 5.3s.1 4.1-.4 5.3z"/></svg>',
    yt: '<svg viewBox="0 0 24 24"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15V9l5.8 3-5.8 3z"/></svg>',
  };
  const socials = `<a href="#" aria-label="Facebook">${icon.fb}</a><a href="#" aria-label="Instagram">${icon.ig}</a><a href="#" aria-label="YouTube">${icon.yt}</a>`;
  const logo = '<span>c</span><span>utella</span><sup>®</sup>';

  /* ---------- header ---------- */
  const header = $("#site-header");
  if (header) {
    header.outerHTML = `
    <a class="skip-link" href="#main">Skip to main content</a>
    <div class="topbar"><div class="container">
      <span class="tb-msg">Free delivery on Dunk Kits across India this October 🍪</span>
      <div class="socials">${socials}</div>
    </div></div>
    <header class="site-header"><div class="container">
      <a class="logo" href="index.html" aria-label="Cutella home">${logo}</a>
      <nav class="nav" id="nav" aria-label="Main">
        ${D.nav.map((g, i) => `
          <div class="nav__item">
            <button class="nav__link" aria-expanded="false" aria-controls="dd${i}">${g.label}${icon.chev}</button>
            <div class="dropdown" id="dd${i}">${g.links.map(([t, h]) => `<a href="${h}">${t}</a>`).join("")}</div>
          </div>`).join("")}
      </nav>
      <div class="header-actions">
        <button class="icon-btn" id="searchOpen" aria-label="Search">${icon.search}</button>
        <button class="icon-btn menu-toggle" id="menuToggle" aria-label="Open menu" aria-expanded="false">${icon.menu}</button>
      </div>
    </div></header>
    <div class="search-panel" id="searchPanel" role="dialog" aria-label="Search">
      <div class="search-box">
        <form onsubmit="return false"><input id="searchInput" type="search" placeholder="Search recipes, products, FAQs…" autocomplete="off"><button class="icon-btn" type="button" id="searchClose" aria-label="Close search">${icon.close}</button></form>
        <ul class="search-results" id="searchResults"></ul>
      </div>
    </div>`;
  }

  /* ---------- footer ---------- */
  const footer = $("#site-footer");
  if (footer) {
    footer.outerHTML = `
    <footer class="site-footer"><div class="container">
      <div class="footer-grid">
        <div>
          <a class="logo" href="index.html">${logo}</a>
          <p style="margin-top:14px;max-width:300px">Hazelnut spread with cocoa, made to be dunked, spread and shared — since ${D.company.founded}.</p>
          <div class="socials" style="gap:16px">${socials}</div>
          <button class="country-btn" id="countryBtn">🌐 India · English</button>
        </div>
        ${D.nav.map(g => `<div><h4>${g.label}</h4><ul>${g.links.map(([t, h]) => `<li><a href="${h}">${t}</a></li>`).join("")}</ul></div>`).join("")}
      </div>
      <div class="footer-bottom">
        <span>© Cutella Foods ${new Date().getFullYear()}. All rights reserved. · <a href="contact.html">Contact us</a></span>
        <ul><li><a href="#">Cookie Policy</a></li><li><a href="#">Terms of Use</a></li><li><a href="#">Privacy Policy</a></li><li><a href="#">Sitemap</a></li></ul>
      </div>
    </div></footer>
    <div class="cookie" id="cookie" role="dialog" aria-label="Cookie consent">
      <h3 style="font-size:1.05rem">We use cookies 🍪 (the digital kind)</h3>
      <p>We use cookies to improve your experience and understand how our site is used. You can change your choice anytime.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn" data-cookie="all">Accept all</button><button class="btn btn--ghost" data-cookie="necessary">Only necessary</button></div>
    </div>`;
  }

  /* ---------- nav dropdowns + mobile menu ---------- */
  $$(".nav__item").forEach(item => {
    const btn = $(".nav__link", item);
    btn.addEventListener("click", e => {
      e.stopPropagation();
      const open = !item.classList.contains("open");
      $$(".nav__item").forEach(i => { i.classList.remove("open"); $(".nav__link", i).setAttribute("aria-expanded", "false"); });
      if (open) { item.classList.add("open"); btn.setAttribute("aria-expanded", "true"); }
    });
  });
  document.addEventListener("click", () => $$(".nav__item").forEach(i => i.classList.remove("open")));
  const nav = $("#nav"), toggle = $("#menuToggle");
  toggle && toggle.addEventListener("click", () => {
    nav.style.top = document.querySelector(".site-header").getBoundingClientRect().bottom + "px";
    const open = nav.classList.toggle("open");
    toggle.innerHTML = open ? icon.close : icon.menu;
    toggle.setAttribute("aria-expanded", open);
    document.body.style.overflow = open ? "hidden" : "";
  });
  $$(".dropdown a").forEach(a => a.addEventListener("click", () => {
    nav.classList.remove("open"); document.body.style.overflow = ""; if (toggle) toggle.innerHTML = icon.menu;
  }));

  /* ---------- search ---------- */
  const index = [
    ...D.nav.flatMap(g => g.links.map(([t, h]) => ({ t, h, k: g.label }))),
    ...D.recipes.map(r => ({ t: r.title, h: `recipes.html#${r.id}`, k: `Recipe · ${r.cat} · ${r.time}` })),
    ...D.products.map(p => ({ t: p.name, h: `products.html#${p.id}`, k: "Product" })),
    { t: "Contact us", h: "contact.html", k: "Help" },
  ];
  const panel = $("#searchPanel"), input = $("#searchInput"), results = $("#searchResults");
  const renderResults = q => {
    q = q.trim().toLowerCase();
    const list = q ? index.filter(i => (i.t + " " + i.k).toLowerCase().includes(q)) : index.slice(0, 6);
    results.innerHTML = list.length ? list.map(i => `<li><a href="${i.h}">${i.t}<small>${i.k}</small></a></li>`).join("") : `<li style="padding:10px 14px;color:#7a5a45">No results for “${q}”. Try “pancakes” or “jar”.</li>`;
  };
  const openSearch = () => { panel.classList.add("open"); renderResults(""); setTimeout(() => input.focus(), 30); };
  const closeSearch = () => panel.classList.remove("open");
  $("#searchOpen") && $("#searchOpen").addEventListener("click", openSearch);
  $("#searchClose") && $("#searchClose").addEventListener("click", closeSearch);
  panel && panel.addEventListener("click", e => { if (e.target === panel) closeSearch(); });
  input && input.addEventListener("input", e => renderResults(e.target.value));
  $$(".search-results").forEach(r => r.addEventListener("click", e => { if (e.target.closest("a")) closeSearch(); }));
  document.addEventListener("keydown", e => {
    if (e.key === "Escape") { closeSearch(); closeModal(); }
    if (e.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA") { e.preventDefault(); openSearch(); }
  });

  /* ---------- cookie banner ---------- */
  const cookie = $("#cookie");
  let consent = null;
  try { consent = localStorage.getItem("cutella-cookie"); } catch (e) {}
  if (cookie && !consent) setTimeout(() => cookie.classList.add("show"), 1200);
  $$("[data-cookie]").forEach(b => b.addEventListener("click", () => {
    try { localStorage.setItem("cutella-cookie", b.dataset.cookie); } catch (e) {}
    cookie.classList.remove("show");
  }));
  $("#countryBtn") && $("#countryBtn").addEventListener("click", () => alertToast("Cutella is currently available in India only. More countries coming soon!"));

  /* ---------- toast ---------- */
  function alertToast(msg) {
    let t = $("#toast");
    if (!t) { t = document.createElement("div"); t.id = "toast"; t.style.cssText = "position:fixed;left:50%;bottom:28px;transform:translateX(-50%);background:#4e2610;color:#fff;padding:14px 22px;border-radius:999px;font:600 .9rem Poppins,sans-serif;z-index:400;box-shadow:0 10px 30px rgba(0,0,0,.25);max-width:90vw;text-align:center"; document.body.appendChild(t); }
    t.textContent = msg; t.style.display = "block";
    clearTimeout(t._h); t._h = setTimeout(() => (t.style.display = "none"), 3200);
  }
  window.cutellaToast = alertToast;

  /* ---------- recipe card ---------- */
  const recipeCard = r => `
    <a class="card" href="recipes.html#${r.id}" data-recipe="${r.id}" data-cat="${r.cat}">
      <div class="card__media"><img src="${r.img}" alt="${r.title}" loading="lazy"></div>
      <div class="card__body">
        <span class="tag">${r.cat}</span>
        <h3>${r.title}</h3>
        <div class="card__meta"><span>⏱ ${r.time}</span><span>👩‍🍳 ${r.level}</span><span>🍽 Serves ${r.serves}</span></div>
        <span class="card__link">View recipe ${icon.arrow.replace('<svg', '<svg width="16" height="16"')}</span>
      </div>
    </a>`;
  $$("[data-recipes]").forEach(el => {
    const n = +el.dataset.recipes || D.recipes.length;
    el.innerHTML = D.recipes.slice(0, n).map(recipeCard).join("");
  });

  /* recipe filters */
  $$(".filters .tab").forEach(btn => btn.addEventListener("click", () => {
    $$(".filters .tab").forEach(b => b.setAttribute("aria-selected", "false"));
    btn.setAttribute("aria-selected", "true");
    const c = btn.dataset.filter;
    $$("#recipeGrid .card").forEach(card => (card.style.display = c === "All" || card.dataset.cat === c ? "" : "none"));
  }));

  /* recipe modal (on recipes page) */
  const modal = $("#recipeModal");
  function openRecipe(id) {
    const r = D.recipes.find(x => x.id === id);
    if (!r || !modal) return false;
    $(".modal__box", modal).innerHTML = `
      <button class="icon-btn modal__close" aria-label="Close">${icon.close}</button>
      <img src="${r.img}" alt="${r.title}">
      <div class="modal__content">
        <span class="tag">${r.cat}</span>
        <h2 style="font-size:2rem;margin-top:10px">${r.title}</h2>
        <p style="color:#7a5a45">${r.intro}</p>
        <div class="card__meta" style="margin-bottom:18px"><span>⏱ ${r.time}</span><span>👩‍🍳 ${r.level}</span><span>🍽 Serves ${r.serves}</span></div>
        <h3>Ingredients</h3><ul>${r.ingredients.map(i => `<li>${i}</li>`).join("")}</ul>
        <h3>Method</h3><ol>${r.steps.map(s => `<li>${s}</li>`).join("")}</ol>
        <button class="btn" style="margin-top:10px" onclick="navigator.clipboard&&navigator.clipboard.writeText(location.href);cutellaToast('Recipe link copied — share the love!')">Share recipe</button>
      </div>`;
    modal.classList.add("open");
    document.body.style.overflow = "hidden";
    $(".modal__close", modal).addEventListener("click", closeModal);
    return true;
  }
  function closeModal() {
    if (!modal || !modal.classList.contains("open")) return;
    modal.classList.remove("open"); document.body.style.overflow = "";
    history.replaceState(null, "", location.pathname);
  }
  if (modal) {
    modal.addEventListener("click", e => { if (e.target === modal) closeModal(); });
    $$("#recipeGrid .card").forEach(c => c.addEventListener("click", e => { e.preventDefault(); history.replaceState(null, "", "#" + c.dataset.recipe); openRecipe(c.dataset.recipe); }));
    const tryHash = () => { const id = location.hash.slice(1); if (id) openRecipe(id); };
    window.addEventListener("hashchange", tryHash); tryHash();
  }

  /* ---------- products ---------- */
  const productCard = p => `
    <article class="product" id="${p.id}">
      ${p.ribbon ? `<span class="ribbon">${p.ribbon}</span>` : ""}
      <img src="${p.img}" alt="${p.name}" loading="lazy">
      <h3>${p.name}</h3>
      <p>${p.desc}</p>
      <div class="sizes">${p.sizes.map(([s, pr], i) => `<button class="${i === 0 ? "active" : ""}" data-price="${pr}">${s}</button>`).join("")}</div>
      <div class="price">₹${p.sizes[0][1]}</div>
      <button class="btn" data-buy="${p.name}" style="margin-top:8px">Shop now</button>
    </article>`;
  $$("[data-products]").forEach(el => {
    const n = +el.dataset.products || D.products.length;
    el.innerHTML = D.products.slice(0, n).map(productCard).join("");
  });
  document.addEventListener("click", e => {
    const s = e.target.closest(".sizes button");
    if (s) {
      const card = s.closest(".product");
      $$(".sizes button", card).forEach(b => b.classList.remove("active"));
      s.classList.add("active");
      $(".price", card).textContent = "₹" + s.dataset.price;
    }
    const buy = e.target.closest("[data-buy]");
    if (buy) {
      const size = $(".sizes .active", buy.closest(".product"));
      alertToast(`${buy.dataset.buy} (${size ? size.textContent : ""}) added to your basket 🛒`);
    }
  });

  /* ---------- carousels ---------- */
  $$("[data-carousel]").forEach(c => {
    const track = $(".carousel__track", c);
    const step = () => track.firstElementChild.getBoundingClientRect().width + 24;
    $("[data-prev]", c).addEventListener("click", () => track.scrollBy({ left: -step(), behavior: "smooth" }));
    $("[data-next]", c).addEventListener("click", () => track.scrollBy({ left: step(), behavior: "smooth" }));
  });

  /* ---------- tabs ---------- */
  $$("[data-tabs]").forEach(group => {
    const tabs = $$(".tab", group);
    tabs.forEach(t => t.addEventListener("click", () => {
      tabs.forEach(x => { x.setAttribute("aria-selected", "false"); $("#" + x.getAttribute("aria-controls")).hidden = true; });
      t.setAttribute("aria-selected", "true");
      $("#" + t.getAttribute("aria-controls")).hidden = false;
    }));
  });

  /* ---------- accordion ---------- */
  $$(".acc-item button").forEach(b => b.addEventListener("click", () => {
    const item = b.parentElement, panel = item.querySelector(".acc-panel");
    const open = item.classList.toggle("open");
    b.setAttribute("aria-expanded", open);
    panel.style.maxHeight = open ? panel.scrollHeight + "px" : 0;
  }));

  /* ---------- forms ---------- */
  $$("form[data-demo]").forEach(f => f.addEventListener("submit", e => {
    e.preventDefault();
    const msg = $(".form-msg", f) || f.nextElementSibling;
    if (msg) msg.textContent = f.dataset.demo;
    f.reset();
  }));

  /* ---------- reveal on scroll ---------- */
  const io = "IntersectionObserver" in window ? new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } }), { threshold: .12 }) : null;
  $$(".reveal").forEach(el => (io ? io.observe(el) : el.classList.add("in")));

  /* ---------- counters ---------- */
  $$("[data-count]").forEach(el => {
    const end = +el.dataset.count, suf = el.dataset.suffix || "";
    let n = 0; const t = setInterval(() => { n += Math.ceil(end / 40); if (n >= end) { n = end; clearInterval(t); } el.textContent = n.toLocaleString("en-IN") + suf; }, 30);
  });
})();
