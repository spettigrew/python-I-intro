"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!). Dictionaries are a set of key:value pairs with key unique.

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [ # (waypoints is a list) a list of dictionaries vs. JS an array of objects. Instead of an object in JS, it's a dictionary.
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]
# [1, 2, 3, 4, 5]
# array = [1, 2, 3, 4, 5]
# array[1] #reference value. Calling index of 1 to get number 2. 
# print(array[1])

# integer = 0 #assign a variable to a value
# block = {
#         "lat": 43,
#         "lon": -122,
#         "name": "a third place"
#     }
# print(block["lat"])

# Add a new waypoint to the list - by using append(). Waypoints is the dictionary itself. Inside is the lists or values in the dictionary.
# YOUR CODE HERE
waypoints.append({"lat": 42, "lon": -120, "name": "made up place"})
print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
waypoints[0] = {"lon:": -130, "name": "not a place"}
print(waypoints[0])


# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
# values = waypoints.values()
# values

# for value in waypoints.values():
#     print(value)
# total_waypoints = 0
#for lat, lon, name in waypoints.values():

for values in waypoints:
    print(waypoints)

# for waypoints.values(["lat", "lon", "name"]):
# print(f'{lat} : {lon} : {name}')
