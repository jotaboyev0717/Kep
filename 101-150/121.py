from django.db.models import Model, QuerySet


def get_students(University: Model, Student: Model) -> QuerySet:
    return Student.objects.filter(rating_balls__mod=[2, 0])