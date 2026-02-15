import csv
from collections import defaultdict

# ─── Leer el CSV ───
rows = []
with open("sesion-9/streak_rescue_experiment.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["is_premium"] = int(row["is_premium"])
        row["retained_d14"] = int(row["retained_d14"])
        row["lessons_completed_week"] = float(row["lessons_completed_week"])
        row["time_in_app_minutes"] = float(row["time_in_app_minutes"])
        row["streak_rescue_used"] = int(row["streak_rescue_used"])
        row["streak_at_start"] = int(row["streak_at_start"])
        row["days_since_signup"] = int(row["days_since_signup"])
        rows.append(row)

print(f"Total de filas leídas: {len(rows)}")

# ─── Separar grupos ───
control = [r for r in rows if r["group"] == "control"]
treatment = [r for r in rows if r["group"] == "treatment"]

print(f"Grupo control: {len(control)} usuarios")
print(f"Grupo tratamiento: {len(treatment)} usuarios")

# ─── Funciones auxiliares ───
def mean(values):
    return sum(values) / len(values) if values else 0

def std(values):
    m = mean(values)
    variance = sum((x - m) ** 2 for x in values) / len(values)
    return variance ** 0.5

# ─── PARTE A: Comprensión ───

print("\n" + "=" * 60)
print("PARTE A: COMPRENSIÓN")
print("=" * 60)

# 1. Retención D14
ret_control = mean([r["retained_d14"] for r in control])
ret_treatment = mean([r["retained_d14"] for r in treatment])
diff_ret = ret_treatment - ret_control

print(f"\n--- Pregunta 1: Retención D14 ---")
print(f"Retención control:     {ret_control:.4f} ({ret_control*100:.2f}%)")
print(f"Retención tratamiento: {ret_treatment:.4f} ({ret_treatment*100:.2f}%)")
print(f"Diferencia:            {diff_ret:.4f} ({diff_ret*100:.2f} pp)")
print(f"Cambio relativo:       {diff_ret/ret_control*100:.2f}%")

# P-value aproximado con test Z para proporciones
import math
n1 = len(control)
n2 = len(treatment)
p1 = ret_control
p2 = ret_treatment
p_pool = (p1 * n1 + p2 * n2) / (n1 + n2)
se = math.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
z = (p2 - p1) / se if se > 0 else 0

# Aproximación del p-value usando la función de distribución normal
def norm_cdf(x):
    """Aproximación de la CDF de la normal estándar."""
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

p_value = 2 * (1 - norm_cdf(abs(z)))  # test de dos colas
print(f"Z-score:               {z:.4f}")
print(f"P-value (dos colas):   {p_value:.6f}")
print(f"¿Significativo (p<0.05)? {'SÍ' if p_value < 0.05 else 'NO'}")

# 2. Métricas secundarias
print(f"\n--- Pregunta 2: Métricas secundarias ---")

lessons_control = mean([r["lessons_completed_week"] for r in control])
lessons_treatment = mean([r["lessons_completed_week"] for r in treatment])
print(f"\nLecciones/semana control:     {lessons_control:.2f}")
print(f"Lecciones/semana tratamiento: {lessons_treatment:.2f}")
print(f"Diferencia:                   {lessons_treatment - lessons_control:.2f}")

time_control = mean([r["time_in_app_minutes"] for r in control])
time_treatment = mean([r["time_in_app_minutes"] for r in treatment])
print(f"\nTiempo en app (min) control:     {time_control:.2f}")
print(f"Tiempo en app (min) tratamiento: {time_treatment:.2f}")
print(f"Diferencia:                      {time_treatment - time_control:.2f}")

# Z-test para medias
def z_test_means(vals1, vals2):
    m1, m2 = mean(vals1), mean(vals2)
    s1, s2 = std(vals1), std(vals2)
    n1, n2 = len(vals1), len(vals2)
    se = math.sqrt(s1**2/n1 + s2**2/n2)
    z = (m2 - m1) / se if se > 0 else 0
    p = 2 * (1 - norm_cdf(abs(z)))
    return z, p

z_l, p_l = z_test_means(
    [r["lessons_completed_week"] for r in control],
    [r["lessons_completed_week"] for r in treatment]
)
print(f"Lecciones - Z: {z_l:.4f}, p-value: {p_l:.6f} {'(significativo)' if p_l < 0.05 else '(no significativo)'}")

z_t, p_t = z_test_means(
    [r["time_in_app_minutes"] for r in control],
    [r["time_in_app_minutes"] for r in treatment]
)
print(f"Tiempo app - Z: {z_t:.4f}, p-value: {p_t:.6f} {'(significativo)' if p_t < 0.05 else '(no significativo)'}")

# 3. Análisis por segmento
print(f"\n--- Pregunta 3: Análisis por segmento ---")

segments = ["new", "mid", "veteran"]
for seg in segments:
    seg_control = [r for r in control if r["segment"] == seg]
    seg_treatment = [r for r in treatment if r["segment"] == seg]
    ret_c = mean([r["retained_d14"] for r in seg_control])
    ret_t = mean([r["retained_d14"] for r in seg_treatment])
    diff = ret_t - ret_c

    # P-value para el segmento
    nc, nt = len(seg_control), len(seg_treatment)
    pp = (ret_c * nc + ret_t * nt) / (nc + nt)
    se_seg = math.sqrt(pp * (1 - pp) * (1/nc + 1/nt)) if pp > 0 and pp < 1 else 0
    z_seg = (ret_t - ret_c) / se_seg if se_seg > 0 else 0
    p_seg = 2 * (1 - norm_cdf(abs(z_seg)))

    print(f"\nSegmento '{seg}' (control: {nc}, tratamiento: {nt}):")
    print(f"  Retención control:     {ret_c*100:.2f}%")
    print(f"  Retención tratamiento: {ret_t*100:.2f}%")
    print(f"  Diferencia:            {diff*100:.2f} pp")
    print(f"  P-value:               {p_seg:.6f} {'(significativo)' if p_seg < 0.05 else '(no significativo)'}")

# Por premium vs free
print(f"\n--- Por tipo de usuario (premium vs free) ---")
for prem in [0, 1]:
    label = "Premium" if prem == 1 else "Free"
    prem_control = [r for r in control if r["is_premium"] == prem]
    prem_treatment = [r for r in treatment if r["is_premium"] == prem]
    ret_c = mean([r["retained_d14"] for r in prem_control])
    ret_t = mean([r["retained_d14"] for r in prem_treatment])
    diff = ret_t - ret_c
    print(f"\n{label} (control: {len(prem_control)}, tratamiento: {len(prem_treatment)}):")
    print(f"  Retención control:     {ret_c*100:.2f}%")
    print(f"  Retención tratamiento: {ret_t*100:.2f}%")
    print(f"  Diferencia:            {diff*100:.2f} pp")

# Por país
print(f"\n--- Por país (top 5) ---")
countries = defaultdict(lambda: {"control": [], "treatment": []})
for r in rows:
    countries[r["country"]][r["group"]].append(r)

country_sizes = sorted(countries.items(), key=lambda x: len(x[1]["control"]) + len(x[1]["treatment"]), reverse=True)
for country, groups in country_sizes[:5]:
    ret_c = mean([r["retained_d14"] for r in groups["control"]]) if groups["control"] else 0
    ret_t = mean([r["retained_d14"] for r in groups["treatment"]]) if groups["treatment"] else 0
    print(f"\n{country} (control: {len(groups['control'])}, tratamiento: {len(groups['treatment'])}):")
    print(f"  Retención control:     {ret_c*100:.2f}%")
    print(f"  Retención tratamiento: {ret_t*100:.2f}%")
    print(f"  Diferencia:            {(ret_t - ret_c)*100:.2f} pp")

# Uso de Streak Rescue en tratamiento
print(f"\n--- Uso de Streak Rescue en grupo tratamiento ---")
used = [r for r in treatment if r["streak_rescue_used"] == 1]
not_used = [r for r in treatment if r["streak_rescue_used"] == 0]
print(f"Usaron Streak Rescue:    {len(used)} ({len(used)/len(treatment)*100:.1f}%)")
print(f"No lo usaron:            {len(not_used)} ({len(not_used)/len(treatment)*100:.1f}%)")
print(f"Retención (usaron):      {mean([r['retained_d14'] for r in used])*100:.2f}%")
print(f"Retención (no usaron):   {mean([r['retained_d14'] for r in not_used])*100:.2f}%")

print("\n" + "=" * 60)
print("RESUMEN")
print("=" * 60)
print(f"""
Métrica primaria (retención D14):
  Control: {ret_control*100:.2f}% | Tratamiento: {ret_treatment*100:.2f}%
  Diferencia: {diff_ret*100:.2f} pp | p-value: {p_value:.6f}

Métricas secundarias:
  Lecciones/semana: {lessons_control:.2f} vs {lessons_treatment:.2f} (p={p_l:.4f})
  Tiempo en app:    {time_control:.2f} vs {time_treatment:.2f} min (p={p_t:.4f})
""")
