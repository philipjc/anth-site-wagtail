from .models import *
from django import forms

from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel, FieldPanel, \
    MultiFieldPanel

from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel

# Categorie
HealthCategory.panels = [
    FieldPanel('name'),
]

# Treatment
HealthTreatment.content_panels = HealthTreatment.content_panels + [
    ImageChooserPanel('treatment_image'),
    FieldPanel('treatment_title'),
    FieldPanel('treatment_desc'),
    FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
]

# Index Page
HealthIndex.content_panels = HealthIndex.content_panels + [
    FieldPanel('page_title'),
    ImageChooserPanel('page_header_image'),
    FieldPanel('page_intro'),
]
