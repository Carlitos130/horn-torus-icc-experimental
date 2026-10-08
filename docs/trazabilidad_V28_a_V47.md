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

## Auditoría de la rama fusion-prcc y decisión sobre el worktree horn-fusion (3 de octubre de 2026)

- **Qué es `horn-fusion/`**: un **worktree registrado del repo real**
  (`horn-torus-icc-model-real/.git/worktrees/horn-fusion`), checkout de la rama
  `fusion-prcc` — la línea de fusión (kill-critic, psicometría, baremos por
  población, marcas de fantasía, Prcc) que entró a `main` por el PR #1
  (`1bad4f9`) durante el ciclo V47. Su README público ya describe el modelo en
  términos V44+ (Ding/censura, p como orificio doble, Prcc sin borde).
- **Comparación con `main` del repo real**:
  * `main..fusion-prcc` = **0 commits**: la rama no aporta nada que `main` no
    tenga; es ancestro puro (la base que se fusionó).
  * `fusion-prcc..main` = 7 commits: los 3 de la línea kill-critic previa al
    ciclo (`0baf7cd`, `987d2ba`, `cd99dcd`) y los 3 de V47 (`e329036`,
    `35a47fd`, `abf8452`) más el merge del PR.
  * Diff de archivos (fusion-prcc → main): le faltan `package-lock.json`
    (trackeado) y `src/utils/vortexSound.ts` (153 líneas), y difieren
    `App.tsx`, `HornTorusCanvas.tsx`, `Scl90rForm.tsx`,
    `SpectralSingularityPanel.tsx` (5 líneas: nota LECTURA + rótulo V44–V47),
    `TheoreticalManualModal.tsx` (17: alineación V47), `types.ts` (53:
    interfaces espectrales), `hornTorusMath.ts` (523: funciones espectrales +
    ajuste LECTURA por vecindad A_cr), `.env.example`, `vite.config.ts`.
- **Qué le faltaría para alinearse a V47**: nada de trabajo — sería un
  fast-forward (`git -C horn-fusion merge --ff-only main`), porque no tiene
  ningún commit propio. No hay ninguna modificación única en disco (solo un
  `package-lock.json` sin trackear, ruido de una instalación local).
- **Decisión**: **conservar el worktree, sin tocarlo**, como archivo de la
  línea de fusión pre-V47 (acceso local de solo lectura). La rama ya está
  pusheada a origin (`4855b3a`), así que GitHub conserva la historia; el
  worktree no se commitea en el repo padre — se lo ignora vía `.gitignore`
  (junto con `_backup_v47_antes_pull_2026-10-01/`, commit `8e11c82`), porque
  commitear un worktree sería anidar un repositorio dentro de otro.
- **Verificación en GitHub web (3 de octubre de 2026)**: `docs/` del repo
  padre (`horn-torus-icc-experimental`) lista los 4 archivos de la adenda V47 2
  (commit `eb964d1`, 9:04 GMT-3); el render de `V47_escritos_completos.md`
  muestra la §8 íntegra («LECTURA del análisis espectral», «vecindad A_cr»),
  sin mojibake. La carpeta queda enlazada desde el README del repo padre.

## Alineación del worktree horn-fusion a main — estado V47 (4 de octubre de 2026)

- **Operación**: sobre el worktree `horn-fusion/` (rama `fusion-prcc`) se borró
  el único pendiente de disco (`package-lock.json` sin trackear, ruido de una
  instalación local) y se ejecutó `git -C horn-fusion merge --ff-only main`,
  tal como anticipaba la auditoría del 3/10 (fast-forward garantizado: la rama
  no tenía ningún commit propio, `main..fusion-prcc` = 0).
- **Resultado**: fast-forward limpio `4855b3a → abf8452` («docs: alinea los
  paneles integrados…»): 12 archivos, +5130/−2534. Entra así todo el contenido
  V47 que le faltaba (`vortexSound.ts`, funciones espectrales + ajuste LECTURA
  en `hornTorusMath.ts`, paneles y formularios, `package-lock.json` trackeado,
  `vite.config.ts`, `.env.example`; se retira `bun.lock`).
