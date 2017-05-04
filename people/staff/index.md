---
layout: page
title: Staff
tab: People
longtitle: Program Staff
summary:
subtitle: International Clinics on Infectious Disease Dynamics and Data
---

{% include topTable.html %}

### Administrative Staff

{% for profile in site.profiles %}
  {% if profile.type == "admin" %}
**{{ profile.name }}** ([more](../{{ profile.title | downcase }} "{{ profile.name }}")) <br>
*{{ profile.role }}* <br>
{{ profile.affiliation }}
  {% endif %}
{% endfor %}


{% include centerTable.html %}

### Program Evaluator

{% for profile in site.profiles %}
  {% if profile.type == "evaluator" %}
**{{ profile.name }}** ([more](../{{ profile.title | downcase }} "{{ profile.name }}")) <br>
*{{ profile.role }}* <br>
{{ profile.position }} <br>
{{ profile.affiliation }}
  {% endif %}
{% endfor %}

{% include bottomTable.html %}
