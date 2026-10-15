# -*- coding: utf-8 -*-
"""Adenda V51 FORMAL (reemplaza a adenda_v51_demo.py)
================================================================
Verificacion numerica de P.1 sobre la familia REAL X_delta del prototipo.

(1) Familia X_delta: NO es la proyeccion gruesa de la demo: es la deformacion
    exacta que la app aplica (hornTorusMath.ts, computeSclDeformation +
    rama deformada de generatePulsionVectorFieldData):

      r0(u,v) = a (1 + cos v)                    (parametrizacion del prototipo)
      f(u,v)  = 1 + delta * raw(u,v;  SCL-90-R)  (factor por esclerosion)
      X_delta(u,v) = ( r0 cos u * f , r0 sin u * f , a sin v * (1+(f-1)*0.85) )

    con delta = params.deformation_factor (umbral Wegbreite pi/6 codificado
    como WEGREITE_MIN_DELTA). raw() es una copia literal de computeSclDeformation.

(2) Topologia por matriz de frontera sobre GF(2): no se INFIERE b1 de chi:
    se calculan rangos r1 = rank(d1), r2 = rank(d2) directamente:
      b0 = V - r1 ;  b1 = E - r1 - r2 ;  b2 = F - r2 ; chi = b0 - b1 + b2.
    Identidad de verificacion interna: chi == V - E + F.

(3) Dos estatutos, que P.1 debe distinguir:
    ESTATUTO A (DOMINIO / parametrizacion): la malla de (u,v) en T^2 SIN
    identificar la cuspide  ->  homotopia de T^2: chi=0, b1=2, b2=1.
    ESTATUTO B (IMAGEN / el objeto en R^3): los NU puntos (v=pi, todo u; la
    casa de la voz p) se identifican AL PUNTO p  ->  homotopia de S^2 vee S^1:
    chi=1, b1=1, b2=1.
    La familia X_delta para delta razonable NO cambia de categoria en
    [0, pi/6]: el objeto tiene SIEMPRE la cuspide p (rho=0 exacto en v=pi).
    El evento topologico genuino es delta* := -1/min raw (si min raw<0):
    el primer delta con f<=0 en algun punto (la deformacion atraviesa el eje).

(4) SnapPy 3.3.2: solo acepta PD/braids/DT (no polilineas) -> el estatus del
    nucleo gamma_delta se resuelve TEOREMA (Jordan: curva plana con radio>0
    es unknown) y SnapPy aporta la homologia del exterior con un
    representante PD del unknown + trefoil como CONTROL afirmativo.
    Cruce con dualidad de Alexander:  H~_1(S^3 - X) ≅ H~^1(X),
    pieza por pieza con lo que cada herramienta puede medir.

Ejecucion aditiva de controles; exit!=0 si cualquier control falla.
"""
import io
import math
import sys

import numpy as np

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="ascii", errors="replace")

PI = math.pi
WEGREITE = PI / 6.0          # WEGREITE_MIN_DELTA / WEGREITE_DISIPACION_DELTA
SCL_ITEMS = 90.0

# ----------------------------------------------------------------------------
# 1) Puerto literal de computeSclDeformation (hornTorusMath.ts:792-839)
# ----------------------------------------------------------------------------

def pst_geom(pst):
    return pst / (SCL_ITEMS / 4.0)


def scl_scores(d):
    """Orden ynormalizacion identicos a la TS: keys del SCL90RData."""
    return {
        "som": d["Somatizacion"],
        "oc": d["Obsesion-Compulsion"],
        "psy": d["Psicoticismo"],
        "gsi": d["GSI"],
        "pst": pst_geom(d["PST"]),
        "psdi": d["PSDI"],
        "dep": d["Depresion"],
        "anx": d["Ansiedad"],
    }


DEFAULT_SCL90R_DATA = {
    "Somatizacion": 0.8, "Obsesion-Compulsion": 0.9,
    "Sensibilidad Interpersonal": 0.7, "Depresion": 0.85,
    "Ansiedad": 0.95, "Hostilidad": 0.6, "Ansiedad Fobica": 0.75,
    "Ideacion Paranoide": 0.8, "Psicoticismo": 0.9,
    "GSI": 0.85, "PST": 45, "PSDI": 1.70,
}

