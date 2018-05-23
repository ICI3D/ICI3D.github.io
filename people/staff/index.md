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

{% for profile in site.team %}
{% assign key = profile.relative_path | split: '/' | last | split: '.' | first %}
{% assign member = site.data.team[key] %}
  {% if member.type == "admin" %}
  <div class="team-member media" style="font-size:18px">
    <img src="{{site.url}}/assets/img/{{member.img}}" class="media-object img-circle pull-left" alt="{{ member.name }}" height="115" />
    <div class="media-body">
      <h3 class="media-heading team-name">{{ member.name }}</h3>
      <strong>{{ member.role }} <br>{% if member.type == "director" %}{{ member.involvement }} <br>{% endif %}</strong>
      <hr class="pull-left">
      <div class="clearfix"></div>
      <p style="font-size:14px"> <em>{{ member.position }}<br>{{ member.affiliation }}</em></p>
      <p style="font-size:14px">(<a href="../{{ key }}">more info</a>)</p>
  </div><!-- media-body -->
</div><!-- team-member media -->
  {% endif %}
{% endfor %}


{% include centerTable.html %}

<h2 style="color: #15378a">Program Evaluator</h2>
<br>

{% for profile in site.team %}
{% assign key = profile.relative_path | split: '/' | last | split: '.' | first %}
{% assign member = site.data.team[key] %}
  {% if member.type == "evaluator" %}
  <div class="team-member media" style="font-size:18px">
    <img src="{{site.url}}/assets/img/{{member.img}}" class="media-object img-circle pull-left" alt="{{ member.name }}" height="115" />
    <div class="media-body">
      <h3 class="media-heading team-name">{{ member.name }}</h3>
      <strong>{{ member.role }} <br>{% if member.type == "director" %}{{ member.involvement }} <br>{% endif %}</strong>
      <hr class="pull-left">
      <div class="clearfix"></div>
      <p style="font-size:14px"> <em>{{ member.position }}<br>{{ member.affiliation }}</em></p>
      <p style="font-size:14px">(<a href="../{{ key }}">more info</a>)</p>
  </div><!-- media-body -->
</div><!-- team-member media -->
  {% endif %}
{% endfor %}

{% include bottomTable.html %}
