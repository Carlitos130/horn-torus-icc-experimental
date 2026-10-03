# horn-torus-icc-experimental

Repositorio experimental del proyecto **Horn Torus ICC Model**: computacionalización de la tesis RSI–Poincaré (Lic. Carlos Vonsik) — un modelo topológico del inconsciente (Icc) sobre un **horn torus**, alimentado con puntajes del inventario **SCL-90-R**.

> **No es una herramienta diagnóstica.** Las asignaciones entre escalas del SCL-90-R y la geometría son construcciones del modelo (marcadas como **AXIOMA**), no resultados validados. Un puntaje de malestar no determina una estructura clínica.

## Repos del proyecto

| Repositorio | Contenido |
|---|---|
| `horn-torus-icc-model` (https://github.com/Carlitos130/https-github.com-Carlitos130-horn-torus-icc-model) | La aplicación (React + TypeScript + Three.js + Vite), rama `main` (línea de tesis V44–V47) y rama `fusion-prcc` (línea de fusión). |
| `horn-torus-icc-experimental` (este repo) | Prototipos y **documentación de la tesis**: la tesis misma, los escritos completos y la trazabilidad de versiones. |

## Documentación de la tesis (`docs/`)

- **[tesis_rsi_poincare V47 2.docx](docs/tesis_rsi_poincare%20V47%202.docx)** — la tesis, versión V47 2: incorpora la **adenda al Capítulo 7** con el estatuto epistémico de la LECTURA del análisis espectral del panel «Espectral K» (homología del modelo, no inferencia de estructura; reactivación traumática por vecindad A_cr; en la configuración (a) no dispersa ni eyecta — Corolario II condicional a (b)).
- **[V47_escritos_completos.md](docs/V47_escritos_completos.md)** — documento único: mapa de situación, tesis, resumen, manual, rótulos de código, trazabilidad y textos verbatim (§7 integración GitHub, §8 adenda V47 2). Versión docx: [V47_escritos_completos 2.docx](docs/V47_escritos_completos%202.docx).
- **[trazabilidad_V28_a_V47.md](docs/trazabilidad_V28_a_V47.md)** — trazabilidad de versiones V28→V47, con la integración de la línea de GitHub, la adenda V47 2 y la auditoría de la rama `fusion-prcc`.

## Estado

- `main` sincronizada con origin; los orígenes de cada versión y sus commits están documentados en la trazabilidad.
- El prototipo computacional corre desde el repo de la aplicación (`npm run dev`, puerto 3000).
