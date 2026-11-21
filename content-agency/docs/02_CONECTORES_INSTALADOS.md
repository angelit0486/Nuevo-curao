# 02 — CONECTORES (investigación e instalación)
Leyenda de estado: **INSTALADO** (existe en la organización) · **CONFIGURADO** (cargado en la sesión) · **AUTENTICADO** (OAuth/credencial válida) · **PROBADO** (llamada real con respuesta correcta) · **PENDIENTE**.

> Los conectores de claude.ai son servidores MCP remotos oficiales del directorio de Anthropic que se conectan por OAuth desde claude.ai → Settings → Connectors. No se instalaron paquetes npm/pip de terceros: no hacía falta y evita software de procedencia dudosa.

## Resumen
| Integración | Tipo | ¿MCP oficial? | Auth | Estado | Prueba realizada |
|---|---|---|---|---|---|
| **Canva** | MCP remoto (directorio) | Sí (Canva) | OAuth | INSTALADO · CONFIGURADO · AUTENTICADO · **PROBADO** | `list-brand-kits` → 0 kits; `search-designs` → 3 diseños devueltos |
| **Exa** (búsqueda web) | MCP remoto | Sí (Exa) | OAuth/API gestionada | **PROBADO** | `web_search_exa` → 5 resultados (Instagram Reels ranking, transparency.meta.com) y 8 tostadoras GDL |
| **WebSearch** | Herramienta nativa Claude Code | n/a | — | **PROBADO** (disponible) | — |
| **Unsplash** | MCP remoto | Sí | OAuth | **PROBADO** | `search_photos "coffee shop product"` → 1.891 resultados |
| **Brandfetch** | MCP remoto | Sí | OAuth | **PROBADO** | `get_brand_data canva.com` → logos, colores, fuentes |
| **Gamma** | MCP remoto | Sí | OAuth | **PROBADO** | `get_themes` → 102 temas |
| **Figma** | MCP remoto | Sí | OAuth | CONFIGURADO · AUTENTICADO (no probado en esta tarea) | — |
| **ElevenLabs** (voz/vídeo/imagen IA) | MCP remoto | Sí | OAuth | CONFIGURADO · **PENDIENTE permisos** | `account_get_usage` → "requires additional permissions" |
| **Google Drive** | MCP remoto | Sí (Google, directorio) | OAuth Google | INSTALADO · **PENDIENTE autenticación** | No cargado en sesión |
| **Google Docs / Sheets** | MCP remoto | Sí | OAuth Google | **PENDIENTE instalación** (no instalados) | — |
| **Supermetrics** (Instagram/Meta Insights) | MCP remoto | Sí (Supermetrics) | OAuth + cuenta Supermetrics (de pago) | INSTALADO · **PENDIENTE** | — |
| **Windsor.ai** (Instagram, Meta Ads, comentarios, posts) | MCP remoto | Sí (Windsor.ai) | OAuth + cuenta Windsor (de pago) | INSTALADO · **PENDIENTE** | — |
| **vidIQ** (investigación YouTube/Instagram/TikTok) | MCP remoto | Sí | OAuth | INSTALADO · **PENDIENTE** | — |
| **Cloudinary** (gestión/transformación de imágenes y vídeo) | MCP remoto | Sí | OAuth | INSTALADO · **PENDIENTE** | — |
| **Make** | MCP remoto | Sí (Make) | OAuth/token Make | **PENDIENTE instalación** | — |
| **n8n** | MCP remoto | Sí (n8n) | Instancia n8n + token | **PENDIENTE instalación** | Plantilla de workflow lista (`automation/`) |
| **Zapier** | MCP remoto | Sí | OAuth | **PENDIENTE** (alternativa a Make/n8n) | — |
| **Instagram Graph API / Meta Business Suite** | API REST (no MCP) | **No hay MCP oficial** en el directorio consultado | OAuth Meta (app de desarrollador + cuenta profesional) | **PENDIENTE** — host bloqueado por red | `curl graph.facebook.com` → bloqueado (000) |
| **Adobe Creative Cloud** | — | No se encontró MCP oficial compatible | — | **NO INSTALADO** (sin opción confiable) | — |
| **Generación de imagen** | Canva `generate-image`, ElevenLabs creative, Figma, Gamma | Sí | ya conectados | Disponible vía Canva/Gamma (no probado para no gastar créditos) | — |
| **Edición audiovisual** | Canva `create-video`, ElevenLabs | Sí | — | Canva disponible; ElevenLabs pendiente | — |

## Detalle por integración (permisos · acciones · limitaciones)
### Canva
- Acciones: buscar/leer diseños, crear y editar diseños, generar diseños e imágenes, kits de marca, plantillas de marca, exportar, carpetas, comentarios, vídeo.
- Permisos: acceso a la cuenta Canva del usuario (OAuth).
- Limitaciones: algunas funciones (Brand Kit, plantillas de marca) requieren Canva Pro/Teams. Regla de la agencia: crear siempre borradores nuevos; no editar diseños existentes sin permiso.
### Exa / WebSearch
- Acciones: búsqueda semántica, lectura de URLs, investigación multi-paso (`agent_run`).
- Limitaciones: no accede a contenido detrás de login (Instagram); verificar fecha de fuentes.
### Unsplash / Brandfetch
- Unsplash: fotos libres para moodboards (atribuir autor). Brandfetch: identidad de marcas por dominio (cuota por plan).
### Google Drive / Docs / Sheets
- Acciones (Drive): buscar, leer, crear, copiar, subir archivos, metadatos y permisos. Sheets: leer/escribir valores. Docs: leer/editar.
- Permisos: OAuth Google con alcance a Drive del usuario. Recomendado: carpeta dedicada `/Content Agency/`.
### Supermetrics / Windsor.ai (analítica Instagram)
- Acciones: consultar métricas de Instagram, Meta Ads, Google Analytics, etc.; Windsor también gestiona posts/comentarios.
- Requisitos: cuenta Instagram **profesional** vinculada a página de Facebook; plan de pago del proveedor (no contratado — requiere decisión del usuario).
- Regla: en la 1ª etapa solo lectura; nada de publicar/responder.
### Instagram Graph API (directo)
- Requiere: app en developers.facebook.com, cuenta profesional, permisos `instagram_basic`, `instagram_manage_insights`, `instagram_content_publish` (publicar requiere revisión de app de Meta), token de larga duración.
- No es un conector MCP: se usaría vía Make/n8n o un servidor propio. Host bloqueado en este entorno.
### Make / n8n
- MCP oficiales que permiten listar/ejecutar escenarios/workflows. Requieren cuenta propia. Ver doc 04 para arquitectura.

## Comandos / acciones ejecutadas
```
ListConnectors · SearchMcpRegistry ["instagram","meta",...] ["google drive",...] ["n8n","make",...]
mcp__Canva__list-brand-kits · mcp__Canva__search-designs
mcp__Exa__web_search_exa (x2) · mcp__Unsplash__search_photos · mcp__Brandfetch__get_brand_data
mcp__Gamma__get_themes · mcp__ElevenLabs__account_get_usage
curl https://graph.facebook.com | graph.instagram.com | api.n8n.io | hook.make.com | www.googleapis.com
```
