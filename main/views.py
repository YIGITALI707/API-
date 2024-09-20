from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .models import Products,Cats
# Create your views here.



class ListAPIProducts(APIView):
    def get(self,requets):
        product=Products.objects.all()
        data=[]
        for i in product:
            data.append(
                {
                  "name":i.name,
                   "description":i.description,
                    "created_add":i.created_add,
                }
            )

        return Response(data)


class ListAPICats(APIView):
    def get(self,requets):
        cat=Cats.objects.all()
        data=[]
        for i in cat:
            data.append(
                {
                  "ism":i.ism,
                   "turi":i.turi,
                    "xususiyati":i.xususiyati,
                }
            )

        return Response(data)