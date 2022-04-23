import json
import os

from django.conf import settings
from django.shortcuts import render
from .models import AddModel
from .main import RecommendationEngine


import pandas as pd



def home(request):
    return render(request, 'home.html')

def add(request):
    return render(request,'add.html')


#CREATE
def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        items = name.split(" ")
        for item in items:
            obj = AddModel()
            obj.description = item
            obj.save()
    return render(request,'home.html')

#DELETE
def delete(request,id):
    obj = AddModel.objectHandler.get(id=id)
    obj.delete()
    return render(request, 'home.html')

def cook(request):
    df = pd.read_csv("../top_ten_possible_recipes.csv")
    df.drop(['Category'], axis=1)
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'cook.html', context)

def recommendations(request):
    base_directory = settings.BASE_DIR
    csv_file =os.path.join(base_directory, "original_recipes_dataset.csv")
    recommendation = RecommendationEngine(csv_file)

    dataframe = recommendation.recommend_recipes()
    json_records = dataframe.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'recom.html', context)