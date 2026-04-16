<h4 style="margin:0 10px 0;">Teaching</h4>

<ul style="margin:0 0 5px;">
  <li><a href="https://ecampus.uni-bonn.de/ilias.php?baseClass=ilrepositorygui&cmdNode=z6:n8&cmdClass=ilObjCourseGUI&cmd=view&ref_id=4061048"><autocolor>Option Pricing — 2025/2026, University of Bonn</autocolor></a></li>
  <li><a href="https://studiegids.uva.nl/xmlpages/page/2024-2025-en/search-course/course/120522"><autocolor>Econometrics 2 — 2024/2025, University of Amsterdam</autocolor></a></li>
  <li><a href="https://studiegids.uva.nl/xmlpages/page/2024-2025-en/search-course/course/120460"><autocolor>Statistics — 2024/2025, University of Amsterdam</autocolor></a></li>
  <li><a href="https://studiegids.uva.nl/xmlpages/page/2024-2025/zoek-vak/vak/120456"><autocolor>Mathematics 1 for Economics — 2024/2025, University of Amsterdam</autocolor></a></li>
  <li><a href="https://studiegids.uva.nl/xmlpages/page/2024-2025/zoek-vak/vak/120612"><autocolor>Microeconomics for AE  — 2024/2025, University of Amsterdam</autocolor></a></li>
  <li><a href="https://www.unive.it/data/insegnamento/449593/programma"><autocolor>Optimization — 2019/2020, 2022/2023, University of Venice</autocolor></a></li>
  <li><a href="https://www.unive.it/data/insegnamento/279104/programma"><autocolor>Financial Mathematics — 2019/2020, University of Venice</autocolor></a></li>
  <li><a href="https://www.unive.it/data/insegnamento/382916"><autocolor>Mathematics for Economics - 2019/2020, University of Venice</autocolor></a></li>
</ul>

<details style="margin:10px 10px 0;">
<summary style="cursor:pointer; font-style:italic; color:#700f0f; font-size:0.95em;">Option Pricing — grade calculator</summary>
<div id="grade-calc" style="margin:10px 0 0 0; font-size:0.93em; line-height:1.7;">
  <table style="border:none; border-collapse:collapse;">
    <tr>
      <td style="padding:2px 10px 2px 0;"><label for="gc-final">Final exam (0–100):</label></td>
      <td style="padding:2px 0;"><input id="gc-final" type="number" min="0" max="100" value="70"
          style="width:60px; font-family:inherit; font-size:1em; border:1px solid #aaa; padding:1px 4px;"
          oninput="gcCompute()"></td>
    </tr>
    <tr>
      <td style="padding:2px 10px 2px 0;"><label for="gc-mid">Mid-term (0–100, optional):</label></td>
      <td style="padding:2px 0;"><input id="gc-mid" type="number" min="0" max="100" value="0"
          style="width:60px; font-family:inherit; font-size:1em; border:1px solid #aaa; padding:1px 4px;"
          oninput="gcCompute()"></td>
    </tr>
  </table>
  <div id="gc-result" style="margin-top:8px;"></div>
</div>
</details>

<script>
(function () {
  var GRADES = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 5.0];

  function bavarianGrade(f) { return 1 + 3 * (100 - f) / 50; }
  function bonus(m) { return 0.7 * Math.max(0, (m - 50) / 50); }
  function roundDiscrete(g) {
    return GRADES.reduce(function (a, b) {
      return Math.abs(b - g) < Math.abs(a - g) ? b : a;
    });
  }
  function computeGrade(f, m) {
    if (f < 50) return 5.0;
    var b = bavarianGrade(f);
    var gradeNoBonus = roundDiscrete(b);
    var grade = roundDiscrete(Math.max(1.0, b - bonus(m)));
    if (gradeNoBonus - grade > 0.7) grade = roundDiscrete(gradeNoBonus - 0.7);
    return grade;
  }
  function fmt(x) { return x.toFixed(1); }

  window.gcCompute = function () {
    var f = parseInt(document.getElementById('gc-final').value, 10);
    var m = parseInt(document.getElementById('gc-mid').value, 10);
    var out = document.getElementById('gc-result');
    if (isNaN(f) || isNaN(m) || f < 0 || f > 100 || m < 0 || m > 100) {
      out.innerHTML = '<em>Please enter valid scores (0–100).</em>';
      return;
    }
    var grade = computeGrade(f, m);
    var gradeNoBonus = computeGrade(f, 0);
    var html = 'Grade: <strong>' + fmt(grade) + '</strong>';
    if (m > 0) html += ' &nbsp;<span style="color:#555;">(without mid-term: ' + fmt(gradeNoBonus) + ')</span>';
    out.innerHTML = html;
  };

  document.addEventListener('DOMContentLoaded', function () { window.gcCompute(); });
})();
</script>

