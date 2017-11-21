from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^grado/nuevo/$', views.grado_nuevo, name='grado_nuevo'),
    url(r'^grado/(?P<pk>[0-9]+)/$', views.detalle_grado, name='ver_grado'),
]
