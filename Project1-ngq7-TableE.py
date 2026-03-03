# CS 4346 - Project 1 - Table E: Should the car sound an alert?
# Student ID: ngq7
# PSR Definition: PSR(P) = #{rows where P=1 AND Y=1} / #{rows where P=1}
#
# Rules discovered using PSR:
#   Rule 1: If Driver_Drowsy=1 AND Speed_Exceeded=1 => Y=1
#   Rule 2: If Seatbelt_Off=1 AND Lane_Departure=1  => Y=1
#   Default: Otherwise => Y=0

# ── Dataset ───────────────────────────────────────────────────────────────────
# Columns: Label, Driver_Drowsy, Speed_Exceeded, Lane_Departure, Seatbelt_Off, Y
data = [
(1,1,1,1,1,1),(2,1,1,1,0,1),(3,0,1,0,1,0),(4,0,1,1,1,1),(5,1,0,1,0,0),
(6,0,1,0,1,0),(7,0,1,0,0,0),(8,1,0,0,1,0),(9,1,1,1,0,1),(10,1,1,1,1,1),
(11,0,0,0,1,0),(12,0,0,1,0,0),(13,0,1,0,1,0),(14,0,0,1,0,0),(15,1,1,1,1,1),
(16,0,0,1,0,0),(17,0,0,0,1,0),(18,0,1,0,0,0),(19,1,1,1,1,1),(20,0,1,1,0,0),
(21,0,1,1,1,1),(22,1,1,1,1,1),(23,0,1,1,0,0),(24,0,1,1,1,1),(25,1,0,1,1,1),
(26,0,0,1,1,1),(27,0,1,0,0,0),(28,1,0,0,0,0),(29,1,1,0,1,1),(30,0,0,1,1,1),
(31,1,0,0,0,0),(32,1,1,0,1,1),(33,1,1,1,0,1),(34,1,0,0,0,0),(35,1,1,0,1,1),
(36,0,1,0,1,0),(37,1,1,1,1,1),(38,0,0,1,0,0),(39,1,0,0,1,0),(40,1,1,0,0,1),
(41,0,0,1,1,1),(42,0,0,0,0,0),(43,1,1,1,1,1),(44,0,1,0,1,0),(45,1,1,0,1,1),
(46,0,1,1,0,0),(47,1,0,1,1,1),(48,0,1,1,0,0),(49,0,1,0,0,0),(50,0,0,1,0,0),
(51,0,0,0,0,0),(52,0,0,1,0,0),(53,0,1,0,0,0),(54,1,0,0,0,0),(55,0,0,1,0,0),
(56,1,0,0,1,0),(57,0,0,1,0,0),(58,0,1,1,1,1),(59,0,1,0,0,0),(60,1,1,0,0,1),
(61,1,1,1,0,1),(62,1,1,0,0,1),(63,1,0,0,0,0),(64,1,1,1,1,1),(65,1,1,0,0,1),
(66,0,1,1,0,0),(67,1,1,1,1,1),(68,1,0,1,1,1),(69,1,1,1,0,1),(70,1,0,0,0,0),
(71,0,1,0,1,0),(72,0,0,1,0,0),(73,1,1,1,0,1),(74,1,1,1,0,1),(75,0,0,1,0,0),
(76,0,1,1,0,0),(77,1,0,1,0,0),(78,1,0,0,1,0),(79,1,1,1,0,1),(80,0,0,1,0,0),
(81,0,0,0,0,0),(82,1,1,1,1,1),(83,0,1,1,1,1),(84,0,0,0,0,0),(85,0,0,1,1,1),
(86,1,1,1,1,1),(87,1,0,0,1,0),(88,1,0,1,1,1),(89,1,0,0,1,0),(90,0,0,0,1,0),
(91,0,0,1,1,1),(92,1,0,0,1,0),(93,1,0,0,1,0),(94,0,1,0,1,0),(95,0,1,0,1,0),
(96,0,1,1,1,1),(97,1,1,0,1,1),(98,0,1,0,1,0),(99,1,0,1,0,0),(100,0,1,1,0,0),
]

DD, SE, LD, SB, Y = 1, 2, 3, 4, 5  # column indices

# ── Input Table (Y removed) ────────────────────────────────────────────────────
print("=" * 60)
print("CS 4346 Project 1 - Table E: Should the car sound an alert?")
print("=" * 60)
print("\n--- Input Table (Y values hidden) ---")
print(f"{'Label':>6}  {'Driver_Drowsy':>13}  {'Speed_Exceeded':>14}  {'Lane_Departure':>14}  {'Seatbelt_Off':>12}")
print("-" * 70)
for row in data:
    print(f"{row[0]:>6}  {row[DD]:>13}  {row[SE]:>14}  {row[LD]:>14}  {row[SB]:>12}")

