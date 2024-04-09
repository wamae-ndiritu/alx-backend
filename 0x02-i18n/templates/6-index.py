<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ _('home_title') }}</title>
</head>
<body>
    <h1>{{ _('home_header') }}</h1>
    {% if user %}
        <p>{{ _('logged_in_as', username=user['name']) }}</p>
    {% else %}
        <p>{{ _('not_logged_in') }}</p>
    {% endif %}
</body>
</html>
