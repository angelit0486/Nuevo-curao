# 07 — RESULTADOS DE PRUEBAS (2026-11-21)
Cliente de prueba para A–D: **Tostadora Cielo** (ficticio, café de especialidad en Guadalajara). En E se investigaron **competidores reales** con datos públicos.

| Prueba | Qué se probó | Skills | Resultado | Evidencia |
|---|---|---|---|---|
| A | Estrategia de crecimiento para tienda comercial | competitor-intelligence → instagram-strategist → instagram-seo | ✅ PASA | `tests/PRUEBA_A_estrategia.md` |
| B | 5 conceptos de Reels para un producto | viral-reels-creator → hook-engineering | ✅ PASA | `tests/PRUEBA_B_conceptos_reels.md` |
| C | Guion audiovisual completo | viral-reels-creator → hook-engineering → creative-director → social-copywriter → instagram-seo | ✅ PASA | `tests/PRUEBA_C_guion.md` |
| D | Calendario de 7 días | content-producer (+4) | ✅ PASA | `tests/PRUEBA_D_calendario_7_dias.md` |
| E | Auditoría de competidores | competitor-intelligence (Exa real) → instagram-strategist | ✅ PASA | `tests/PRUEBA_E_auditoria_competidores.md` |
| F | Activación y colaboración automática de Skills | 3 sesiones `claude -p` independientes | ✅ PASA | ver abajo |
| G | Respuesta de conectores MCP | Canva, Exa, Unsplash, Brandfetch, Gamma, ElevenLabs | ⚠️ PARCIAL (5/6 OK) | ver abajo |
| H | Permisos, dependencias, autenticación | validador, red, credenciales | ⚠️ PARCIAL | ver abajo |

## Prueba F — enrutamiento automático
Comando: `claude -p "<pedido>" --output-format stream-json --verbose --max-turns 6` (sesiones nuevas, sin mencionar nombres de Skills).
| Pedido | Skill invocada automáticamente | Comportamiento observado |
|---|---|---|
| "5 conceptos de Reels para una crema de manos artesanal… Puebla" | `viral-reels-creator` | Anunció "Skills: viral-reels-creator", declaró supuestos, puntuación /20 |
| "Caption con CTA para Reel de panadería…" | `social-copywriter` | Usó marcadores `[HORARIO DE HORNEADO]`, `[UBICACIÓN]` en vez de inventar |
| "Analiza a la competencia de una barbería en Monterrey…" | `competitor-intelligence` → `instagram-strategist` | Avisó "versión rápida sin investigación, todo es [SUPUESTO]" |
Además, al crearlas, las 10 Skills aparecieron registradas en la sesión de instalación.

## Prueba G — conectores
| Conector | Llamada | Resultado |
|---|---|---|
| Canva | `list-brand-kits`, `search-designs` | ✅ 0 brand kits; 3 diseños listados |
| Exa | `web_search_exa` ×2 | ✅ resultados reales con fuentes |
| Unsplash | `search_photos` | ✅ 1.891 resultados |
| Brandfetch | `get_brand_data canva.com` | ✅ datos completos |
| Gamma | `get_themes` | ✅ 102 temas |
| ElevenLabs | `account_get_usage` | ❌ "requires additional permissions" → reconectar |
| Google Drive, Supermetrics, Windsor.ai, Make, n8n | — | ⏳ no conectados (requieren al usuario) |

## Prueba H — permisos, dependencias, autenticación
| Comprobación | Resultado |
|---|---|
| Validador de Skills (`validate_skills.py`) | ✅ 10/10 OK (tras corregir 1 sección faltante en instagram-analytics) |
| JSON de workflow n8n | ✅ válido, `active: false` |
| Escaneo de secretos en archivos nuevos | ✅ sin secretos |
| Dependencias | ✅ ninguna nueva (solo Python estándar); app Next.js intacta |
| Red a Meta/n8n/Make | ❌ bloqueada por política del entorno (esperado; documentado en 08) |
| Autenticaciones pendientes | ⏳ Google Drive, analítica Instagram, automatización, ElevenLabs |
| Plugins de marketing con MCP (ahrefs, hubspot, notion, slack, etc.) | ❌ fallan por proxy 403 — no bloqueante para la agencia |

## Leyenda final de estado
- **INSTALADO**: 10 Skills, coordinador, plantilla n8n, validador, documentación.
- **CONFIGURADO**: CLAUDE.md importa el coordinador; conectores cargados en sesión.
- **AUTENTICADO**: Canva, Exa, Unsplash, Brandfetch, Gamma, Figma.
- **PROBADO**: Skills (A–F), Canva, Exa, Unsplash, Brandfetch, Gamma.
- **PENDIENTE**: Google Drive/Docs/Sheets, Instagram/Meta, Make/n8n, Supermetrics/Windsor, ElevenLabs (permisos).
