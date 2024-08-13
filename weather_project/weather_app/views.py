from django.shortcuts import render, redirect
import requests
import datetime
def index(request):
    error_message = None 
    if request.method == 'POST':
        city = request.POST.get('city', 'India')
    else:
        city = 'India'

    Apikey = '23162c1c558ac47bc541ef468a735ad0'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': Apikey, 'units': 'metric'}
    
    
    try:
        r = requests.get(url=URL, params=PARAMS)
        r.raise_for_status()  # Raises HTTPError for bad responses
        res = r.json()

        if res.get('cod') != 200:
            error_message = "City not found. Please enter a valid location."
            description = "N/A"
            icon = ""
            temp = "N/A"
            wind = "N/A"
            pressure = "N/A"
            humidity = "N/A"
        else:
            description = res['weather'][0]['description']
            icon = res['weather'][0]['icon']
            temp = res['main']['temp']
            wind = res['wind']['speed']
            pressure = res['main']['pressure']
            humidity = res['main']['humidity']
    except requests.RequestException as e:
        print(f"Request error: {e}")
        error_message = "There Is An Error! Please Add Valid Data."
        description = "N/A"
        icon = ""
        temp = "N/A"
        wind = "N/A"
        pressure = "N/A"
        humidity = "N/A"

    day = datetime.date.today()
    
    return render(request, "index.html", {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'wind':wind,'humidity':humidity,'pressure':pressure,'error_message': error_message})

