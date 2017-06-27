---
layout: page
title: Faculty
tab: People
longtitle: Program Faculty
summary: The ICI3D program faculty consists of core faculty, who are regular instructors and are responsible for overall design and execution of the program, and workshop faculty, who serve as workshop instructors.
---

{% include topTable.html %}

<h2 style="color: #15378a">Core Faculty</h2>
<br>

{% for profile in site.profiles %}
  {% if profile.type == "core" or profile.type == "director" %}
  <div class="team-member media" style="font-size:18px">
    <img src="{{site.url}}/assets/img/{{profile.img}}" class="media-object img-circle pull-left" alt="{{ profile.name }}" height="115" />
    <div class="media-body">
      <h3 class="media-heading team-name">{{ profile.name }}</h3>
      <strong>{{ profile.role }} <br>{% if profile.type == "director" %}{{ profile.involvement }} <br>{% endif %}</strong>
      <hr class="pull-left">
      <div class="clearfix"></div>
      <p style="font-size:14px"> <em>{{ profile.position }}<br>{{ profile.affiliation }}</em></p>
      <p style="font-size:14px">(<a href="../{{ profile.title | downcase}}">more info</a>)</p>
  </div><!-- media-body -->
</div><!-- team-member media -->
  {% endif %}
{% endfor %}

{% include centerTable.html %}

<h2 style="color: #15378a">Workshop Faculty</h2>
<br>

{% for profile in site.profiles %}
{% if profile.type == "workshop" %}
  <div class="team-member media" style="font-size:18px">
    <img src="{{site.url}}/assets/img/{{profile.img}}" class="media-object img-circle pull-left" alt="{{ profile.name }}" height="115" />
    <div class="media-body">
      <h3 class="media-heading team-name">{{ profile.name }}</h3>
      <strong>{{ profile.involvement }}</strong>
      <hr class="pull-left">
      <div class="clearfix"></div>
      <p style="font-size:14px"> <em>{{ profile.position }}<br>{{ profile.affiliation }}</em></p>
      <p style="font-size:14px">(<a href="../{{ profile.title | downcase}}">more info</a>)</p>
  </div><!-- media-body -->
</div><!-- team-member media -->
  {% endif %}
{% endfor %}

{% include bottomTable.html %}
