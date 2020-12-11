from rest_framework.serializers import ModelSerializer
from ..models import Self_Rating, Manager_Rating


class SelfRatingSerializer(ModelSerializer):
    class Meta:
        model = Self_Rating
        fields = "__all__"

    def create(self, validated_data):
        self_rating, created = Self_Rating.objects.update_or_create(
            user_appraisal_list=validated_data.get("uder_appraisal_list", None),
            defaults={
                **validated_data,
            },
        )
        return self_rating


class HrmanagerReviewRatingsSerializer(ModelSerializer):
    class Meta:
        model = Manager_Rating
        fields = "__all__"

    def create(self, validated_data):
        hr_ratings, created = Manager_Rating.objects.update_or_create(
            employee_self_rating=validated_data.get("employee_self_rating", None),
            defaults={**validated_data},
        )
        return hr_ratings