# ── PSR calculation ───────────────────────────────────────────────────────────
positives = [r for r in data if r[Y] == 1]
negatives = [r for r in data if r[Y] == 0]
print(f"\nTotal rows : {len(data)}")
print(f"Positives  : {len(positives)}  (Y=1, sound alert)")
print(f"Negatives  : {len(negatives)}  (Y=0, no alert)")

params = [('Driver_Drowsy', DD), ('Speed_Exceeded', SE), ('Lane_Departure', LD), ('Seatbelt_Off', SB)]

def psr(subset, col):
    p1    = [r for r in subset if r[col] == 1]
    p1_y1 = [r for r in p1    if r[Y]   == 1]
    ratio = len(p1_y1) / len(p1) if p1 else 0
    return len(p1_y1), len(p1), ratio

print("\n--- Step 1A: Initial PSR Values (all rows) ---")
for name, col in params:
    n_pos, n, ratio = psr(data, col)
    print(f"  PSR({name}) = {n_pos}/{n} = {ratio:.4f}")
print("  => Highest: Driver_Drowsy (0.6531) — selected")

print("\n--- Step 1B: PSR inside Driver_Drowsy=1 subset ---")
sub1 = [r for r in data if r[DD] == 1]
for name, col in [(n,c) for n,c in params if c != DD]:
    n_pos, n, ratio = psr(sub1, col)
    print(f"  PSR({name} | DD=1) = {n_pos}/{n} = {ratio:.4f}")
print("  => Speed_Exceeded PSR = 1.000 (PERFECT) — Rule 1 complete")

print("\n--- Step 2A: PSR on remaining positives (Rule 1 covered positives removed) ---")
rule1_covered = {r[0] for r in data if r[DD]==1 and r[SE]==1 and r[Y]==1}
remaining = [r for r in data if r[0] not in rule1_covered]
rem_pos = sum(1 for r in remaining if r[Y]==1)
print(f"  Remaining positives after Rule 1: {rem_pos}")
for name, col in params:
    n_pos, n, ratio = psr(remaining, col)
    print(f"  PSR({name}) = {n_pos}/{n} = {ratio:.4f}")
print("  => Highest: Seatbelt_Off (0.4286) — selected")

print("\n--- Step 2B: PSR inside Seatbelt_Off=1 subset (of remaining) ---")
sub2 = [r for r in remaining if r[SB] == 1]
for name, col in [(n,c) for n,c in params if c != SB]:
    n_pos, n, ratio = psr(sub2, col)
    print(f"  PSR({name} | SB=1) = {n_pos}/{n} = {ratio:.4f}")
print("  => Lane_Departure PSR = 1.000 (PERFECT) — Rule 2 complete")

# ── Rules ─────────────────────────────────────────────────────────────────────
def predict(row):
    rule1 = (row[DD]==1 and row[SE]==1)
    rule2 = (row[SB]==1 and row[LD]==1)
    return 1 if (rule1 or rule2) else 0

print("\n--- Generated Rules ---")
print("  Rule 1: Driver_Drowsy=1 AND Speed_Exceeded=1  =>  Y=1")
print("  Rule 2: Seatbelt_Off=1  AND Lane_Departure=1  =>  Y=1")
print("  Default: Otherwise  =>  Y=0")
print("  Compact: Y = (Driver_Drowsy AND Speed_Exceeded) OR (Seatbelt_Off AND Lane_Departure)")

# ── Verification ──────────────────────────────────────────────────────────────
print("\n--- Predictions vs Actual ---")
print(f"{'Label':>6}  {'DD':>2}  {'SE':>2}  {'LD':>2}  {'SB':>2}  {'Actual Y':>8}  {'Pred Y':>6}  {'Match':>5}")
print("-" * 55)
errors = []
for row in data:
    pred = predict(row)
    match = "OK" if pred == row[Y] else "FAIL"
    if pred != row[Y]:
        errors.append(row)
    print(f"{row[0]:>6}  {row[DD]:>2}  {row[SE]:>2}  {row[LD]:>2}  {row[SB]:>2}  {row[Y]:>8}  {pred:>6}  {match:>5}")

print("\n--- Verification Summary ---")
print(f"  Total rows : {len(data)}")
print(f"  Correct    : {len(data) - len(errors)}")
print(f"  Errors     : {len(errors)}")
print(f"  Accuracy   : {(len(data)-len(errors))/len(data)*100:.1f}%")
if not errors:
    print("\n  RESULT: Rules satisfy ALL 100 rows. Verification PASSED.")
else:
    print(f"\n  RESULT: {len(errors)} row(s) failed.")
    for e in errors:
        print(f"    Row {e[0]}: {e}")
