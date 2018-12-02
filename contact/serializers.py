from rest_framework import serializers
from contact.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','created', 'name', 'email', 'subject', 'message', 'client_ip', 'is_read')