import requests
import smtplib

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "650e4f74ee8376464a1a8c29ec21cf10"
my_email = 'ziriamanda@gmail.com'
password = 'qtnydxglyshyfcex'


lat = 44.106701
lon = 9.829260

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)
print(data["list"][0]["weather"][0]["id"])
print(data["list"][0]["weather"][0]["description"])

weather_code_list = []

will_rain = False
for i in range(0, 4):
    weather_id = data["list"][i]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure connection and encrypt email
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="siriamandaraaf@gmail.com",
                            msg=f"Subject:Rain Alert \n\n It is going to rain today. Remember to bring an umbrella.")
