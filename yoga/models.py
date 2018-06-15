from django.db import models
from wagtail.core.models import Page


# Create your models here.
class YogaIndex(Page):

    class Meta:
        verbose_name = 'Yoga Index Page'

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

        # Start context
        context = super(YogaIndex, self).get_context(request)

        context['lessons'] = YogaLesson.objects.all()

        return context


class YogaLesson(Page):

    class Meta:
        verbose_name = 'Yoga Lesson'

    lesson_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    lesson_title = models.CharField(max_length=200, null=True)

    lesson_level = models.CharField(max_length=100, blank=True, null=True)

    lesson_date = models.DateTimeField(blank=True, null=True)

    lesson_price = models.CharField(max_length=20, blank=True, null=True)

    lesson_duration = models.CharField(max_length=50, blank=True, null=True)

    lesson_desc = models.CharField(max_length=500, null=True)

    lesson_additional_desc = models.CharField(max_length=500, blank=True, null=True)

    lesson_teacher = models.CharField(max_length=100, blank=True, null=True)

    loc_name = models.CharField(max_length=200, blank=True, null=True)

    loc_lat = models.CharField(max_length=40, blank=True, null=True)

    loc_lng = models.CharField(max_length=40, blank=True, null=True)

    def get_context(self, request, *args, **kwargs):

        # Start context
        context = super(YogaLesson, self).get_context(request)

        return context
