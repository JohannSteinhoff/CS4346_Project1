# CS 4346 - Project 1 - Table B: Should the car change lanes?
# Student ID: ngq7
# PSR Definition: PSR(P) = #{rows where P=1 AND Y=1} / #{rows where P=1}
#
# Rule discovered using PSR:
#   Rule 1: If Lane_Clear=1 AND Turn_Signal_On=1 AND No_Blind_Spot=1 => Y=1
#   Default: Otherwise => Y=0
#   Note: Speed_Safe has no effect on Y in this dataset.

# ── Dataset ───────────────────────────────────────────────────────────────────
# Columns: Label, Lane_Clear, Speed_Safe, Turn_Signal_On, No_Blind_Spot, Y
data = [
[1,1,1,1,1,1],[2,1,0,1,1,1],[3,0,1,1,0,0],[4,1,0,1,0,0],[5,1,0,1,1,1],
[6,1,1,0,0,0],[7,0,0,1,0,0],[8,1,1,1,0,0],[9,1,1,1,1,1],[10,1,1,0,1,0],
[11,0,0,1,0,0],[12,1,1,0,1,0],[13,0,0,1,0,0],[14,1,1,1,0,0],[15,1,1,0,1,0],
[16,1,1,1,1,1],[17,1,1,1,1,1],[18,0,1,0,0,0],[19,1,0,1,1,1],[20,0,1,1,0,0],
[21,0,1,0,0,0],[22,0,1,1,1,0],[23,1,1,0,0,0],[24,0,0,0,1,0],[25,0,1,1,1,0],
[26,1,0,1,1,1],[27,1,1,1,0,0],[28,1,0,1,0,0],[29,1,0,1,0,0],[30,1,1,0,1,0],
[31,1,1,0,1,0],[32,1,1,1,0,0],[33,1,1,1,1,1],[34,0,0,0,1,0],[35,1,1,0,1,0],
[36,0,1,0,1,0],[37,1,0,1,1,1],[38,1,1,0,0,0],[39,1,1,1,1,1],[40,1,1,1,1,1],
[41,1,1,1,0,0],[42,1,1,1,1,1],[43,1,1,0,0,0],[44,1,0,1,1,1],[45,1,0,1,1,1],
[46,0,1,1,1,0],[47,1,1,1,1,1],[48,1,1,1,0,0],[49,1,1,1,1,1],[50,1,1,1,1,1],
[51,0,1,1,1,0],[52,1,1,1,1,1],[53,1,1,0,1,0],[54,1,1,1,1,1],[55,0,1,0,0,0],
[56,1,1,0,1,0],[57,1,0,1,0,0],[58,0,1,1,1,0],[59,0,1,1,1,0],[60,1,0,1,0,0],
[61,1,1,1,1,1],[62,1,0,1,0,0],[63,1,1,1,1,1],[64,1,1,0,0,0],[65,1,1,1,1,1],
[66,1,1,0,1,0],[67,0,1,1,1,0],[68,1,1,0,1,0],[69,0,1,1,1,0],[70,1,1,1,1,1],
[71,1,1,1,1,1],[72,1,0,1,1,1],[73,1,0,1,0,0],[74,1,1,1,1,1],[75,1,1,1,0,0],
[76,1,0,0,1,0],[77,1,1,1,1,1],[78,1,1,1,0,0],[79,0,1,1,1,0],[80,1,0,1,1,1],
[81,0,0,1,0,0],[82,1,1,1,1,1],[83,0,1,0,0,0],[84,1,1,1,1,1],[85,1,1,1,1,1],
[86,1,0,1,1,1],[87,1,1,0,0,0],[88,0,1,0,1,0],[89,1,1,1,1,1],[90,1,1,1,1,1],
[91,1,0,1,1,1],[92,1,0,0,1,0],[93,1,1,1,0,0],[94,1,0,1,1,1],[95,0,1,0,1,0],
[96,1,1,1,1,1],[97,1,1,0,1,0],[98,1,0,0,1,0],[99,0,1,1,0,0],[100,0,1,1,0,0],
]

headers = ['Label', 'Lane_Clear', 'Speed_Safe', 'Turn_Signal_On', 'No_Blind_Spot', 'Y']
LC, SS, TS, NB, Y = 1, 2, 3, 4, 5  # column indices

