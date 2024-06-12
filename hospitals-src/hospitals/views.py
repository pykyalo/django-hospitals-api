from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import HospitalsFilter
from .models import Hospital
from .serializers import HospitalSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    filterset_class = HospitalsFilter
    filter_backends = (DjangoFilterBackend,)

    @action(detail=False, methods=["get"])
    def total_bed_capacity(self, request):
        bed_capacity = Hospital.objects.aggregate(bed_capacity=Sum("beds"))
        return Response(bed_capacity)

    @action(detail=False, methods=["get"])
    def province_beds_capacity(self, request):
        province_beds_capacity = Hospital.objects.values("province_name").annotate(
            bed_capacity=Sum("beds")
        )
        return Response(province_beds_capacity)

    @action(detail=False, methods=["get"])
    def closest_hostpitals(self, request):
        """
        Get Hospitals that are at least 3km away from the given point
        :param request: GET request
        """
        longitude = request.query_params.get("lo")
        latitude = request.query_params.get("la")

        if longitude and latitude:
            point = Point(float(longitude), float(latitude), srid=4326)
            closest_hospitals = Hospital.objects.filter(
                geom__distance_lte=(point, D(km=8))
            )
            serializer = self.get_serializer_class()
            serialized_hospitals = serializer(closest_hospitals, many=True).data
            return Response(serialized_hospitals, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_bad_request)
