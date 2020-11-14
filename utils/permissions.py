from rest_framework import permissions

DEFAULT_PERMISSIONS_CLASSES = (permissions.IsAuthenticated,)
DEFAULT_PERMISSIONS_NOT_REQUIRED = (permissions.AllowAny,)
