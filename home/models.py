from django.db import models
from wagtail.core.models import Page
from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import StreamField

from yoga.models import YogaLesson
from health.models import HealthTreatment
from utils.models import GeneralStreamBlock

from itertools import chain


# Home Index
class HomePage(Page):

    class Meta:
        verbose_name = 'Home Page'

    page_title = models.CharField(max_length=200, null=True)

    page_header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    page_intro_header = models.CharField(max_length=200, null=True, blank=True)

    page_intro = models.CharField(max_length=500, null=True)

    body_header = models.CharField(max_length=200, null=True, blank=True)

    body = StreamField(GeneralStreamBlock, blank=True)

    def get_context(self, request, *args, **kwargs):

        lessons = YogaLesson.objects.all()

        treatments = HealthTreatment.objects.all()

        # Start context
        context = super(HomePage, self).get_context(request)

        context['latest_lessons'] = lessons

        context['latest_treatments'] = treatments

        return context
