from rest_framework import serializers
from GnC import models

class UserCommentSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = models.Comment_box
        fields = ('id','user_profile','user_comments','created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only':True
            }
        }
