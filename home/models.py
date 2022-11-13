from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from wagtail.search import index
from wagtail.snippets.models import register_snippet

from events.models import EventPage

class HomePage(Page):
	body = RichTextField(verbose_name='Зміст Сторінки', blank=True)
	keywords = models.CharField('Ключові слова для пошуку', max_length=500, blank=True, null=True)

	def get_context(self, request, *args, **kwargs):
		context = super().get_context(request, *args, **kwargs)

		events = EventPage.objects.live().public().order_by('-date')[:5]
		context['events'] = events

		return context

	content_panels = Page.content_panels + [
		FieldPanel('body'),
	]

	search_fields = Page.search_fields + [
		index.SearchField('title'),
		index.SearchField('body'),
	]

	promote_panels = Page.promote_panels + [
		FieldPanel('keywords')
	]

	class Meta:
		verbose_name = 'Сторінка'

@register_snippet
class FooterModel(models.Model):
    body = RichTextField('Зміст')

    panels = [
        FieldPanel('body')
    ]

    def __str__(self):
        return 'Футтер'

    class Meta:
        verbose_name = 'Футтер'
        verbose_name_plural = 'Футтери'