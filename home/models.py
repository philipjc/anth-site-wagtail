from django.db import models
from wagtail.core.models import Page


# Create your models here.

class HomePage(Page):

    class Meta:
        verbose_name = 'Home Page'

    def get_context(self, request, *args, **kwargs):

        # Start context
        context = super(HomePage, self).get_context(request)

        return context
