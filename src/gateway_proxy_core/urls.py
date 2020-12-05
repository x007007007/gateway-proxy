from django.urls import path
from . import views


urlpatterns = [
    path('config/type/<int:ct_pk>/table/', views.ConfigTemplateAPI.as_view()),
]
