# customer/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest

@login_required
def customer_dashboard(request):
    """
    This view renders the customer dashboard, showing all service requests for the logged-in customer.
    """
    requests = ServiceRequest.objects.filter(user=request.user)  # Filter by the logged-in user
    return render(request, 'customer/customer_dashboard.html', {'requests': requests})

# customer/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

@login_required
def create_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)  # Don't forget to include request.FILES here
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('customer_dashboard')
        else:
            print(form.errors)  # Debugging: check form errors
    else:
        form = ServiceRequestForm()

    return render(request, 'customer/create_request.html', {'form': form})



