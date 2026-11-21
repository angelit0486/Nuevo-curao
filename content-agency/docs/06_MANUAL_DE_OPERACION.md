# 06 — MANUAL DE OPERACIÓN

## 1. Cómo pedir trabajo
Abre una sesión de Claude Code en este repositorio y escribe en lenguaje natural. El coordinador elige las Skills y lo indica al inicio (`Skills: A → B → C`). Ejemplos:
| Quiero… | Escribe |
|---|---|
| Arrancar una marca | "Nueva marca: [qué vendes, dónde, objetivo]. Haz el brief estratégico." |
| Ideas | "5 conceptos de Reels para [producto]." |
| Guion | "Guion completo del concepto 2, 20 segundos, sin salir a cámara." |
| Calendario | "Calendario de 7 días desde el lunes, 3 Reels y 2 carruseles." |
| Competencia | "Audita a [@ o webs] y dime cómo diferenciarme." |
| Copy | "Caption con CTA a WhatsApp para este Reel." |
| Perfil | "Optimiza mi bio y nombre para que me encuentren en [ciudad]." |
| Diseño | "Crea en Canva una plantilla de carrusel 4:5 con mi paleta." |
| Campaña | "Campaña de Navidad, 2 semanas, oferta [X], presupuesto [Y o solo orgánico]." |
| Métricas | "Analiza estas capturas de Insights del mes." |
| Desde un material | Adjunta foto/vídeo/catálogo: "Convierte esto en contenido para la semana." |

## 2. Organización de archivos
```
content-agency/clientes/<marca>/
  BRIEF_ESTRATEGICO.md          ← fuente de verdad (instagram-strategist)
  GUIA_VISUAL.md                ← creative-director
  MAPA_KEYWORDS.md              ← instagram-seo
  <AAAA-MM>/AAAAMMDD_tipo_titulo_vN.md   ← calendarios, guiones, reportes
```
En Google Drive (cuando esté conectado): `/Content Agency/<Marca>/<AAAA-MM>/01_Brutos 02_Editados 03_Diseños 04_Copys 05_Aprobados 06_Publicados 07_Reportes`.

## 3. Ciclo semanal recomendado
| Día | Actividad | Skill |
|---|---|---|
| Lunes | Reporte de la semana anterior + ajustes | instagram-analytics |
| Martes | Conceptos y hooks de la próxima semana | viral-reels-creator, hook-engineering |
| Miércoles | Guiones + copy + calendario | content-producer, social-copywriter |
| Jueves | Aprobación del cliente | (humano) |
| Viernes/Sábado | Rodaje en bloque | content-producer (plan de rodaje) |
| Domingo | Programación manual de lo aprobado | (humano) |

## 4. Aprobación humana
Ver tabla en `CLAUDE_CONTENT_AGENCY.md` §7. Regla corta: **Claude prepara; la persona aprueba y publica.** Cada pieza aprobada debe tener `Aprobado por / fecha` en su paquete de publicación.

## 5. Control de calidad
Antes de entregar, cada Skill aplica su checklist. Si ves `[SUPUESTO]`, `[A VALIDAR]`, `[DATO DEL CLIENTE]` o `[PRECIO]`, debes completar o confirmar ese dato antes de publicar.

## 6. Mantenimiento
| Tarea | Frecuencia | Cómo |
|---|---|---|
| Validar Skills | Tras cada edición | `python3 content-agency/automation/validate_skills.py` |
| Revisar normas de Instagram | Trimestral | "Revisa cambios recientes en recomendaciones de Instagram en fuentes oficiales y actualiza las Skills" |
| Verificar conectores | Mensual o tras error | "Verifica conectores" |
| Actualizar brief de cada marca | Cada 90 días | instagram-strategist con datos de instagram-analytics |
| Respaldo | Continuo | Todo está en git; hacer commit/push tras cada entrega |

## 7. Restaurar la configuración original
`CLAUDE.md` original respaldado en `content-agency/backups/CLAUDE.md.bak-20261121`. Para desactivar la agencia: quitar la línea `@content-agency/CLAUDE_CONTENT_AGENCY.md` de `CLAUDE.md` (las Skills seguirán disponibles bajo demanda).
