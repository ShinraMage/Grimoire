---
layout: default
---

# Copywriting

## Lists
<ul>
{% assign sorted_pages = site.pages | sort: 'date' | reverse %}
{% for page in sorted_pages %}
  {% if page.categories contains 'Copywriting' %}
    <li>
      <a style="font-size: 2em;" href="{{ page.url \| relative_url }}">{{ page.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>