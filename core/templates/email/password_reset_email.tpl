{% extends "mail_templated/base.tpl" %}

{% block subject %}
Reset Password
{% endblock %}

{% block html %}
http://127.0.0.1:9000/accounts/api/v1/reset_password/{{token}}
{% endblock %}
