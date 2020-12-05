from django.shortcuts import get_object_or_404
from rest_framework import (
    views,
    generics,
    request as d_request,
    response
)
from .models import (
    ConfigTypeModel,
    ConfigTemplateTableModel,
    ConfigTemplateValueModel,
    ConfigModel
)

class ConfigTemplateAPI(views.APIView):

    def get_parent(self, request, ct_pk):
        config_type = ConfigTypeModel.objects.get(pk=ct_pk)
        return config_type

    def get(self, request: d_request.Request, *args, **kwargs):
        parent = self.get_parent(request, *args, **kwargs)  # type: ConfigTypeModel
        tpl_table = parent.tpl_table
        if tpl_id := request.query_params.get('id', None):
            tpl_table = get_object_or_404(ConfigTemplateTableModel, pk=tpl_id)  # type: ConfigTemplateTableModel
            print(tpl_table)
        res = []
        for v in ConfigTemplateValueModel.objects.filter(table=tpl_table).order_by('order'):  # type:ConfigTemplateValueModel
            d = {
                'type': v.type_name,
                'default': v.get_default_value(),
                'required': v.required,
                'name': v.name,
                # 'id': v.pk
            }
            if v.type == v.TYPE_SWITCH:
                d['switch'] = ConfigTemplateTableModel.objects.filter(
                    switch=v
                ).order_by('order').values("id", "name", 'have_sub_config')
            res.append(d)
        return response.Response(res)
