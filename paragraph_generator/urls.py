from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views
from .healthcheck import health_check

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

urlpatterns = [
     # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    # Application URLs
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('generate/', views.generate_paragraph_index, name='generate_paragraph'),
    path('stream-generate/', views.stream_generate, name='stream_generate'),

    # Health check — used by Railway for deployment monitoring
    path('health/', health_check, name='health_check'),

    # Sitemap URL
    path('sitemap.xml', sitemap, {'sitemaps': {'static': StaticViewSitemap}}, name='sitemap'),
]
