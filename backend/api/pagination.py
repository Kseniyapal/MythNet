from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Пагинация, 10 элементов на странице"""

    page_size_query_param = 'limit'
    page_size = 10
