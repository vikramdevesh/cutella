"""Generates the flat illustrations used across the Cutella site."""
import os
OUT = "/home/claude/site/assets/img"
os.makedirs(OUT, exist_ok=True)

BR, BR2, BRL = "#4E2610", "#6A3418", "#9A5C34"
RED, CREAM, GOLD, GOLD2, WHITE = "#D61020", "#FBEFDF", "#E6B062", "#C98A3E", "#FFFFFF"

def svg(name, body, vb="0 0 400 300"):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img">{body}</svg>')

def jar(x, y, sc=1.0, label="cutella", sub="HAZELNUT SPREAD WITH COCOA", lid=True, band=RED):
    # jar 200 wide x 240 tall in local units
    g = f'<g transform="translate({x} {y}) scale({sc})">'
    g += '<ellipse cx="100" cy="246" rx="112" ry="10" fill="#000" opacity=".12"/>'
    g += f'<path d="M0 30 H200 V214 a26 26 0 0 1 -26 26 H26 a26 26 0 0 1 -26 -26Z" fill="{BR}"/>'
    g += '<rect x="0" y="30" width="16" height="210" fill="#2c1206" opacity=".35"/><rect x="184" y="30" width="16" height="210" fill="#2c1206" opacity=".35"/>'
    if lid:
        g += '<rect x="-4" y="0" width="208" height="38" rx="8" fill="#F4F1EA"/><rect x="-4" y="0" width="208" height="14" rx="7" fill="#FFFFFF"/>'
        g += ''.join(f'<rect x="{2+i*9.6}" y="16" width="2" height="18" fill="#E1DBD0"/>' for i in range(21))
    g += f'<rect x="0" y="96" width="200" height="98" fill="#FDFBF7"/><rect x="0" y="96" width="200" height="5" fill="{band}"/><rect x="0" y="189" width="200" height="5" fill="{band}"/>'
    g += f'<text x="100" y="152" text-anchor="middle" font-family="Poppins,Arial,sans-serif" font-weight="700" font-size="44" letter-spacing="-1"><tspan fill="#3E1E0C">{label[0]}</tspan><tspan fill="{RED}">{label[1:]}</tspan></text>'
    g += f'<text x="100" y="174" text-anchor="middle" font-family="Poppins,Arial,sans-serif" font-weight="500" font-size="8.5" letter-spacing="1.4" fill="#5A321A">{sub}</text>'
    g += '<rect x="14" y="44" width="10" height="186" rx="5" fill="#fff" opacity=".22"/><rect x="30" y="48" width="4" height="176" rx="2" fill="#fff" opacity=".14"/>'
    return g + '</g>'

def hazelnut(cx, cy, r):
    return (f'<g><ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r*.86}" fill="#96582E"/>'
            f'<ellipse cx="{cx-r*.3}" cy="{cy-r*.2}" rx="{r*.3}" ry="{r*.2}" fill="#BD8048"/>'
            f'<path d="M{cx-r*.8} {cy-r*.45} Q{cx} {cy-r*1.25} {cx+r*.8} {cy-r*.45} Q{cx} {cy-r*.2} {cx-r*.8} {cy-r*.45}Z" fill="#6C3E1C"/></g>')

def biscuit(x, y, w=120, h=78, rot=0):
    holes = ''.join(f'<circle cx="{x+22+i*(w-44)/4}" cy="{y+h*.3}" r="2.6" fill="#A6682C"/><circle cx="{x+22+i*(w-44)/4}" cy="{y+h*.7}" r="2.6" fill="#A6682C"/>' for i in range(5))
    return (f'<g transform="rotate({rot} {x+w/2} {y+h/2})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{GOLD2}"/>'
            f'<rect x="{x+5}" y="{y+5}" width="{w-10}" height="{h-10}" rx="7" fill="{GOLD}"/>'
            f'<rect x="{x+13}" y="{y+13}" width="{w-26}" height="{h-26}" rx="4" fill="none" stroke="#CB8C45" stroke-width="2"/>{holes}</g>')

def bg(color, extra=""):
    return f'<rect width="400" height="300" fill="{color}"/>{extra}'

