---
layout: redirect
redirect: ./faculty
tab: People
title: Faculty & Staff
longtitle: Faculty & Staff
summary:
subtitle: International Clinics on Infectious Disease Dynamics and Data
---

## Program Faculty

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
