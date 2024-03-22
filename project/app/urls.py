from django.urls import path
from .views import integer
urlpatterns=[
    path("combination/<int:pk>/<str:id>/<slug:pkid>/<path:idpk>",integer,name="integer")
]