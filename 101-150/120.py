from django.db.models import Model, QuerySet


def get_students(University: Model, Student: Model) -> QuerySet:
    return University.objects.filter(name='TATUUF')