import requests
import time

API_KEY = 'aff7e5bea63b4d9aa32120512240701'
weather_endpoint = 'https://api.weatherapi.com/v1/current.json'

def get_weather(api_key, city):
    weather_params = {
        'key': api_key,
        'q': city
    }

    try:
        response = requests.get(weather_endpoint, params=weather_params)
        weather_data = response.json()

        if 'error' in weather_data:
            print(f"Error: {weather_data['error']['message']}")
        else:
            current_condition = weather_data['current']
            location = weather_data['location']

            print(f"Weather in {location['name']}, {location['region']}, {location['country']}")
            print(f"Temperature: {current_condition['temp_c']}°C")
            print(f"Condition: {current_condition['condition']['text']}")
            print(f"Wind Speed: {current_condition['wind_kph']} km/h")
            print(f"Humidity: {current_condition['humidity']}%")

    except requests.RequestException as e:
        print(f"Error making API request: {e}")

def display_favorite_list(favorite_list):
    print("Favorite Cities:")
    for city in enumerate(favorite_list, start=1):
        print(f"{city}")

def add_to_favorite(favorite_list, city):
    if city not in favorite_list:
        favorite_list.append(city)
        print(f"{city} added to favorites.")
    else:
        print(f"{city} is already in favorites.")

def remove_from_favorite(favorite_list, index):
    try:
        removed_city = favorite_list.pop(index)
        print(f"{removed_city} removed from favorites.")
    except IndexError:
        print("Invalid index. Please provide a valid index from the favorites list.")

def main():
    favorite_cities = []
    auto_refresh_enabled = False

    while True:
        print("\n=== Weather Checking Application ===")
        print("1. Check weather by city")
        print("2. Manage favorite cities")
        print("3. Toggle auto-refresh")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            city_name = input("Enter city name: ")
            get_weather(API_KEY, city_name)

        elif choice == '2':
            print("\n=== Manage Favorite Cities ===")
            display_favorite_list(favorite_cities)
            print("1. Add city to favorites")
            print("2. Remove city from favorites")
            print("3. Back")

            manage_choice = input("Enter your choice (1-3): ")

            if manage_choice == '1':
                city_name = input("Enter city name to add to favorites: ")
                add_to_favorite(favorite_cities, city_name)

            elif manage_choice == '2':
                display_favorite_list(favorite_cities)
                index = input("Enter the index to remove from favorites: ")
                remove_from_favorite(favorite_cities, int(index) - 1)

            elif manage_choice == '3':
                continue

        elif choice == '3':
            auto_refresh_enabled = not auto_refresh_enabled
            print(f"Auto-refresh {'enabled' if auto_refresh_enabled else 'disabled'}.")

        elif choice == '4':
            print("Exiting the Weather Checking Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        if auto_refresh_enabled:
            time.sleep(15)

if __name__ == "__main__":
    main()