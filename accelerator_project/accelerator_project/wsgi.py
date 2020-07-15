"""
WSGI config for accelerator_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
# import time
# import traceback
# import signal
import sys

#from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/virtualaccelerator/accelerator_project')
# adjust the Python version in the line below as needed
sys.path.append('/var/www/virtualaccelerator/accelerator_project/venv/lib/python3.6/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "accelerator_project.settings")

# try:
application = get_wsgi_application()
# except Exception:
#     # Error loading applications
#     if 'mod_wsgi' in sys.modules:
#         traceback.print_exc()
#         os.kill(os.getpid(), signal.SIGINT)
#         time.sleep(2.5)
