from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from customer.models import ServiceRequest  # Import from customer.models
from .filters import ServiceRequestFilter

@login_required
def support_dashboard(request):
    # Check the available fields of the model
    print("ServiceRequest fields:", [f.name for f in ServiceRequest._meta.get_fields()])

    filter = ServiceRequestFilter(request.GET, queryset=ServiceRequest.objects.all())
    service_requests = filter.qs  # Get filtered service requests

    total_requests = service_requests.count()
    pending_requests = service_requests.filter(status='Pending').count()
    completed_requests = service_requests.filter(status='Completed').count()

    context = {
        'filter': filter,
        'service_requests': service_requests,
        'total_requests': total_requests,
        'pending_requests': pending_requests,
        'completed_requests': completed_requests,
    }

    return render(request, 'support/support_dashboard.html', context)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from customer.models import ServiceRequest

@login_required
def assign_request(request, request_id):
    """
    This view allows support agents to assign or update the status of a service request.
    Only authenticated support users should have access to this view.
    """
    service_request = get_object_or_404(ServiceRequest, id=request_id)

    if request.method == 'POST':
        service_request.status = request.POST.get('status', service_request.status)
        service_request.save()

        return redirect('support_dashboard')  # Redirect to the support dashboard after updating

    return render(request, 'support/assign_request.html', {'service_request': service_request})
