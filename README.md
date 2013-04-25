# django-balanced

## How to send ACH payments in 10 minutes

1. Visit www.balancedpayments.com and get yourself an API key

2. `pip install django-balanced`

3. Edit your `settings.py` and add the API key like so:

        import os

        BALANCED = {
            'DASHBOARD_URL': 'https://www.balancedpayments.com',
            'API_URL': 'https://api.balancedpayments.com',
            'API_KEY': os.environ.get('BALANCED_API_KEY'),
        }

4. Add `django_balanced` to your `INSTALLED_APPS` in `settings.py`

        INSTALLED_APPS = (
           ...
           'django.contrib.admin',  # if you want to use the admin interface
           'django_balanced',
           ...
        )

5. Add middleware in `settings.py`:

        MIDDLEWARE_CLASSES = (
            ...
            'django_balanced.middleware.BalancedMiddleware',
            ...
        )

6. Add context processors in `settings.py`:

        TEMPLATE_CONTEXT_PROCESSORS = [
            ...
            'django_balanced.context_processors.balanced_library',
            'django_balanced.context_processors.balanced_settings',
            ...
        ]

7. Run `django-admin.py syncdb`
8. Run `python manage.py runserver`
9. Visit `http://127.0.0.1:8000/admin` and pay some people!
