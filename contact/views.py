from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from contact.models import Contact
from contact.serializers import ContactSerializer
from contact.permissions import has_permission
from contact.utils import get_client_ip
# Create your views here.

@api_view(['GET'])
@ensure_csrf_cookie
def ensure_csrf(request):
    return Response(status=status.HTTP_200_OK)

# class ContactList(APIView):
#     permission_classes = (has_permission, )
#     def get(self, request, format=None):
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         request.data['is_read'] = False
#         request.data['client_ip'] = get_client_ip(request)
#         serializer = ContactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ContactList(generics.ListCreateAPIView):
    permission_classes = (has_permission, )
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(is_read=False, client_ip=get_client_ip(self.request))

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAdminUser, )