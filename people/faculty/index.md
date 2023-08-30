---
layout: page
title: Faculty
tab: People
longtitle: Program Faculty
summary: The ICI3D program faculty consists of core faculty, who are regular instructors and are responsible for overall design and execution of the program, and workshop faculty, who serve as workshop instructors.
---

{% include topTable.html %}

<h2 style="color: #15378a">Current Faculty</h2>
<br>

{% for profile in site.team %}
{% assign key = profile.relative_path | split: '/' | last | split: '.' | first %}
{% assign member = site.data.team[key] %}
  {% if member.type == "core" or member.type == "director" %}
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

<h2 style="color: #15378a"><br></h2>
<br>

{% for profile in site.team %}
{% assign key = profile.relative_path | split: '/' | last | split: '.' | first %}
{% assign member = site.data.team[key] %}
{% if member.type == "workshop" %}
  <div class="team-member media" style="font-size:18px">
    <img src="{{site.url}}/assets/img/{{member.img}}" class="media-object img-circle pull-left" alt="{{ member.name }}" height="115" />
    <div class="media-body">
      <h3 class="media-heading team-name">{{ member.name }}</h3>
      <strong>{{ member.involvement }}</strong>
      <hr class="pull-left">
      <div class="clearfix"></div>
      <p style="font-size:14px"> <em>{{ member.position }}<br>{{ member.affiliation }}</em></p>
      <p style="font-size:14px">(<a href="../{{ key | downcase}}">more info</a>)</p>
  </div><!-- media-body -->
</div><!-- team-member media -->
  {% endif %}
{% endfor %}

{% include bottomTable.html %}


{% include topTable.html %}

<h2 style="color: #15378a">Founding Faculty</h2>
<br>

{% for profile in site.team %}
{% assign key = profile.relative_path | split: '/' | last | split: '.' | first %}
{% assign member = site.data.team[key] %}
  {% if member.type == "founding" %}
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

<h2 style="color: #15378a">Former Faculty</h2>
<br>

{% for profile in site.team %}
{% assign key = profile.relative_path | split: '/' | last | split: '.' | first %}
{% assign member = site.data.team[key] %}
  {% if member.type == "inactive" %}
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
