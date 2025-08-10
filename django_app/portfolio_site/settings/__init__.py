import os

# Automatically load the correct settings based on environment
if os.getenv('DJANGO_ENV') == 'production':
    from .production import *
else:
    from .development import *