---
layout: page
title: Faculty
tab: People
longtitle: Program Faculty
summary: The ICI3D program faculty consists of core faculty, who are regular instructors and are responsible for overall design and execution of the program, and workshop faculty, who serve as workshop instructors.
subtitle: International Clinics on Infectious Disease Dynamics and Data
---

{% include topTable.html %}

### Core Faculty

{% for profile in site.profiles %}
  {% if profile.type == "director" or profile.type == "core" %}
**{{ profile.name }}** ([more](../{{ profile.title | downcase }} "{{ profile.name }}"))<br>
*{{ profile.role }}* <br>{% if profile.type == "director" %}*{{ profile.involvement }}* <br>{% endif %}
{{ profile.position }} <br>
{{ profile.affiliation }}
  {% endif %}
{% endfor %}

{% include centerTable.html %}

### Workshop Faculty

{% for profile in site.profiles %}
  {% if profile.type == "workshop" %}
**{{ profile.name }}** ([more](../{{ profile.title | downcase }} "{{ profile.name }}")) <br>
*{{ profile.involvement }}* <br>
{{ profile.position }} <br>
{{ profile.affiliation }}
  {% endif %}
{% endfor %}

{% include bottomTable.html %}
