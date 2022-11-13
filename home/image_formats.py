"""
Цей файл потрібен для адаптивного формату картинок у Rich Text Field в редакторі Плиски. 
"""
from wagtail.images.formats import Format, register_image_format

register_image_format(Format('fluidimage', 'Адаптивна Картинка(Рекомендовано)', 'rural_image', 'original'))