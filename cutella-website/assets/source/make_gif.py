"""Cutella hero animation: a biscuit drops into a jar of Cutella, spread splashes,
biscuit gets dunked and lifted out coated. Renders at 2x, downsamples, encodes GIF/MP4."""
import math, random, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(7)
S = 2                    # supersampling
W = H = 640
BG = (251, 239, 223)
SPREAD = (78, 38, 16)
SPREAD_SURF = (98, 50, 22)
SPREAD_HI = (150, 92, 52)
SPREAD_DK = (50, 22, 8)
RED = (214, 16, 32)
FONT_B = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FONT_M = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"

OUT = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(OUT, "frames"); os.makedirs(FR, exist_ok=True)

def s(v): return v * S
def box(x0, y0, x1, y1): return [s(x0), s(y0), s(x1), s(y1)]
def ell(cx, cy, rx, ry): return box(cx - rx, cy - ry, cx + rx, cy + ry)
def layer(): return Image.new("RGBA", (s(W), s(H)), (0, 0, 0, 0))

# ---- geometry (1x units) ----
CX = 320
JX0, JX1, JTOP, JBOT = 180, 460, 292, 590
RIM_RX, RIM_RY = 140, 24
YS, SRX, SRY = 312, 137, 22           # spread surface
FLOOR = 592

# ---------------- static layers ----------------
def hazelnut(d, cx, cy, r, tilt=0):
    d.ellipse(ell(cx, cy, r, r * 0.86), fill=(150, 92, 48))
    d.ellipse(ell(cx - r * 0.25, cy - r * 0.25, r * 0.35, r * 0.25), fill=(185, 125, 72))
    d.chord(ell(cx, cy - r * 0.45, r * 0.8, r * 0.42), 180, 360, fill=(108, 62, 28))
    d.ellipse(ell(cx, cy - r * 0.95, r * 0.12, r * 0.12), fill=(90, 50, 20))

