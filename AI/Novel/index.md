---
layout: default
---

# Novel

## Lists
<ul>
{% assign sorted_pages = site.pages | sort: 'date' | reverse %}
{% for page in sorted_pages %}
  {% if page.categories contains 'Novel' %}
    <li>
      <a style="font-size: 2em;" href="{{ page.url \| relative_url }}">{{ page.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>