# ---- product jar (transparent) ----
svg("jar.svg", jar(20, 10), "0 0 240 270")
svg("jar-cocoa.svg", jar(20, 10, label="cutella", sub="DARK COCOA  ·  LESS SUGAR", band="#3E1E0C"), "0 0 240 270")
svg("jar-crunch.svg", jar(20, 10, label="cutella", sub="CRUNCHY HAZELNUT BITS", band="#E6B062"), "0 0 240 270")
svg("biscuits-pack.svg",
    '<ellipse cx="160" cy="250" rx="140" ry="10" fill="#000" opacity=".12"/>'
    f'<path d="M20 70 Q160 40 300 70 L300 236 Q160 258 20 236Z" fill="{RED}"/>'
    f'<path d="M20 70 Q160 40 300 70 L300 98 Q160 74 20 98Z" fill="#B00C1A"/>'
    + biscuit(60, 120, 120, 78, -8) + biscuit(140, 132, 120, 78, 6) +
    f'<text x="160" y="232" text-anchor="middle" font-family="Poppins,Arial" font-weight="700" font-size="30" fill="#fff">cutella</text>'
    '<text x="160" y="112" text-anchor="middle" font-family="Poppins,Arial" font-weight="600" font-size="12" letter-spacing="3" fill="#fff">DUNK BISCUITS</text>', "0 0 320 270")
svg("bites.svg",
    '<ellipse cx="160" cy="250" rx="130" ry="10" fill="#000" opacity=".12"/>'
    f'<rect x="40" y="40" width="240" height="200" rx="28" fill="{BR}"/><rect x="40" y="40" width="240" height="56" rx="28" fill="{RED}"/><rect x="40" y="70" width="240" height="26" fill="{RED}"/>'
    '<text x="160" y="78" text-anchor="middle" font-family="Poppins,Arial" font-weight="700" font-size="28" fill="#fff">cutella</text>'
    + ''.join(f'<g transform="translate({80+i*56} {130+ (i%2)*26})"><rect width="44" height="44" rx="12" fill="{GOLD}"/><circle cx="22" cy="22" r="11" fill="{BR2}"/></g>' for i in range(4)) +
    '<text x="160" y="222" text-anchor="middle" font-family="Poppins,Arial" font-weight="600" font-size="13" letter-spacing="3" fill="#F6D7A8">GO BITES</text>', "0 0 320 270")

# ---- recipe & section illustrations (400x300 with bg) ----
def plate(cx=200, cy=232, rx=150, ry=26):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#fff"/><ellipse cx="{cx}" cy="{cy-4}" rx="{rx-26}" ry="{ry-8}" fill="#F1ECE4"/>'

drip = lambda x, y, l: f'<path d="M{x-6} {y} h12 v{l} a6 6 0 0 1 -12 0Z" fill="{BR2}"/>'

svg("recipe-pancakes.svg", bg("#F8D9C4") + plate() +
    ''.join(f'<ellipse cx="200" cy="{214-i*24}" rx="110" ry="26" fill="#D99A52"/><ellipse cx="200" cy="{208-i*24}" rx="106" ry="22" fill="#EDB86E"/>' for i in range(4)) +
    f'<path d="M110 128 Q200 96 290 128 Q292 140 280 142 Q240 152 230 168 Q222 150 200 146 Q170 150 160 166 Q150 146 120 142 Q106 140 110 128Z" fill="{BR2}"/>' +
    f'<ellipse cx="180" cy="122" rx="30" ry="6" fill="{BRL}" opacity=".6"/>' + hazelnut(206, 108, 12) + hazelnut(232, 114, 10))
svg("recipe-crepe.svg", bg("#FCE7B8") + plate() +
    '<path d="M70 220 L200 110 L330 220Z" fill="#EEC27A"/><path d="M70 220 L200 110 L230 220Z" fill="#E2AE5E"/>' +
    f'<path d="M120 190 Q200 160 280 192 L250 210 Q200 196 150 210Z" fill="{BR2}"/>' + drip(160, 204, 18) + drip(232, 204, 24) +
    '<circle cx="270" cy="150" r="10" fill="#D61020"/><circle cx="290" cy="166" r="8" fill="#D61020"/><path d="M268 140 l4 -10 l4 10" fill="#3D8A3A"/>')