def make_back():
    im = Image.new("RGBA", (s(W), s(H)), BG + (255,))
    sh = layer(); d = ImageDraw.Draw(sh)
    d.ellipse(ell(CX, FLOOR + 2, 170, 18), fill=(120, 80, 40, 70))
    d.ellipse(ell(548, FLOOR + 2, 72, 10), fill=(120, 80, 40, 60))
    d.ellipse(ell(110, 603, 50, 7), fill=(120, 80, 40, 50))
    sh = sh.filter(ImageFilter.GaussianBlur(s(6)))
    im.alpha_composite(sh)
    d = ImageDraw.Draw(im)
    # hazelnuts + crumbs on the table (left)
    hazelnut(d, 92, 586, 20); hazelnut(d, 136, 598, 16)
    for (x, y, r) in [(60, 606, 3), (165, 610, 2.5), (40, 596, 2), (182, 604, 2)]:
        d.ellipse(ell(x, y, r, r * 0.7), fill=(214, 160, 90))
    # lid on the right
    d.rounded_rectangle(box(482, 548, 614, 590), radius=s(8), fill=(232, 228, 220))
    d.rectangle(box(482, 548, 614, 570), fill=(240, 237, 230))
    d.ellipse(ell(548, 548, 66, 13), fill=(250, 249, 245))
    d.ellipse(ell(548, 548, 58, 10), outline=(225, 220, 212), width=s(2))
    for i in range(22):  # grip ridges
        x = 488 + i * 5.8
        d.line([s(x), s(556), s(x), s(586)], fill=(220, 214, 205), width=s(1))
    # jar inner back wall (inside opening)
    d.ellipse(ell(CX, JTOP, RIM_RX, RIM_RY), fill=(214, 196, 176))
    # jar body: glass band above contents, contents below
    body = layer(); bd = ImageDraw.Draw(body)
    bd.rounded_rectangle(box(JX0, JTOP, JX1, JBOT), radius=s(42), fill=(255, 255, 255, 255))
    bd.rectangle(box(JX0, JTOP, JX1, JBOT - 60), fill=(255, 255, 255, 255))
    mask = body.getchannel("A")
    fill = layer(); fd = ImageDraw.Draw(fill)
    fd.rectangle(box(JX0, JTOP, JX1, YS), fill=(226, 212, 196, 255))
    fd.rectangle(box(JX0, YS, JX1, JBOT), fill=SPREAD + (255,))
    # side shading on contents (cylinder look)
    for i in range(26):
        a = int(110 * (1 - i / 26) ** 1.6)
        fd.line([s(JX0 + i), s(YS), s(JX0 + i), s(JBOT)], fill=SPREAD_DK + (a,), width=s(1))
        fd.line([s(JX1 - i), s(YS), s(JX1 - i), s(JBOT)], fill=SPREAD_DK + (a,), width=s(1))
    fill.putalpha(Image.composite(fill.getchannel("A"), Image.new("L", fill.size, 0), mask))
    im.alpha_composite(fill)
    d = ImageDraw.Draw(im)
    # back rim edge
    d.arc(ell(CX, JTOP, RIM_RX, RIM_RY), 180, 360, fill=(240, 232, 222), width=s(3))
    # label
    lab = layer(); ld = ImageDraw.Draw(lab)
    ld.rectangle(box(JX0, 392, JX1, 524), fill=(253, 251, 247, 255))
    for i in range(30):
        a = int(70 * (1 - i / 30) ** 1.8)
        ld.line([s(JX0 + i), s(392), s(JX0 + i), s(524)], fill=(120, 90, 60, a), width=s(1))
        ld.line([s(JX1 - i), s(392), s(JX1 - i), s(524)], fill=(120, 90, 60, a), width=s(1))
    ld.rectangle(box(JX0, 392, JX1, 397), fill=RED + (255,))
    ld.rectangle(box(JX0, 519, JX1, 524), fill=RED + (255,))
    fb = ImageFont.truetype(FONT_B, s(60)); fm = ImageFont.truetype(FONT_M, s(11))
    c_w = ld.textlength("c", font=fb); u_w = ld.textlength("utella", font=fb)
    x0 = CX - (c_w + u_w) / 2 / S
    ld.text((s(x0), s(404)), "c", font=fb, fill=(62, 30, 12))
    ld.text((s(x0) + c_w, s(404)), "utella", font=fb, fill=RED)
    sub = "HAZELNUT  SPREAD  WITH  COCOA"
    tw = ld.textlength(sub, font=fm)
    ld.text((s(CX) - tw / 2, s(484)), sub, font=fm, fill=(90, 50, 25))
    ld.line([s(CX - 50), s(504), s(CX + 50), s(504)], fill=(214, 16, 32, 160), width=s(1))
    im.alpha_composite(lab)
    return im

def make_front():
    f = layer(); d = ImageDraw.Draw(f)
    d.arc(ell(CX, JTOP, RIM_RX, RIM_RY), 0, 180, fill=(255, 255, 255, 170), width=s(4))
    d.arc(ell(CX, JTOP + 3, RIM_RX - 2, RIM_RY), 15, 165, fill=(255, 255, 255, 70), width=s(2))
    d.rounded_rectangle(box(196, 300, 210, 572), radius=s(7), fill=(255, 255, 255, 70))
    d.rounded_rectangle(box(219, 304, 224, 560), radius=s(3), fill=(255, 255, 255, 45))
    d.rounded_rectangle(box(436, 306, 442, 566), radius=s(3), fill=(255, 255, 255, 35))
    return f

BACK, FRONT = make_back(), make_front()

