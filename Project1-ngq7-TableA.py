# CS 4346 - Project 1 - Table A: Should the car brake?
# Student ID: ngq7
# PSR Definition: PSR(P) = #{rows where P=1 AND Y=1} / #{rows where P=1}
#
# Rules discovered using PSR:
#   Rule 1: If Obstacle_Detected=1 AND Short_Distance=1 => Y=1
#   Rule 2: If Speed_High=1 AND Wet_Road=1 AND Short_Distance=1 => Y=1
#   Default: Otherwise => Y=0

# ── Dataset ───────────────────────────────────────────────────────────────────
# Columns: Label, Obstacle_Detected, Speed_High, Wet_Road, Short_Distance, Y
data = [
[1,0,0,1,0,0],[2,0,0,0,0,0],[3,1,0,0,0,0],[4,0,0,0,0,0],[5,1,0,1,1,1],
[6,0,0,1,1,0],[7,1,0,0,1,1],[8,0,0,1,0,0],[9,1,1,1,0,0],[10,1,0,1,0,0],
[11,1,1,0,0,0],[12,0,0,1,0,0],[13,0,0,1,1,0],[14,1,1,0,1,1],[15,1,0,1,0,0],
[16,0,0,0,1,0],[17,1,1,0,1,1],[18,0,0,0,1,0],[19,1,1,0,0,0],[20,1,0,1,1,1],
[21,1,0,1,0,0],[22,0,1,1,1,1],[23,1,0,0,1,1],[24,0,0,0,0,0],[25,0,1,0,1,0],
[26,1,1,1,0,0],[27,0,1,1,0,0],[28,1,1,0,1,1],[29,0,1,0,0,0],[30,1,0,0,1,1],
[31,0,0,1,1,0],[32,0,0,1,1,0],[33,0,0,0,0,0],[34,0,1,0,0,0],[35,0,1,0,1,0],
[36,1,0,0,1,1],[37,1,1,1,1,1],[38,0,0,0,0,0],[39,1,0,0,0,0],[40,0,0,0,0,0],
[41,0,0,1,0,0],[42,0,1,1,0,0],[43,0,1,0,1,0],[44,1,0,0,0,0],[45,1,1,1,1,1],
[46,1,0,0,0,0],[47,1,1,0,0,0],[48,0,0,1,0,0],[49,1,0,1,1,1],[50,0,0,1,0,0],
[51,0,0,0,0,0],[52,0,1,1,1,1],[53,0,1,0,0,0],[54,1,0,1,1,1],[55,1,1,1,1,1],
[56,0,0,1,0,0],[57,0,0,1,0,0],[58,0,1,0,0,0],[59,0,0,0,0,0],[60,0,1,0,0,0],
[61,0,0,1,1,0],[62,1,0,1,0,0],[63,1,1,0,1,1],[64,1,1,0,0,0],[65,1,0,0,0,0],
[66,1,0,1,0,0],[67,0,1,1,0,0],[68,1,1,0,1,1],[69,0,0,1,0,0],[70,0,0,1,1,0],
[71,0,1,0,1,0],[72,1,1,0,0,0],[73,1,1,0,0,0],[74,1,0,1,0,0],[75,1,1,0,0,0],
[76,0,0,0,1,0],[77,0,1,0,0,0],[78,1,1,0,1,1],[79,0,0,0,1,0],[80,1,0,0,0,0],
[81,0,1,0,0,0],[82,1,1,0,1,1],[83,0,0,1,0,0],[84,1,0,0,1,1],[85,1,1,0,0,0],
[86,0,0,1,1,0],[87,1,0,1,1,1],[88,1,1,0,0,0],[89,1,0,1,0,0],[90,0,1,1,1,1],
[91,1,0,1,0,0],[92,1,0,1,0,0],[93,0,1,1,0,0],[94,1,1,0,1,1],[95,1,1,1,1,1],
[96,1,0,0,1,1],[97,1,0,1,1,1],[98,0,1,1,0,0],[99,1,1,1,1,1],[100,1,0,1,0,0],
]

headers = ['Label', 'Obstacle_Detected', 'Speed_High', 'Wet_Road', 'Short_Distance', 'Y']
OB, SP, WR, SD, Y = 1, 2, 3, 4, 5  # column indices

# ── Input Table (Y removed) ────────────────────────────────────────────────────
print("=" * 55)
print("CS 4346 Project 1 - Table A: Should the car brake?")
print("=" * 55)
print("\n--- Input Table (Y values hidden) ---")
print(f"{'Label':>6}  {'Obstacle_Detected':>17}  {'Speed_High':>10}  {'Wet_Road':>8}  {'Short_Distance':>14}")
print("-" * 65)
for row in data:
    print(f"{row[0]:>6}  {row[OB]:>17}  {row[SP]:>10}  {row[WR]:>8}  {row[SD]:>14}")

# ── PSR calculation ───────────────────────────────────────────────────────────
positives = [r for r in data if r[Y] == 1]
negatives = [r for r in data if r[Y] == 0]
print(f"\nTotal rows : {len(data)}")
print(f"Positives  : {len(positives)}  (Y=1, car should brake)")
print(f"Negatives  : {len(negatives)}  (Y=0, no braking needed)")

print("\n--- PSR Values ---")
params = [
    ('Obstacle_Detected', OB),
    ('Speed_High',        SP),
    ('Wet_Road',          WR),
    ('Short_Distance',    SD),
]
for name, col in params:
    p1       = [r for r in data     if r[col] == 1]
    p1_y1    = [r for r in p1       if r[Y]   == 1]
    psr_val  = len(p1_y1) / len(p1) if p1 else 0
    print(f"  PSR({name}) = {len(p1_y1)}/{len(p1)} = {psr_val:.3f}")

# ── Rules ─────────────────────────────────────────────────────────────────────
def predict(row):
    rule1 = (row[OB] == 1 and row[SD] == 1)
    rule2 = (row[SP] == 1 and row[WR] == 1 and row[SD] == 1)
    return 1 if (rule1 or rule2) else 0

print("\n--- Generated Rules ---")
print("  Rule 1: Obstacle_Detected=1 AND Short_Distance=1  =>  Y=1")
print("  Rule 2: Speed_High=1 AND Wet_Road=1 AND Short_Distance=1  =>  Y=1")
print("  Default: Otherwise  =>  Y=0")

# ── Verification ──────────────────────────────────────────────────────────────
print("\n--- Predictions vs Actual ---")
print(f"{'Label':>6}  {'Obstacle':>8}  {'Speed':>5}  {'Wet':>3}  {'Short':>5}  {'Actual Y':>8}  {'Pred Y':>6}  {'Match':>5}")
print("-" * 65)
errors = []
for row in data:
    pred = predict(row)
    match = "OK" if pred == row[Y] else "FAIL"
    if pred != row[Y]:
        errors.append(row)
    print(f"{row[0]:>6}  {row[OB]:>8}  {row[SP]:>5}  {row[WR]:>3}  {row[SD]:>5}  {row[Y]:>8}  {pred:>6}  {match:>5}")

print("\n--- Verification Summary ---")
print(f"  Total rows   : {len(data)}")
print(f"  Correct      : {len(data) - len(errors)}")
print(f"  Errors       : {len(errors)}")
print(f"  Accuracy     : {(len(data)-len(errors))/len(data)*100:.1f}%")
if not errors:
    print("\n  RESULT: Rules satisfy ALL 100 rows. Verification PASSED.")
else:
    print(f"\n  RESULT: {len(errors)} row(s) failed. Verification FAILED.")
    for e in errors:
        print(f"    Row {e[0]}: {e}")
