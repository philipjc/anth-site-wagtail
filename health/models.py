from django.db import models
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField

from modelcluster.fields import ParentalManyToManyField
from utils.models import GeneralStreamBlock

# Categories
@register_snippet
class HealthCategory(models.Model):

    class Meta:
        verbose_name = 'Health Category'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Health Treatment
class HealthTreatment(Page):

    class Meta:
        verbose_name = 'Health Treatment'

    treatment_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    treatment_title = models.CharField(max_length=200, null=True)

    treatment_price = models.CharField(max_length=20, blank=True, null=True)

    treatment_duration = models.CharField(max_length=20, blank=True, null=True)

    treatment_desc = models.CharField(max_length=500, null=True)

    categories = ParentalManyToManyField('health.HealthCategory', blank=True)

    body = StreamField(GeneralStreamBlock, blank=True)

    def get_context(self, request, *args, **kwargs):

        context = super(HealthTreatment, self).get_context(request)

        context['categories'] = self.categories

        return context


# Index Page
class HealthIndex(Page):

    class Meta:
        verbose_name = 'Health Index Page'

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

        context = super(HealthIndex, self).get_context(request)

        context['treatments'] = HealthTreatment.objects.all()

        return context
