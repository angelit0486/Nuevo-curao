"""Renderiza Reels 'Mito vs Verdad' (1080x1920, 30 fps) en la estética Alien Demon.

Uso:  python3 render_reel_mito.py config.json salida.mp4
El config define el texto de cada escena; ver CONFIG_GLAUCOMA abajo como ejemplo.
Sin dependencias externas salvo Pillow, numpy y ffmpeg.
"""
import json, math, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H, FPS = 1080, 1920, 30
BLACK = (5, 7, 10); GREEN = (57, 255, 20); SILVER = (201, 206, 214); WHITE = (242, 245, 247); GRAPH = (26, 31, 38)
FONT_DIR = "/usr/share/fonts/opentype/inter/"
def font(weight, size):
    return ImageFont.truetype(FONT_DIR + {"black": "Inter-Black.otf", "bold": "Inter-Bold.otf",
                                          "semi": "Inter-SemiBold.otf", "reg": "Inter-Regular.otf"}[weight], size)

CONFIG_GLAUCOMA = {
    "series": "MITO VS VERDAD",
    "hook": ["¿Cura el", "GLAUCOMA?"], "hook_sub": "Esto dice la ciencia",
    "verdict": "MITO",
    "evidence_title": "Revisión de las Academias Nacionales de EE. UU. (2017)",
    "evidence_claim": ["Cannabinoides para la", "presión del ojo", "en glaucoma"],
    "evidence_level": "LIMITADA · NO EFECTIVO",
    "takeaway": ["El glaucoma se trata", "con tu oftalmólogo."],
    "source": "Fuente: NASEM 2017, conclusión 4-14",
    "cta": "Envíaselo a quien todavía lo cree",
    "brand": "ALIEN DEMON", "brand_sub": "Información con fuentes",
    "disclaimer": "Contenido informativo para adultos. No es consejo médico.",
}

def ease(t):  # easeOutCubic, t en [0,1]
    t = max(0.0, min(1.0, t)); return 1 - (1 - t) ** 3
def seg(t, a, b):
    return 0.0 if t <= a else 1.0 if t >= b else (t - a) / (b - a)

def text_center(d, y, s, f, fill, alpha=1.0, base=None):
    w = d.textlength(s, font=f); x = (W - w) / 2
    col = tuple(int(c * alpha + bc * (1 - alpha)) for c, bc in zip(fill, base or BLACK))
    d.text((x, y), s, font=f, fill=col); return x, w

def glow_layer(img, radius=18, strength=1.0):
    g = img.filter(ImageFilter.GaussianBlur(radius))
    return Image.blend(Image.new("RGB", img.size, BLACK), g, min(1.0, strength))

def background(t):
    img = Image.new("RGB", (W, H), BLACK); d = ImageDraw.Draw(img)
    # retícula tenue
    for x in range(0, W, 90): d.line([(x, 0), (x, H)], fill=(10, 13, 17))
    for y in range(0, H, 90): d.line([(0, y), (W, y)], fill=(10, 13, 17))
    # marco HUD
    d.line([(60, 200), (60, 1700)], fill=GRAPH, width=3); d.line([(W - 60, 200), (W - 60, 1700)], fill=GRAPH, width=3)
    d.line([(60, 200), (220, 200)], fill=GREEN, width=3); d.line([(W - 220, 1700), (W - 60, 1700)], fill=GREEN, width=3)
    return img, d

def draw_tunnel(d, t):
    vx, vy = W / 2, 820
    for i in range(14):
        z = ((i / 14) + t * 0.9) % 1.0; s = z ** 2.2
        w2, h2 = 40 + s * 900, 30 + s * 1500
        c = tuple(int(v * (0.25 + 0.75 * s)) for v in GREEN)
        d.rectangle([vx - w2, vy - h2 * 0.55, vx + w2, vy + h2 * 0.45], outline=c, width=max(1, int(1 + s * 5)))

