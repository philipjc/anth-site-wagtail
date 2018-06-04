from django.db import models
from wagtail.core.models import Page


# Create your models here.

class YogaIndex(Page):

    class Meta:
        verbose_name = 'Yoga Index Page'

    def get_context(self, request, *args, **kwargs):

        # Start context
        context = super(YogaIndex, self).get_context(request)

        return context
