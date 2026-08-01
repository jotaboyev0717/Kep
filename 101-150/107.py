from django.db.models import Model, QuerySet


def update_universities(University: Model) -> None:
    University.objects.filter(students_count__gt=10).update(name='UNIVER')