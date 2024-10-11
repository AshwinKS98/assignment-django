# settings/development.py

from .base import *

# Development-specific settings
DEBUG = True  # Ensure this is True for development
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# You can override or add settings specific to the development environment
# Example: Additional installed apps, logging settings, etc.