# ---------------- biscuit sprite ----------------
BW, BH = 164, 106
def biscuit_sprite(coat_y=None, drips=None):
    w, h = s(BW + 20), s(BH + 40)     # padding for drips
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    ox, oy = s(10), s(10)
    def B(x0, y0, x1, y1): return [ox + s(x0), oy + s(y0), ox + s(x1), oy + s(y1)]
    # scalloped silhouette
    d.rounded_rectangle(B(6, 6, BW - 6, BH - 6), radius=s(10), fill=(196, 132, 60))
    step = 14.6
    for i in range(11):
        x = 10 + i * step
        d.ellipse(B(x - 7, 0, x + 7, 13), fill=(196, 132, 60))
        d.ellipse(B(x - 7, BH - 13, x + 7, BH), fill=(196, 132, 60))
    for j in range(7):
        y = 10 + j * 14.3
        d.ellipse(B(0, y - 7, 13, y + 7), fill=(196, 132, 60))
        d.ellipse(B(BW - 13, y - 7, BW, y + 7), fill=(196, 132, 60))
    shape = im.getchannel("A").copy()
    d.rounded_rectangle(B(9, 8, BW - 9, BH - 10), radius=s(9), fill=(230, 176, 98))
    d.rounded_rectangle(B(9, 8, BW - 9, 30), radius=s(9), fill=(238, 190, 116))
    d.rounded_rectangle(B(20, 19, BW - 20, BH - 21), radius=s(6), outline=(204, 142, 66), width=s(2))
    for gx in range(6):
        for gy in (32, BH - 32):
            x = 34 + gx * 19.2
            d.ellipse(B(x - 2.6, gy - 2.6, x + 2.6, gy + 2.6), fill=(166, 104, 44))
    fb = ImageFont.truetype(FONT_B, s(15))
    tw = d.textlength("CUTELLA", font=fb)
    d.text((ox + s(BW / 2) - tw / 2 + s(1), oy + s(BH / 2 - 11) + s(1)), "CUTELLA", font=fb, fill=(246, 206, 140))
    d.text((ox + s(BW / 2) - tw / 2, oy + s(BH / 2 - 11)), "CUTELLA", font=fb, fill=(178, 114, 48))
    if coat_y is not None and coat_y < BH:
        c = Image.new("RGBA", (w, h), (0, 0, 0, 0)); cd = ImageDraw.Draw(c)
        pts = []
        for i in range(0, 61):
            x = -4 + i * (BW + 8) / 60
            y = coat_y + 3.5 * math.sin(i * 0.9) + 2 * math.sin(i * 2.3)
            pts.append((ox + s(x), oy + s(y)))
        pts += [(ox + s(BW + 4), oy + s(BH + 6)), (ox + s(-4), oy + s(BH + 6))]
        cd.polygon(pts, fill=SPREAD_SURF + (255,))
        cmask = Image.composite(c.getchannel("A"), Image.new("L", c.size, 0), shape)
        c.putalpha(cmask)
        # gloss
        g = ImageDraw.Draw(c)
        for (x, ln) in [(30, 26), (88, 18), (132, 22)]:
            y = coat_y + 10
            if y + ln < BH - 6:
                g.rounded_rectangle([ox + s(x), oy + s(y), ox + s(x + 5), oy + s(y + ln)], radius=s(2), fill=(170, 110, 66, 150))
        im.alpha_composite(c)
        d = ImageDraw.Draw(im)
        for (x, ln, r) in (drips or []):   # drips hanging from bottom edge
            d.rounded_rectangle([ox + s(x - r * 0.7), oy + s(BH - 8), ox + s(x + r * 0.7), oy + s(BH - 4 + ln)], radius=s(r * 0.7), fill=SPREAD_SURF)
            d.ellipse([ox + s(x - r), oy + s(BH - 4 + ln - r), ox + s(x + r), oy + s(BH - 4 + ln + r)], fill=SPREAD_SURF)
    return im

def place_sprite(sprite, cx, cy, ang, alpha=1.0):
    r = sprite.rotate(ang, resample=Image.BICUBIC, expand=True)
    L = layer()
    # sprite centre is the biscuit centre (+ padding offset)
    th = math.radians(ang); dd = s(10)
    pcx = r.width / 2 - dd * math.sin(th); pcy = r.height / 2 - dd * math.cos(th)
    L.paste(r, (int(s(cx) - pcx), int(s(cy) - pcy)), r)
    if alpha < 1:
        L.putalpha(L.getchannel("A").point(lambda v: int(v * alpha)))
    return L

ABOVE = Image.new("L", (s(W), s(H)), 0)
ImageDraw.Draw(ABOVE).rectangle([0, 0, s(W), s(YS)], fill=255)
SURF_MASK = Image.new("L", (s(W), s(H)), 0)
ImageDraw.Draw(SURF_MASK).ellipse(ell(CX, YS, SRX, SRY), fill=255)

def clip(L, m):
    L.putalpha(Image.composite(L.getchannel("A"), Image.new("L", L.size, 0), m)); return L

# ---------------- timeline ----------------
N = 92
F_IMP, F_REST, F_LIFT, F_GONE, F_FADE = 16, 28, 54, 74, 76
Y_START, Y_IMP, Y_REST, Y_END = -140, YS - 46, YS - 18, -170

