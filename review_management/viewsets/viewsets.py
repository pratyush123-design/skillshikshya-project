from rest_framework import viewsets
from  review_management.models import Review
from review_management.serializers.serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
