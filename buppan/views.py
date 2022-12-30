from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import render
import requests
import json

SEARCH_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&applicationId=1041325084269081277'


def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    result = json.loads(api)
    items = []
    print(result)
    if not 'error' in result:
        items = result['Items']
    return items


# Create your views here.
class ProductSearchView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = self.request.data
        name = data["name"]
        product_data = Stock.objects.filter(name=name)
        res = {}
        if stock_data.exists():
            stock_data = stock_data[0]
            res = {
                "name": stock_data.name,
                "content": stock_data.content,
                "id": stock_data.id
            }

        return Response(res, status=status.HTTP_200_OK)

class EbaycircleView(View):
    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST or None)

        if form.is_valid():
            keyword = form.cleaned_data['title']
            params = {
                'keyword': keyword,
                # 'sort' : '+itemPrice',
                'hits' : 10,
                'imageFlag' : 1
            }
            items = get_api_data(params)
            product_data = []
            for i in items:
                item = i['Item']
                # print(item)
                image = item['mediumImageUrls'][0]['imageUrl']
                itemName = item['itemName']
                itemPrice = item['itemPrice']
                query = {
                    'image': image,
                    'itemName' : itemName,
                    'itemPrice' : itemPrice,
                }
                product_data.append(query)

            product_data=sorted(product_data,key=lambda x: x['itemPrice'])

            return render(request, 'api/ebay_circle_result.html', {
                'product_data': product_data[0],
                'keyword': keyword
            })

        return render(request, 'api/ebay_circle.html', {
            'form': 'form'
        })