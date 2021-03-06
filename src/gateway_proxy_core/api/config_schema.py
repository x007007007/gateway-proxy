from django.shortcuts import get_object_or_404
from rest_framework import views, request as d_request, response

from gateway_proxy_core.models import ConfigTypeModel, ConfigStructSchemaGroupModel, ConfigStructSchemaItemModel


class ConfigSchemaAPI(views.APIView):

    def get_parent(self, request, ct_pk):
        config_type = ConfigTypeModel.objects.get(pk=ct_pk)
        return config_type

    def get(self, request: d_request.Request, *args, **kwargs):
        parent = self.get_parent(request, *args, **kwargs)  # type: ConfigTypeModel
        tpl_schema = parent.tpl_schema
        if tpl_id := request.query_params.get('id', None):
            tpl_schema = get_object_or_404(ConfigStructSchemaGroupModel, pk=tpl_id)  # type: ConfigStructSchemaGroupModel
            print(tpl_schema)
        res = []
        for v in ConfigStructSchemaItemModel.objects.filter(group=tpl_schema).order_by('order'):  # type:ConfigStructSchemaItemModel
            d = {
                'type': v.type_name,
                'default': v.get_default_value(),
                'required': v.required,
                'display_name': v.display_name,
                'name': v.name,
                # 'id': v.pk
            }
            if v.type == v.TYPE_SWITCH:
                d['items'] = ConfigStructSchemaGroupModel.objects.filter(
                    item=v
                ).order_by('order').values("id", "name", 'have_sub_config')
            res.append(d)
        return response.Response(res)