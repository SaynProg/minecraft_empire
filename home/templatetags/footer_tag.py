from django import template
from home.models import FooterModel

register = template.Library()

@register.inclusion_tag('home/footer.html', takes_context=True)
def footer_item_tag(context):
	return {
		'item':FooterModel.objects.first(),
		'request':context['request'],
	}