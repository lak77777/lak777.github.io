---
layout: home
---

<div class="container">
  <div class="row">
    <div class="col-lg-8 col-md-10 mx-auto">
      {% for post in site.posts %}
      <div class="post-preview">
        <a href="{{ post.url | prepend: site.baseurl }}">
          <h2 class="post-title">{{ post.title }}</h2>
          <h3 class="post-subtitle">{{ post.description | default: "Click to read this amazing life hack!" }}</h3>
        </a>
        <p class="post-meta">Posted on {{ post.date | date: '%B %d, %Y' }}</p>
      </div>
      <hr>
      {% endfor %}
    </div>
  </div>
</div>
