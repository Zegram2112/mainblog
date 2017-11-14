from urllib.parse import urlencode
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_append_get(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


@register.simple_tag(takes_context=True)
def GET_field(context, field):
    GET_dict = context['request'].GET
    return GET_dict[field]

