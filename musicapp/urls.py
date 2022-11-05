from django.conf.urls import url
from django.urls import path, include
from musicapp.views import (
#    ArtisteListApiView,
    SongListApiView,
)

urlpatherns = [
#    path('api', ArtisteListApiView.as_view()),
    path('api', SongListApiView.as_view()),
]  