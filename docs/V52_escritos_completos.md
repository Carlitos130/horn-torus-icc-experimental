# Horn Torus ICC Model — Escritos completos del ciclo V52

**Documento único** con todo el texto escrito por el agente (Buffy / Codebuff)
a pedido del Lic. Carlos Vonsik durante el ciclo V52, 15 de octubre de 2026.
El ciclo V52 formaliza la **Adenda V51** — la verificación numérica que el punto (3)
del estatuto de **Proposición P.1** (V51) había declarado como tarea — sobre la
familia REAL X_δ del prototipo: topología por matriz de frontera (GF(2)), barrido
δ ∈ [0, π/6], detección de δ* por perfil y cruce con SnapPy / dualidad de Alexander.
Todo está extraído textualmente de los archivos que se indican en cada sección.

---

## 0. Qué es la V52 y cómo se produjo

- **Fuente:** `tesis_rsi_poincare V51.docx` (3.627.491 bytes, 341 párrafos) — intacta, nunca pisada.
- **Verificación previa:** `Claude outputs/adenda_v51_formal.py` (puerto literal de `computeSclDeformation` de `hornTorusMath.ts`; rangos GF(2) por bitsets; SnapPy 3.3.2) — **todos los controles OK, exit=0**; gráfico `fig_adenda_v51.png`; reporte `report_adenda_v51.txt`. La demo previa (`adenda_v51_demo.py`, 14/10/2026) queda **sustituida**.
- **Generador:** `Claude outputs/gen_v52.py` (zipfile rewrite, patrón `gen_v51.py`; inserción por ancla exacta con pPr heredado).
- **Resultado:** `tesis_rsi_poincare V52.docx` (3.628.972 bytes, 347 párrafos = 341 + 6; XML válido).
- **Cambios:** inserción pura de 6 párrafos (título + 5) tras la Proposición P.1, antes del heading «Bibliografía». Nada más cambia (V51 íntegra).
- **Enmienda honesta que la adenda registra:** el paso χ = 0 → 1 **no es un evento en δ = π/6** — es la diferencia entre los dos estatutos de descripción (dominio: T², χ = 0; imagen: S² ∨ S¹, χ = 1, con p presente para todo δ). El umbral π/6 queda métrico (Wegbreite, Corolario I). El evento topológico genuino por perfil es δ\* = −1/min raw (default: 0.7613 > π/6; Ruptura: 0.2154 < π/6).

---

## 1. Tesis V52 — la Adenda V51 (texto íntegro)

Inserción pura: +6 párrafos, −0. Verbatim de `v52_diff.txt` / `v52_extract.txt`.

**Adenda V51 — Verificación numérica del estatuto de P.1: matriz de frontera sobre la familia real X_δ y cruce con SnapPy.**

El estatuto de P.1 deja la verificación numérica como tarea declarada — su punto (3) remite a esta adenda. La adenda la desarrolla. La familia X_δ se toma exactamente como la implementación la deforma: f(u, v) = 1 + δ·raw(u, v; SCL-90-R), con raw() el agregado lineal de las ocho subescalas — Somatización, Obsesión-Compulsión, Psicoticismo (distorsión en la cúspide), GSI, PST, PSDI, Depresión, Ansiedad —, X_δ(u, v) = ((1 + cos v) cos u·f, (1 + cos v) sin u·f, sin v·(1 + (f − 1)·0.85)), y δ = deformation_factor, el mismo parámetro que fija el umbral Wegbreite del Corolario I (π/6, §6.2). La topología se calcula por rangos de matrices de frontera sobre GF(2) — r₁ = rank ∂₁, r₂ = rank ∂₂; b₀ = V − r₁, b₁ = E − r₁ − r₂, b₂ = F − r₂; χ = b₀ − b₁ + b₂, con la identidad de Euler como verificación interna del conteo. b₁ no se infiere de χ y supuestos sobre b₂: se calcula.

El resultado exige distinguir dos estatutos de descripción que el numeral anterior — y la leyenda del prototipo — habían leído como uno. (A) El dominio: la triangulación de la malla (u, v) ∈ T², con la fila v = π como vértices propios, mide χ = 0, b₁ = 2, b₂ = 1 — homotopía del toro — para todo δ. (B) La imagen en E³: la fila v = π ES el punto p de la voz (ρ = 0 exacto en v = π para todo δ), identificada a un único vértice, con descarte de las caras degeneradas; mide χ = 1, b₁ = 1, b₂ = 1 — homotopía de S² ∨ S¹ — para todo δ, incluido δ = 0. Enunciado corregido: el paso χ = 0 → 1 no es un evento en δ = π/6; es la diferencia entre los dos estatutos. El umbral δ ≥ π/6 queda estatuido como condición métrica del cruce (Wegbreite, Corolario I): en [0, π/6] la imagen se mantiene S² ∨ S¹ en las 15 muestras del barrido (min f ≥ 0.3122 en el extremo). El argumento de categoría de P.1 no se debilita: se precisa — el objeto nunca fue una superficie cerrada orientable (χ = 1 constante de la imagen, con p en ella para todo δ), y la transición «0 → 1» del prototipo era el pasaje entre la descripción paramétrica y la descripción como objeto.

