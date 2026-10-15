# -*- coding: utf-8 -*-
"""Genera tesis_rsi_poincare V52.docx desde la V51 (Adenda V51).

Inserta 6 parrafos (titulo + 5) al final del Capitulo 7, tras la Proposicion
P.1 y antes del heading «Bibliografia» — el mismo ancla de gen_v51.py.

La Adenda V51 es la verificacion numerica que el punto (3) del estatuto de
P.1 declaro como tarea: (i) la familia REAL X_delta (puerto literal de
computeSclDeformation + rama deformada, delta = deformation_factor);
(ii) topologia por rangos de matrices de frontera sobre GF(2) (b1 calculado,
no inferido); (iii) barrido delta en [0, pi/6] con dos estatutos — dominio
(T2: chi=0, b1=2) e imagen (S^2 vee S^1: chi=1, b1=1, para TODO delta) —;
(iv) delta* = -1/min raw por perfil (default 0.7613 > pi/6; Ruptura 0.2154
< pi/6); (v) SnapPy (unknot T(2,1) y trefoil sigma1^3) cruzado con la
dualidad de Alexander, con el teorema de Jordan para el nucleo plano.

Resultado central (enmienda honesta de P.1): el salto chi 0 -> 1 NO ocurre
en delta = pi/6; es la diferencia entre los dos estatutos de descripcion.
El umbral queda metrico (Wegbreite, Corolario I).

Corrida de la adenda: Claude outputs/adenda_v51_formal.py -> report_adenda_v51.txt
(todos los controles OK, exit=0) + fig_adenda_v51.png.

Patron gen_v51.py: zipfile rewrite, insercion por ancla exacta con pPr
heredado, re-extraccion y verificacion por claves + orden + XML.
"""
import zipfile, re, shutil, os, sys, io, difflib
from xml.sax.saxutils import escape

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='ascii', errors='replace')

BASE = 'C:/Users/cvons/OneDrive/Escritorio/Poincare varios/Claude outputs/'
SRC = BASE + 'tesis_rsi_poincare V51.docx'
DST = BASE + 'tesis_rsi_poincare V52.docx'
EXT = BASE + 'v52_extract.txt'
EXT_SRC = BASE + 'v51_extract.txt'
DIFF = BASE + 'v52_diff.txt'

assert os.path.isfile(SRC), 'no existe el SRC: %s' % SRC

z = zipfile.ZipFile(SRC)
xml = z.read('word/document.xml').decode('utf-8')

paras = re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)
assert len(paras) == 341, u'V51 no tiene 341 parrafos: %d' % len(paras)

def para_text(p):
    return u''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p))

def find_one(prefix):
    hits = [i for i, p in enumerate(paras) if para_text(p).startswith(prefix)]
    assert len(hits) == 1, u'prefijo no unico %r -> %r' % (prefix[:60], hits)
    return hits[0]

def get_pPr(p):
    m = re.search(r'<w:pPr>.*?</w:pPr>', p, re.S)
    return m.group(0) if m else u''

def mk_p(text, pPr):
    return u'<w:p>' + pPr + u'<w:r><w:t xml:space="preserve">' + escape(text) + u'</w:t></w:r></w:p>'

# pPr del heading de P.1 (titulo de la adenda) y del cuerpo de P.1
i_p1 = find_one(u'Proposición P.1 — la transición topológica como cambio de categoría')
pPr_hd = get_pPr(paras[i_p1])
pPr_b1 = get_pPr(paras[i_p1 + 1])

# ================================================================
# ADENDA V51 — 6 parrafos (titulo + 5), insertados ANTES de «Bibliografia»
# ================================================================
T0 = u'Adenda V51 — Verificación numérica del estatuto de P.1: matriz de frontera sobre la familia real X_δ y cruce con SnapPy.'

