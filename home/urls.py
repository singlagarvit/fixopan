from django.contrib import admin
from django.urls import path

from .views import home_view, about_view, advantages_view, waterstop_view, profiles_view, contruction_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home_view, name="index"),
    path('about-us/', about_view, name="about"),
    path('advantages/', advantages_view, name="advnatages"),
    path('pvc-waterstop/', waterstop_view, name="waterstop"),
    path('pvc-profiles/', profiles_view, name="profiles"),
	path('construction-joints/', contruction_view, name="construction"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
