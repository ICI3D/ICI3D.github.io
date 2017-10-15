---
layout: page
title: Staff
tab: People
longtitle: Program Staff
summary:
subtitle: International Clinics on Infectious Disease Dynamics and Data
---

{% include topTable.html %}

<h2 style="color: #15378a">Administrative Staff</h2>
<br>

{% for profile in site.profiles %}
  {% if profile.type == "admin" %}
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

<h2 style="color: #15378a">Program Evaluator</h2>
<br>

{% for profile in site.profiles %}
  {% if profile.type == "evaluator" %}
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

{% include bottomTable.html %}
