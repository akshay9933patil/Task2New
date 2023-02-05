from rest_framework import permissions



class IsOwnerPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if obj.owner == str(request.user):

            return True
            
        return False

# in has_permission, 
# 1st it will check whether the request is in SAFE_METHOD or not
# if request is not in SAFE_METHOD then it will check whether user is authenticated or not

# if user is authenticated has_object method gets called
# 1st it will check whether user is admin or not
# if user is not admin it will check whether the request.user is owner of the post
# line number 22 request.user is converted to string as type class of request.user is not string


""" 
1. function based API
2. Classs Based API
3. Generic API --> CreateAPIView, ListApiView, ,
                   CreateListAPIVIew, 
                   RetrieveAPIView UpdateAPIView, RetrieveUpdateAPIView, RetrievUpdateDetroyAPIView

4. Viewsets
"""
