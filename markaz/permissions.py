from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #faqatgina ko'rish uchun ruxsat berish
        if request.method in permissions.SAFE_METHODS:
            return True
        #ozgartirish va yozish faqatgina post muallifiga beriladi
        return obj.teacher.username == request.user.username