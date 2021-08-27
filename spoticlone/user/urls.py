from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.user_page, name='user'),
    path('login', views.signin, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout_view, name='logout')


    ] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
