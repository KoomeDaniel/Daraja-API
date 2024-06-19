from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView
# from rest_framework.permissions import IsAdminUser

from mpesa.models import LNMonline
from mpesa.api.serializers import LNMonlineSerializer

class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMonline.objects.all()
    serializer_class = LNMonlineSerializer
    # permission_classes = [IsAdminUser]

    def create(self,request):
        print(request.data,"This is request.data")