"""
{% set preset_requirements = [] %}

{% if cookiecutter.preset == 'basic' -%}
{{ preset_requirements.append('pytest') }}
{{ preset_requirements.append('sphinx') }}
{{ preset_requirements.append('tox') }}
{% endif -%}

{{ preset_requirements.sort() }}

{{ cookiecutter.update({ 'preset_requirements': preset_requirements }) }}
"""
