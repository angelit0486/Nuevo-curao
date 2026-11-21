# 03 — SKILLS INSTALADAS
Ubicación: **`/home/user/Nuevo-curao/.claude/skills/<nombre>/SKILL.md`** (Skills de proyecto). Se cargan automáticamente en cualquier sesión de Claude Code abierta en este repositorio (cloud, CLI o desktop) y quedan versionadas en git.

Formato: frontmatter YAML (`name`, `description`) + cuerpo Markdown, según el estándar de Agent Skills de Anthropic.

| # | Skill | Función diferenciada | Estado |
|---|---|---|---|
| 01 | `instagram-strategist` | Brief estratégico: segmentos, posicionamiento, pilares, embudo, KPIs, plan 90 d | INSTALADO · PROBADO |
| 02 | `viral-reels-creator` | Conceptos puntuados y guiones con tabla de producción y shot list | INSTALADO · PROBADO (auto-activado) |
| 03 | `hook-engineering` | Trío visual/texto/verbal, 10 mecanismos, test 5/5, variantes A/B | INSTALADO · PROBADO |
| 04 | `creative-director` | Guía visual en hex/px, brief de foto, Reels/carruseles, Canva | INSTALADO · PROBADO |
| 05 | `social-copywriter` | Captions corta/larga, CTA único, banco de objeciones | INSTALADO · PROBADO (auto-activado) |
| 06 | `instagram-seo` | Mapa de keywords, perfil (nombre/bio), SEO por pieza, hashtags | INSTALADO · PROBADO |
| 07 | `content-producer` | Calendario, briefs, plan de rodaje, carpetas, estados y aprobación | INSTALADO · PROBADO |
| 08 | `instagram-analytics` | Fórmulas de tasas, reporte, registro de experimentos | INSTALADO · PROBADO (estructura; sin datos reales) |
| 09 | `competitor-intelligence` | Fichas con fuente, matriz, mapa de posicionamiento, huecos | INSTALADO · PROBADO (auto-activado, con datos reales vía Exa) |
| 10 | `marketing-campaign-builder` | Campañas por fases, embudo, pauta orientativa, atribución, riesgos | INSTALADO · PROBADO (estructura) |

Cada SKILL.md contiene: nombre y descripción · rol · información mínima y **criterios para pedir datos faltantes** · procedimiento paso a paso · plantillas reutilizables · criterios de calidad (checklist) · reglas para evitar errores · ejemplo entrada/salida · colaboración con otras Skills.

## Validación automática
```bash
python3 content-agency/automation/validate_skills.py
```
Comprueba frontmatter, `name` = nombre de directorio, descripción ≤ 1024 caracteres y presencia de las 7 secciones obligatorias. Resultado actual: **10/10 OK**.

## Mantenimiento
- Editar el SKILL.md correspondiente → ejecutar el validador → commit.
- Para añadir una Skill: crear `.claude/skills/<nombre>/SKILL.md`, añadirla a la tabla de selección en `content-agency/CLAUDE_CONTENT_AGENCY.md` §3.
- Revisar cada trimestre las reglas de plataforma (originalidad, duración recomendable, métricas) con búsqueda en fuentes oficiales.
- Para usarlas fuera de este repo (todas tus sesiones): copiar las carpetas a `~/.claude/skills/` en tu máquina local (en la nube esa ruta se borra al terminar la sesión).
