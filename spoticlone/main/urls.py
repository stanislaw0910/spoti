from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import RenderHTMLPlayer, ArtistView, AlbumView, FavoritesView, SearchResultsView, About, Index

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('about', About.as_view(), name='about'),
    #path('search', views.search, name='search'),
    path('search', SearchResultsView.as_view(), name='search'),
    path('favorites', FavoritesView.as_view(), name='favorites'),
    path('artist/<int:pk>', ArtistView.as_view(), name='artist_page'),
    path('album/<int:pk>', AlbumView.as_view(), name='album_page'),
    path('<int:id>', RenderHTMLPlayer.as_view(), name='player'),

    ] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
