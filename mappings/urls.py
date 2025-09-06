from django.urls import path
from . import views

urlpatterns = [
    path('', views.MappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:pk>/', views.MappingDetailView.as_view(), name='mapping-detail'),
    path('patient/<int:patient_id>/', views.get_patient_doctors, name='patient-doctors'),
]
