---
layout: default
---

# Novel

## Lists
<ul>
{% for page in site.pages %}
  {% if page.categories contains 'Novel' %}
    <li>
      <a href="{{ page.url \| relative_url }}">{{ page.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>