from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.account, name='account'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),

    ] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
