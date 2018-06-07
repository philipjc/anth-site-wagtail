from yoga.models import YogaLesson
from health.models import HealthTreatment

from django import template

register = template.Library()


@register.inclusion_tag('partials/footer.html')
def footer():

    lessons = YogaLesson.objects.all()

    treatments = HealthTreatment.objects.all()

    return {
        'latest_lessons': lessons,
        'latest_treatments': treatments
    }
