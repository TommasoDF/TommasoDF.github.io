#!/usr/bin/env python3
"""
Option Pricing course grade calculator — University of Bonn.

Grading rules
-------------
- Final exam:  0–100 points. Passing threshold: 50.
- Bavarian formula: base_grade = 1 + 3 * (100 - final) / (100 - 50)
  => score 100 -> 1.0, score 50 -> 4.0, score < 50 -> fail (5.0)
- Mid-term bonus (optional):
    bonus = 0.7 * max(0, (midterm - 50) / 50)
  The bonus is subtracted from the base grade (lower = better in German system).
  Maximum bonus: 0.7 grade points (when midterm = 100).
  The bonus cannot raise the grade above 1.0.
- Discrete rounding to: {1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 5.0}
  using nearest-neighbour rounding.
"""

DISCRETE_GRADES = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 5.0]


def bavarian_grade(final_score: int) -> float:
    """Continuous German grade via the Bavarian formula."""
    return 1.0 + 3.0 * (100 - final_score) / 50.0


def midterm_bonus(midterm_score: int) -> float:
    """Bonus to subtract from the German grade (always >= 0)."""
    return 0.7 * max(0.0, (midterm_score - 50) / 50.0)


def round_to_discrete(continuous_grade: float) -> float:
    """Round a continuous grade to the nearest discrete German grade."""
    return min(DISCRETE_GRADES, key=lambda g: abs(g - continuous_grade))


def compute_grade(final_score: int, midterm_score: int = 0) -> float:
    """
    Compute the final course grade.

    Parameters
    ----------
    final_score : int
        Final exam score, 0–100.
    midterm_score : int
        Mid-term score, 0–100.  Default 0 (not taken or ignored).

    Returns
    -------
    float
        Discrete German grade in {1.0, 1.3, 1.7, 2.0, 2.3, 2.7,
        3.0, 3.3, 3.7, 4.0, 5.0}.
    """
    if not (0 <= final_score <= 100):
        raise ValueError(f"final_score must be 0–100, got {final_score}")
    if not (0 <= midterm_score <= 100):
        raise ValueError(f"midterm_score must be 0–100, got {midterm_score}")

    # Fail immediately if final exam is below the passing threshold.
    if final_score < 50:
        return 5.0

    base = bavarian_grade(final_score)
    grade_no_bonus = round_to_discrete(base)

    bonus = midterm_bonus(midterm_score)
    # Cap at 1.0: the bonus cannot push the grade above the maximum.
    continuous = max(1.0, base - bonus)
    grade = round_to_discrete(continuous)

    # Enforce that discrete improvement is at most 0.7 grade points.
    # Rounding can otherwise amplify a continuous improvement of exactly 0.7
    # into a discrete jump of 1.0 in edge cases.
    if grade_no_bonus - grade > 0.7:
        grade = round_to_discrete(grade_no_bonus - 0.7)

    return grade


# ---------------------------------------------------------------------------
# Command-line interface
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Compute the Option Pricing course grade (University of Bonn)."
    )
    parser.add_argument(
        "final",
        type=int,
        metavar="FINAL",
        help="Final exam score, integer 0–100.",
    )
    parser.add_argument(
        "midterm",
        type=int,
        nargs="?",
        default=0,
        metavar="MIDTERM",
        help="Mid-term score, integer 0–100 (default: 0 = not taken).",
    )
    args = parser.parse_args()

    grade = compute_grade(args.final, args.midterm)

    print(f"Final exam  : {args.final}/100")
    print(f"Mid-term    : {args.midterm}/100")

    if args.final >= 50:
        base = bavarian_grade(args.final)
        bonus = midterm_bonus(args.midterm)
        continuous = max(1.0, base - bonus)
        print(f"Base grade (Bavarian formula) : {base:.4f}")
        print(f"Mid-term bonus               : {bonus:.4f}")
        print(f"Continuous grade after bonus : {continuous:.4f}")
    else:
        print("Result: FAIL (final exam below passing threshold of 50)")

    print(f"Final course grade : {grade:.1f}")
