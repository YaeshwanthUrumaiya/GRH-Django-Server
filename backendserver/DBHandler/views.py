from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# from django.utils import timezone
# from datetime import datetime
# import pytz

from DBHandler.models import GameUserData
from DBHandler.serializers import GameUserDataSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def DBTest(request):
    if request.method == 'GET':
        return JsonResponse("DB API Working(GET)", safe = False)
    if request.method == 'PUT':
        return JsonResponse("DB API Working(PUT)", safe = False)
    if request.method == 'DELETE':
        return JsonResponse("DB API Working(DELET)", safe = False)

@api_view(['POST'])
def AddData(request):
    JsonFormate = JSONParser().parse(request)
    print(JsonFormate)
    serializer = GameUserDataSerializer(data=JsonFormate)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Added", safe=False)
    return JsonResponse("Error in POST", safe=False, status = 400)

@api_view(['GET'])
def GetData(request):
    modeldata = GameUserData.objects.all()
    serializer_data = GameUserDataSerializer(modeldata, many = True)
    return JsonResponse(serializer_data.data, safe = False)

@api_view(["GET"])
def GetUserData(request):
    queryset = GameUserData.objects.all()
    if ('UserName' in request.data):
        queryset = queryset.filter(UserName=request.data['UserName'])
    if ('GameName' in request.data):
        queryset = queryset.filter(GameName=request.data['GameName'])
    queryset = queryset.order_by('-DateTime')

    serializer_data = GameUserDataSerializer(queryset, many = True)
    return JsonResponse(serializer_data.data, safe = False)