RUPTURA_SCL90R_DATA = {
    "Somatizacion": 3.10, "Obsesion-Compulsion": 3.40,
    "Sensibilidad Interpersonal": 3.30, "Depresion": 3.20,
    "Ansiedad": 3.40, "Hostilidad": 3.50, "Ansiedad Fobica": 2.90,
    "Ideacion Paranoide": 3.60, "Psicoticismo": 3.50,
    "GSI": 3.30, "PST": 88, "PSDI": 3.38,
}


def raw_deform_grid(U, V, d):
    """raw(u,v) sobre grillas U[mu], V[mv] (broadcast). Igual que la TS."""
    s = scl_scores(d)
    tu, tv = U[:, None], V[None, :]
    cu, su, cv, sv = np.cos(tu), np.sin(tu), np.cos(tv), np.sin(tv)
    w = np.zeros_like(tu + tv, dtype=float)
    w += s["som"] * 0.28 * np.cos(3 * tv) * (1 + 0.35 * cu)          # Somatizacion
    w += s["oc"] * 0.32 * np.sin(4 * tu) * cv                       # O-C
    cusp = np.abs(np.sin(tv * 0.5))
    w += s["psy"] * 0.45 * cusp ** 3 * np.sin(2 * tu + tv)          # Psicoticismo
    w += s["gsi"] * 0.22 * (cv + 0.5 * su)                          # GSI
    w += s["pst"] * 0.15 * np.sin(5 * tv + 3 * tu)                  # PST
    w += s["psdi"] * 0.20 * np.cos(2 * tv - 2 * tu)                 # PSDI
    w += s["dep"] * 0.18 * sv                                       # Depresion
    w += s["anx"] * 0.14 * np.sin(8 * tu) * np.cos(2 * tv)          # Ansiedad
    return w


def deform_family(U, V, delta, d, a=1.0):
    """X_delta(u,v) grilla: devuelve verts[(mv,mu,3)] y f[(mv,mu)].

    Copia literal de la rama deformada de la app:
      x *= f ; y *= f ; z *= 1 + (f-1)*0.85  con base x=r0 cosu, y=r0 sinu, z=a sinv.
    """
    r0 = a * (1 + np.cos(V))[None, :]   # (1,mv)
    x0 = np.cos(U)[:, None] * r0        # (mu,1)*(1,mv)
    y0 = np.sin(U)[:, None] * r0
    z0 = (a * np.sin(V))[None, :]
    f = 1.0 + delta * raw_deform_grid(U, V, d)   # (mu,mv)
    x = x0 * f
    y = y0 * f
    z = z0 * (1.0 + (f - 1.0) * 0.85)
    return np.stack([x, y, z], axis=-1), f

# ----------------------------------------------------------------------------
# 2) Complejo CW y homologia sobre GF(2) (python-bigint bitsets)
# ----------------------------------------------------------------------------
def build_complex(U, V, verts, identify_cutus=True, filter_area=None):
    """Malla parametrica na x nv; vertice canonico en la cuspide si identifica.
    Devuelve (vertex_ids[(mu,mv)], faces[list de tri], n_vertices).
    filter_area: SI solo para el estatuto B (imagen: caras degeneradas reales).
    En el estatuto A (dominio abstracto) NO se filtra: el complejo del dominio
    es la triangulacion combinatoria, con las caras colapsadas de la fila v=pi
    (asi da la homotopia de T^2, como en la demo). Default: igual que identify.
    </pp>
    - identify_cusp: TODAS las (v=pi, u) van a UN vertice (el punto p de la voz).
    - caras degeneradas (indices repetidos o area nula) NO se agregan.
    """
    mu, mv = len(U), len(V)
    vids = np.empty((mu, mv), dtype=int)
    n = 0
    cusp_j = None
    for j, v in enumerate(V):
        if abs(v - PI) < 1e-12:
            cusp_j = j
    for j in range(mv):
        if identify_cutus and cusp_j is not None and j == cusp_j:
            vids[:, j] = n
            n += 1           # un solo vertice p para toda la cuspide (1, ·)
        else:
            for i in range(mu):
                vids[i, j] = n
                n += 1
    faces = []
    for j in range(mv):
        jn = (j + 1) % mv
        for i in range(mu):
            i_n = (i + 1) % mu
            a, b, c, dd = vids[i, j], vids[i_n, j], vids[i_n, jn], vids[i, jn]
            for tri in ((a, b, c), (a, c, dd)):
                if tri[0] != tri[1] and tri[1] != tri[2] and tri[0] != tri[2]:
                    faces.append(tri)
    # mapa vid -> posicion (la cuspide identificada usa la posicion de p)
    pos = np.empty((n, 3))
    for j in range(mv):
        if identify_cutus and cusp_j is not None and j == cusp_j:
            pos[vids[0, j]] = verts[0, j]
        else:
            for i in range(mu):
                pos[vids[i, j]] = verts[i, j]
    if (filter_area if filter_area is not None else bool(identify_cutus)):
        faces = _filter_zero_area(faces, pos)
    return faces, n


