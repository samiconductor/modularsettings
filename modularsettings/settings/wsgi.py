def require(**kwargs):

    # Python dotted path to the WSGI application used by Django's runserver.
    WSGI_APPLICATION = 'modularsettings.wsgi.application'

    return locals()
