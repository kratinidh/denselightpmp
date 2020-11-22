from rest_framework import permissions

class UpdateOwnComment(permissions.BasePermission):
    """"""
    def has_object_permission(self, request, view, obj):
        """"""
        if request.method in permissions.SAFE_METHODS:
            # print("safe met")
            return True

        # print("out")
        # return obj.user_profile.employee_ID == request.user.employee_ID
        return True