- **Verificación del estado V47**:
  * `git rev-parse HEAD` = `abf8452…` = `main` del repo real; `git status
    --short --branch` limpio: `## fusion-prcc...origin/fusion-prcc [ahead 7]`.
  * `git diff fusion-prcc main` vacío: el árbol del worktree es idéntico a main.
  * Marcadores V47 en el worktree: «Lectura (V47» en
    `SpectralSingularityPanel.tsx`, «Config Axioma 2» en `App.tsx`,
    `src/utils/vortexSound.ts` en disco y `package-lock.json` trackeado
    (`git ls-files`), junto a `vite.config.ts` y `.env.example`.
  * `npx tsc --noEmit` en el worktree: sin errores (TSC_OK).
- **Estado de la rama**: `fusion-prcc` local quedó **adelantada 7** respecto de
  `origin/fusion-prcc` (que seguía en `4855b3a`). **Pusheada a origin el mismo
  4 de octubre, por pedido explícito**: fast-forward `4855b3a..abf8452` en
  `origin/fusion-prcc`, verificado (`fusion-prcc...origin/fusion-prcc` sin
  adelantos; ambos refs = `abf8452`). GitHub refleja ahora en la rama el
  estado V47, idéntico a `main`; el estado pre-V47 de la auditoría del 3/10
  queda accesible localmente vía `4855b3a` y en la historia de la rama.

## Tesis V48 — Joyce como paradigma de la LECTURA (7 de octubre de 2026)

- **Pedido**: desarrollar en la tesis la sección anunciada «Joyce como paradigma de la LECTURA» (eje (a) del §6.1; anuncio «Joyce paradigma» de la Adenda V47 2). Decisión del autor: **nueva §6.3 + renumerar** (no adenda): la sección entra después de la BME, y Diagnóstico diferencial / Relectura Joyce pasan a 6.4 / 6.5 con referencias cruzadas actualizadas.
- **Fuente → resultado**: `Claude outputs\tesis_rsi_poincare V47 2.docx` (3.619.276 bytes, 307 párrafos; intacta) → `tesis_rsi_poincare V48.docx` (3.621.575 bytes, **313 párrafos** = 307 + 6), con `Claude outputs\gen_v48.py` (zipfile rewrite, patrón `gen_v47_2.py`; `replace_once` robusto: modo single + ventana entre w:t consecutivos preservando rPr).
- **Inserción** (tras «Se conserva el instrumento en este capítulo…», cierre de la BME): título «6.3 Joyce como paradigma de la LECTURA: la epifanía como homología y el sinthome como axioma» + 5 párrafos: (1) epifanía (Stephen Hero) como homología, no representación; títulos de Ulysses (Gilbert/Linati) ~ asignaciones axiomáticas del prototipo (§6.2); (2) estatuto de oído: «What can't be coded can be decorded» (FW) y la letra pública (the letter! the litter!, I.5) como garantía no circular de la BME; (3) el sinthome (R.S.I., SXIII; lectura secundaria, cotejo pendiente) como axioma análogo a las asignaciones marcadas en la interfaz; (4) Ballast Office y la circularidad del Wake (riverrun, «a way a lone…») ~ horn torus: circularidad topológica ≠ circularidad epistémica; (5) Advertencia metodológica con cuatro puntos (i)–(iv): paradigma no es validación; el sinthome no sustituye la BME; Joyce no diagnostica (HCE/ALP); quedan las tareas del Cap. 7 (cotejos Joyce/R.S.I. + tarea (11)).
- **Renumeraciones (5)**: «6.3 Diagnóstico diferencial estructural…» → **6.4**; «6.4 Relectura clínica del caso Joyce…» → **6.5**; tarea (11) «mero anudamiento (§6.3)» → **(§6.4)**; biblio SXIII «(caso Joyce, §6.4)» → **(§6.5)**; Adenda V47 2 «§6.2, Joyce paradigma» → **§6.3**.
- **Verificación (FIN OK, exit=0)**: 313 párrafos; claves 21/21 (título ×1; citas Joyce: Stephen Hero, FW coded ×1 / letter ×2 / riverrun / final / HCE, Ballast; RSI nombre-propio-ego; renumeraciones ×1 c/u); residuos = 0 (títulos 6.3/6.4 viejos, refs viejas, tesis V22, «NO publicado»); orden 6.2 < 6.3 < 6.4 < 6.5 < Cap 7 (pendiente) < Adenda < Bibliografía = **True**; XML válido. Corrección del check de orden: marcadores inequívocos (`Adenda V47 2 — LECTURA` ×3, `Bibliografía secundaria` ×1) — el índice y la nota del proceso mencionan «Bibliografía» y el texto nuevo de §6.3 menciona «La Adenda V47 2 (Capítulo 7)», lo que daba el mismo falso alarma que ya figuraba en V47 2 (`orden adenda<biblio: False`).
- **Espejos**: `Horn Torus\V48_escritos_completos.md` + `V48_escritos_completos.docx` (`md_to_docx.py`; texto íntegro verbatim de la §6.3 + renumeraciones + verificación). Artefactos: `v48_extract.txt` (313 párrafos), `v48_diff.txt`, `_gen_v48_out.txt`; constructor del espejo `gen_espejo_v48.py`.
- **Publicación**: copiado a `docs\` del repo padre (`horn-torus-icc-model-experimental`, tesis V48 + espejos + trazabilidad) con README actualizado y push a origin, patrón autorizado de los ciclos anteriores (7/10/2026).
- **La app y la tesis V48 (7/10/2026)**: el prototipo (worktree `horn-fusion`, rama `fusion-prcc` @ abf8452 = main = origin, **sin cambios de código**) implementa los paneles «Espectral K», «Manual & Lacan» y «Config Axioma 2» de la doctrina V47 y se lee junto con la tesis en estado V48: la §6.3 es el registro epistemológico del prototipo, no una función nueva de la app, así que el avance documental no exige modificar el worktree. Preview rearmado el 7/10 (server vite desde `horn-fusion`, puerto 3000, pid verificado en `.freebuff\run.md`); render validado por DOM (título + botón «Config Axioma 2» + tabs «Espectral K» y «Manual & Lacan»).

## Convenciones de archivo

- Resumen: `Horn_Torus_del_Icc_resumen_v8..v15.md` (espejos en `Claude outputs\*-V28..V47.md`), docx por versión.
- Manual: `MANUAL_HORN_TORUS_v3..v10.md` (en `Metapsicologia Freud Lacan\`).
- Extractores y diffs: `extract_vNN.py` + `vNN_extract.txt` + `vNN_diff.txt` en `Claude outputs\` (V47: generador `gen_v47.py` que inserta los bloques del Axioma 2 rearticulado sobre el zip de `V46 3.docx`).
- Verificación por versión: `verify_v33/v35/v38_2/v40/v44/v46/v47.py` (docx + claves + residuos vetados = 0).
- Propuesta previa a V47: `axioma2_rearticulado_propuesta.md` (original en `Horn Torus\`, espejo en `Claude outputs\`).
- Originales nunca se pisan: cada versión escribe un archivo nuevo.
