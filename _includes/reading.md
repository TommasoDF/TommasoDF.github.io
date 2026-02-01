## Reading List

<ul style="list-style:none; padding-left:0;">
{% for item in site.data.reading.main %}
  <li style="margin-bottom:10px;">
    {% if item.read %}
      <span style="margin-right:6px;">☑</span>
    {% else %}
      <span style="margin-right:6px;">☐</span>
    {% endif %}

    <strong>
      <a href="{{ item.url }}" target="_blank" rel="noopener">
        {{ item.title }}
      </a>
    </strong><br>
    <span style="color:#555;">
      {{ item.authors }} — <em>{{ item.venue }}</em>, {{ item.date | date: "%b. %Y" }}

    </span>
  </li>
{% endfor %}
</ul>
