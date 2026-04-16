#!/usr/bin/env python3
"""
Visualize Option Pricing course grades as a function of
final exam score and mid-term score.

Two panels
----------
Left  — Final course grade (with mid-term bonus applied).
Right — Grade improvement due to mid-term bonus
        (grade_without_bonus - grade_with_bonus; higher = better for student).

The dashed diagonal marks mid-term = final exam score.
Everything below the diagonal is the region where the mid-term score
is lower than the final exam score — yet improvement is still possible
wherever the mid-term is above 50.
"""

import sys, os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.colors import BoundaryNorm
from matplotlib.patches import Patch

sys.path.insert(0, os.path.dirname(__file__))
from grade_calculator import compute_grade, DISCRETE_GRADES

# ---------------------------------------------------------------------------
# Build grade grids
# ---------------------------------------------------------------------------
finals   = np.arange(50, 101)   # x: passing range only
midterms = np.arange(0, 101)    # y

F, M = np.meshgrid(finals, midterms)   # shape (101, 51)

grade_with    = np.vectorize(compute_grade)(F, M)
grade_without = np.vectorize(lambda f, m: compute_grade(f, 0))(F, M)
improvement   = grade_without - grade_with

# ---------------------------------------------------------------------------
# Colour maps
# ---------------------------------------------------------------------------
passing_grades = [g for g in DISCRETE_GRADES if g <= 4.0]   # 1.0 … 4.0
all_levels     = passing_grades + [4.5]                       # boundary edges

# Left panel: discrete grade colours (green = good, red = bad)
grade_cmap = plt.get_cmap("RdYlGn_r", len(passing_grades))
grade_norm = BoundaryNorm(all_levels, grade_cmap.N)

# Right panel: improvement 0 → 0.7
impr_levels = np.linspace(0, 0.7, 256)
impr_cmap   = plt.get_cmap("Blues")

# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5), constrained_layout=True)
fig.suptitle("Option Pricing — Grade Calculator  (University of Bonn)",
             fontsize=13, fontweight="bold")

# ---- Panel 1: final grade ------------------------------------------------
ax = axes[0]
im = ax.pcolormesh(finals, midterms, grade_with,
                   cmap=grade_cmap, norm=grade_norm,
                   shading="nearest")

cb = fig.colorbar(im, ax=ax, ticks=passing_grades, pad=0.02)
cb.set_label("Final course grade", fontsize=10)
cb.ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.1f"))

ax.set_title("Final course grade (with mid-term bonus)", fontsize=11)
ax.set_xlabel("Final exam score", fontsize=10)
ax.set_ylabel("Mid-term score", fontsize=10)

# diagonal: mid-term = final (only where both axes overlap: 50–100)
diag_x = np.arange(50, 101)
ax.plot(diag_x, diag_x, "k--", linewidth=1.2, label="mid-term = final")
ax.axhline(50, color="grey", linewidth=0.8, linestyle=":", label="mid-term = 50 (bonus threshold)")
ax.legend(fontsize=8, loc="upper left")
ax.set_xlim(50, 100)
ax.set_ylim(0, 100)

# ---- Panel 2: improvement -----------------------------------------------
ax = axes[1]
im2 = ax.pcolormesh(finals, midterms, improvement,
                    cmap=impr_cmap, vmin=0, vmax=0.7,
                    shading="nearest")

cb2 = fig.colorbar(im2, ax=ax, ticks=[0, 0.3, 0.6, 0.7], pad=0.02)
cb2.set_label("Grade improvement (grade points)", fontsize=10)

ax.set_title("Improvement from mid-term bonus", fontsize=11)
ax.set_xlabel("Final exam score", fontsize=10)
ax.set_ylabel("Mid-term score", fontsize=10)

ax.plot(diag_x, diag_x, "k--", linewidth=1.2, label="mid-term = final")
ax.axhline(50, color="grey", linewidth=0.8, linestyle=":", label="mid-term = 50 (bonus threshold)")

# shade the region mid-term < final but mid-term > 50 to highlight
# "mid-term below final yet still improves grade"
ax.fill_between(diag_x, 50, diag_x, alpha=0.12, color="orange",
                label="mid-term < final & mid-term > 50")
ax.legend(fontsize=8, loc="upper left")
ax.set_xlim(50, 100)
ax.set_ylim(0, 100)

plt.savefig("scripts/grade_heatmap.png", dpi=150, bbox_inches="tight")
print("Saved scripts/grade_heatmap.png")
plt.show()