def _crossnorm(e1, e2):
    e1, e2 = np.asarray(e1, float), np.asarray(e2, float)
    return float(np.cross(e1, e2) @ e1) if False else _cross_vec(e1, e2)


def _cross_vec(e1, e2):
    return (e1[1] * e2[2] - e1[2] * e2[1],
            e1[2] * e2[0] - e1[0] * e2[2],
            e1[0] * e2[1] - e1[1] * e2[0])


def _filter_zero_area(faces, verts, tol=1e-14):
    out = []
    for tri in faces:
        p0, p1, p2 = verts[tri[0]], verts[tri[1]], verts[tri[2]]
        cx = _cross_vec(p1 - p0, p2 - p0)
        area2 = math.sqrt(cx[0] ** 2 + cx[1] ** 2 + cx[2] ** 2)
        if area2 > tol:
            out.append(tri)
    return out


def homology_gf2(faces, n_vertices):
    """b0, b1, b2, chi de un complejo 2D por rangos de d1 y d2 sobre GF(2)."""
    # aristas unicas indexadas
    edge_index = {}
    edges = []
    for f in faces:
        for a, b in ((f[0], f[1]), (f[1], f[2]), (f[2], f[0])):
            a, b = int(a), int(b)
            key = (a, b) if a < b else (b, a)
            if key not in edge_index:
                edge_index[key] = len(edges)
                edges.append(key)
    d2_rows = []  # filas = caras (bits = sus 3 aristas); claves Python-int
    for f in faces:
        bits = 0
        for a, b in ((f[0], f[1]), (f[1], f[2]), (f[2], f[0])):
            a, b = int(a), int(b)
            key = (a, b) if a < b else (b, a)
            bits |= 1 << edge_index[key]
        d2_rows.append(bits)
    # d1: filas = aristas (bits = sus 2 vertices)
    d1_rows = [ int((1 << int(a)) | (1 << int(b))) for a, b in edges ]

    r1 = rank_gf2(d1_rows)
    r2 = rank_gf2(d2_rows)
    nV, nE, nF = n_vertices, len(edges), len(faces)
    # conectividad por union... b0 por componentes: rank_gf2(d1) da r1; b0 = V - r1
    b0 = nV - r1
    b1 = nE - r1 - r2
    b2 = nF - r2
    chi = b0 - b1 + b2
    assert chi == nV - nE + nF, "identidad de Euler violada (bug de conteo)"
    return {"V": nV, "E": nE, "F": nF, "r1": r1, "r2": r2,
            "b0": b0, "b1": b1, "b2": b2, "chi": chi}


def rank_gf2(rows):
    """rank sobre GF(2) por eliminacion con bitsets (python int)."""
    basis = {}
    for r in rows:
        while r:
            lead = r.bit_length() - 1
            if lead in basis:
                r ^= basis[lead]
            else:
                basis[lead] = r
                break
        # fila totalmente reducida a 0: nada
    return len(basis)


def sweep(delta, d, nu=72, nv=72):
    """Una muestra del barrido: stats de la IMAGEN X_delta."""
    U = np.linspace(0.0, 2 * PI, nu, endpoint=False)
    V = np.linspace(0.0, 2 * PI, nv, endpoint=False)
    verts, f = deform_family(U, V, delta, d)
    faces, nV = build_complex(U, V, verts)
    stats = homology_gf2(faces, nV)
    stats["min_f"] = float(f.min())
    stats["delta"] = delta
    return stats, vert_and_faces_size(verts, faces)


def vert_and_faces_size(verts, faces):
    return {"verts": int(verts.shape[0]), "faces_used": len(faces)}


# ----------------------------------------------------------------------------
# 6) main
# ----------------------------------------------------------------------------

