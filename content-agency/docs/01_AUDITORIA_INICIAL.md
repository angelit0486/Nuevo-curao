# 01 — AUDITORÍA INICIAL DEL ENTORNO
Fecha: 2026-11-21 · Ejecutada por Claude Code (sesión cloud)

## 1. Entorno detectado
| Elemento | Valor | Cómo se verificó |
|---|---|---|
| Tipo de entorno | **Claude Code en la nube** (claude.ai/code), contenedor efímero | Contexto de sesión + `~/.claude/` |
| Versión Claude Code | 2.1.330 | `claude --version` |
| Sistema operativo | Linux x86_64 (kernel 6.18.44) | `uname -a` |
| Node.js / npm | v22.23.5 / 10.9.9 | `node -v`, `npm -v` |
| Python | 3.13.18 | `python3 --version` |
| Repositorio | `angelit0486/Nuevo-curao` (app Next.js 16.3.4 "app-cursos") | `git`, `package.json` |
| Rama de trabajo | `ccr-988f4b5a-x6mm59` | `git branch` |
| Red | Política **limitada**: registros de paquetes y servidores MCP permitidos; resto de hosts bloqueados por proxy | `get_environment`, `curl` |

## 2. Conectores MCP existentes (claude.ai, nivel organización)
**Conectados y cargados en sesión:** Canva, Exa, Unsplash, Brandfetch, Gamma, Figma, ElevenLabs (*permisos insuficientes*), Supabase, Vercel, Lovable, Macaly Cloud, Mobbin, tldraw, Three.js, Anthropic Economic Index, Claude Docs, GitHub.
**Instalados pero sin completar conexión:** Google Drive, Supermetrics, Windsor.ai, vidIQ, Cloudinary, Similarweb, HTML/CSS to Image, Linear, Mem0, Send, Webflow, Base44, Khan Academy, Viberate.
**Plugins de marketing con MCP que fallan por red** (proxy 403): ahrefs, amplitude, hubspot, klaviyo, notion, similarweb, slack, supermetrics, asana, atlassian, clickup, linear, monday, hex, definite, intercom, sentry; bigquery (incompatible con registro dinámico OAuth).

## 3. Skills existentes
- Usuario (`~/.claude/skills`): `session-start-hook` (sistema).
- Plugins: marketing (campaign-plan, content-creation, competitive-brief, seo-audit, draft-content, performance-report, brand-review, email-sequence), design, data, productivity, superpowers, etc.
- Proyecto (`.claude/skills`): **no existía** → sin riesgo de duplicado.
- Solapamiento evaluado: los skills genéricos del plugin `marketing` cubren marketing multicanal; las nuevas Skills son **específicas de Instagram** (Reels, hooks, SEO de Instagram, métricas de Instagram), por lo que se complementan y no se duplican.

## 4. Problemas detectados
| # | Problema | Impacto | Acción |
|---|---|---|---|
| P1 | `graph.facebook.com` y `graph.instagram.com` bloqueados por la red del entorno | No se puede usar la API de Instagram desde aquí | Pendiente (doc 08) |
| P2 | No existe conector MCP oficial de Instagram/Meta en el directorio consultado | Publicación/métricas nativas no disponibles | Alternativas: Supermetrics/Windsor.ai (analítica), Make/n8n/Zapier (programación) |
| P3 | Google Drive instalado pero no conectado | Sin detección de materiales | Requiere OAuth del usuario (doc 05) |
| P4 | ElevenLabs: "requiere permisos adicionales" | Sin voz en off generada | Reconectar con permisos (doc 05) |
| P5 | Canva sin Brand Kit | Diseños no heredan marca automáticamente | Crear Brand Kit en Canva (acción del usuario o con aprobación) |
| P6 | Contenedor efímero | Lo instalado en `~/.claude` se pierde | Todo se instaló en el **repositorio** (`.claude/skills`, `content-agency/`) y se versiona en git |
| P7 | Muchos MCP de plugins fallan por proxy | Ruido en sesiones, no bloqueante | Documentado; habilitar hosts solo si se van a usar |

## 5. Permisos y restricciones
- Puedo: editar el repositorio, ejecutar comandos, usar conectores conectados, hacer commits y push a la rama de trabajo.
- No puedo (ni debo sin el usuario): completar OAuth de conectores, crear cuentas, comprar planes, publicar en Instagram, ampliar la red del entorno sin aprobación.

## 6. Plan de instalación priorizado (ejecutado)
1. ✅ Verificar conectores ya disponibles (Canva, Exa, Unsplash, Brandfetch, Gamma) con pruebas de solo lectura.
2. ✅ Investigar conectores para Google, Meta/Instagram, automatización (registro MCP).
3. ✅ Crear e instalar 10 Skills en `.claude/skills/` (nivel proyecto, persistente).
4. ✅ Crear coordinador `content-agency/CLAUDE_CONTENT_AGENCY.md` e importarlo en `CLAUDE.md` (respaldo previo).
5. ✅ Preparar automatización (plantilla n8n inactiva + arquitectura).
6. ✅ Pruebas A–H.
7. ⏳ Autenticaciones que requieren al usuario (Google Drive, Supermetrics/Windsor, Make/n8n, ElevenLabs).
