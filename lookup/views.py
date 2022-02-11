from django.shortcuts import render


# Create your views here.

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST["zipcode"]
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=11C8A1F0-5E06-447B-95CB-BB5B0E88E8C1")
        try:
            api = json.loads(api_request.content)
        except:
            api = "Error.."
    else:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=11C8A1F0-5E06-447B-95CB-BB5B0E88E8C1")
        try:
            api = json.loads(api_request.content)
        except:
            api = "Error.."
    if api[0]['Category']['Name'] == "Good":
        category_description = "Air quality is satisfactory, and air pollution poses little or no risk."
        category_color = "good"
    elif api[0]["Category"]["Name"] == "Moderate":
        category_description = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
        category_color = "moderate"
    elif api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
        category_description = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
        category_color = "usg"
    elif api[0]["Category"]["Name"] == "Unhealthy":
        category_description = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
        category_color = "unhealthy"
    elif api[0]["Category"]["Name"] == "Very Unhealthy":
        category_description = "Health alert: The risk of health effects is increased for everyone."
        category_color = "veryunhealty"
    elif api[0]["Category"]["Name"] == "Hazardous":
        category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
        category_color = "hazardous"
    else:
        category_description = "Couldn't find.."
    return render(request, "lookup/home.html",
                  {"api": api, "category_description": category_description, "category_color": category_color})


def about(request):
    return render(request, "lookup/about.html", {})
