from app.controllers.front_end import home
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.routes.api import urlpatterns as PrimeNoView
from app.routes.main import urlpatterns as front_end


def loadRoutes():
    routes = [PrimeNoView, front_end]
    urls = [
        path(f'{url["suffix"]}/', url['view'], name=url['suffix']) if 'view' in url else path(f'{url["suffix"]}', url['include'])
        for r in routes 
        for url in r
    ]
    return urls

urlpatterns = loadRoutes()
urlpatterns += [ path('', home) ]

# for development server
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
