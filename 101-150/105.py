from django.db.models import Model, QuerySet, Q


def get_universities(University: Model) -> QuerySet:
    return University.objects.filter(
        Q(students_count__gte=12) | ~Q(name__contains = 'e')
    )