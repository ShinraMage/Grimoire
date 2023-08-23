---
layout: default
---

# Copywriting

## Lists
<ul>
{% assign sorted_pages = site.pages | sort: 'name' | reverse %}
{% for page in sorted_pages %}
  {% if page.categories contains 'Copywriting' %}
    <li>
      <a href="{{ page.url | relative_url }}">{{ page.name }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>