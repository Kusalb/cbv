
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from cbv.views import Ex2View

app_name = 'cbv'
urlpatterns = [
    path('ex1', TemplateView.as_view(template_name='ex1.html', extra_context={'title': 'new title'})),
    path('ex2', Ex2View.as_view(), name='ex2')

]
