from django.db.models import Model, QuerySet


def get_universities(University: Model) -> QuerySet:
    return University.objects.filter(
        Q(students_count__lt=10) | Q(name__endwith='u')
    )