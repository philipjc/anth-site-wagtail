from .models import *

from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel, FieldPanel, \
    MultiFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

YogaIndex.content_panels = YogaIndex.content_panels + [
    FieldPanel('page_title'),
    ImageChooserPanel('page_header_image'),
    FieldPanel('page_intro'),
]

YogaLesson.content_panels = YogaLesson.content_panels + [
    ImageChooserPanel('lesson_image'),
    FieldPanel('lesson_title'),
    FieldPanel('lesson_level'),
    FieldPanel('lesson_date'),
    FieldPanel('lesson_price'),
    FieldPanel('lesson_duration'),
    FieldPanel('lesson_desc'),
    FieldPanel('lesson_additional_desc'),
    FieldPanel('lesson_teacher'),
    FieldPanel('loc_name'),
    FieldPanel('loc_lat'),
    FieldPanel('loc_lng'),
]
