---
layout: default
---

# Copywriting

## Lists
<ul>
{% for page in site.pages %}
  {% if page.categories contains 'Copywriting' %}
    <li>
      <a href="{{ page.url \| relative_url }}">{{ page.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>