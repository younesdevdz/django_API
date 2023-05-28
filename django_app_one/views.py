from django.shortcuts import render
from django.http import JsonResponse 
from .models import Reporting , Intervention , Breakdown
from rest_framework.decorators import api_view
from .serializers import BreakdownSerializer, ReportingSerilalizer
from rest_framework import status , filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics , mixins , viewsets
# Create your views here.
def no_rest (request):
    breakdwons = [

        {
            'tag' : "cr201",
            'machine' :'tc201'
            },
         {
            'tag' : "cr201",
            'machine' :'tc201'
        }
    ]
    return JsonResponse (breakdwons , safe=False)


# methode 2
def no_rest_module (request):
    data = Breakdown.objects.all()
    response = {
        'breakdowns' : list(data.values('tag' , 'machine'))
    }
    return JsonResponse (response)

# methode3 FBV
@api_view(["GET" , "POST"])
def FBV_List (request):
    if request.method == "GET" :
        breakdowns = Breakdown.objects.all()
        serlializer = BreakdownSerializer(breakdowns , many = True)
        return Response(serlializer.data)
    
    elif request.method  == "post":
        serlializer = BreakdownSerializer(data= request.data)
        if serlializer.is_valid :
            serlializer.save()
            return Response(serlializer.data , status = status.HTTP_201_CREATED)
        return Response(serlializer.data , status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET' ,'PUT' , 'DELETE'])  
def FBV_ID(request , id) :
    try :
        breakdown = Breakdown.objects.get(id= id)
    except  Breakdown.DoesNotExist :
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method == "GET" :  
        serializer = BreakdownSerializer(breakdown)
        return Response(serializer.data)
    
    elif request.method  == "PUT":
        serializer = BreakdownSerializer(data= request.data)
        if serializer.is_valid :
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.data , status = status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        breakdown.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


# CBV methode

# GET & POST
class CBV_List(APIView):
    def get(self , request):
        breakdown = Breakdown.objects.all()
        serializer = BreakdownSerializer(breakdown , many = True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = BreakdownSerializer(data= request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)
class CBV_ID (APIView):
    def get_object(self , id):
        try :
            return Breakdown.objects.get(id= id)
        except Breakdown.DoesNotExist:
            raise Http404

    def get(self , request , id):
        breakdown = self.get_object(id)
        serializer = BreakdownSerializer(breakdown)
        return Response(serializer.data)
    
    def put(self , request , id):
        breakdown = self.get_object(id)
        serializer = BreakdownSerializer(breakdown , data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    def delete(self , request , id):
       breakdown = self.get_object(id)
       breakdown.delete()
    
       return Response(status=status.HTTP_204_NO_CONTENT)
    
    # mixins

class Mixin_List (mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,):
    queryset = Breakdown.objects.all()
    serializer_class = BreakdownSerializer

    def get(self , request):
        return self.list(request)
    def post(self ,request):
        return self.create(request)
    
class mixins_id(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Breakdown.objects.all() 
    serializer_class = BreakdownSerializer
    def get(self , request , pk):
        return self.retrieve(request)
    def put(self ,request , pk):
        return self.update(request)
    def delete(self ,request , pk):
        return self.destroy(request)
    
# generics 

class generics_list(generics.ListCreateAPIView):
    queryset = Breakdown.objects.all()
    serializer_class = BreakdownSerializer
   
    # permission_classes = [IsAuthenticated]

#6.2 get put and delete 
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breakdown.objects.all()
    serializer_class = BreakdownSerializer 
    

# viewset

class viewsets_Breakdown(viewsets.ModelViewSet):
    queryset = Breakdown.objects.all()
    serializer_class = BreakdownSerializer
    filter_backends =[filters.SearchFilter]
    search_fields = ["tag"]

class viewsets_reporting (viewsets.ModelViewSet):
    queryset = Reporting.objects.all()
    serializer_class = ReportingSerilalizer


@api_view(["GET"])
def find_breakdown (request):
    #breakdown = Breakdown.objects.filter(
    #    tag = request.data['tag'],
    #    )
    #serializer = BreakdownSerializer (breakdown, many= True)
    #return Response(serializer.data)

    if 'tag' in request.data:
        breakdown = Breakdown.objects.filter(tag=request.data['tag'])
        serializer = BreakdownSerializer(breakdown, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'tag not found in request data'})



    
        
        

    