El evento topológico genuino, por perfil, es δ* = −1/min raw: el primer δ con f ≤ 0 en algún punto — la deformación atraviesa el eje y la familia pierde el estatuto de superficie. Perfil por omisión (IGS 0.85): raw_min = −1.3135, δ* = 0.7613 &gt; π/6 = 0.5236: en el régimen Wegbreite f &gt; 0 siempre, y no hay evento topológico en [0, π/6]. Perfil «Ruptura del modelo» (IGS 3.30, fuera de baremo): raw_min = −4.6427, δ* = 0.2154 &lt; π/6: la deformación atraviesa el eje antes del umbral Wegbreite — el extremo rompe el objeto antes de que la anchura lo disipe, consistente con su estatuto clínico (AXIOMA de eyección, no un caso del régimen, §6.2). δ* es función del perfil: la adenda lo declara como cantidad computable, no como universal.

El núcleo del sólido delimitado por X_δ, γ_δ(u) = (a cos u, a sin u, 0)·f̄(u) con f̄ el promedio radial del factor, es una curva plana (z = 0) con f̄ &gt; 0 en el régimen: por el teorema de Jordan es un unknot — verificación de tres líneas, más fuerte que un chequeo de software. SnapPy 3.3.2 aporta la homología del complemento vía O8: sobre un representante del unknot con una componente (T(2,1)), H₁(exterior) = ℤ, volumen 0; control afirmativo con el trefoil (σ₁³), H₁ = ℤ, volumen 0 — las herramientas no confunden unknot con nudo genuino — y verificación, con nuestra propia matriz de frontera, de que la frontera del tubo del trefoil mide χ = 0, b₁ = 2, b₂ = 1 como la de todo tubo nudo genuino. El cruce con la dualidad de Alexander (H̃₁(S³∖X_δ) ≅ H̃¹(X_δ)): por matriz de frontera H̃¹(X_δ) = ℤ (b₁ = 1), y las dos piezas del complemento miden ℤ ⊕ 0 — el interior, homotópico a γ_δ (unknot: ℤ por SnapPy), y el exterior, acíclico (H₁(E) = 0; la línea 115 de la tesis lo registraba por cita: aquí se suma cómputo directo). Quedan para el topólogo externo — que la tesis misma se autoexige — π₁(E) = 1 («E simplemente conexo») y la regularidad (tameness) exigida por las hipótesis de Alexander.

Artefactos y estatuto. La verificación corre en adenda_v51_formal.py: puerto literal del cálculo de deformación del prototipo (hornTorusMath.ts), rangos de frontera sobre GF(2) por reducción bitset, controles A/B (toro / S² ∨ S¹), barrido de δ en [0, π/6] y detección de δ* por perfil, bloque SnapPy (unknot T(2,1) y trefoil σ₁³) y gráfico (fig_adenda_v51.png: χ, b₁ y min f contra δ, con las líneas π/6 y δ*). Reporte de corrida: todos los controles OK, exit = 0 (report_adenda_v51.txt; la demo previa, adenda_v51_demo.py, queda sustituida: su colapso por proyección era el modelo del gesto, y sus b₁ «inferidos» por supuestos sobre b₂ — 3 y 1 — son reemplazados por el cómputo directo: b₁ = 1, χ = 1). Estatuto: esta adenda es verificación ejecutada del enunciado corregido, no reemplaza la prueba formal de P.1, que sigue pendiente y declarada como tarea (construcción del autor); queda cerrado el punto (3) del esqueleto — la verificación «antes y después del umbral» se realizó, y su resultado reubica el salto de χ: no en δ, sino en el estatuto de descripción.

---

## 2. La verificación en números (report_adenda_v51.txt)

