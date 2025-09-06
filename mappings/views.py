from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingListSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(assigned_by=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PatientDoctorMappingListSerializer
        return PatientDoctorMappingSerializer

class MappingDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientDoctorMappingSerializer
    
    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(assigned_by=self.request.user)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_patient_doctors(request, patient_id):
    mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id, assigned_by=request.user)
    serializer = PatientDoctorMappingListSerializer(mappings, many=True)
    return Response(serializer.data)
