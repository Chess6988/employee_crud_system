from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Employee
from .forms import EmployeeForm
from django.urls import reverse_lazy
from datetime import datetime

# Create Employee
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

# List Employees
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    

    def get_context_data(self, **kwargs):
        # Get the default context data (which includes the list of employees)
        context = super().get_context_data(**kwargs)
        # Add the current time to the context
        current_time = datetime.now().strftime('%Y-%m-%d')
        context['current_time'] = current_time
        return context
    

# View Employee Details
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'

# Update Employee
class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employee_list')

# Delete Employee
class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')



def home(request):
    return render(request, 'employees/home.html')