# ── Input Table (Y removed) ────────────────────────────────────────────────────
print("=" * 60)
print("CS 4346 Project 1 - Table B: Should the car change lanes?")
print("=" * 60)
print("\n--- Input Table (Y values hidden) ---")
print(f"{'Label':>6}  {'Lane_Clear':>10}  {'Speed_Safe':>10}  {'Turn_Signal_On':>14}  {'No_Blind_Spot':>13}")
print("-" * 65)
for row in data:
    print(f"{row[0]:>6}  {row[LC]:>10}  {row[SS]:>10}  {row[TS]:>14}  {row[NB]:>13}")

# ── PSR calculation ───────────────────────────────────────────────────────────
positives = [r for r in data if r[Y] == 1]
negatives = [r for r in data if r[Y] == 0]
print(f"\nTotal rows : {len(data)}")
print(f"Positives  : {len(positives)}  (Y=1, change lane)")
print(f"Negatives  : {len(negatives)}  (Y=0, stay in lane)")

print("\n--- Step 0: Initial PSR Values (all rows) ---")
params = [
    ('Lane_Clear',     LC),
    ('Speed_Safe',     SS),
    ('Turn_Signal_On', TS),
    ('No_Blind_Spot',  NB),
]
for name, col in params:
    p1    = [r for r in data if r[col] == 1]
    p1_y1 = [r for r in p1   if r[Y]   == 1]
    psr   = len(p1_y1) / len(p1) if p1 else 0
    print(f"  PSR({name}) = {len(p1_y1)}/{len(p1)} = {psr:.4f}")

print("\n  => Highest PSR: No_Blind_Spot (0.5758) — selected first")

print("\n--- Step 1: PSR inside No_Blind_Spot=1 subset ---")
sub1 = [r for r in data if r[NB] == 1]
for name, col in [(n,c) for n,c in params if c != NB]:
    p1    = [r for r in sub1 if r[col] == 1]
    p1_y1 = [r for r in p1   if r[Y]   == 1]
    psr   = len(p1_y1) / len(p1) if p1 else 0
    print(f"  PSR({name} | No_Blind_Spot=1) = {len(p1_y1)}/{len(p1)} = {psr:.4f}")
print("  => Highest: Turn_Signal_On (0.8085) — selected")

print("\n--- Step 2: PSR inside No_Blind_Spot=1 AND Turn_Signal_On=1 subset ---")
sub2 = [r for r in sub1 if r[TS] == 1]
for name, col in [(n,c) for n,c in params if c not in (NB, TS)]:
    p1    = [r for r in sub2 if r[col] == 1]
    p1_y1 = [r for r in p1   if r[Y]   == 1]
    psr   = len(p1_y1) / len(p1) if p1 else 0
    print(f"  PSR({name} | NB=1, TS=1) = {len(p1_y1)}/{len(p1)} = {psr:.4f}")
print("  => Lane_Clear PSR = 1.000 (PERFECT) — selected")

# ── Rules ─────────────────────────────────────────────────────────────────────
def predict(row):
    return 1 if (row[LC]==1 and row[TS]==1 and row[NB]==1) else 0

print("\n--- Generated Rule ---")
print("  Rule 1: Lane_Clear=1 AND Turn_Signal_On=1 AND No_Blind_Spot=1  =>  Y=1")
print("  Default: Otherwise  =>  Y=0")
print("  Note: Speed_Safe has no effect on Y in this dataset.")

# ── Verification ──────────────────────────────────────────────────────────────
print("\n--- Predictions vs Actual ---")
print(f"{'Label':>6}  {'LC':>2}  {'SS':>2}  {'TS':>2}  {'NB':>2}  {'Actual Y':>8}  {'Pred Y':>6}  {'Match':>5}")
print("-" * 55)
errors = []
for row in data:
    pred = predict(row)
    match = "OK" if pred == row[Y] else "FAIL"
    if pred != row[Y]:
        errors.append(row)
    print(f"{row[0]:>6}  {row[LC]:>2}  {row[SS]:>2}  {row[TS]:>2}  {row[NB]:>2}  {row[Y]:>8}  {pred:>6}  {match:>5}")

print("\n--- Verification Summary ---")
print(f"  Total rows : {len(data)}")
print(f"  Correct    : {len(data) - len(errors)}")
print(f"  Errors     : {len(errors)}")
print(f"  Accuracy   : {(len(data)-len(errors))/len(data)*100:.1f}%")
if not errors:
    print("\n  RESULT: Rule satisfies ALL 100 rows. Verification PASSED.")
else:
    print(f"\n  RESULT: {len(errors)} row(s) failed.")
    for e in errors:
        print(f"    Row {e[0]}: {e}")
