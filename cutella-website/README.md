# Cutella® — website

Static marketing site for **Cutella**, a hazelnut spread with cocoa (all brand details, addresses and figures are dummy data).

## Pages
| File | Content |
|---|---|
| `index.html` | Home: animated biscuit-splash hero, recipes carousel, hazelnuts & cocoa, up-cycling, Cutella World tabs, products, newsletter |
| `products.html` | Product range with size/price selector, nutrition table, store finder |
| `recipes.html` | Filterable recipes with recipe pop-ups (deep-linkable, e.g. `recipes.html#pancakes`), jar up-cycling ideas |
| `inside.html` | Sustainability, quality & ingredients, recycling, new look, heritage timeline, FAQ |
| `news.html` | Cutella Café, Travel with Cutella, Dunk Day |
| `contact.html` | Contact details and form |

## Structure
```
assets/css/style.css   all styles (design tokens at the top)
assets/js/data.js      ALL editable content: nav, products, recipes, company details
assets/js/main.js      shared header/footer + interactions
assets/img/            hero GIF (+ MP4), SVG illustrations
assets/source/         Python scripts that generate the GIF and SVGs
```

## Run locally
Just open `index.html` in a browser — no build step. Or serve it:
```
python3 -m http.server 8000
```

## Regenerate the hero animation
```
pip install pillow   # ffmpeg must be installed too
python3 assets/source/make_gif.py
```

## Deploy
Push to GitHub and enable GitHub Pages (or import into Vercel/Netlify) — it's plain static HTML.
