from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from .serializers import StockSerializer
from .models import Stock
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render

import requests
import json

api = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json?date={target}"


def corporate_officer_list(request):
    return render(request, 'edinet/corporate_officer_list.html', {})


def call_edinet_api(request):

    url = api.format(target="2018-06-19")
    r = requests.get(url)
    data = json.loads(r.text)
    print("+ メタデータ=", data["metadata"])

    return render(request, 'edinet/corporate_officer_list.html', {})


class StockView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (AllowAny,)


class StockDetailView(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (AllowAny,)


class StockSearchView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = self.request.data
        name = data["name"]
        stock_data = Stock.objects.filter(name=name)
        res = {}
        if stock_data.exists():
            stock_data = stock_data[0]
            res = {
                "name": stock_data.name,
                "content": stock_data.content,
                "id": stock_data.id
            }

        return Response(res, status=status.HTTP_200_OK)
