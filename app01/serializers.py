from  rest_framework import views
from  . import models
from rest_framework import serializers

class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model=None

class BookView(views.APIView):
    def get(self,request):
        qs=models.Book.objects.all()
        print(qs)
