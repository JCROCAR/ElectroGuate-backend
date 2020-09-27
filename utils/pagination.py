# Django REST Framework
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
# Utilities
from collections import OrderedDict

MESSAGE_OK = 'OK'
PAGINATION_PAGE_SIZE = 10

class DefaultPageNumberPagination(PageNumberPagination):
    """
    Own implementation for information paging
    """

    def get_paginated_response(self, data, message_status=MESSAGE_OK):
        """
        Build the response structure.
        {
            'status': [status_message | 'OK']
            'links': {
                'previous': [PREVIOUS_DATA_LINK | null],
                'next': [NEXT_DATA_LINK | null]
            },
            'total_pages': len(data)/self.page_size,
            'count': len(data),
            'results': data
        }
        """
        return Response(OrderedDict([
            ('status', message_status),
            ('links', OrderedDict([
                ('previous', self.get_previous_link()),
                ('next', self.get_next_link()),
            ])),
            ('count', self.page.paginator.count),
            ('total_pages', self.page.paginator.num_pages),
            ('results', data)
        ]))

class PaginationData(PageNumberPagination):
    """
    Own implementation for information paging
    """
    page_size = PAGINATION_PAGE_SIZE

    def get_paginated_response(self, data, status_message=MESSAGE_OK, status_code=status.HTTP_200_OK):
        """
        Build a Response with a JSON similar to:
        {
            'status': [status_message | 'OK']
            'links': {
                'previous': [PREVIOUS_DATA_LINK | null],
                'next': [NEXT_DATA_LINK | null]
            },
            'total_pages': len(data)/self.page_size,
            'count': len(data),
            'results': data
        }
        """
        response = {
            'status': status_message,
            'links': {
                'previous': self.get_previous_link(),
                'next': self.get_next_link()
            },
            'total_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'results': data
        }
        return Response(response, status=status_code)
