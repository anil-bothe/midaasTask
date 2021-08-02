from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.routes.api import urlpatterns as PrimeNoView
from app.routes.main import urlpatterns as admin


def loadRoutes():
    routes = [PrimeNoView, admin]
    urls = [
        path(f'midaas/{url["suffix"]}/', url['view'], name=url['suffix']) if 'view' in url else path(f'{url["suffix"]}', url['include'])
        for r in routes 
        for url in r
    ]
    return urls

urlpatterns = loadRoutes()

# for development server
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
