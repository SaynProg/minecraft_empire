from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from wagtail.search import index

from wagtail.snippets.models import register_snippet

from events.models import EventPage

class TeamPage(Page):
	parent_page_types = ['home.HomePage']
	template = 'team/team.html'

	body = RichTextField(verbose_name='Кортокий Опис Сторінки')
	keywords = models.CharField('Ключові слова для пошуку', max_length=500, blank=True, null=True)

	def get_context(self, request, *args, **kwargs):
		context = super().get_context(request, *args, **kwargs)

		events = EventPage.objects.live().public().order_by('-date')[:5]
		context['events'] = events
		team = MemberModel.objects.all()
		context['team'] = team 

		return context

	content_panels = Page.content_panels + [
		FieldPanel('body')
	]

	search_fields = Page.search_fields + [
		index.SearchField('title'),
		index.SearchField('body'),
	]
	
	promote_panels = Page.promote_panels + [
		FieldPanel('keywords')
	]

	class Meta:
		verbose_name = 'Сторінка Команди'

@register_snippet
class MemberModel(models.Model):
	name = models.CharField(verbose_name='Ім\'я', max_length=200)
	photo = models.ForeignKey(
		'wagtailimages.Image', 
		verbose_name='Зображення', 
		null=True, blank=True, 
		on_delete=models.SET_NULL, 
		related_name='+'
		)
	detail_of_person = models.TextField(verbose_name='Опис Учасника')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Учасник Команди'
		verbose_name_plural = 'Учасники Команди'