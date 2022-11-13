from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from wagtail.search import index
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import datetime

class EventsPage(Page):
	parent_page_types = ['home.HomePage']
	subpage_types = ['events.EventPage']
	template = 'events/events.html'

	body = RichTextField(verbose_name='Зміст Сторінки', blank=True)
	keywords = models.CharField('Ключові слова для пошуку', max_length=500, blank=True, null=True)


	def get_context(self, request, *args, **kwargs):
		context = super().get_context(request, *args, **kwargs)

		objects = EventPage.objects.live().public().order_by('-date')

		# search_query = request.GET.get("query", None)
		page = request.GET.get("page")

		# Pagination
		paginator = Paginator(objects, 10)
		try:
			objects = paginator.page(page)
		except PageNotAnInteger:
			objects = paginator.page(1)
		except EmptyPage:
			objects = paginator.page(paginator.num_pages)

		context['events'] = objects 
		context['timenow'] = datetime.datetime.now()

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
		verbose_name = 'Сторінка Подій'

class EventPage(Page):
	parent_page_types = ['events.EventsPage']
	template = 'events/event.html'

	body = RichTextField(verbose_name='Опис', blank=True)
	photo = models.ForeignKey(
		'wagtailimages.Image', 
		verbose_name='Зображення', 
		null=True, blank=True, 
		on_delete=models.SET_NULL, 
		related_name='+'
		)
	date = models.DateTimeField(verbose_name='Час Події')

	content_panels = Page.content_panels + [
		FieldPanel('body'),
		FieldPanel('photo'),
		FieldPanel('date'),
	]

	search_fields = Page.search_fields + [
		index.SearchField('title'),
		index.SearchField('body'),
	]

	class Meta:
		verbose_name = 'Подія'
		verbose_name_plural = 'Події'