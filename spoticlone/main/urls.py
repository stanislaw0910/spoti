from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import RenderHTMLPlayer, ArtistView, AlbumView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('artist/<int:pk>', ArtistView.as_view(), name='artist_page'),
    path('album/<int:pk>', AlbumView.as_view(), name='album_page'),
    path('<int:id>', RenderHTMLPlayer.as_view(), name='player')

    ] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
