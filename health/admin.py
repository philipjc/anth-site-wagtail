from .models import *
from django import forms

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel, FieldPanel, \
    MultiFieldPanel

# Categorie
HealthCategory.panels = [
    FieldPanel('name'),
]

# Treatment
HealthTreatment.content_panels = HealthTreatment.content_panels + [
    ImageChooserPanel('treatment_image'),
    FieldPanel('treatment_title'),
    FieldPanel('treatment_price'),
    FieldPanel('treatment_duration'),
    FieldPanel('treatment_desc'),
    FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    StreamFieldPanel('body'),
]

# Index Page
HealthIndex.content_panels = HealthIndex.content_panels + [
    FieldPanel('page_title'),
    ImageChooserPanel('page_header_image'),
    FieldPanel('page_intro'),
]
