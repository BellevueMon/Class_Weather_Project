import requests

welcome = input("Welcome to the Python Weather Report: Press Enter to Continue")

# making the request by city

def by_city():
    city = input('Please Enter Your City Name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&appid=00757d5b13aa6a6837cbb131fd3c2e90&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

# creating loop question

    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Thank you for checking the weather. Good Bye!")
        exit()

# making the request by zip

def by_zip():
    zip_code = str(input('Please Enter Your Zip code: '))
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=00757d5b13aa6a6837cbb131fd3c2e90'.format(zip_code)
    res = requests.get(url)
    data = res.json()
    show_data(data)

# creating loop question

    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes':
        main()
    if question == 'No':
        print("Thank you for checking the weather. Good Bye!")
        exit()

# This will display the weather information for the weather report.

def show_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))


# defining main function with while loop code to run the program

def main():
    while True:
        answer = input("\nWant to know the weather? Please type zip for zip code or city for city name: ")
        if answer == 'city':
            try:
                print("\nAlright, Connection established.")
                by_city()

            except Exception:
                print("\nhmm, You did not enter a valid name. Try again")
                by_city()
        if answer == 'zip':
            try:
                print("\nAlright, Connection established.")
                by_zip()

            except Exception:
                print("\nhmm, You did not enter a valid zip code numbers. Try again")
                by_zip()
        else:
            print("\nwell, that is not one of the options. Try again.")


main()