from django.db.models import Model, QuerySet


def create_university(University: models.Model, name: str, students_count: int) -> QuerySet:
    University.objects.create(name=name, students_count=students_count)