def draw_eye(d, cx, cy, r, prog, col=GREEN, width=8):
    # contorno de almendra dibujado progresivamente
    pts = []
    for k in range(0, 101):
        a = k / 100 * 2 * math.pi
        pts.append((cx + r * math.cos(a), cy + r * 0.48 * math.sin(a) * abs(math.sin(a)) ** 0.2 * (1 if math.sin(a) >= 0 else 1)))
    n = int(len(pts) * ease(prog))
    if n > 1: d.line(pts[:n], fill=col, width=width, joint="curve")
    if prog > 0.6:
        a = ease(seg(prog, 0.6, 1.0)); rr = r * 0.32 * a
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], outline=col, width=width)
        rr2 = r * 0.12 * a; d.ellipse([cx - rr2, cy - rr2, cx + rr2, cy + rr2], fill=col)

def frame(t, C):
    img, d = background(t); glow = Image.new("RGB", (W, H), BLACK); g = ImageDraw.Draw(glow)
    fs, fh, fm = font("bold", 34), font("black", 150), font("semi", 54)
    # etiqueta de serie (siempre)
    d.text((90, 232), C["series"], font=fs, fill=SILVER)

    if t < 2.4:  # INTRO túnel + hook
        draw_tunnel(g, t)
        a = ease(seg(t, 0.4, 1.4))
        text_center(d, 640, C["hook"][0], fh, WHITE, a); text_center(d, 800, C["hook"][1], fh, GREEN, a)
        text_center(g, 800, C["hook"][1], fh, GREEN, a)
        text_center(d, 990, C["hook_sub"], fm, WHITE, ease(seg(t, 1.2, 2.0)))
    elif t < 6.0:  # ojo se dibuja + hook arriba
        p = seg(t, 2.4, 4.6)
        draw_eye(d, W / 2, 1060, 300, p); draw_eye(g, W / 2, 1060, 300, p, width=14)
        text_center(d, 420, C["hook"][0], font("black", 110), WHITE)
        text_center(d, 540, C["hook"][1], font("black", 110), GREEN); text_center(g, 540, C["hook"][1], font("black", 110), GREEN)
    elif t < 9.2:  # veredicto: sello MITO con glitch
        draw_eye(d, W / 2, 1060, 300, 1.0, col=(30, 60, 25))
        p = ease(seg(t, 6.0, 6.5)); sz = int(260 * (1.6 - 0.6 * p))
        fv = font("black", sz); jitter = (np.random.randint(-14, 15) if t < 6.6 else 0)
        tw = d.textlength(C["verdict"], font=fv); x = (W - tw) / 2 + jitter; y = 960 - sz / 2
        pad = 40
        d.rectangle([x - pad, y - 10, x + tw + pad, y + sz * 1.05], outline=GREEN, width=12)
        g.rectangle([x - pad, y - 10, x + tw + pad, y + sz * 1.05], outline=GREEN, width=20)
        d.text((x, y - sz * 0.08), C["verdict"], font=fv, fill=WHITE)
        text_center(d, 1330, "Es de los mitos más repetidos.", fm, WHITE, ease(seg(t, 7.0, 7.8)))
    elif t < 14.0:  # evidencia
        a = ease(seg(t, 9.2, 9.8))
        text_center(d, 420, C["evidence_title"], font("semi", 38), SILVER, a)
        for i, line in enumerate(C["evidence_claim"]):
            text_center(d, 560 + i * 96, line, font("bold", 78), WHITE, ease(seg(t, 9.4 + i * 0.25, 10.2 + i * 0.25)))
        # barra de evidencia: 4 niveles, se queda en "limitada" hacia el lado NO
        bx, by, bw, bh = 140, 1040, W - 280, 70
        labels = ["NO EFECTIVO", "", "", "EFECTIVO"]
        d.rectangle([bx, by, bx + bw, by + bh], outline=SILVER, width=4)
        fill = ease(seg(t, 10.8, 12.0)) * 0.22
        d.rectangle([bx + 6, by + 6, bx + 6 + (bw - 12) * fill, by + bh - 6], fill=GREEN)
        g.rectangle([bx + 6, by + 6, bx + 6 + (bw - 12) * fill, by + bh - 6], fill=GREEN)
        d.text((bx, by + bh + 18), labels[0], font=font("semi", 30), fill=SILVER)
        d.text((bx + bw - d.textlength(labels[3], font=font("semi", 30)), by + bh + 18), labels[3], font=font("semi", 30), fill=SILVER)
        text_center(d, 1240, "Nivel de evidencia:", fm, WHITE, ease(seg(t, 11.8, 12.4)))
        text_center(d, 1320, C["evidence_level"], font("black", 66), GREEN, ease(seg(t, 12.0, 12.6)))
        text_center(g, 1320, C["evidence_level"], font("black", 66), GREEN, ease(seg(t, 12.0, 12.6)))
    elif t < 17.4:  # takeaway
        for i, line in enumerate(C["takeaway"]):
            text_center(d, 820 + i * 120, line, font("black", 92), WHITE if i == 0 else GREEN, ease(seg(t, 14.0 + i * 0.3, 14.8 + i * 0.3)))
        text_center(g, 940, C["takeaway"][1], font("black", 92), GREEN, ease(seg(t, 14.3, 15.1)))
    else:  # cierre: fuente + CTA + marca
        a = ease(seg(t, 17.4, 18.0))
        text_center(d, 560, C["brand"], font("black", 120), WHITE, a); text_center(g, 560, C["brand"], font("black", 120), GREEN, a * 0.6)
        text_center(d, 710, C["brand_sub"], font("semi", 48), GREEN, a)
        text_center(d, 1000, C["cta"], font("bold", 56), WHITE, ease(seg(t, 17.8, 18.4)))
        text_center(d, 1380, C["source"], font("semi", 36), SILVER, ease(seg(t, 18.0, 18.6)))
        text_center(d, 1440, C["disclaimer"], font("reg", 30), SILVER, ease(seg(t, 18.0, 18.6)))

    out = Image.blend(img, glow_layer(glow), 0.0)
    out = Image.fromarray(np.clip(np.asarray(img, dtype=np.int16) + np.asarray(glow_layer(glow), dtype=np.int16) * 0.9, 0, 255).astype(np.uint8))
    # scanline + grano sutil
    arr = np.asarray(out, dtype=np.int16)
    arr[::4] = (arr[::4] * 0.88).astype(np.int16)
    arr += np.random.randint(-6, 7, arr.shape[:2] + (1,), dtype=np.int16)
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

def render(C, out_path, duration=20.0):
    # audio: drone grave + "ping" en cada cambio de escena
    beats = [0.0, 2.4, 6.0, 9.2, 14.0, 17.4]
    pings = "+".join(f"0.35*sin(2*PI*1320*t)*exp(-6*(t-{b}))*gte(t,{b})" for b in beats)
    aexpr = f"0.18*sin(2*PI*55*t)+0.08*sin(2*PI*110.5*t)+{pings}"
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-i", f"aevalsrc='{aexpr}':s=48000:d={duration}",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "20", "-b:v", "0",
           "-c:a", "aac", "-b:a", "160k", "-af", "loudnorm=I=-16:TP=-1.5", "-shortest", "-movflags", "+faststart", out_path]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    np.random.seed(7)
    for i in range(int(duration * FPS)):
        p.stdin.write(frame(i / FPS, C).tobytes())
    p.stdin.close(); p.wait()
    if p.returncode: raise SystemExit("ffmpeg falló")

if __name__ == "__main__":
    cfg = json.load(open(sys.argv[1], encoding="utf-8")) if len(sys.argv) > 2 else CONFIG_GLAUCOMA
    render(cfg, sys.argv[-1] if len(sys.argv) > 1 else "reel.mp4")