> FAMILIA REAL X_delta (adenda_v51_formal.py)
>   perfil: DEFAULT_SCL90R_DATA; raw_min=-1.313542  raw_max=1.482226
>   delta* (f<=0) teorico = 0.761300   |   Wegbreite pi/6 = 0.523599
> CONTROL A - dominio (T^2, delta=0, sin identificar cuspide):
>   [ OK  ] chi A: got 0, want 0
>   [ OK  ] b1 A: got 2, want 2
>   [ OK  ] b2 A: got 1, want 1
> CONTROL B - imagen (cuspide p identificada, delta=0):
>   [ OK  ] chi B: got 1, want 1
>   [ OK  ] b1 B: got 1, want 1
>   [ OK  ] b2 B: got 1, want 1
> BARRIDO delta (imagen, SCL default):
>    delta    min_f   chi  b0  b1  b2   E      F
>   0.0000    1.0000   1   1   1   1 15336 10224
>   0.0374    0.9509   1   1   1   1 15336 10224
>   0.0748    0.9017   1   1   1   1 15336 10224
>   0.1122    0.8526   1   1   1   1 15336 10224
>   0.1496    0.8035   1   1   1   1 15336 10224
>   0.1870    0.7544   1   1   1   1 15336 10224
>   0.2244    0.7052   1   1   1   1 15336 10224
>   0.2618    0.6561   1   1   1   1 15336 10224
>   0.2992    0.6070   1   1   1   1 15336 10224
>   0.3366    0.5579   1   1   1   1 15336 10224
>   0.3740    0.5087   1   1   1   1 15336 10224
>   0.4114    0.4596   1   1   1   1 15336 10224
>   0.4488    0.4105   1   1   1   1 15336 10224
>   0.4862    0.3614   1   1   1   1 15336 10224
>   0.5236    0.3122   1   1   1   1 15336 10224
>   => en [0, pi/6] la imagen X_delta se mantiene homotopa a S^2 vee S^1
>      (chi=1, b1=1, b2=1 en todos los deltas): el umbral pi/6 es METRICO
>   delta* = 0.761300 > pi/6 : en el regimen Wegbreite f>0 siempre:
>   NO hay evento topologico en [0, pi/6] para este perfil.
> perfil RUPTURA (IGS 3.30, fuera de baremo): raw_min=-4.642719  delta*=0.215391  (pi/6=0.523599)
>   ATENCION: en el perfil extrema delta* <= pi/6: f<=0 ANTES del umbral
>   Wegbreite. Estatuto B antes/despu?s de delta*:
>     pre  (delta=0.2111): chi=1 b1=1 b2=1 min_f=0.0200
>     (despues de delta* la parametrizacion atraviesa el eje: la familia
>      pierde estado de superficie: reportado, no silenciado)
> SNAPPY 3.3.2 (exterior .homology() via O8; volumen geometrico):
>   [ OK  ] unknot 1 componente: 1
>   [ OK  ] unknot homology: Z
>   [ OK  ] unknot vol==0: True
>   trefoil (s1^3):        homology=Z  volume=0.0000
>   [ OK  ] trefoil ext homology == Z: Z
>   frontera tubo trefoil (nuestro complejo): chi=0 b1=2 b2=1
>   [ OK  ] trefoil tube chi==0: 0
>   [ OK  ] trefoil tube b1==2: 2
>   [ OK  ] trefoil tube b2==1: 1
>   sintesis dualidad X_delta (imagen):
>     H~^1(X_delta) = Z (b1=1 por matriz de frontera)
>     H~_1(S^3\X_delta) = Z (interior ~gamma=unknown: SnapPy Z) + H_1(exterior)=0
> grafico: fig_adenda_v51.png
> ADENDA FORMAL OK

Gráfico: `Claude outputs/fig_adenda_v51.png` — χ(X_δ), b₁(X_δ) y min f contra δ, con las líneas π/6 (rojo) y δ\* (violeta).

---

## 3. Verificación (15 de octubre de 2026)

Corrida final de `gen_v52.py`: exit=0, **FIN OK**.

- paragraphs V52: **347** (esperado 347 = 341 + 6).
- Claves **20/20 OK** (BAD=0): título adenda ×1; «b₁ no se infiere de χ» ×1; «homotopía de S² ∨ S¹» ×1; «Enunciado corregido» ×1; δ\* default y Ruptura ×1 c/u; unknot (T(2,1)) ×1; trefoil σ₁³ ×2; dualidad de Alexander ×1; artefactos (script/report/fig/demo sustituida) ×1 c/u; V50/V51 intactos ×1 c/u.
- **Orden** P.1 < Adenda V51 < Bibliografía: **True**; orden general V52 (Cap 5 < Axioma 5 < Cap 6 < Joyce < Adenda V47 2 < Cierre < P.1 < Adenda V51 < biblio): **True**.
- XML válido: OK. Diff: inserción pura de 6 párrafos (`v52_diff.txt`).

---

## 4. Ubicaciones (15/10/2026)

| Qué | Archivo |
|---|---|
| **Tesis V52** | `…\Poincare varios\Claude outputs\tesis_rsi_poincare V52.docx` |
| Script de la adenda | `…\Claude outputs\adenda_v51_formal.py` (exit=0) |
| Reporte / gráfico | `…\Claude outputs\report_adenda_v51.txt` / `fig_adenda_v51.png` |
| Extracto / diff | `…\Claude outputs\v52_extract.txt` (347 párrafos) / `v52_diff.txt` |
| Generador | `…\Claude outputs\gen_v52.py` |
| Trazabilidad | `…\Poincare varios\Horn Torus\trazabilidad_V28_a_V47.md` (sección V52, 15/10/2026) |
| Espejo público | `docs\` del repo padre `horn-torus-icc-model-experimental` (GitHub, commit del 15/10/2026) |
| Espejo docx | `…\Horn Torus\V52_escritos_completos.docx` (este .md convertido con `md_to_docx.py`) |

Nota de estatuto: la Adenda es verificación ejecutada, no reemplaza la prueba formal
de P.1 (pendiente, construcción del autor); la verificación «E simplemente conexo»
(π₁(E) = 1) y la tameness siguen siendo tarea del topólogo externo (tesis, línea 115).
