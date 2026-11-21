# 05 — GUÍA DE AUTENTICACIÓN (acciones que debes hacer tú)
Nunca pegues contraseñas, tokens ni API keys en el chat. Todas las conexiones se hacen por OAuth en las páginas oficiales o en el gestor de credenciales de cada herramienta.

**Página de conectores:** https://claude.ai/customize/connectors
Después de conectar algo, **abre una sesión nueva**: los conectores se leen al iniciar la sesión.

## Prioridad 1 — Google Drive (detección y organización de materiales)
1. Abre https://claude.ai/customize/connectors → **Google Drive** (ya instalado, estado "no conectado") → **Connect**.
2. Inicia sesión con la cuenta de Google donde estarán los materiales y acepta los permisos.
3. (Recomendado) Crea en Drive la carpeta `/Content Agency/<Marca>/` con las subcarpetas del doc 06.
4. Opcional: en la misma página busca e instala **Google Sheets** y **Google Docs** (no instalados) para el tablero y los reportes.
5. Nueva sesión → pídeme "prueba el conector de Google Drive" y verificaré con una búsqueda de solo lectura.

## Prioridad 2 — Canva (ya autenticado ✅)
- Opcional: crear un **Brand Kit** en Canva (requiere Canva Pro/Teams) para que los diseños hereden tu marca. Puedo prepararlo si me das logo/colores y me autorizas.

## Prioridad 3 — Investigación web (Exa ✅, WebSearch ✅) — nada que hacer.

## Prioridad 4 — Instagram / Meta (métricas y, más adelante, publicación)
No existe conector MCP oficial de Instagram. Opciones, de menor a mayor esfuerzo:
**A. Analítica vía conector (recomendado para empezar)** — Supermetrics o Windsor.ai (ya instalados, "conexión incompleta"):
1. Requisito: tu Instagram debe ser **cuenta profesional** (Configuración → Tipo de cuenta y herramientas → Cambiar a cuenta profesional) y estar vinculada a una página de Facebook.
2. https://claude.ai/customize/connectors → Supermetrics **o** Windsor.ai → completar conexión.
3. Dentro del proveedor, conecta la fuente "Instagram Insights". ⚠️ Ambos son servicios de pago: revisa su plan antes; yo no contrato nada.
**B. Sin conector:** exporta Insights o envíame capturas; la Skill `instagram-analytics` trabaja con ellas.
**C. API directa (fase 2, vía n8n/Make):** crear app en https://developers.facebook.com → producto "Instagram" → permisos `instagram_basic`, `instagram_manage_insights` (lectura) y, solo cuando decidas automatizar publicación, `instagram_content_publish` (requiere revisión de Meta). El token se guarda en n8n/Make, nunca aquí.

## Prioridad 5 — Automatización (Make o n8n)
1. Elige una: n8n (más control, puede ser self-hosted) o Make.
2. https://claude.ai/customize/connectors → busca **n8n** o **Make** → instalar → conectar con tu cuenta.
3. En n8n: Workflows → Import from file → `content-agency/automation/n8n_drive_to_brief.workflow.json`. Crea las credenciales "Google Drive — Agencia", "Google Sheets — Agencia" y "Anthropic API (x-api-key)" (Header Auth, nombre `x-api-key`, valor tu clave de console.anthropic.com). Reemplaza los `REEMPLAZAR_*`. **Déjalo inactivo** hasta revisarlo conmigo.
4. Si quieres que este entorno cloud llame a n8n/Make/Meta directamente, habría que permitir esos hosts en la red del entorno: pídemelo y te mostraré la propuesta de cambio para que la apruebes.

## Prioridad 6 — Opcionales
| Conector | Para qué | Acción |
|---|---|---|
| ElevenLabs | Voz en off / vídeo IA | Reconectar en connectors con permisos completos (hoy da "requires additional permissions") |
| vidIQ | Ideas/tendencias de vídeo corto | Completar conexión |
| Cloudinary | Biblioteca y transformación de medios | Completar conexión |
| Similarweb | Tráfico web de competidores | Completar conexión (el plugin también necesita red) |

## Verificación tras cada conexión
Pídeme: "verifica conectores". Ejecutaré una llamada de solo lectura y actualizaré `02_CONECTORES_INSTALADOS.md` y `07_RESULTADOS_DE_PRUEBAS.md`.
