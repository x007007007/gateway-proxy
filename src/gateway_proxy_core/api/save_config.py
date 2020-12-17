from django.shortcuts import get_object_or_404
from rest_framework import (
    views,
    serializers,
    generics,
)
from gateway_proxy_core.models import ConfigModel, ConfigTypeModel


class ConfigSerializer(serializers.ModelSerializer):
    config_type = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = ConfigModel
        fields = '__all__'


class ListCreateConfigAPI(generics.ListCreateAPIView, views.APIView):
    serializer_class = ConfigSerializer

    def get_root_filter(self):
        return dict(
            config_type=get_object_or_404(ConfigTypeModel, pk=self.kwargs['ct_pk'])
        )

    def get_queryset(self):
        return ConfigModel.objects.filter(**self.get_root_filter())

    def perform_create(self, serializer):
        serializer.save(**self.get_root_filter())


class RetrieveUpdateDeleteConfigAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ConfigSerializer

    def get_root_filter(self):
        return dict(
            config_type=get_object_or_404(ConfigTypeModel, pk=self.kwargs['ct_pk'])
        )

    def get_queryset(self):
        return ConfigModel.objects.filter(**self.get_root_filter())

    lookup_url_kwarg = 'c_pk'


