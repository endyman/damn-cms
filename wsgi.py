import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
