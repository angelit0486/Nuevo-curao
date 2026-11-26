"""Reel 'Mitos y verdades' en formato lista (varios mitos por video), estética Alien Demon.

Uso:  python3 render_reel_lista.py salida.mp4 [config.json]
Reutiliza estilos y helpers de render_reel_mito.py.
"""
import json, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw
from render_reel_mito import (W, H, FPS, BLACK, GREEN, SILVER, WHITE, GRAPH, font, ease, seg,
                              text_center, glow_layer, background, draw_tunnel)

CONFIG_WAX = {
    "series": "MITOS Y VERDADES",
    "hook": ["4 mitos del", "WAX"], "hook_sub": "que casi todos creen",
    "items": [
        {"mito": "“Es solo marihuana más pura.”",
         "verdad": "Es un concentrado: en promedio 54–69% de THC, y hay muestras de más de 80%. La flor ronda 15%.",
         "fuente": "NIDA, Marijuana Concentrates (2020)"},
        {"mito": "“Más potente = más seguro porque usas menos.”",
         "verdad": "La dosis entra de golpe. El uso diario de cannabis de alta potencia se asoció con 4.8 veces más probabilidad de psicosis.",
         "fuente": "Di Forti et al., The Lancet Psychiatry (2019)"},
        {"mito": "“Hacerlo en casa no tiene riesgo.”",
         "verdad": "La extracción casera con butano ha causado incendios, explosiones y quemaduras graves.",
         "fuente": "NIDA (2020)"},
        {"mito": "“En vape es más sano.”",
         "verdad": "En EE. UU., productos de vapeo con THC de fuentes informales se ligaron a 2,807 hospitalizados y 68 muertes (2019–2020).",
         "fuente": "CDC, brote EVALI (2020)"},
    ],
    "close_title": "Infórmate con datos,", "close_title2": "no con rumores.",
    "cta": "Envíaselo a quien cree que es “más puro”",
    "legal": "En México los vapeadores están prohibidos por la Constitución (2025).",
    "disclaimer": "Contenido informativo para adultos. No es consejo médico ni invitación al consumo.",
    "brand": "ALIEN DEMON",
}

HOOK_END, ITEM_LEN, CLOSE_LEN = 3.0, 6.2, 4.0

def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if d.textlength(test, font=f) <= maxw: cur = test
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def item_frame(d, g, t0, t, i, n, it):
    lt = t - t0
    # encabezado de número
    d.text((90, 300), f"MITO {i + 1}/{n}", font=font("bold", 40), fill=GREEN)
    # mito: aparece y luego se tacha
    fm = font("bold", 66)
    lines = wrap(d, it["mito"], fm, W - 200)
    y = 420
    a = ease(seg(lt, 0.0, 0.5))
    for ln in lines:
        x, w = text_center(d, y, ln, fm, WHITE, a * (1 - 0.55 * ease(seg(lt, 1.6, 2.0))))
        s = ease(seg(lt, 1.3, 1.9))
        if s > 0: d.line([(x - 10, y + 44), (x - 10 + (w + 20) * s, y + 44)], fill=GREEN, width=8)
        y += 84
    # sello VERDAD + texto
    if lt > 1.9:
        vy = max(y + 70, 760)
        ap = ease(seg(lt, 1.9, 2.3))
        fv = font("black", 72); tw = d.textlength("VERDAD", font=fv); vx = (W - tw) / 2
        d.rectangle([vx - 30, vy - 8, vx + tw + 30, vy + 92], outline=GREEN, width=6)
        g.rectangle([vx - 30, vy - 8, vx + tw + 30, vy + 92], outline=GREEN, width=12)
        d.text((vx, vy), "VERDAD", font=fv, fill=tuple(int(c * ap) for c in GREEN))
        ft = font("semi", 52); yy = vy + 150
        for k, ln in enumerate(wrap(d, it["verdad"], ft, W - 200)):
            text_center(d, yy, ln, ft, WHITE, ease(seg(lt, 2.2 + k * 0.12, 2.8 + k * 0.12))); yy += 68
        text_center(d, max(yy + 40, 1500), "Fuente: " + it["fuente"], font("reg", 32), SILVER, ease(seg(lt, 2.8, 3.3)))
    # barra de progreso inferior
    d.rectangle([90, 1640, 90 + (W - 180) * min(1, lt / ITEM_LEN), 1646], fill=GREEN)

