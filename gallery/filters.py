from .models import Image
import django_filters
# filterset
class ImageFilter(django_filters.FilterSet):
    class Meta:
        model = Image
        fields = ['location']