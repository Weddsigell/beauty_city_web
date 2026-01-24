from .models import Category


def get_categories():
    return Category.objects.all()