def ease_in(u, p=2): return u ** p
def ease_out(u): return 1 - (1 - u) ** 3

def biscuit_state(f):
    if f < F_IMP:
        u = f / F_IMP
        return Y_START + (Y_IMP - Y_START) * ease_in(u), -30 + 20 * u
    if f < F_REST:
        u = (f - F_IMP) / (F_REST - F_IMP)
        return Y_IMP + (Y_REST - Y_IMP) * ease_out(u), -10 + 3 * ease_out(u)
    if f < F_LIFT:
        return Y_REST + 1.5 * math.sin((f - F_REST) * 0.35) * max(0, 1 - (f - F_REST) / 14), -7
    if f < F_GONE:
        u = (f - F_LIFT) / (F_GONE - F_LIFT)
        return Y_REST + (Y_END - Y_REST) * ease_in(u, 2.3), -7 - 8 * u
    return None, None

# ---------------- splash particles ----------------
class Drop:
    def __init__(self, delay):
        th = random.uniform(0, 2 * math.pi)
        rad = random.uniform(60, 105)
        self.x = CX + rad * math.cos(th)
        self.y = YS + rad * 0.16 * math.sin(th) - random.uniform(10, 40)
        sp = random.uniform(4.5, 11)
        self.vx = math.cos(th) * sp + random.uniform(-1, 1)
        self.vy = -random.uniform(9, 17)
        self.r = random.uniform(3.5, 9)
        self.start = F_IMP + delay
        self.state = "air"
        self.floor = random.uniform(FLOOR - 4, 628)
        self.front = math.sin(th) > -0.2
    def step(self):
        if self.state != "air":
            if self.state == "drip":
                self.dl += (self.dmax - self.dl) * 0.12
            return
        self.vy += 1.05; self.x += self.vx; self.y += self.vy
        if self.vy > 0:
            inside_x = JX0 - 2 <= self.x <= JX1 + 2
            if inside_x and abs(self.x - CX) < SRX - 8 and self.y >= YS - 6:
                self.state = "gone"
            elif inside_x and self.y >= JTOP - 2:
                Drop.ndrip = getattr(Drop, 'ndrip', 0) + 1
                if Drop.ndrip > 3: self.state = "gone"; return
                self.state = "drip"; self.y = JTOP + 4; self.dl = 0
                self.dmax = random.uniform(40, 130)
            elif not inside_x:
                fl = self.floor
                if 470 < self.x < 625: fl = max(fl, 600)
                if self.y >= fl:
                    self.state = "splat"; self.y = fl
                    self.dots = [(random.uniform(-3, 3) * self.r, random.uniform(-0.6, 0.6) * self.r, random.uniform(1, 2.5)) for _ in range(3)]

drops = [Drop(random.choice([0, 0, 1, 2, 3, 5])) for _ in range(30)]
# guarantee a few dramatic rim drips
for x in (196, 236, 412, 448):
    dd = Drop(0); dd.state = "drip"; dd.x = x; dd.y = JTOP + 4; dd.dl = 0; dd.dmax = random.uniform(60, 150)
    dd.r = random.uniform(5, 8); dd.start = F_IMP + 6 + random.randint(0, 6); drops.append(dd)

def draw_drop(d, x, y, vx, vy, r, col=SPREAD_SURF):
    v = math.hypot(vx, vy); st = min(1 + v * 0.07, 2.3)
    a, b = r * st, r / math.sqrt(st)
    ang = math.atan2(vy, vx)
    pts = []
    for i in range(24):
        t = 2 * math.pi * i / 24
        lx, ly = a * math.cos(t), b * math.sin(t)
        if math.cos(t) < 0: lx *= 1.25   # tail
        pts.append((s(x + lx * math.cos(ang) - ly * math.sin(ang)), s(y + lx * math.sin(ang) + ly * math.cos(ang))))
    d.polygon(pts, fill=col)
    d.ellipse(ell(x - r * 0.3, y - r * 0.35, r * 0.28, r * 0.22), fill=(190, 130, 90))

