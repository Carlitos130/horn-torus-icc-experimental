# Trazabilidad de versiones — V28 → V33 → V35 → V38_2 → V40 → V44 → V46 → V47

Qué cambió en cada versión de `tesis_rsi_poincare` y dónde aterrizó en el
Resumen, el Manual y el prototipo. Fechas de adaptación: 28 de septiembre –
1 de octubre de 2026. Elaborada el 30 de septiembre de 2026 (V28–V44) y
extendida el 1 de octubre de 2026 (V46–V47 e integración con la línea de
GitHub, ese mismo día). Este archivo reemplaza a
`trazabilidad_V28_a_V44.md`, que se conserva sin modificar.

| Versión tesis | Qué cambió en la tesis | Resumen | Manual | Prototipo |
|---|---|---|---|---|
| **V28** | Dos modelos declarados (nudo M_L = S³∖N(L); Icc = par (U, X)); §4.7 revisado: χ = 1, H₁ = ℤ⟨μ⟩, género indefinido, sin Heegaard ni duplicación, sin nudo borromeo sobre X, neckpinch retirado; **Corolario I (Wegbreite)** re-anclado al arco de la cinta S-I-Σ (ya no adelgazamiento de pared); Corolario II (Umbau): reenganche de cadenas; Σ leído como **sinthome** (Axioma 2); Prcc como campo que entra por la voz | **v8**: §16 archivada con ese carácter; cabecera y tópica reasentadas | **v3** (tras correcciones de v2: χ = 1, H₁, género) | Umbral Wegbreite: `isPsychoticRupture` exige δ ≥ π/6 (disipación del cruce angosto); `umbauCadenaS/I` en `computePostEpisodeState`; docblock de `types.ts` (Wegbreite = arco de cinta) |
| **V33** | Solo enriquecimientos, dentro de los Axiomas 2 y 4: Σ **recorre junto con S e I** desde el inicio; Σ es **síntoma que anuda** (fundamento freudiano independiente del Sem. XXIII, GW XIV 121–123); **la intensidad decide el destino de la marca**; **fantasía no es síntoma**; **las marcas se depositan por el circuito**; Grenze como evento de investidura (GW X, p. 286); cita del Sem. X ampliada (aproximación nombrada por Lacan) | **v9**: 5 axiomas nuevos anotados en §5 y §18 | **v4**: ítem Σ y marcas ampliados | Distribución de marcas en caracol por el circuito; banda Σ siempre sobre la superficie; la intensidad ya modelada por el corte 3× se vuelve doctrina del resumen |
| **V35** | Primera corrección de fondo: la censura **ya no es pared con adelgazamientos** (propiedad de la marca, ligada o no a Wortvorstellung; X sin espesor); Reizschutz = **capacidad de ligadura** (GW X, p. 300); epistémica: lo decifrable es el **trauma**, no la fantasía (marcas F no se decifran; punción no es producto de ningún cruce); recotejos GW X p. 130 y GW XII 204–205 | **v10**: corrección anotada en cabecera, §8 y §16 | **v5**: censura redefinida; epistémica corregida | Comentarios V35 en `types.ts` y motor («no hay pared ni adelgazamientos»); lectura del umbral δ como propiedad del cruce, no del borde |
| **V38_2** | Cuatro precisiones: cita del Sem. XXIV sobre el Nombre del Padre es de **Didier-Weill** (testimonio secundario); recotejo Sem. XI p. 107 / p. 110; **Prcc = campo de intensidad sin borde ni tabique** (axioma de diseño); Freud GW II 573–574 (Wächter) vs 615–616 (topische→dynamische); figs. 5.5–5.6 regeneradas sin pared ni anillo | **v11**: nota Didier-Weill en §2; Prcc precisado | **v6**: los cuatro puntos en cabecera y §2 | **Verificación en vivo del Prcc**: sub-malla de la misma superficie (`prccIndices` = cos(vMid) ≤ 0), translúcida (opacity 0.36, DoubleSide, depthWrite false), campo de angustia continuo en las fronteras, zona 1,69 % ≈ motor 1,72 % ≈ HUD 1,7 %; barra «Superficie = Icc · Prcc = campo sin borde · Cc = exterior» |
| **V40** | Revisión más honda desde V28: **Régimen 1 = aproximación al núcleo fantasmático** (angustia del fantasma); **Régimen 2 = marca del trauma** con salida a Cc **contingente** (estatuto modal del sinthome); **Régimen 3: el Agieren se deriva** de la tabla de condiciones; **objeto a = la punción** (PENDIENTE su relación con −i); **A_cr derivado = 1/(a·k_max)**, k_max ≈ 0,599 («cerrazón del giro», no largo del rodeo; articula Wegbreite: arco más ancho rompe antes); Drei Abhandlungen a **CITA** (GW V, p. 65); repetición = GW X pp. 130–131; segundo toro del deseo (Sem. IX, 14/3/1962); Prcc: embudo = ingreso, infiltración = despliegue | **v12**: cabecera, bloque de regímenes, HECHO MATEMÁTICO, cita cotejada §17, cierre §18 | **v7**: cabecera V40, regímenes + A_cr en §4, sección nueva **«Sonido del vórtice»** | **Sonido del vórtice** implementado: `src/utils/vortexSound.ts` (VortexSynth Web Audio), cableado en `HornTorusCanvas.tsx` (GSI → f₀, detune rotacional, lowpass, LFO, ruptura) y botón «Sonido» en `App.tsx`; tsc = 0; probado en vivo |
| **V44** (decidida entre V41 y V43) | Segunda corrección de fondo: **Axioma 1 reescrito** — S e I **dejan de ser toros sólidos**: son la **serie de Vorstellungsrepräsentanzen** (GW X, p. 251) inscritas una por una sobre Ding (cada inscripción repite A→a' del esquema L, Sem. II 26/4/1955, i(a) con Rabinovich); **R es Ding mismo**; afecto se desprende de la VR (GW X, p. 255), la marca queda en el cuerpo; **Axioma 2 RETIRADO** (configuraciones (a)/(b) en M_L) → PENDIENTE de rearticulación, material en espera; **Σ redefinido provisorio**: una VR (S2, Sem. XI 3 y 10/6/1964) se activa y encadena a otras — síntoma que liga; **hilo pulsional ≠ Σ**: ancla solo voz y oído en p, exige Gegenbesetzung (GW X, p. 280); modelo del nudo = **borromeo genérico** (censo L6a4): L = S∪I∪Σ PENDIENTE; Milnor, cuspidal y a = −i se sostienen; **Corolario II reforzado**: Σ suelta las cadenas → el hilo pulsional queda como único camino de descarga → la eyección sale específicamente por la voz; Sem. XXII («tore» por redondel) sigue fiel: cambia la arquitectura del autor | **v13**: cabecera Versión 13; nota de relectura en la zona del Entwurf; Corolario II reformulado; §18 con dos bloques nuevos (V44 relee el cuadro Σ; V44 reescribe el Axioma 1) | **v8**: cabecera V44; banda Σ re-leída; ítem Vorstellungsrepräsentanz promovido a fundamento del Axioma 1; Corolario II con la relectura | Tres rótulos: botón Σ en `App.tsx` («Cinta Σ (Síntoma, serie de VR — tesis V44)»), leyenda del canvas «Σ: Síntoma (VR)» e informe «Función (tesis V44): Σ = que una VR (S2…) se activa y encadena» en `hornTorusMath.ts`; comentario del conmutador Cap. 7 actualizado (el anudamiento en M_L quedó retirado). Dinámica sin cambios; tsc = 0 |
| **V46** | Tres ediciones, sin doctrina nueva: **(1) Precisión sobre la cinta** — la cinta S-I-Σ **no se retira**: es el **soporte de las series** (las VR de S y de I se inscriben sobre sendas bandas de la superficie; Σ no es una tercera banda); **(2)** el no-borromeo sobre Ding de §4.7 vale de los **soportes** (no de las series); Corolario I conserva su referente sin re-anclaje; **(3) advertencia de suspenso en §6.3**: el diferencial neurosis/Border y el caso Joyce quedan PENDIENTES junto con el Axioma 2 (retirado en V44) | **v14**: 5 reemplazos; espejo `Horn_Torus_del_Icc_resumen_v14-V46.md` | **v9**: 4 reemplazos (incl. arreglo tipográfico `cuerpo.-`) | Rótulos del repo → V46 (botón Σ, leyenda «Σ: Síntoma (VR)», informe del motor); verificación en vivo del preview (tesisV46 = true, tesisV44 = false); tsc = 0 |
| **V47** | **Axioma 2 REARTICULADO** (inserción pura: +6 párrafos en 2 bloques, tras §4.7 y en §6.3; Σ no se redefine): la configuración se define por la **relación entre los soportes de las dos series** + el **estatuto modal de Σ**. **(a) Neurosis** = soportes en **superposición** (unión conexa; trayecto A→a' sin trecho; correspondencia de origen — Entwurf p. 416) → Σ **contingente**. **(b) Border** (psicosis no desencadenada) = soportes **disjuntos** (trecho; la correspondencia de origen falta — Hombre de los Lobos GW XII 72–73; Carta 52) → Σ **exigida** (GW XIV 121–123). El trecho **no es un cuarto defecto** (no se suma a voz, punción, marca). **§6.3 reactivado**: en (a) el trauma ni dispersa ni eyecta; en (b) el pasaje puede forzar a Σ a soltar → **Corolario II queda condicional a (b)**; Joyce como paradigma | **v15**: 4 reemplazos — cabecera Versión 15; Corolario II condicional a (b); bloque §18 «V47 rearticula el Axioma 2»; bloque §18 «V47 reactiva §6.3»; espejo `Horn_Torus_del_Icc_resumen_v15-V47.md` | **v10**: 4 reemplazos — cabecera V47; banda Σ con la Rearticulación V47; §3 con bloque nuevo **«Config Axioma 2 (V47, solo visual)»**; Corolario II condicional a (b) | **Parámetro visual de configuración** (SOLO VISUAL, sin tocar el cálculo): `configAxioma2?: 'a' \| 'b'` en `types.ts`; botón **«Config Axioma 2»** en `App.tsx` (indigo en (b), title = tesis V47); en (b) la banda S se desfasa (`bandGap` 0.55 → `lacVis.v_S + bandGap` en `HornTorusCanvas.tsx`), I/Pulsión/Σ quedan fijas; informe del motor con línea «Configuración (Axioma 2 rearticulado, V47): (a)…/(b)…»; tsc = 0; verificado en vivo (toggle alterna; curveS cambia, curveI/curvePulsion/curveSigma idénticas) |

## Integración con la línea de GitHub (1 de octubre de 2026)

El remoto `origin` — `github.com/Carlitos130/https-github.com-Carlitos130-horn-torus-icc-model`
— traía 17 commits no presentes en el disco local: una línea de desarrollo
fusionada por PR #1 («snapshot/Fusión: versión local kill-critic, psicometría…
con el Prcc»), los paneles **«Espectral K»** (`SpectralSingularityPanel.tsx`)
y **«Manual & Lacan»** (`TheoreticalManualModal.tsx`), el README público,
`docs/figuras` + `docs/modelo.md`, el visor HTML estático y refactors de
rendimiento. Los archivos centrales habían divergido ~4.000 líneas.

- **Backup previo**: `_backup_v47_antes_pull_2026-10-01\` (12 archivos, junto al repo).
- **Commit `e329036`** — trabajo V47 local: `configAxioma2`, rótulos V46–V47,
  `vortexSound.ts`, `baremos/formatMetric/ruptureSequence`, package-lock;
  README restaurado al README público del proyecto (el informe del motor que
  lo había pisado queda en el backup).
- **Merge `35a47fd`** — los 5 archivos centrales (types, App, Scl90rForm,
  HornTorusCanvas, hornTorusMath) resueltos a favor de la línea V44–V47.
  Portado del remoto (sin tocar el cálculo de la tesis):
  `computePointGaussianCurvature`, `computeSpectralSingularityAnalysis`
  (+ tipos `SingularityCriticalPoint`/`SpectralSingularityReport`) y
  `generateInteractiveHTMLScript`; tabs nuevas cableadas en `App.tsx` con los
  handlers locales de ruptura (`launchPsychoticRupture`, `ruptureVisual`).
- **Ajuste de integración (LECTURA)**: `computeSpectralSingularityAnalysis`
  usaba `lac.isTraumaReactivated`, campo de la línea remota que la interfaz
  local no tiene. Reemplazado por el cálculo directo coherente con el Axioma 4:
  la cinta S está reactivada si pasa dentro de la vecindad A_cr de alguna marca
  (distancia angular envuelta). Documentado como LECTURA en el propio panel.
- **Alineación doctrinal de los paneles** (heredaban rótulos de la V22):
  *Manual & Lacan* → V47 (cinta = soporte de las series, VR sobre soportes con
  las configuraciones (a)/(b), Corolario II condicional a (b), sinthome sin
  definirse y Joyce paradigma de (b), ítem nuevo «Config Axioma 2»);
  *Espectral K* → fundamentación re-rotulada V44–V47 + nota LECTURA de la
  reactivación traumática.
- **Verificación**: `tsc --noEmit` = 0; preview en vivo con botón «Config
  Axioma 2» intacto y ambos paneles renderizando; marcadores V47 presentes.
- **Push**: `0baf7cd..35a47fd main -> main` — remoto actualizado y
  sincronizado; `main...origin/main` sin desvíos.

## Tesis V47 2 — LECTURA del análisis espectral en el Capítulo 7 (2 de octubre de 2026)

- **Pedido**: documentar en la tesis (Cap. 7) la LECTURA del análisis espectral
  (panel «Espectral K» del prototipo) como herramienta de exploración del modelo,
  con su estatuto epistémico.
- **Generador**: `gen_v47_2.py` (patrón `gen_v47.py`) sobre el zip de
  `tesis_rsi_poincare V47.docx` → archivo NUEVO `tesis_rsi_poincare V47 2.docx`
  (V47 no se pisa). Ancla: el párrafo «Sección pendiente de desarrollo…» del
  esquema del Cap. 7; inserción después de él, antes de la línea en blanco y de
  «Bibliografía». 3 párrafos nuevos con pPr heredado del ancla.
- **Contenido** (verbatim en la §8 de `V47_escritos_completos.md`):
  1. Estatuto epistémico: LECTURA del modelo, herramienta de exploración, no
     inferencia de estructura ni validación empírica; «calcula, no mide»;
     perfiles SCL-90-R como entrada axiomática (§6.2), no como datos validados.
  2. Reactivación por vecindad A_cr (Axioma 4, aproximación): cinta S reactivada
     si pasa dentro de la vecindad de alguna marca (distancia angular envuelta);
     equivalencia por construcción del «desborde» del panel (A = A_max − d,
     A_max = π√2); estado de p leído del baremo de Psicoticismo y δ — tensión
     geométrica, no estructura clínica; en (a) no dispersa ni eyecta
     (Corolario II condicional a (b); Joyce paradigma en §6.2).
  3. Alcance y tareas: exploración del modelo, no contraste con datos; ninguna
     tesis depende de las salidas del panel; enmarcado en la advertencia de la
     BME; tareas abiertas = las de la BME (validez convergente/discriminante,
     no-circularidad de asignaciones, función F).
- **Verificación**: 3.619.276 bytes; 307 párrafos (304 + 3); XML válido
  (xml.dom.minidom); diff puramente aditivo (dst[0:262] ≡ src[0:262], dst[265:] ≡
  src[262:]: línea en blanco + Bibliografía intactas); claves: «Adenda V47 2» ×3,
  «LECTURA del análisis espectral» ×3, «herramienta de exploración» ×2,
  «vecindad A_cr» ×1, «Corolario II, condicional a (b)» ×1, «Σ contingente» ×1;
  orden esquema < adenda < Bibliografía = True; residuos «tesis V22» ×0,
  «NO publicado» ×0. Extractos: `v47_extract.txt` (fuente) y `v47_2_extract.txt`
  (nuevo); verificador `_verify_v47_2.py`.

## Convenciones de archivo

- Resumen: `Horn_Torus_del_Icc_resumen_v8..v15.md` (espejos en `Claude outputs\*-V28..V47.md`), docx por versión.
- Manual: `MANUAL_HORN_TORUS_v3..v10.md` (en `Metapsicologia Freud Lacan\`).
- Extractores y diffs: `extract_vNN.py` + `vNN_extract.txt` + `vNN_diff.txt` en `Claude outputs\` (V47: generador `gen_v47.py` que inserta los bloques del Axioma 2 rearticulado sobre el zip de `V46 3.docx`).
- Verificación por versión: `verify_v33/v35/v38_2/v40/v44/v46/v47.py` (docx + claves + residuos vetados = 0).
- Propuesta previa a V47: `axioma2_rearticulado_propuesta.md` (original en `Horn Torus\`, espejo en `Claude outputs\`).
- Originales nunca se pisan: cada versión escribe un archivo nuevo.
