=====
introspectmodels
=====

introspectmodels is a Django app to introspect models in your django projetct.
It will create a '.forestadmin-schema.json' file describing the models you're using at server start.

Quick start
-----------

1. Add "introspectmodels" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'introspectmodels',
    ]


2. Start the development server and visit http://127.0.0.1:8000/admin/

3. Watch the $DJANGO_PROJECT_ROOT/.forestadmin-schema.json