def crown(f, half):
    L = layer(); d = ImageDraw.Draw(L)
    t = (f - F_IMP) / 17
    if not (0 <= t <= 1): return L
    hmul = math.sin(math.pi * t) ** 0.8
    r0 = 62 + 55 * t
    n = 18
    random.seed(99)
    hs = [random.uniform(40, 95) for _ in range(n)]
    offs = [random.uniform(-0.12, 0.12) for _ in range(n)]
    random.seed(f + 1000)
    # sheet
    pts_top, pts_base = [], []
    rng = (math.pi, 2 * math.pi) if half == "back" else (0, math.pi)
    steps = 40
    for i in range(steps + 1):
        th = rng[0] + (rng[1] - rng[0]) * i / steps
        bx, by = CX + r0 * math.cos(th), YS + r0 * 0.16 * math.sin(th)
        k = (th / (2 * math.pi) * n) % n
        hh = hs[int(k)] * 0.45 * hmul
        pts_base.append((s(bx), s(by + 3))); pts_top.append((s(bx + math.cos(th) * hh * 0.25), s(by - hh)))
    col = SPREAD if half == "back" else SPREAD_SURF
    d.polygon(pts_top + pts_base[::-1], fill=col)
    # spikes with droplet tips
    for k in range(n):
        th = 2 * math.pi * (k + 0.5 + offs[k]) / n
        if (math.sin(th) < 0) != (half == "back"): continue
        bx, by = CX + r0 * math.cos(th), YS + r0 * 0.16 * math.sin(th)
        hh = hs[k] * hmul
        tx, ty = bx + math.cos(th) * hh * 0.35, by - hh
        bw = 9
        d.polygon([(s(bx - bw), s(by - hh * 0.3)), (s(bx + bw), s(by - hh * 0.3)), (s(tx), s(ty))], fill=col)
        if t < 0.75:
            rr = 4 + 3 * (k % 3)
            d.ellipse(ell(tx, ty - rr * 0.6, rr, rr * 1.1), fill=col)
    if half == "front":
        for i in range(0, steps, 6):
            x, y = pts_top[i]
            d.ellipse([x - s(3), y + s(4), x + s(3), y + s(14)], fill=SPREAD_HI + (140,))
    return L

def ripples(f):
    L = layer(); d = ImageDraw.Draw(L)
    for k, st in enumerate((F_IMP + 4, F_IMP + 11, F_LIFT + 9)):
        u = (f - st) / 26
        if 0 <= u <= 1:
            r = 55 + 85 * u
            a = int(170 * (1 - u))
            d.ellipse(ell(CX, YS, r, r * 0.16), outline=SPREAD_HI + (a,), width=s(2))
    return clip(L, SURF_MASK)

def surface_gloss():
    L = layer(); d = ImageDraw.Draw(L)
    d.arc(ell(CX - 10, YS - 4, SRX - 22, SRY - 7), 195, 250, fill=SPREAD_HI + (160,), width=s(3))
    d.ellipse(ell(CX + 70, YS - 9, 14, 3), fill=SPREAD_HI + (90,))
    return clip(L, SURF_MASK)

def surface():
    L = layer(); d = ImageDraw.Draw(L)
    d.ellipse(ell(CX, YS, SRX, SRY), fill=SPREAD_SURF + (255,))
    return L

SURF, GLOSS = surface(), surface_gloss()
coat_line = None
random.seed(3)
biscuit_drips = [(26, 10, 5), (58, 22, 6), (101, 14, 5), (140, 26, 6)]