V1 = (u'El estatuto de P.1 deja la verificación numérica como tarea declarada — su punto (3) remite '
      u'a esta adenda. La adenda la desarrolla. La familia X_δ se toma exactamente como la '
      u'implementación la deforma: f(u, v) = 1 + δ·raw(u, v; SCL-90-R), con raw() el agregado lineal '
      u'de las ocho subescalas — Somatización, Obsesión-Compulsión, Psicoticismo (distorsión en la '
      u'cúspide), GSI, PST, PSDI, Depresión, Ansiedad —, X_δ(u, v) = ((1 + cos v) cos u·f, '
      u'(1 + cos v) sin u·f, sin v·(1 + (f − 1)·0.85)), y δ = deformation_factor, el mismo parámetro '
      u'que fija el umbral Wegbreite del Corolario I (π/6, §6.2). La topología se calcula por rangos '
      u'de matrices de frontera sobre GF(2) — r₁ = rank ∂₁, r₂ = rank ∂₂; b₀ = V − r₁, '
      u'b₁ = E − r₁ − r₂, b₂ = F − r₂; χ = b₀ − b₁ + b₂, con la identidad de Euler como verificación '
      u'interna del conteo. b₁ no se infiere de χ y supuestos sobre b₂: se calcula.')

V2 = (u'El resultado exige distinguir dos estatutos de descripción que el numeral anterior — y la '
      u'leyenda del prototipo — habían leído como uno. (A) El dominio: la triangulación de la malla '
      u'(u, v) ∈ T², con la fila v = π como vértices propios, mide χ = 0, b₁ = 2, b₂ = 1 — homotopía '
      u'del toro — para todo δ. (B) La imagen en E³: la fila v = π ES el punto p de la voz (ρ = 0 '
      u'exacto en v = π para todo δ), identificada a un único vértice, con descarte de las caras '
      u'degeneradas; mide χ = 1, b₁ = 1, b₂ = 1 — homotopía de S² ∨ S¹ — para todo δ, incluido '
      u'δ = 0. Enunciado corregido: el paso χ = 0 → 1 no es un evento en δ = π/6; es la diferencia '
      u'entre los dos estatutos. El umbral δ ≥ π/6 queda estatuido como condición métrica del cruce '
      u'(Wegbreite, Corolario I): en [0, π/6] la imagen se mantiene S² ∨ S¹ en las 15 muestras del '
      u'barrido (min f ≥ 0.3122 en el extremo). El argumento de categoría de P.1 no se debilita: se '
      u'precisa — el objeto nunca fue una superficie cerrada orientable (χ = 1 constante de la '
      u'imagen, con p en ella para todo δ), y la transición «0 → 1» del prototipo era el pasaje '
      u'entre la descripción paramétrica y la descripción como objeto.')

V3 = (u'El evento topológico genuino, por perfil, es δ* = −1/min raw: el primer δ con f ≤ 0 en algún '
      u'punto — la deformación atraviesa el eje y la familia pierde el estatuto de superficie. Perfil '
      u'por omisión (IGS 0.85): raw_min = −1.3135, δ* = 0.7613 > π/6 = 0.5236: en el régimen '
      u'Wegbreite f > 0 siempre, y no hay evento topológico en [0, π/6]. Perfil «Ruptura del modelo» '
      u'(IGS 3.30, fuera de baremo): raw_min = −4.6427, δ* = 0.2154 < π/6: la deformación atraviesa '
      u'el eje antes del umbral Wegbreite — el extremo rompe el objeto antes de que la anchura lo '
      u'disipe, consistente con su estatuto clínico (AXIOMA de eyección, no un caso del régimen, '
      u'§6.2). δ* es función del perfil: la adenda lo declara como cantidad computable, no como '
      u'universal.')

V4 = (u'El núcleo del sólido delimitado por X_δ, γ_δ(u) = (a cos u, a sin u, 0)·f̄(u) con f̄ el '
      u'promedio radial del factor, es una curva plana (z = 0) con f̄ > 0 en el régimen: por el '
      u'teorema de Jordan es un unknot — verificación de tres líneas, más fuerte que un chequeo de '
      u'software. SnapPy 3.3.2 aporta la homología del complemento vía O8: sobre un representante '
      u'del unknot con una componente (T(2,1)), H₁(exterior) = ℤ, volumen 0; control afirmativo con '
      u'el trefoil (σ₁³), H₁ = ℤ, volumen 0 — las herramientas no confunden unknot con nudo genuino '
      u'— y verificación, con nuestra propia matriz de frontera, de que la frontera del tubo del '
      u'trefoil mide χ = 0, b₁ = 2, b₂ = 1 como la de todo tubo nudo genuino. El cruce con la '
      u'dualidad de Alexander (H̃₁(S³∖X_δ) ≅ H̃¹(X_δ)): por matriz de frontera H̃¹(X_δ) = ℤ '
      u'(b₁ = 1), y las dos piezas del complemento miden ℤ ⊕ 0 — el interior, homotópico a γ_δ '
      u'(unknot: ℤ por SnapPy), y el exterior, acíclico (H₁(E) = 0; la línea 115 de la tesis lo '
      u'registraba por cita: aquí se suma cómputo directo). Quedan para el topólogo externo — que la '
      u'tesis misma se autoexige — π₁(E) = 1 («E simplemente conexo») y la regularidad (tameness) '
      u'exigida por las hipótesis de Alexander.')

