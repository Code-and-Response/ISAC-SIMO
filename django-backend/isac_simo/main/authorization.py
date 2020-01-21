# Authorize Users to check user passes test in view
from rest_framework.permissions import BasePermission

login_url = '/login/?error=unauthorized'

def is_admin(user):
    if user and user.is_authenticated:
        return user.is_active and user.is_admin
    return False

def is_engineer(user):
    if user and user.is_authenticated:
        return user.is_active and user.is_engineer
    return False

def is_government(user):
    if user and user.is_authenticated:
        return user.is_active and user.is_government
    return False

def is_user(user):
    if user and user.is_authenticated:
        return user.is_active and user.is_user
    return False

class HasAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.is_active and request.user.is_admin

class HasEngineerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.is_active and request.user.is_engineer

class HasGovernmentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.is_active and request.user.is_government

class HasUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.is_active and request.user.is_user