"""
WSGI config for ai_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import signal
import logging
import threading

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_project.settings')

logger = logging.getLogger(__name__)

application = get_wsgi_application()


# ---------------------------------------------------------------------------
# Graceful shutdown — handle SIGTERM from Railway during deploys/restarts
# Only register in the main thread (Django runserver uses a child thread)
# ---------------------------------------------------------------------------

def handle_shutdown(signum, frame):
    """Log and allow Gunicorn to shut down workers gracefully."""
    sig_name = signal.Signals(signum).name
    logger.info("Received %s — shutting down gracefully...", sig_name)
    raise SystemExit(0)


if threading.current_thread() is threading.main_thread():
    signal.signal(signal.SIGTERM, handle_shutdown)
    signal.signal(signal.SIGINT, handle_shutdown)
