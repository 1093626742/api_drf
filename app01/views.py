from django.shortcuts import render

# Create your views here.
from  rest_framework import views
from  . import models
from rest_framework import response
from rest_framework import serializers

class Bookserializers(serializers.ModelSerializer):
    name=serializers.CharField(max_length=10,error_messages={"max_length":"太长了"})
    class Meta:
        model=models.Book
        #fields= "__all__"
        fields= (
            "name",
            "date"
                 )


class BookView(views.APIView):
    def get(self,request):
        qs=models.Book.objects.all()
        print(qs)
        ser = Bookserializers(qs,many=True)
        # ser =Bookserializers(qs.first())
        return response.Response(
            {
                "code":0,
                "data":ser.data
            }
        )

    def post(self,request):
        ser=Bookserializers(data=request.data)
        print(ser)
        if ser.is_valid():
            instance=ser.save()
            print(instance)
            return response.Response({
                "code":0,
                "data":instance.pk
            }
            )
        else:
            return response.Response({
                "code":1,
                "data":ser.errors
            })


class BookDetailView(views.APIView):
    def put(self,request,pk):
        print(pk)
        instance=models.Book.objects.filter(pk=pk).first
        if not instance:
            return  response.Response({
                "code":1,
                "data":"数据不存在"
            })
        else:
            ser=Bookserializers(instance=instance,data=request.data)
            print(ser)
            if ser.is_valid():
                instance=ser.save()
                print("11")
                return response.Response({
                    "code":0,
                    "data":instance.pk
                })
            else:
                return response.Response({
                    "code":1,
                    "data":ser.errors

                })
    def delete(self,request):
        pass
