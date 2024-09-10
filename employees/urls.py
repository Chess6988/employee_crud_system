from django.urls import path
from .views import create_employee, EmployeeListView, EmployeeDetailView, EmployeeUpdateView, EmployeeDeleteView,  home 

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('new/', create_employee, name='employee_create'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('home/', home, name='home'),
]
