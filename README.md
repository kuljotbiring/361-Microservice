# CS361 Communication Contract

A. the data can be requested from the microservice using HTTP requests
(GET, POST, and DELETE). These HTTP request will connect with the
Flask app to take certain actions to add (city, state) names to a favorite list, delete selected
entries, delete all entries or retrieve the current list. using 
a localhost associated route on port 5000 which will trigger with the call. The routes are have intuitive names
as to their purpose and are as follows:
* /add/location          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;using POST
* /get_locations         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;using GET
* /delete_locations      &nbsp;&nbsp;&nbsp;&nbsp;using DELETE
* /clear_data            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;using DELETE

for add_location and delete_location
the city state should be formatted as follows:
data = {"city": city, "state": state}

example calls:
```
requests.post("http://localhost:5000/add_location", json=data)
requests.get("http://localhost:5000/get_locations")
requests.delete("http://localhost:5000/delete_location", json=data)
requests.delete("http://localhost:5000/clear_data")
```
B. the data is received from the microservice by making the GET request as shown above,
the Flask app route/function is triggered which loads a JSON object from a file
(which is keeping track of favorites) into a variable and returns it
using jsonify as a response. The client checks if the response is successful
and then stores it in a variable for use. Note that the favorites list is being stored
locally on a JSON file named locations.JSON which allows data persistence after the program
is closed

Client:
```
resposnse = requests.get("http://localhost:5000/get_locations")    
    if response.status_code == 200:
        locations = response.json()["locations"]
```
Server:
```
@app.route("/get_locations", methods=["GET"])
def get_locations():
    with open("locations.json", "r") as f:
        data = json.load(f)
        f.flush()
    # return the contents as JSON response
    return jsonify(data)
```
![Screenshot 2023-05-19 at 11 10 49 AM](https://github.com/kuljotbiring/361-Microservice/assets/34665034/2b07ad84-e4e1-4eef-aa8f-cc84ebbcb6a5)