svg("recipe-toast.svg", bg("#E9D7F2") + plate() +
    '<path d="M110 220 V120 Q110 70 200 70 Q290 70 290 120 V220Z" fill="#C98A3E"/><path d="M122 214 V124 Q122 84 200 84 Q278 84 278 124 V214Z" fill="#F0CF94"/>' +
    f'<path d="M132 206 V130 Q132 96 200 96 Q268 96 268 130 V206Z" fill="{BR2}"/>' +
    '<g fill="#F6E7A6">' + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="9" transform="rotate(-20 {x} {y})"/>' for x, y in [(170, 140), (226, 132), (196, 172), (240, 186)]) + '</g>')
svg("recipe-brownie.svg", bg("#D8E8D1") + plate() +
    f'<path d="M100 200 L140 150 L300 150 L300 200 L260 230 L100 230Z" fill="{BR}"/><path d="M100 200 L140 150 L300 150 L260 200Z" fill="{BR2}"/><path d="M260 200 L300 150 L300 200 L260 230Z" fill="#3A1A08"/>' +
    hazelnut(170, 170, 12) + hazelnut(214, 176, 11) + hazelnut(240, 162, 10) +
    f'<path d="M150 152 Q160 170 170 152 M200 152 Q212 172 222 152" stroke="{BRL}" stroke-width="5" fill="none"/>')
svg("recipe-shake.svg", bg("#FAD0D3") +
    '<path d="M140 90 H260 L244 260 H156Z" fill="#fff" opacity=".85"/><path d="M146 120 H254 L244 256 H156Z" fill="#B57A4E"/>' +
    f'<path d="M140 90 H260 L256 118 Q240 108 230 124 Q220 106 200 118 Q182 104 170 124 Q158 108 144 118Z" fill="{BR2}"/>' +
    '<ellipse cx="200" cy="82" rx="66" ry="22" fill="#FFF6EA"/><ellipse cx="190" cy="66" rx="40" ry="18" fill="#FFF6EA"/>' +
    f'<rect x="222" y="18" width="10" height="70" rx="5" fill="{RED}" transform="rotate(16 227 50)"/>' + biscuit(116, 52, 54, 34, -24))
svg("recipe-cookies.svg", bg("#FFE1B0") + plate() +
    ''.join(f'<g><circle cx="{x}" cy="{y}" r="46" fill="#D9A055"/><circle cx="{x}" cy="{y}" r="40" fill="#E8B56E"/>'
            f'<circle cx="{x-14}" cy="{y-10}" r="6" fill="{BR}"/><circle cx="{x+12}" cy="{y+12}" r="7" fill="{BR}"/><circle cx="{x+16}" cy="{y-16}" r="5" fill="{BR}"/></g>'
            for x, y in [(150, 190), (250, 186)]) +
    f'<ellipse cx="200" cy="140" rx="54" ry="16" fill="{BR2}"/><circle cx="200" cy="120" r="44" fill="#D9A055"/><circle cx="200" cy="120" r="38" fill="#E8B56E"/>' + drip(184, 150, 14) + drip(216, 150, 20))

svg("hazelnuts.svg", bg("#F3E2C7") + '<path d="M40 260 Q200 200 360 260 V300 H40Z" fill="#8DB360"/>' +
    '<path d="M200 40 Q150 120 200 190 Q250 120 200 40Z" fill="#6E9A3C"/><path d="M200 50 V190" stroke="#4E7A26" stroke-width="3"/>' +
    hazelnut(150, 220, 34) + hazelnut(225, 236, 28) + hazelnut(280, 212, 22))
svg("cocoa.svg", bg("#F4D3B8") +
    '<path d="M60 150 Q200 -10 340 150 Q200 310 60 150Z" fill="#B85B2C"/><path d="M80 150 Q200 20 320 150" stroke="#8E3E18" stroke-width="5" fill="none"/>'
    '<path d="M80 150 Q200 280 320 150" stroke="#8E3E18" stroke-width="5" fill="none"/><path d="M60 150 H340" stroke="#D07A44" stroke-width="5"/>' +
    ''.join(f'<ellipse cx="{x}" cy="{250}" rx="22" ry="14" fill="{BR}"/>' for x in (120, 170, 230, 280)))
svg("upcycle.svg", bg("#D7E9E3") +
    '<path d="M200 150 Q150 60 120 70 Q130 130 200 150Z M200 150 Q260 50 300 70 Q280 140 200 150Z" fill="#5E9C4A"/><path d="M200 150 V200" stroke="#3F7A2C" stroke-width="5"/>'
    '<path d="M120 170 H280 V250 a20 20 0 0 1 -20 20 H140 a20 20 0 0 1 -20 -20Z" fill="#fff" opacity=".7" stroke="#B9D3CA" stroke-width="3"/>'
    '<path d="M124 215 H276 V250 a18 18 0 0 1 -18 18 H142 a18 18 0 0 1 -18 -18Z" fill="#8A5A3A"/>' +
    f'<rect x="120" y="230" width="160" height="14" fill="{RED}" opacity=".9"/>')
svg("quality.svg", bg("#FBE3E5") + jar(140, 46, .6) + hazelnut(110, 240, 22) + hazelnut(300, 246, 18) +
    '<g transform="translate(290 70)"><circle r="40" fill="#FFD24A"/><circle r="32" fill="#FFE07A"/><path d="M-14 0 l10 10 l18 -20" stroke="#4E2610" stroke-width="7" fill="none" stroke-linecap="round"/></g>')
svg("recycle.svg", bg("#DCEBF5") + jar(150, 60, .5) +
    '<g fill="none" stroke="#2F7FB5" stroke-width="12" stroke-linecap="round"><path d="M110 90 A110 110 0 0 1 290 90"/><path d="M300 210 A110 110 0 0 1 100 210"/></g>'
    '<path d="M280 64 l26 24 l-34 8Z M120 236 l-26 -24 l34 -8Z" fill="#2F7FB5"/>')
svg("newlook.svg", bg("#FFE9C9") + jar(140, 50, .6) +
    ''.join(f'<path d="M{x} {y-16} L{x+5} {y-5} L{x+16} {y} L{x+5} {y+5} L{x} {y+16} L{x-5} {y+5} L{x-16} {y} L{x-5} {y-5}Z" fill="{c}"/>' for x, y, c in [(100, 80, RED), (310, 110, "#F2A93B"), (296, 230, RED), (96, 210, "#F2A93B")]))
svg("heritage.svg", bg("#EFE2CF") +
    '<rect x="110" y="60" width="180" height="200" rx="12" fill="#fff" stroke="#C9B79E" stroke-width="3"/><rect x="126" y="76" width="148" height="120" fill="#D3B88F"/>'
    '<path d="M126 196 L180 130 L220 170 L244 146 L274 196Z" fill="#9E7A4E"/><circle cx="240" cy="104" r="14" fill="#F4E3C2"/>'
    '<text x="200" y="236" text-anchor="middle" font-family="Georgia,serif" font-size="26" fill="#6A4A2A">since 1978</text>')
svg("faq.svg", bg("#E5E1F7") +
    f'<path d="M80 70 H280 a20 20 0 0 1 20 20 V170 a20 20 0 0 1 -20 20 H150 L110 226 V190 H80 a20 20 0 0 1 -20 -20 V90 a20 20 0 0 1 20 -20Z" fill="{RED}"/>'
    '<text x="180" y="160" text-anchor="middle" font-family="Poppins,Arial" font-weight="700" font-size="80" fill="#fff">?</text>'
    f'<circle cx="300" cy="230" r="40" fill="{BR}"/><text x="300" y="246" text-anchor="middle" font-family="Poppins,Arial" font-weight="700" font-size="44" fill="#fff">!</text>')
svg("cafe.svg", bg("#F3D9C9") +
    '<path d="M110 120 H270 V200 a50 50 0 0 1 -50 50 H160 a50 50 0 0 1 -50 -50Z" fill="#fff"/><path d="M270 140 a30 30 0 0 1 0 60" stroke="#fff" stroke-width="14" fill="none"/>'
    f'<ellipse cx="190" cy="122" rx="80" ry="14" fill="{BRL}"/><path d="M160 122 Q190 108 220 122" stroke="#F3D9C9" stroke-width="4" fill="none"/>'
    '<path d="M160 90 q-12 -18 0 -36 M190 90 q-12 -18 0 -36 M220 90 q-12 -18 0 -36" stroke="#C9A58E" stroke-width="5" fill="none" stroke-linecap="round"/>'
    f'<rect x="110" y="170" width="160" height="12" fill="{RED}"/>')
svg("travel.svg", bg("#D4E6F1") +
    f'<rect x="120" y="100" width="160" height="150" rx="18" fill="{RED}"/><rect x="170" y="70" width="60" height="34" rx="10" fill="none" stroke="{BR}" stroke-width="10"/>'
    '<rect x="150" y="100" width="12" height="150" fill="#B00C1A"/><rect x="238" y="100" width="12" height="150" fill="#B00C1A"/>'
    '<circle cx="200" cy="176" r="26" fill="#fff"/><text x="200" y="186" text-anchor="middle" font-family="Poppins,Arial" font-weight="700" font-size="28" fill="#D61020">c</text>'
    '<path d="M300 60 l40 -10 l-12 12 l-8 30Z" fill="#fff"/>')
svg("og-image.svg", bg(CREAM) + jar(130, 30, .6) + biscuit(150, 10, 100, 64, -10))
svg("favicon.svg", f'<rect width="64" height="64" rx="16" fill="{RED}"/><text x="32" y="46" text-anchor="middle" font-family="Poppins,Arial" font-weight="700" font-size="44" fill="#fff">c</text>', "0 0 64 64")
print("ok", len(os.listdir(OUT)))
