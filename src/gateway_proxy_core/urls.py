from django.urls import path

from . import api


urlpatterns = [
    path('config/type/<int:ct_pk>/schema/', api.config_schema.ConfigSchemaAPI.as_view()),
    path('config/type/<int:ct_pk>/ins/', api.save_config.ListCreateConfigAPI.as_view()),
    path('config/type/<int:ct_pk>/ins/<int:c_pk>/', api.save_config.RetrieveUpdateDeleteConfigAPI.as_view())
]
