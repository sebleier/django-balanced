
BALANCED = {
    'DASHBOARD_URL': 'https://www.balancedpayments.com',
    'API_URL': 'https://api.balancedpayments.com',
    'API_KEY': None,
}

TEMPLATE_CONTEXT_PROCESSORS = [
    'django_balanced.context_processors.balanced_library',
    'django_balanced.context_processors.balanced_settings',
]

MIDDLEWARE_CLASSES = (
    'django_balanced.middleware.BalancedMiddleware',
)


