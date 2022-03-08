from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    """
    Set up the pagination to 25 for
    the custom Sale by 25 view
    """
    page_size = 25
    page_size_query_param = 'page_size'
