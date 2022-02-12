from django.urls import path
from django.views.generic import TemplateView

aoo_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html")),
]