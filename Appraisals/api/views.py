from rest_framework.generics import CreateAPIView
from ..models import Self_Rating,HrmanagerReviewRatings
from .serializers import *
from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse

class CreateSelfRating(CreateAPIView):
    queryset = Self_Rating.objects.all()
    serializer_class = SelfRatingSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('Appraisals:Update_AppraisalCareer', args=(request.data.get('uder_appraisal_list'),)))
   
    
 
class CreateHrmanagerReviewRatings(CreateAPIView):
    queryset = HrmanagerReviewRatings.objects.all()
    serializer_class = HrmanagerReviewRatingsSerializer

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('Appraisals:Update_AppraisalCareer_M', args=(request.data.get('employee_appraisal_id'),)))
   

 