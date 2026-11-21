"""Valida las Skills de la agencia: frontmatter, nombre=directorio, secciones obligatorias."""
import pathlib, re, sys
REQ = ["Información mínima", "Procedimiento", "Plantilla", "Criterios de calidad", "Reglas para evitar errores", "Ejemplo", "Colaboración"]
root = pathlib.Path(__file__).resolve().parents[2] / ".claude" / "skills"
ok = True
for d in sorted(p for p in root.iterdir() if p.is_dir()):
    f = d / "SKILL.md"; txt = f.read_text(encoding="utf-8")
    m = re.match(r"^---\nname: (.+)\ndescription: (.+?)\n---\n", txt, re.S)
    errs = []
    if not m: errs.append("frontmatter inválido")
    else:
        if m.group(1).strip() != d.name: errs.append("name != directorio")
        if len(m.group(2)) > 1024: errs.append("description > 1024")
    errs += [f"falta sección '{s}'" for s in REQ if s not in txt]
    print(f"{'OK ' if not errs else 'ERR'} {d.name:28} {len(txt.splitlines()):4} líneas {'; '.join(errs)}")
    ok &= not errs
sys.exit(0 if ok else 1)
