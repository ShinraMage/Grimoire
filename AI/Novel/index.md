---
layout: default
---

# Novel

## Lists
<ul>
{% assign novel_pages = site.pages | where_exp: "page", "page.categories contains 'Novel'" %}
{% assign sorted_pages = novel_pages | sort: 'name' | reverse %}
{% for page in sorted_pages %}
    <li>
      <a href="{{ page.url | relative_url }}">{{ page.name }}</a>
    </li>
{% endfor %}
</ul>