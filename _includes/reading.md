## Reading List

<p style="font-size:0.9em; color:#555; margin-top:-10px; margin-bottom:20px;">
This list is automatically generated using a custom script
(<a href="https://github.com/TommasoDF/TommasoDF.github.io/tree/main/scripts/update_reading.py" target="_blank" rel="noopener">see script</a>).
As a result, some noise may be present (e.g. front matter, replies, or non-research items).
I am still working on the filtering, so for now I will use ★ for recommended reading.
</p>



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

    {% if item.recommended %}
    <span style="font-size:1.1em;">★</span>
    {% endif %}

  </li>
{% endfor %}
</ul>
