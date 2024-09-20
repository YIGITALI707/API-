from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class News:
    def __init__(self,title,content):
        self.title=title
        self.content=content

a=News('Zo‘ravonlik, samosud va qo‘rquv mashinasi bilan xodimlarni ishlatish qadriyatga aylangan',"O‘tgan hafta oxirida sodir bo‘lgan Inbazar do‘konlari tarmog‘ida yosh xodimga nisbatan o‘ta qo‘pol munosabat, zo‘ravonlik va samosud jamoatchilikning keskin g‘azabini qo‘zg‘atdi.")



class NewsSerializers(serializers.Serializer):
    title=serializers.CharField(max_length=150)
    content=serializers.CharField()


def json():
    serializers=NewsSerializers(a)
    print(serializers.data)

    json=JSONRenderer().render(serializers.data)
    print(json)




class Products:
    def __init__(self,name,description):
        self.name=name
        self.description=description

a=Products( "Rolls-Royce Ghost","The latest presentation event by Suzuki dealers in France lifted the veil of updated S-Cross surface. The first images of what a facelifted crossover would look like were revealed online, and they are…too blurred to get all the details")



class ProductsSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=150)
    description=serializers.CharField()



def json():
    serializers=ProductsSerializers(a)
    print(serializers.data)

    json=JSONRenderer().render(serializers.data)
    print(json)