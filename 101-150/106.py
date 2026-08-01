from django.db.models import Model, QuerySet
from django.utils import timezone
from datetime import timedelta

def get_universities_count(University: Model) -> QuerySet:
    hundred = timezone.now() - timedelta(days=100)
    return University.objects.filter(created__lt=hundred).count()