def render(f):
    global coat_line
    im = BACK.copy()
    im.alpha_composite(SURF); im.alpha_composite(GLOSS); im.alpha_composite(ripples(f))
    im.alpha_composite(crown(f, "back"))
    by, ang = biscuit_state(f)
    if by is not None:
        cosA = math.cos(math.radians(ang))
        local = (YS - by) / cosA + BH / 2
        if f >= F_IMP:
            coat_line = local if coat_line is None else min(coat_line, local)
        sub = by + BH / 2 > YS - 4
        nd = int(max(0, min(1, (f - F_LIFT) / 6)) * 4) if f >= F_LIFT else 0
        ds = [(x, ln * min(1, (f - F_LIFT) / 10), r) for (x, ln, r) in biscuit_drips[:nd]] if f >= F_LIFT else []
        spr = biscuit_sprite(coat_line if f >= F_IMP else None, ds)
        if f < F_IMP:  # motion ghosts
            for g, al in ((2, 0.18), (1, 0.32)):
                pb, pa = biscuit_state(max(0, f - g * 0.6))
                im.alpha_composite(clip(place_sprite(spr, CX, pb - 12 * g, pa, al), ABOVE))
        im.alpha_composite(clip(place_sprite(spr, CX, by, ang), ABOVE))
        if sub:  # collar of spread hugging the biscuit
            L = layer(); d = ImageDraw.Draw(L)
            hw = BW / 2 * cosA + 6
            d.ellipse(ell(CX + 3, YS + 1, hw, 7), fill=SPREAD_SURF + (255,))
            d.arc(ell(CX + 3, YS - 1, hw - 8, 5), 200, 340, fill=SPREAD_HI + (170,), width=s(2))
            im.alpha_composite(L)
        # strand during lift
        if F_LIFT <= f < F_GONE:
            bot = by + BH / 2 * cosA + 4
            gap = bot - YS
            if gap < -2 and gap > -95 and f < F_LIFT + 12:
                L = layer(); d = ImageDraw.Draw(L)
                thin = max(3, 14 - (-gap) * 0.12)
                mid = (YS + bot) / 2
                d.polygon([(s(CX - 20), s(YS + 2)), (s(CX - thin), s(mid)), (s(CX - 10), s(bot)),
                           (s(CX + 10), s(bot)), (s(CX + thin), s(mid)), (s(CX + 20), s(YS + 2))], fill=SPREAD_SURF + (255,))
                im.alpha_composite(L)
    im.alpha_composite(crown(f, "front"))
    im.alpha_composite(FRONT)
    # particles
    P = layer(); d = ImageDraw.Draw(P)
    for dr in drops:
        if f < dr.start: continue
        if dr.state == "air":
            draw_drop(d, dr.x, dr.y, dr.vx, dr.vy, dr.r)
        elif dr.state == "splat":
            d.ellipse(ell(dr.x, dr.y, dr.r * 2.1, dr.r * 0.62), fill=SPREAD_SURF)
            d.ellipse(ell(dr.x - dr.r * 0.5, dr.y - dr.r * 0.2, dr.r * 0.7, dr.r * 0.18), fill=SPREAD_HI)
            for (ox, oy, rr) in dr.dots:
                d.ellipse(ell(dr.x + ox, dr.y + oy, rr, rr * 0.55), fill=SPREAD_SURF)
        elif dr.state == "drip":
            w = dr.r * 0.75
            d.rounded_rectangle(box(dr.x - w, JTOP - 2, dr.x + w, JTOP + 4 + dr.dl), radius=s(w), fill=SPREAD_SURF)
            d.ellipse(ell(dr.x, JTOP + 4 + dr.dl, dr.r * 0.95, dr.r * 1.05), fill=SPREAD_SURF)
            d.ellipse(ell(dr.x - dr.r * 0.3, JTOP + 2 + dr.dl, dr.r * 0.25, dr.r * 0.3), fill=SPREAD_HI)
            d.ellipse(ell(dr.x, JTOP - 1, w * 1.6, 4), fill=SPREAD_SURF)
    if f >= F_FADE:
        a = max(0.0, 1 - (f - F_FADE) / (N - F_FADE - 3))
        P.putalpha(P.getchannel("A").point(lambda v: int(v * a)))
    im.alpha_composite(P)
    for dr in drops:
        if f >= dr.start: dr.step()
    return im.convert("RGB").resize((W, H), Image.LANCZOS)

for f in range(N):
    render(f).save(os.path.join(FR, f"f{f:03d}.png"))
print("frames done")

pal = os.path.join(OUT, "palette.png")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "25", "-i", os.path.join(FR, "f%03d.png"),
                "-vf", "palettegen=max_colors=200:stats_mode=full", pal], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "25", "-i", os.path.join(FR, "f%03d.png"), "-i", pal,
                "-lavfi", "paletteuse=dither=sierra2_4a:diff_mode=rectangle", "-loop", "0", os.path.join(OUT, "cutella-splash.gif")], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "25", "-i", os.path.join(FR, "f%03d.png"),
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-movflags", "+faststart", os.path.join(OUT, "cutella-splash.mp4")], check=True)
print("encoded")
