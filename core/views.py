from django.shortcuts import render
import requests
variables = ['Make', 'Model', 'Model Year', 'Series', 'Plant Country', 'Body Class', 'Transmission Style', 'Engine Number Of Cylinders', 'Displacement (L)', 'Fuel Type - Primary', 'Turbo', 'Other Restraint System Info', 'Front Air Bag Locations', 'Knee Air Bag Locations', 'Side Air Bag Locations']
# Create your views here.

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact.html')
    

def magazine_list(request):
    return render(request, 'magazine-list.html')


def parts_select(request):
    return render(request, 'parts-select.html')


def result(request):
    res = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{request.GET.get("vin")}?format=json')
    resp = res.json()
    data = []
    for item in resp["Results"]:
        if item["Variable"] in variables:
            data.append({
                'variable': item["Variable"],
                'value':item["Value"]
            })
    name = f'{data[0]["value"]} {data[1]["value"]}'
    context = {
        'data': data,
        'name': name,
        'vin': request.GET.get("vin"),
        'engine': data[7]["value"],
        'year': data[2]["value"],
        'body': data[5]["value"],
        'image': f'https://raw.githubusercontent.com/filippofilip95/car-logos-dataset/master/logos/optimized/{data[0]["value"].lower()}.png'
    
    }
    print(name)
    return render(request, 'result.html', context)