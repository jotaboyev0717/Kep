from django.db.models import Model, QuerySet, F
from django.db.models.functions import Length


def get_students(University: Model, Student: Model) -> QuerySet:
    return Student.objects.annotate(
        first_len=Length('first_name'),
        last_len=Length('last_name')
    ).filter(first_len__gt=F('last_len'))