def frame(t, C):
    img, d = background(t); glow = Image.new("RGB", (W, H), BLACK); g = ImageDraw.Draw(glow)
    d.text((90, 232), C["series"], font=font("bold", 34), fill=SILVER)
    n = len(C["items"])
    if t < HOOK_END:
        draw_tunnel(g, t)
        a = ease(seg(t, 0.2, 1.0)); fh = font("black", 140)
        text_center(d, 650, C["hook"][0], fh, WHITE, a)
        text_center(d, 810, C["hook"][1], font("black", 220), GREEN, a); text_center(g, 810, C["hook"][1], font("black", 220), GREEN, a)
        text_center(d, 1080, C["hook_sub"], font("semi", 56), WHITE, ease(seg(t, 0.9, 1.6)))
    elif t < HOOK_END + n * ITEM_LEN:
        i = int((t - HOOK_END) // ITEM_LEN)
        item_frame(d, g, HOOK_END + i * ITEM_LEN, t, i, n, C["items"][i])
    else:
        t0 = HOOK_END + n * ITEM_LEN; a = ease(seg(t, t0, t0 + 0.6))
        text_center(d, 520, C["close_title"], font("black", 84), WHITE, a)
        text_center(d, 620, C["close_title2"], font("black", 84), GREEN, a); text_center(g, 620, C["close_title2"], font("black", 84), GREEN, a)
        text_center(d, 860, C["cta"], font("bold", 50), WHITE, ease(seg(t, t0 + 0.4, t0 + 1.0)))
        text_center(d, 1120, C["brand"], font("black", 96), WHITE, ease(seg(t, t0 + 0.6, t0 + 1.2)))
        text_center(g, 1120, C["brand"], font("black", 96), GREEN, 0.5 * ease(seg(t, t0 + 0.6, t0 + 1.2)))
        ff = font("reg", 30); yy = 1380
        for s in (C["legal"], C["disclaimer"]):
            for ln in wrap(d, s, ff, W - 220):
                text_center(d, yy, ln, ff, SILVER, ease(seg(t, t0 + 0.8, t0 + 1.4))); yy += 42
    arr = np.clip(np.asarray(img, dtype=np.int16) + np.asarray(glow_layer(glow), dtype=np.int16) * 0.9, 0, 255)
    arr[::4] = (arr[::4] * 0.88)
    arr += np.random.randint(-4, 5, arr.shape[:2] + (1,), dtype=np.int16)
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

def render(C, out):
    n = len(C["items"]); dur = HOOK_END + n * ITEM_LEN + CLOSE_LEN
    beats = [0.0, HOOK_END] + [HOOK_END + i * ITEM_LEN + 1.9 for i in range(n)] + [HOOK_END + i * ITEM_LEN for i in range(1, n)] + [HOOK_END + n * ITEM_LEN]
    pings = "+".join(f"0.3*sin(2*PI*1320*t)*exp(-6*(t-{b:.2f}))*gte(t,{b:.2f})" for b in beats)
    aexpr = f"0.18*sin(2*PI*55*t)+0.08*sin(2*PI*110.5*t)+{pings}"
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-i", f"aevalsrc='{aexpr}':s=48000:d={dur}",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "slow", "-crf", "26", "-tune", "grain",
           "-c:a", "aac", "-b:a", "160k", "-af", "loudnorm=I=-16:TP=-1.5", "-shortest", "-movflags", "+faststart", out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE); np.random.seed(11)
    for i in range(int(dur * FPS)): p.stdin.write(frame(i / FPS, C).tobytes())
    p.stdin.close(); p.wait()
    if p.returncode: raise SystemExit("ffmpeg falló")

if __name__ == "__main__":
    cfg = json.load(open(sys.argv[2], encoding="utf-8")) if len(sys.argv) > 2 else CONFIG_WAX
    render(cfg, sys.argv[1])
