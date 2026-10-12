# horn-torus-icc-experimental

Repositorio experimental del proyecto **Horn Torus ICC Model**: computacionalización de la tesis RSI–Poincaré (Lic. Carlos Vonsik) — un modelo topológico del inconsciente (Icc) sobre un **horn torus**, alimentado con puntajes del inventario **SCL-90-R**.

> **No es una herramienta diagnóstica.** Las asignaciones entre escalas del SCL-90-R y la geometría son construcciones del modelo (marcadas como **AXIOMA**), no resultados validados. Un puntaje de malestar no determina una estructura clínica.

## Repos del proyecto

| Repositorio | Contenido |
|---|---|
| `horn-torus-icc-model` (https://github.com/Carlitos130/https-github.com-Carlitos130-horn-torus-icc-model) | La aplicación (React + TypeScript + Three.js + Vite), rama `main` (línea de tesis V44–V47 y aviso de estatuto V49) y rama `fusion-prcc` (línea de fusión). |
| `horn-torus-icc-experimental` (este repo) | Prototipos y **documentación de la tesis**: la tesis misma, los escritos completos y la trazabilidad de versiones. |

## Documentación de la tesis (`docs/`)

- **[tesis_rsi_poincare V49.docx](docs/tesis_rsi_poincare%20V49.docx)** — la tesis, versión V49 (12/10/2026): incorpora la **§4.8 «Rearticulación del anudamiento: el borromeo como régimen modal de Σ»** (el anudamiento se lee por la modalidad de Σ —contingente en (a), exigida en (b)— y no por la estructura del enlace), el **Cierre metodológico** del Capítulo 7 que enumera los tres pendientes como contorno declarado del programa (borromeo/tarea (11), sinthome sin definir, transición topológica horn torus → esfera χ = 1 → χ = 2) y el **Resumen (abstract)** en la página de frente, en clave LECTURA. 331 párrafos, XML válido, FIN OK.
- **[tesis_rsi_poincare V48.docx](docs/tesis_rsi_poincare%20V48.docx)** — la tesis, versión V48 (7/10/2026): desarrolla la nueva **§6.3 «Joyce como paradigma de la LECTURA»** — la epifanía (Stephen Hero) como homología y no representación, «What can't be coded can be decorded» y la letra pública (I.5) como estatuto de oído de la LECTURA, el sinthome (R.S.I., SXIII) como axioma análogo a las asignaciones marcadas, la circularidad del Wake (riverrun) contra el horn torus (circularidad topológica ≠ epistémica) — con renumeración (Diagnóstico diferencial → §6.4, Relectura Joyce → §6.5) y referencias cruzadas actualizadas.
- **[tesis_rsi_poincare V47 2.docx](docs/tesis_rsi_poincare%20V47%202.docx)** — la tesis, versión V47 2: incorpora la **adenda al Capítulo 7** con el estatuto epistémico de la LECTURA del análisis espectral del panel «Espectral K» (homología del modelo, no inferencia de estructura; reactivación traumática por vecindad A_cr; en la configuración (a) no dispersa ni eyecta — Corolario II condicional a (b)).
- **[V47_escritos_completos.md](docs/V47_escritos_completos.md)** — documento único: mapa de situación, tesis, resumen, manual, rótulos de código, trazabilidad y textos verbatim (§7 integración GitHub, §8 adenda V47 2). Versión docx: [V47_escritos_completos 2.docx](docs/V47_escritos_completos%202.docx).
- **[V48_escritos_completos.md](docs/V48_escritos_completos.md)** — ciclo V48: texto íntegro verbatim de la §6.3 nueva, las 5 renumeraciones y la verificación (313 párrafos, 21/21 claves, FIN OK). Versión docx: [V48_escritos_completos.docx](docs/V48_escritos_completos.docx).
- **[V49_escritos_completos.md](docs/V49_escritos_completos.md)** — ciclo V49: texto íntegro verbatim de la §4.8, del Cierre metodológico y del Resumen, los ajustes del texto del autor (χ corregido según §4.7, etc.) y la verificación (331 párrafos, 23/23 claves, FIN OK). Versión docx: [V49_escritos_completos.docx](docs/V49_escritos_completos.docx).
- **[trazabilidad_V28_a_V47.md](docs/trazabilidad_V28_a_V47.md)** — trazabilidad de versiones V28→V49, con la integración de la línea de GitHub, la adenda V47 2, la auditoría de la rama `fusion-prcc`, la sección V48 (7/10/2026) y la sección V49 (12/10/2026, con el aviso de estatuto implementado en la app).

## Estado

- `main` sincronizada con origin; los orígenes de cada versión y sus commits están documentados en la trazabilidad.
- El prototipo computacional corre desde el repo de la aplicación (`npm run dev`, puerto 3000).
