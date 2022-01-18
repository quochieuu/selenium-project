import json
from django.http.response import JsonResponse
from rest_framework import viewsets, mixins, status
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from .serializer import CreateDataSerializer
from .models import Data
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://phongtro123.com/?page=2")

total = []  

items = driver.find_elements_by_class_name("vip1")  
for item in items:
    name = item.find_element(By.XPATH,"//h3[@class='post-title']/a").text   
    address = item.find_element(By.XPATH,"//span[@class='post-location']/a").text   
    acreage =  item.find_element(By.XPATH,"//span[@class='post-acreage']").text 
    link =  ""  
    price =  item.find_element(By.XPATH,"//span[@class='post-price']").text 
    description = item.find_element(By.XPATH,"//p[@class='post-summary']").text 
    new = {'name':name, 'address': address, 'acreage': acreage, 'link': link, 'price': price, 'description': description}   
    total.append(new)   

driver.close()
print(total) 



# Create your views here.
class InsertDataViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CreateDataSerializer
    queryset = Data.objects.all()
    permission_classes = {}
    def get_queryset(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://phongtro123.com/")

        # tt = json.loads(total)
        for i in range(len(total)):
            for item in total:
                print(item)

            data = {
                'name': total[i]['name'],
                "address":total[i]['address'],
                "acreage": total[i]['acreage'],
                "link": total[i]['link'],
                "price": total[i]['price'],
                "description": total[i]['description']
            }

            # print(data)

            # product_serializer = CreateDataSerializer(data=data)
            # if product_serializer.is_valid():
            #     product_serializer.save()

        # print(data)

        return JsonResponse({
            'message': 'Update product information unsuccessful!',
            'data': data
        }, status=status.HTTP_400_BAD_REQUEST)
