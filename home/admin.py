from .models import *

from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel, FieldPanel, \
    MultiFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

HomePage.content_panels = HomePage.content_panels + [
    FieldPanel('page_title'),
    ImageChooserPanel('page_header_image'),
    FieldPanel('page_intro_header'),
    FieldPanel('page_intro'),
    StreamFieldPanel('body'),
    FieldPanel('body_header'),
]
