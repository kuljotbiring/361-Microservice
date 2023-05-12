import requests


def add_location():
    # get user input
    city = input("Please enter the city to add: ")
    state = input("Please enter the state to add: ")

    data = {"city": city, "state": state}

    # make a get request to the URL of the Flask server using GET method
    response = requests.post("http://localhost:5000/add_location", json=data)

    # check the response from the server. print it if valid - otherwise show error
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")


def delete_location():
    city = input("Please enter the city to delete: ")
    state = input("Please enter the state to delete: ")

    data = {"city": city, "state": state}

    response = requests.delete("http://localhost:5000/delete_location", json=data)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")


def get_locations():
    # retrieve a JSON response for the current list of
    response = requests.get("http://localhost:5000/get_locations")

    if response.status_code == 200:
        locations = response.json()["locations"]
        for place in locations:
            print(place)
    else:
        print(f"Error: {response.status_code}")


def clear_data():
    response = requests.delete("http://localhost:5000/clear_data")

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")


while True:
    print("\nPlease choose from one of the following options:")
    print("1: Add a city, state to the favorites list")
    print("2: Delete a city, state to the favorites list")
    print("3: View the favorites list")
    print("4: Clear the favorites list")
    print("5: Exit Program")

    user_choice = input("\nPlease enter the number from the selection above: ")

    if user_choice == "1":
        add_location()
    elif user_choice == "2":
        delete_location()
    elif user_choice == "3":
        get_locations()
    elif user_choice == "4":
        clear_data()
    elif user_choice == "5":
        exit(0)
    else:
        print("\nInvalid choice. Please try again!")

