"""
Health check endpoint for Railway deployment.
Returns database connectivity status for automated health monitoring.
"""
import logging
from django.http import JsonResponse
from django.db import connection

logger = logging.getLogger(__name__)


def health_check(request):
    """
    Health check endpoint that verifies database connectivity.
    Railway uses this to determine if the service is healthy.
    """
    health = {"status": "ok"}

    # Verify database connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        health["database"] = "connected"
    except Exception as e:
        logger.error("Health check database failure: %s", e)
        health["status"] = "degraded"
        health["database"] = "disconnected"
        return JsonResponse(health, status=503)

    return JsonResponse(health, status=200)
