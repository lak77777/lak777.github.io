---
layout: home
---

# 🚀 Latest Life Hacks

Welcome to Global Life Hacks! Check out our latest tips below.

---

### 💡 Recent Tips

<ul>
  {% for post in site.posts %}
    <li>
      <strong><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></strong>
      <p>{{ post.description | default: "Click to read more..." }}</p>
      <small>{{ post.date | date: "%B %d, %Y" }}</small>
    </li>
  {% endfor %}
</ul>
