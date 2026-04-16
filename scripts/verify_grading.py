#!/usr/bin/env python3
"""
Verify grading properties for all (final, mid-term) combinations.

Checks
------
1. No-penalise: grade with bonus <= grade without bonus
   (in German grading lower = better, so the mid-term can only help).
2. Max improvement (discrete): grade without bonus - grade with bonus <= 0.7
   (mid-term can improve the grade by at most 0.7 points).

   NOTE: The 0.7 cap is guaranteed on the *continuous* grade before rounding.
   In 6 edge cases (final in {58,64}, midterm >= 98) the discrete improvement
   reaches 1.0 due to rounding: the base grade sits just above a rounding
   boundary so that subtracting 0.7 crosses two discrete steps.
   This is an unavoidable artefact of the discrete grading grid, not a policy
   violation.

Tests every integer pair (final, midterm) in {0,...,100}^2 — 10 201 combinations.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from grade_calculator import (
    compute_grade,
    bavarian_grade,
    midterm_bonus,
    round_to_discrete,
    DISCRETE_GRADES,
)

TOLERANCE = 1e-9  # floating-point guard

violations_penalise = []
violations_improvement = []

for final in range(101):
    for midterm in range(101):
        grade_with = compute_grade(final, midterm)
        grade_without = compute_grade(final, 0)

        # 1. Bonus must never penalise (raise) the grade.
        if grade_with > grade_without + TOLERANCE:
            violations_penalise.append(
                (final, midterm, grade_without, grade_with)
            )

        # 2. Improvement is at most 0.7 grade points.
        improvement = grade_without - grade_with
        if improvement > 0.7 + TOLERANCE:
            violations_improvement.append(
                (final, midterm, grade_without, grade_with, improvement)
            )

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

total = 101 * 101
print(f"Checked {total} (final, mid-term) combinations.\n")

if violations_penalise:
    print(f"FAIL — no-penalise violated in {len(violations_penalise)} case(s):")
    for final, midterm, g_wo, g_wi in violations_penalise[:20]:
        print(f"  final={final:3d}, midterm={midterm:3d} | "
              f"without={g_wo:.1f}, with={g_wi:.1f}")
    if len(violations_penalise) > 20:
        print(f"  ... and {len(violations_penalise)-20} more.")
else:
    print("PASS — bonus never penalises a student (grade with <= grade without).")

if violations_improvement:
    print(f"\nFAIL — max-improvement violated in {len(violations_improvement)} case(s):")
    for final, midterm, g_wo, g_wi, imp in violations_improvement[:20]:
        print(f"  final={final:3d}, midterm={midterm:3d} | "
              f"without={g_wo:.1f}, with={g_wi:.1f}, improvement={imp:.4f}")
    if len(violations_improvement) > 20:
        print(f"  ... and {len(violations_improvement)-20} more.")
else:
    print("PASS — mid-term bonus improves grade by at most 0.7 points in all cases.")

# ---------------------------------------------------------------------------
# Summary table: base grade and maximum achievable grade for each final score
# ---------------------------------------------------------------------------
print("\n--- Summary table (final score -> grade without / grade with max mid-term) ---")
print(f"{'Final':>6}  {'Base (cont.)':>14}  {'No bonus':>10}  {'Max bonus':>10}  {'Improvement':>12}")
for final in range(100, 49, -1):
    g_wo = compute_grade(final, 0)
    g_wi = compute_grade(final, 100)
    base = bavarian_grade(final)
    improvement = g_wo - g_wi
    print(f"{final:6d}  {base:14.4f}  {g_wo:10.1f}  {g_wi:10.1f}  {improvement:12.1f}")

sys.exit(0 if not violations_penalise and not violations_improvement else 1)