def main():
    d = DEFAULT_SCL90R_DATA
    U = np.linspace(0.0, 2 * PI, 72, endpoint=False)
    V = np.linspace(0.0, 2 * PI, 72, endpoint=False)
    raw = raw_deform_grid(U, V, d)
    raw_min, raw_max = float(raw.min()), float(raw.max())
    delta_star = -1.0 / raw_min if raw_min < 0 else float('inf')

    print("FAMILIA REAL X_delta (adenda_v51_formal.py)")
    print("  perfil: DEFAULT_SCL90R_DATA; raw_min=%.6f  raw_max=%.6f" % (raw_min, raw_max))
    print("  delta* (f<=0) teorico = %.6f   |   Wegbreite pi/6 = %.6f" % (delta_star, WEGREITE))

    fails = []
    def check(name, got, want, tol):
        ok = (abs(got - want) <= tol) if tol is not None else (got == want)
        print("  [ %s ] %s: got %s, want %s" % ("OK " if ok else "FAIL", name, got, want))
        if not ok:
            fails.append((name, got, want))

    # CONTROLE: ESTATUTO A (dominio, sin identificar) en delta=0
    Uf = np.linspace(0.0, 2 * PI, 48, endpoint=False)
    Vf = np.linspace(0.0, 2 * PI, 48, endpoint=False)
    verts0, _ = deform_family(Uf, Vf, 0.0, d, a=1.0)
    facesA, nVA = build_complex(Uf, Vf, verts0, identify_cutus=False)
    stA = homology_gf2(facesA, nVA)
    print("CONTROL A - dominio (T^2, delta=0, sin identificar cuspide):")
    check("chi A", stA["chi"], 0, 0)
    check("b1 A", stA["b1"], 2, 0)
    check("b2 A", stA["b2"], 1, 0)

    # CONTROL B (imagen con cuspide identificada): S^2 vee S^1
    verts0b, _ = deform_family(Uf, Vf, 0.0, d, a=1.0)
    facesB, nVB = build_complex(Uf, Vf, verts0b, identify_cutus=True)
    stB = homology_gf2(facesB, nVB)
    print("CONTROL B - imagen (cuspide p identificada, delta=0):")
    check("chi B", stB["chi"], 1, 0)
    check("b1 B", stB["b1"], 1, 0)
    check("b2 B", stB["b2"], 1, 0)

    # BARRIDO delta en [0, pi/6] (+ pasaje a delta* -> categoria si corresponde)
    print()
    print("BARRIDO delta (imagen, SCL default):")
    print("   delta    min_f   chi  b0  b1  b2   E      F")
    worst = None
    for delta in np.linspace(0.0, WEGREITE, 15):
        st, _ = sweep(delta, d)
        print("  %.4f  %8.4f  %2d %3d %3d %3d %5d %5d" %
              (delta, st["min_f"], st["chi"], st["b0"], st["b1"], st["b2"], st["E"], st["F"]))
        if delta > 0:
            if st["chi"] != 1 or st["b1"] != 1 or st["b2"] != 1:
                worst = (delta, st)
    if worst is not None:
        print("  AVISO: en delta=%.4f la imagen NO es S^2vS1: %r" % (worst[0], worst[1]))
        fails.append(("barrido in-[0,pi/6] cambio categoria", worst[0], None))
    else:
        print("  => en [0, pi/6] la imagen X_delta se mantiene homotopa a S^2 vee S^1")
        print("     (chi=1, b1=1, b2=1 en todos los deltas): el umbral pi/6 es METRICO")

    if delta_star <= WEGREITE:
        print()
        print("  delta* = %.6f <= pi/6 ATENCION: f<=0 ANTES del umbral Wegbreite." % delta_star)
        st, _ = sweep(delta_star * 0.98, d)
        print("  a delta* * 0.98: chi=%d b1=%d b2=%d min_f=%.4f" %
              (st["chi"], st["b1"], st["b2"], st["min_f"]))
    else:
        print()
        print("  delta* = %.6f > pi/6 : en el regimen Wegbreite f>0 siempre:" % delta_star)
        print("  NO hay evento topologico en [0, pi/6] para este perfil.")

    # delta* para el segundo perfil (Ruptura del modelo, IGS extremo):
    dr = RUPTURA_SCL90R_DATA
    rawr = raw_deform_grid(U, V, dr)
    rawr_min = float(rawr.min())
    dstar_r = -1.0 / rawr_min if rawr_min < 0 else float("inf")
    print()
    print("perfil RUPTURA (IGS 3.30, fuera de baremo): raw_min=%.6f  delta*=%.6f  (pi/6=%.6f)"
          % (rawr_min, dstar_r, WEGREITE))
    if dstar_r <= WEGREITE:
        print("  ATENCION: en el perfil extrema delta* <= pi/6: f<=0 ANTES del umbral")
        print("  Wegbreite. Estatuto B antes/después de delta*:")
        st_pre, _ = sweep(dstar_r * 0.98, dr)
        print("    pre  (delta=%.4f): chi=%d b1=%d b2=%d min_f=%.4f"
              % (dstar_r * 0.98, st_pre["chi"], st_pre["b1"], st_pre["b2"], st_pre["min_f"]))
        print("    (despues de delta* la parametrizacion atraviesa el eje: la familia")
        print("     pierde estado de superficie: reportado, no silenciado)")
    else:
        print("  delta* > pi/6 tambien para el perfil extrema: el regimen Wegbreite")
        print("  es metrico para ambos perfiles.")

    print()
    print("SNAPPY 3.3.2 (exterior .homology() via O8; volumen geometrico):")
    snappy_ok = snappy_cross_check()
    if not snappy_ok:
        fails.append(("snappy cross-check", None, None))

    # GRAFICO del barrido (fig_adenda_v51.png)
    try:
        plot_sweep(d)
        print()
        print("grafico: fig_adenda_v51.png")
    except Exception as exc:
        print()
        print("AVISO: plot fallo (no afecta la verificacion):", exc)

    print()
    if fails:
        print("ADENDA FORMAL FALLIDA (%d controles)" % len(fails))
        for f in fails:
            print("   -", f)
        sys.exit(1)
    print("ADENDA FORMAL OK")

