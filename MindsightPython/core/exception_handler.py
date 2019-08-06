from __future__ import unicode_literals

from rest_framework.exceptions import ValidationError, NotFound
from rest_framework import status, exceptions
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    if isinstance(exc, NotFound):
        return Response({'error': 'Not found'},
                        status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, ValidationError):
        return Response({'error': 'Bad Request'},
                        status=status.HTTP_400_BAD_REQUEST)

    # Note: Unhandled exceptions will raise a 500 error.
    return None