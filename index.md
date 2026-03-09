---
layout: default
---

# 📝 Latest Life Hacks

---

{% for post in site.posts %}
### 📌 [{{ post.title }}]({{ site.baseurl }}{{ post.url }})
> {{ post.description | default: "Click to read more..." }}
*Posted on: {{ post.date | date: "%Y-%m-%d" }}*

---
{% endfor %}
