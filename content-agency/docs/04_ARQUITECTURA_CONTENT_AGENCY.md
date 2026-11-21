# 04 — ARQUITECTURA CLAUDE ELITE CONTENT AGENCY

## 1. Capas
```
┌──────────────────────────────── INTERFAZ ─────────────────────────────────┐
│ Claude Code (cloud/CLI/desktop) en el repo Nuevo-curao                    │
├──────────────────────────── COORDINACIÓN ─────────────────────────────────┤
│ CLAUDE.md → @content-agency/CLAUDE_CONTENT_AGENCY.md (Director de Cuenta)  │
│ Selección de Skills · orden de encadenado · QC · aprobación humana        │
├────────────────────────────── ESPECIALISTAS ──────────────────────────────┤
│ .claude/skills/  (10 Skills)                                              │
├─────────────────────────────── HERRAMIENTAS ──────────────────────────────┤
│ Investigación: Exa, WebSearch · Visual: Canva, Unsplash, Brandfetch,      │
│ Gamma, Figma · Voz/vídeo IA: ElevenLabs (pend.) · Archivos: Google Drive  │
│ (pend.) · Analítica: Supermetrics/Windsor (pend.) · Datos: Supabase       │
├──────────────────────────── AUTOMATIZACIÓN (fase 2) ──────────────────────┤
│ n8n o Make  ⇄ Google Drive/Sheets ⇄ API de Claude ⇄ Instagram Graph API   │
└───────────────────────────────────────────────────────────────────────────┘
Persistencia: content-agency/clientes/<marca>/ (git) + Google Drive (cuando se conecte)
```

## 2. Flujo de producción
Entrada (foto, vídeo, producto, servicio, catálogo, idea) → análisis → público → oportunidades → conceptos → estrategia → guiones → visual → captions → calendario → paquete de publicación → **aprobación humana** → publicación (manual en etapa 1) → métricas → reporte → ajuste de estrategia.

## 3. Automatización propuesta (n8n recomendado; Make equivalente)
| # | Flujo | Disparador | Pasos | Salida | ¿Acción externa? |
|---|---|---|---|---|---|
| F1 | Detectar materiales | Archivo nuevo en Drive `/01_Brutos` | Leer metadatos → Claude genera brief | Fila en Sheet "Producción" estado PENDIENTE_APROBACION | No |
| F2 | Crear tareas de producción | Fila nueva en Sheet | Crear tarea (Asana/Linear/ClickUp) con brief | Tarea asignada | Interna |
| F3 | Organizar contenidos | Archivo editado en `/02_Editados` | Renombrar según convención, mover | Carpeta ordenada | Interna |
| F4 | Gestionar aprobaciones | Cambio de estado en Sheet a "APROBADO" + nombre del aprobador | Validar campos obligatorios | Estado PROGRAMABLE | No |
| F5 | Programar publicaciones | Estado PROGRAMABLE + fecha | Instagram Content Publishing API (contenedor → publicar) | Publicación | **Sí — DESACTIVADO** hasta autorización explícita |
| F6 | Recuperar métricas | Diario 08:00 | Instagram Insights API / Supermetrics / Windsor | Sheet "Métricas" | Solo lectura |
| F7 | Generar reportes | Semanal lunes | Claude (skill instagram-analytics) sobre Sheet "Métricas" | Reporte en Drive/Docs | No |

Plantilla implementada: `content-agency/automation/n8n_drive_to_brief.workflow.json` (F1, **inactiva**, sin secretos). Importar en n8n → crear credenciales → reemplazar `REEMPLAZAR_*` → activar manualmente tras revisión.

### Salvaguardas
- F5 requiere: (a) permiso `instagram_content_publish` aprobado por Meta, (b) columna "Aprobado por" no vacía, (c) interruptor global `PUBLICACION_AUTOMATICA=false` por defecto.
- Ningún flujo responde comentarios/DMs ni envía mensajes comerciales en la etapa 1.
- Claves (Anthropic, Meta, Google) solo en el gestor de credenciales de n8n/Make — nunca en el repositorio.

## 4. Tablero (Google Sheets) — columnas
`ID · Fecha · Marca · Material · Formato · Pilar · Etapa · Hook · Brief · Caption · Archivo final · Fecha/hora publicación · Estado · Aprobado por · Fecha aprobación · URL publicada · Alcance · Envíos · Guardados · Notas`

## 5. Estados
IDEA → BRIEF → EN PRODUCCIÓN → REVISIÓN INTERNA → PENDIENTE APROBACIÓN → APROBADO → PROGRAMADO → PUBLICADO → MEDIDO