V5 = (u'Artefactos y estatuto. La verificación corre en adenda_v51_formal.py: puerto literal del '
      u'cálculo de deformación del prototipo (hornTorusMath.ts), rangos de frontera sobre GF(2) por '
      u'reducción bitset, controles A/B (toro / S² ∨ S¹), barrido de δ en [0, π/6] y detección de δ* '
      u'por perfil, bloque SnapPy (unknot T(2,1) y trefoil σ₁³) y gráfico (fig_adenda_v51.png: χ, b₁ '
      u'y min f contra δ, con las líneas π/6 y δ*). Reporte de corrida: todos los controles OK, '
      u'exit = 0 (report_adenda_v51.txt; la demo previa, adenda_v51_demo.py, queda sustituida: su '
      u'colapso por proyección era el modelo del gesto, y sus b₁ «inferidos» por supuestos sobre b₂ '
      u'— 3 y 1 — son reemplazados por el cómputo directo: b₁ = 1, χ = 1). Estatuto: esta adenda es '
      u'verificación ejecutada del enunciado corregido, no reemplaza la prueba formal de P.1, que '
      u'sigue pendiente y declarada como tarea (construcción del autor); queda cerrado el punto (3) '
      u'del esqueleto — la verificación «antes y después del umbral» se realizó, y su resultado '
      u'reubica el salto de χ: no en δ, sino en el estatuto de descripción.')

BLOCK = mk_p(T0, pPr_hd) + u''.join(mk_p(t, pPr_b1) for t in [V1, V2, V3, V4, V5])

# ancla: el heading «Bibliografia» del cuerpo (el mismo de gen_v51)
biblio = None
paras_now = re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)
for j in range(len(paras_now) - 1, -1, -1):
    if para_text(paras_now[j]).strip() == u'Bibliografía':
        biblio = paras_now[j]
        break
assert biblio is not None, u'no se hallo el heading Bibliografia del cuerpo'

xml = xml.replace(biblio, BLOCK + biblio, 1)
print(u'insertada Adenda V51 (6 parrafos) tras P.1, antes de Bibliografia')

# ================================================================
# reescritura del zip
# ================================================================
shutil.copyfile(SRC, DST)
zin = zipfile.ZipFile(SRC)
zout = zipfile.ZipFile(DST, 'w', zipfile.ZIP_DEFLATED)
for item in zin.infolist():
    data = zin.read(item.filename)
    if item.filename == 'word/document.xml':
        data = xml.encode('utf-8')
    zout.writestr(item, data)
zout.close(); zin.close()
print('V52 escrito:', os.path.getsize(DST), 'bytes')

# ================================================================
# re-extraer y verificar
# ================================================================
xml2 = zipfile.ZipFile(DST).read('word/document.xml').decode('utf-8')
p2 = re.findall(r'<w:p[ >].*?</w:p>', xml2, re.S)
text2 = u'\n'.join(para_text(_p) for _p in p2)
with open(EXT, 'w', encoding='utf-8') as f:
    f.write(text2)
print('paragraphs V52:', len(p2), '(esperado 347 = 341 + 6)')

with open(EXT_SRC, encoding='utf-8') as f:
    src_text = f.read()
src_lines, dst_lines = src_text.split(u'\n'), text2.split(u'\n')
with open(DIFF, 'w', encoding='utf-8') as f:
    for line in difflib.unified_diff(src_lines, dst_lines, fromfile='v51', tofile='v52', lineterm=''):
        f.write(line + u'\n')
