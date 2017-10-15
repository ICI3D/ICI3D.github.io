---
layout: page
title: I3D Exchange Scholars
tab: People
longtitle: I3D Research Exchange Scholars Program Alumni
summary: The I3D Exchange Program provides an opportunity for former participants in the MMED and DAIDD clinics to engage more deeply with infectious disease research problems in collaboration with the ICI3D faculty.
---

{% include topTable.html %}

<h2 style="color: #15378a">Exchange visits to North America</h2>
<br>

{% for profile in site.profiles %}
{% if profile.type == "i3d_toNA" %}
  <div class="team-member media" style="font-size:18px">
    <img src="{{site.url}}/assets/img/{{profile.img}}" class="media-object img-circle pull-left" alt="{{ profile.name }}" height="105" />
    <div class="media-body">
      <h3 class="media-heading team-name">{{ profile.name }} ({{ profile.year }})</h3>
      <strong>{{ profile.home }}</strong>
      <hr class="pull-left">
      <div class="clearfix"></div>
      <p style="font-size:14px"> <strong>{{ profile.former }}</strong></p>
      <p style="font-size:14px">(<a href="../{{ profile.title | downcase}}">more info</a>)</p>
  </div><!-- media-body -->
</div><!-- team-member media -->
  {% endif %}
{% endfor %}

{% include centerTable.html %}

<h2 style="color: #15378a">Exchange visits to Africa</h2>
<br>

{% for profile in site.profiles %}
{% if profile.type == "i3d_toAfrica" %}
  <div class="team-member media" style="font-size:18px">
    <img src="{{site.url}}/assets/img/{{profile.img}}" class="media-object img-circle pull-left" alt="{{ profile.name }}" height="105" />
    <div class="media-body">
      <h3 class="media-heading team-name">{{ profile.name }} ({{ profile.year }})</h3>
      <strong>{{ profile.home }}</strong>
      <hr class="pull-left">
      <div class="clearfix"></div>
      <p style="font-size:14px"> <strong>{{ profile.former }}</strong></p>
      <p style="font-size:14px">(<a href="../{{ profile.title | downcase}}">more info</a>)</p>
  </div><!-- media-body -->
</div><!-- team-member media -->
  {% endif %}
{% endfor %}

{% include bottomTable.html %}
