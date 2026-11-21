# 08 — PENDIENTES Y LIMITACIONES

## Pendientes (requieren acción del usuario)
| # | Pendiente | Bloquea | Quién | Cómo (doc 05) |
|---|---|---|---|---|
| 1 | Conectar Google Drive (+ instalar Sheets/Docs) | Detección de materiales, tablero, carpetas | Usuario (OAuth) | claude.ai/customize/connectors |
| 2 | Elegir y conectar analítica de Instagram (Supermetrics o Windsor.ai) o aportar exportaciones | Reportes con datos reales | Usuario (+ decisión de plan de pago) | doc 05 §4 |
| 3 | Convertir Instagram a cuenta profesional y vincular a página de Facebook | Cualquier acceso a Insights/API | Usuario | App de Instagram |
| 4 | Elegir Make o n8n, conectar e importar plantilla | Automatizaciones F1–F7 | Usuario | doc 05 §5 |
| 5 | Reconectar ElevenLabs con permisos completos | Voz en off / vídeo IA | Usuario | connectors |
| 6 | (Opcional) Crear Brand Kit en Canva | Diseños automáticamente on-brand | Usuario o Claude con aprobación | Canva |
| 7 | (Opcional) Permitir hosts de Meta/n8n/Make en la red del entorno | Llamadas directas desde la nube | Usuario aprueba propuesta | Pedírmelo |
| 8 | Aportar datos reales de la primera marca (oferta, precios, capacidad, @) | Sustituir supuestos | Usuario | Pedido normal |

## Limitaciones conocidas
1. **Sin publicación automática en Instagram**: no existe MCP oficial; la API de publicación requiere app de Meta revisada. Por diseño, la etapa 1 es publicación manual con aprobación.
2. **No se analizan perfiles de Instagram de terceros directamente** (sin scraping; términos de Meta). La competencia se analiza con webs públicas, datos aportados o herramientas autorizadas.
3. **Métricas de competidores** (seguidores, engagement) no disponibles sin herramienta de pago autorizada.
4. **Tendencias/audios en tendencia**: solo se citan con fuente reciente; sin ella, las Skills trabajan con formatos.
5. **Contenedor cloud efímero**: lo que no está en git se pierde. Todo lo de la agencia está versionado.
6. **Generación de imagen/vídeo IA** (Canva, ElevenLabs, Gamma) consume créditos del usuario: se pide confirmación antes de generaciones costosas.
7. **Adobe Creative Cloud**: no se encontró integración MCP oficial compatible; se usan Canva/Figma.
8. **Pruebas A–D** usan un cliente ficticio; validan el sistema, no resultados de negocio.
9. **Reglas de la plataforma cambian**: las Skills contienen reglas verificadas a nov-2026 (originalidad extendida a fotos/carruseles en abril 2026, Reels ≤ 3 min para recomendación, envíos/likes por alcance). Revisión trimestral recomendada.
10. **Plugins de marketing con MCP** (ahrefs, hubspot, notion, slack, similarweb, etc.) fallan por la red del entorno; solo se habilitarían si se van a usar.