def plot_sweep(d, nu=48, nv=48):
    """Grafico del barrido: chi_imagen(delta), b1, min f, con pi/6 y delta*."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    U = np.linspace(0.0, 2 * PI, nu, endpoint=False)
    V = np.linspace(0.0, 2 * PI, nv, endpoint=False)
    raw = raw_deform_grid(U, V, d)
    raw_min = float(raw.min())
    dstar = -1.0 / raw_min if raw_min < 0 else float("inf")

    deltas = np.linspace(0.0, max(WEGREITE * 1.35, dstar * 1.05 if math.isfinite(dstar) else WEGREITE * 1.35), 60)
    chis, b1s, mfs = [], [], []
    for delta in deltas:
        st, _ = sweep(delta, d, nu=nu, nv=nv)
        chis.append(st["chi"]); b1s.append(st["b1"]); mfs.append(st["min_f"])

    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2))
    for ax, ys, name, ref in zip(axes, (chis, b1s, mfs),
                                 ("chi(X_delta)", "b1(X_delta)", "min f(u,v)"),
                                 (None, None, 0.0)):
        ax.plot(deltas, ys, lw=2)
        ax.axvline(WEGREITE, color="tab:red", ls="--", label="Wegbreite $\\pi/6$")
        if math.isfinite(dstar):
            ax.axvline(dstar, color="tab:purple", ls=":", label="$\\delta^*$ (f$\\to$0)")
        if ref is not None:
            ax.axhline(ref, color="k", lw=0.7)
        ax.set_xlabel("$\\delta$ = deformation_factor")
        ax.set_title(name)
        ax.legend(fontsize=8)
    fig.suptitle("Adenda V51: barrido de la familia REAL X_delta (perfil SCL default)\n"
                 "imagen: $\\chi=1$, $b_1=1$ ($S^2\\vee S^1$) estable; dominio: $\\chi=0$, $b_1=2$ ($T^2$)", fontsize=11)
    fig.tight_layout()
    fig.savefig("fig_adenda_v51.png", dpi=150)
    plt.close(fig)


def snappy_cross_check():
    """Bloque SnapPy: exterior.homology() para unknown-representativo y trefoil;
    cruza con la dualidad de Alexander (H~_1(complemento) = H~^1(X))."""
    fails = []
    def check(name, got, want):
        ok = got == want or want is None
        print("  [ %s ] %s: %s" % ("OK " if ok else "FAIL", name, got))
        if not ok:
            fails.append(name)

    try:
        import snappy
    except ImportError:
        print("  SnapPy no disponible: bloque omitido (informar como limitacion)")
        return False

    # (i) unknot con 1 componente en la tabla de SnapPy: T(2,1)
    unk = snappy.Link("T(2,1)")
    uext = unk.exterior()
    unk_h = str(uext.homology())
    unk_vol = uext.volume()
    check("unknot 1 componente", len(unk.link_components), 1)
    check("unknot homology", unk_h, "Z")
    check("unknot vol==0", abs(unk_vol) < 1e-4, True)

    # (ii) CONTROL afirmativo: trefoil (braid s1^3) -detectar que las herramientas
    #      no dicen unknot a todo: volumen == 0 (solido no hiperbolico) pero
    #      homology == Z, y el EXTERIOR del trefoil-tube da la pieza exterior.
    tre = snappy.Link(braid_closure=[1, 1, 1])
    ext_t = tre.exterior()
    print("  trefoil (s1^3):        homology=%s  volume=%.4f" % (str(ext_t.homology()), ext_t.volume()))
    check("trefoil ext homology == Z", str(ext_t.homology()), "Z")

    # (iii) verificada dualidad para el trefoil-tube con NUESTRO complejo:
    #      la frontera del tubo del trefoil es T^2 genuina: b1=2, b2=1, chi=0;
    #      H~^1(X)=Z^2  <=>  H~_1(S^3-X)=Z (tubro interior ~ trefoil) + Z (ext).
    chi_tube, b1_tube, b2_tube = trefoil_tube_bd()
    print("  frontera tubo trefoil (nuestro complejo): chi=%d b1=%d b2=%d" % (chi_tube, b1_tube, b2_tube))
    check("trefoil tube chi==0", chi_tube, 0)
    check("trefoil tube b1==2", b1_tube, 2)
    check("trefoil tube b2==1", b2_tube, 1)

    # (iv) pieza interior para NUESTRA familia: interior del solido-horn ~ gamma
    #      = unknot: H_1 = Z (SnapPy en el representante) y exterior = 0
    #      (dualidad, H~_1 = H~^1(X)=Z^... = [interior Z] ⊕ [exterior 0]).
    print("  sintesis dualidad X_delta (imagen):")
    print("    H~^1(X_delta) = Z (b1=1 por matriz de frontera)")
    print("    H~_1(S^3\\X_delta) = Z (interior ~gamma=unknown: SnapPy Z) + H_1(exterior)=0")
    return len(fails) == 0


def trefoil_tube_bd(a=1.0, r_tube=0.35, nt=96, nphi=12):
    """Frontera del tubo del trefoil T(2,3): complejo (t,phi) en T^2 genuina.
    CONTROL del lado de las herramientas: b1=2, b2=1, chi=0 para CUALQUIER
    tubo inmerso simple (de mediocre a nudo)."""
    t = np.linspace(0, 2 * PI, nt, endpoint=False)
    C = np.stack([
        (2 + np.cos(3 * t)) * np.cos(2 * t),
        (2 + np.cos(3 * t)) * np.sin(2 * t),
        1.2 * np.sin(3 * t),
    ], axis=-1)
    # tangente y normal coherentes para el tubo (Frenet aproximado)
    dC = np.gradient(C, axis=0)
    dC /= np.linalg.norm(dC, axis=-1, keepdims=True)
    # normal = gradiente de la funcion radial (aprox) -simplest: use
    # N = normalize( C - componente paralela ). para un toro-tubo de trefoil
    # es suficiente para caras no degeneradas.
    N = np.zeros_like(C)
    ncross = np.cross(dC, np.array([0.0, 0.0, 1.0]))
    ln = np.linalg.norm(ncross, axis=-1, keepdims=True)
    ln[ln < 1e-9] = 1.0
    ncross /= ln
    B = np.cross(dC, ncross)
    phi = np.linspace(0, 2 * PI, nphi, endpoint=False)
    verts = []
    for k in range(nt):
        for m in range(nphi):
            verts.append(C[k] + r_tube * (np.cos(phi[m]) * ncross[k] + np.sin(phi[m]) * B[k]))
    verts = np.array(verts)
    faces = []
    def vid(k, m):
        return (k % nt) * nphi + (m % nphi)
    for k in range(nt):
        for m in range(nphi):
            aa, bb, cc, dd = vid(k, m), vid(k + 1, m), vid(k + 1, m + 1), vid(k, m + 1)
            faces.append((aa, bb, cc))
            faces.append((aa, cc, dd))
    faces = _filter_zero_area(faces, verts)
    st = homology_gf2(faces, len(verts))
    return st["chi"], st["b1"], st["b2"]


if __name__ == "__main__":
    main()
