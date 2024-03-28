from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer
from .models import Person
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail

class PersonAPI(APIView):
    def get(self, request, pk=None):
        obj = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            person = serializer.save()
            subject = 'Registerd Successfully!'
            message = 'Thank You for registering with us!'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [person.email])
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        obj = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            subject = 'Person Updated Successfully!'
            message = 'Your Credentials were updated with us.'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [obj.email])
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        obj = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer.save()
            subject = 'Person Updated Successfully!'
            message = 'Your Credentials were updated with us.'
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, [obj.email])
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        obj = get_object_or_404(Person, pk=pk)
        subject = 'Deleted Successfully!'
        message = 'We will love to see you again.'
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, [obj.email])
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)