print('diff escrito:', DIFF)

# ------------------------------------------------------------------- claves
KEYS = [
    (u'Adenda V51 — Verificación numérica del estatuto de P.1', u'AD_titulo', 1),
    (u'b₁ no se infiere de χ', u'AD_b1_calculado', 1),
    (u'homotopía de S² ∨ S¹', u'AD_S2vS1', 1),
    (u'Enunciado corregido', u'AD_enunciado_corregido', 1),
    (u'δ* = 0.7613', u'AD_dstar_default', 1),
    (u'δ* = 0.2154', u'AD_dstar_ruptura', 1),
    (u'(T(2,1))', u'AD_unknot_rep', 1),
    (u'σ₁³', u'AD_trefoil', 2),
    (u'dualidad de Alexander (H̃₁(S³∖X_δ) ≅ H̃¹(X_δ))', u'AD_duality', 1),
    (u'adenda_v51_formal.py', u'AD_script', 1),
    (u'report_adenda_v51.txt', u'AD_report', 1),
    (u'fig_adenda_v51.png', u'AD_fig', 1),
    (u'adenda_v51_demo.py, queda sustituida', u'AD_demo_sustituida', 1),
    (u'Reporte de corrida: todos los controles OK', u'AD_exit0', 1),
    # V51 intacto
    (u'Proposición P.1 — la transición topológica como cambio de categoría', u'V51_p1_intacto', 1),
    (u'la característica de ℝP²', u'V51_rp2_intacto', 1),
    (u'Axioma 5 — instrumentario de medición', u'V51_ax5_intacto', 1),
    (u'la voz no se promedia', u'V51_voz_intacto', 1),
    # V50 intacto
    (u'configAxioma2 no altera ningún cálculo de nudos', u'V50_s48_intacto', 1),
    (u'Here Comes Everybody', u'V51_s63_intacto', 1),
]
bad = 0
for k, label, want in KEYS:
    got = text2.count(k)
    ok = got == want
    if not ok:
        bad += 1
    print('%s %s -> %d (esperado %d)' % ('OK ' if ok else 'BAD', label, got, want))
print('claves en BAD:', bad)

# ------------------------------------------------------------------- orden
def pos(s):
    return text2.find(s)

ORD1 = [u'Proposición P.1 — la transición topológica', u'Adenda V51 — Verificación numérica',
        u'Bibliografía secundaria']
orden_ad = all(-1 < a < b for a, b in zip([pos(s) for s in ORD1], [pos(s) for s in ORD1][1:]))
if not orden_ad:
    print('POS_AD:', ORD1)
print('orden P.1 < Adenda V51 < biblioSec:', orden_ad)

ORD = [u'Los cuatro axiomas siguientes', u'Axioma 5 — instrumentario',
       u'6.1 Ejes de desarrollo', u'Here Comes Everybody',
       u'6.5 Relectura clínica del caso Joyce',
       u'Adenda V47 2 — LECTURA del análisis espectral', u'Cierre metodológico.',
       u'Proposición P.1 — la transición topológica',
       u'Adenda V51 — Verificación numérica', u'Bibliografía secundaria']
orden_gen = all(-1 < a < b for a, b in zip([pos(s) for s in ORD], [pos(s) for s in ORD][1:]))
if not orden_gen:
    print('POSICIONES:', [(s, pos(s)) for s in ORD])
print('orden general V52:', orden_gen)

hemiciclo = [pos(u'Resumen'), pos(u'Índice'), pos(u'Capítulo 1 — Del toro al nudo')]
orden_abs = all(-1 < a < b for a, b in zip(hemiciclo, hemiciclo[1:]))
print('orden Resumen < Índice < Cap1:', orden_abs)

import xml.dom.minidom
ok_xml = True
try:
    xml.dom.minidom.parseString(xml2)
    print('XML valido: OK')
except Exception as e:
    print('XML INVALIDO:', e)
    ok_xml = False

FIN = (bad == 0 and orden_ad and orden_gen and orden_abs and len(p2) == 347 and ok_xml)
print('FIN OK' if FIN else 'FIN CON ERRORES')
sys.exit(0 if FIN else 1)
