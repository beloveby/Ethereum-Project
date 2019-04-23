from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from pools.models import Pool
from pools.serializers import PoolSerializer


@csrf_exempt
def pool_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        pools = Pool.objects.all()
        serializer = PoolSerializer(pools, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PoolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def pool_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        pool = Pool.objects.get(pk=pk)
    except Pool.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PoolSerializer(pool)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PoolSerializer(pool, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pool.delete()
        return HttpResponse(status=204)