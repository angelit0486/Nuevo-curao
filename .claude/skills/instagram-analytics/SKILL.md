---
name: instagram-analytics
description: Analiza el rendimiento de Instagram a partir de Insights (capturas, CSV, exportaciones o API cuando esté conectada) - alcance conectado y no conectado, retención y reproducciones de Reels, compartidos/envíos, guardados, interacciones, visitas al perfil, clics y conversiones - y diseña experimentos de optimización. Úsala para "analiza mis métricas", "qué funcionó", "reporte mensual", "por qué bajó el alcance", "experimento", "KPIs".
---

# instagram-analytics — Análisis y experimentos

## Rol
Conviertes datos en decisiones. Nunca inventas métricas: si no hay datos, diseñas el sistema de medición y dices qué hace falta.

## Fuentes de datos (en orden de preferencia)
1. API de Instagram (Graph API vía integración autorizada) — **pendiente en este entorno** (ver 08_PENDIENTES_Y_LIMITACIONES.md).
2. Conectores de analítica social (Supermetrics, Windsor.ai) — instalados en la organización pero **sin autenticar**.
3. Exportación CSV / Google Sheets compartida por el usuario.
4. Capturas de pantalla de Insights (leer con visión; transcribir a tabla y pedir confirmación).
Declara siempre la fuente, el periodo y el tamaño de muestra.

## Información mínima
- Periodo a analizar y periodo de comparación. Si falta: últimos 30 días vs 30 anteriores.
- Datos por pieza (alcance, reproducciones, likes, comentarios, guardados, envíos, visitas al perfil, seguidores ganados) o capturas de Insights.
- Objetivo/KPI del periodo (del BRIEF_ESTRATEGICO o preguntar).
- Qué piezas tuvieron pauta pagada.
Sin datos → no hay reporte: entrega la plantilla de recogida de datos y el plan de medición.

## Métricas y fórmulas
| Métrica | Fórmula | Qué indica |
|---|---|---|
| Tasa de envíos | envíos / alcance | Potencial de alcance a no seguidores |
| Tasa de guardados | guardados / alcance | Valor de utilidad |
| Tasa de likes | likes / alcance | Afinidad (pesa más en seguidores) |
| Tasa de interacción | (likes+comentarios+guardados+envíos) / alcance | Salud general |
| % alcance no seguidores | alcance no seguidores / alcance | Capacidad de descubrimiento |
| Retención 3 s | espectadores que pasan 3 s / reproducciones iniciales | Fuerza del hook |
| Tiempo medio de visualización / duración | — | Retención relativa |
| Visitas al perfil / alcance | — | Interés en la marca |
| Seguidores / visitas al perfil | — | Fuerza del perfil (bio, cuadrícula) |
| Clics en enlace / visitas al perfil | — | Fuerza del CTA |
| Conversiones atribuidas | por UTM, palabra clave DM o código | Impacto en negocio |

## Procedimiento — REPORTE
1. Valida datos: periodo, piezas incluidas, faltantes, valores atípicos (piezas con pauta pagada separadas de orgánicas).
2. Calcula tasas por pieza y medianas por formato y pilar (usa medianas, no medias, con < 30 piezas).
3. Top 3 y bottom 3 por tasa de envíos y retención; busca patrones (hook, duración, tema, horario, formato).
4. Diagnóstico por embudo: descubrimiento → interés → acción.
5. 3 aprendizajes + 3 acciones concretas para el siguiente periodo + 1 experimento.
6. Si se pueden usar herramientas de código, genera gráficos (Python) y tabla en Sheets/CSV.

## Procedimiento — EXPERIMENTO
1. Hipótesis: "Si [cambio], entonces [métrica] mejorará porque [razón]".
2. Una sola variable (hook, duración, portada, horario, CTA, formato).
3. Diseño: n piezas por variante (mínimo 3 por lado o ≥ 1.000 reproducciones/variante), mismo pilar y franja.
4. Criterio de decisión definido **antes** de empezar.
5. Registro en la tabla de experimentos.

## Plantillas
```markdown
# REPORTE — [Marca] — [periodo] — Fuente: … — Piezas: n
## Resumen ejecutivo (5 líneas)
## KPIs vs meta
| KPI | Periodo anterior | Actual | Δ | Meta | Estado |
## Por formato / pilar (medianas)
## Top 3 / Bottom 3 (con por qué)
## Diagnóstico de embudo
## Aprendizajes · Acciones · Experimento siguiente
## Limitaciones de los datos
```
```markdown
# REGISTRO DE EXPERIMENTOS
| ID | Hipótesis | Variable | Variante A | Variante B | Métrica | Criterio | Fechas | Resultado | Decisión |
```

## Criterios de calidad
- [ ] Toda cifra trazable a la fuente; nada estimado presentado como real.
- [ ] Tasas, no solo absolutos.
- [ ] Separación orgánico vs pagado.
- [ ] Recomendaciones accionables (qué, cuándo, quién).
- [ ] Limitaciones declaradas (muestra pequeña, estacionalidad, cambios de algoritmo).

## Reglas para evitar errores
- No confundas correlación con causalidad; usa "asociado a".
- No concluyas con 1 pieza por variante.
- Las métricas de Instagram cambian de nombre/definición (p. ej. "reproducciones" sustituyó a "impresiones" en 2024–2025): indica la definición usada.
- No solicites contraseñas de Instagram; solo exportaciones o acceso vía integración oficial.

## Ejemplo
**Entrada:** tabla de 12 Reels del mes.
**Salida (extracto):** "Los 3 Reels con mayor tasa de envíos (4.1%, 3.8%, 3.2% vs mediana 1.2%) comparten hook de 'error común' y duración 8–12 s. Acción: 2 de cada 4 Reels del próximo mes con mecanismo 'error'. Experimento EXP-03: duración 10 s vs 25 s en tutoriales, decisión por retención relativa con ≥ 3 piezas por lado."

## Colaboración
Entrega aprendizajes a **instagram-strategist** (ajuste de pilares), **hook-engineering** (resultados A/B), **content-producer** (horarios/mezcla) y **marketing-campaign-builder** (resultados de campaña).
