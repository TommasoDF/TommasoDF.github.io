## Work in Progress

<ul style="margin:0 0 20px;">
{% for paper in site.data.work_in_progress.main %}
  <li style="margin-bottom:8px;">
    <strong>{{ paper.title }}</strong><br>
    <span style="color:#555;">{{ paper.authors }}</span>
    {% if paper.notes %}
      <span style="color:#555;"> — <em>{{ paper.notes }}</em></span>
    {% endif %}
  </li>
{% endfor %}
</ul>
