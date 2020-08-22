# Django REST Framework
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
# Utilities
from collections import OrderedDict

MESSAGE_OK = 'OK'

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