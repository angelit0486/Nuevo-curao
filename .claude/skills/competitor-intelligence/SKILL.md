---
name: competitor-intelligence
description: Investiga y compara competidores en Instagram y en la web - benchmarking de perfiles, análisis de contenido (formatos, hooks, temas, frecuencia), propuesta de valor, precios públicos, reseñas y comentarios, anuncios activos (Biblioteca de anuncios de Meta) - para identificar huecos, oportunidades y diferenciación. Úsala para "analiza a mi competencia", "auditoría de competidores", "benchmark", "qué hacen otros", "cómo me diferencio".
---

# competitor-intelligence — Inteligencia competitiva

## Rol
Produces evidencia, no opiniones. Cada afirmación sobre un competidor debe tener fuente (URL) y fecha de consulta, o marcarse como `[NO VERIFICADO]`.

## Herramientas
- **Exa MCP** (`web_search_exa`, `web_fetch_exa`) y **WebSearch**: webs, reseñas, prensa, menciones. Verificado operativo.
- **Brandfetch MCP**: identidad visual, descripción, redes oficiales por dominio.
- **Biblioteca de anuncios de Meta** (facebook.com/ads/library): consulta manual del usuario o navegador si está disponible; el dominio de Meta está bloqueado por la red de este entorno.
- Instagram no permite extraer datos de perfiles de terceros sin autorización: **no hagas scraping** de Instagram. Usa lo que el usuario capture/comparta, información pública indexada, o herramientas autorizadas.

## Información mínima
- Negocio del cliente y zona.
- 3–5 competidores (@ o web). Si no los hay: propón candidatos encontrados por búsqueda y pide confirmación antes del análisis profundo.
- Qué quiere aprender (posicionamiento, contenido, precios, anuncios).

## Procedimiento
1. **Selección**: 2 directos (misma oferta y zona), 1–2 indirectos (resuelven el mismo problema), 1 referente aspiracional (otra zona/escala).
2. **Ficha por competidor**: propuesta de valor, público aparente, precios públicos, canales, identidad visual (Brandfetch), reseñas (temas positivos/negativos repetidos).
3. **Análisis de contenido** (con datos que el usuario aporte o públicos): frecuencia, mezcla de formatos, pilares, hooks recurrentes, CTA, estética, piezas destacadas (las de interacción claramente superior a su media), uso de colaboraciones, anuncios activos.
4. **Voz del cliente**: frases literales de reseñas/comentarios (deseos, quejas). Son oro para copy y SEO.
5. **Matriz comparativa** y **mapa de posicionamiento** (2 ejes relevantes, ej. precio × especialización).
6. **Huecos/oportunidades**: temas no cubiertos, quejas no resueltas, formatos ausentes, segmentos desatendidos.
7. **Recomendaciones de diferenciación** (3) con riesgo y esfuerzo.

## Plantilla
```markdown
# AUDITORÍA COMPETITIVA — [Cliente] — [fecha] 
Metodología y fuentes: … | Limitaciones: …
## Fichas
### [Competidor] — @… — web …
Propuesta · Público · Precios (fuente) · Frecuencia · Formatos % · Pilares · Hooks típicos · CTA · Estética · Fortalezas · Debilidades
## Matriz
| Criterio | Cliente | C1 | C2 | C3 |
## Voz del cliente (citas literales con fuente)
## Mapa de posicionamiento (ejes: … × …)
## Oportunidades (prioridad, esfuerzo, impacto)
## Diferenciación recomendada
## Fuentes (URL + fecha de consulta)
```

## Criterios de calidad
- [ ] ≥ 1 fuente por competidor; fecha de consulta.
- [ ] Separación clara entre hecho, inferencia y suposición.
- [ ] Oportunidades accionables (se traducen en pilar, pieza o campaña).
- [ ] Sin copiar contenido: se extraen mecanismos, no piezas.

## Reglas para evitar errores
- No inventes seguidores, tasas de interacción ni ventas de competidores. Si el dato no es público, escribe "no disponible".
- No recomiendes desprestigiar competidores ni comparativas engañosas.
- No hagas scraping ni uses servicios que violen los términos de Meta.
- Cumple privacidad: no recopiles datos personales de clientes de la competencia más allá de citas públicas anónimas.

## Ejemplo
**Entrada:** "Audita a 3 cafeterías de especialidad de Guadalajara."
**Salida (extracto):** Oportunidad #1: ninguno publica tutoriales de preparación en casa; reseñas repiten "no sé cómo prepararlo igual en casa" [fuente, fecha] → pilar "Ritual en casa" con Reels de 20–30 s. Esfuerzo bajo, impacto alto.

## Colaboración
Alimenta a **instagram-strategist** (posicionamiento), **instagram-seo** (lenguaje del cliente), **hook-engineering** (mecanismos que funcionan en el nicho), **marketing-campaign-builder** (ofertas de la competencia).
