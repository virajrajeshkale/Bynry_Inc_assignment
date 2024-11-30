import django_filters
from customer.models import ServiceRequest  # Ensure this import is correct

class ServiceRequestFilter(django_filters.FilterSet):
    request_type = django_filters.ChoiceFilter(choices=ServiceRequest.REQUEST_TYPE_CHOICES, label="Request Type")
    status = django_filters.CharFilter(lookup_expr='icontains', label="Status")
    created_at = django_filters.DateFromToRangeFilter(label="Created Date")

    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'status', 'created_at']
