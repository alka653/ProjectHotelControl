from django.views.generic import TemplateView
from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name = "principal/dashboard.html"), {'title': 'Bienvenido'}),
]