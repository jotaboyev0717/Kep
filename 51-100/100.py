from django.db.models import Model, QuerySet


def get_universities(University: Model) -> QuerySet:
    return University.objects.all()