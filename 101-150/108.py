from django.db.models import Model, QuerySet


def delete_universities(University: Model) -> None:
    University.objects.filter(students_count__lt=20).delete()