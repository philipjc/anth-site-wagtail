from django.db import models
from wagtail.core.models import Page
from itertools import chain

from yoga.models import YogaLesson
from health.models import HealthTreatment


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

    page_intro = models.CharField(max_length=500, null=True)

    def get_context(self, request, *args, **kwargs):

        lessons = YogaLesson.objects.all()

        treatments = HealthTreatment.objects.all()

        # Start context
        context = super(HomePage, self).get_context(request)

        context['latest_lessons'] = lessons

        context['latest_treatments'] = treatments

        return context
