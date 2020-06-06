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

waypoints = [
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

# Add a new waypoint to the list
# YOUR CODE HERE
new_waypoints = [{"lat": 42, "lon": -120, "name": "made up place"}]
print(new_waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
mod_waypoints = [{"lon:": -130, "name": "a place"}] 
print(mod_waypoints)

no_place = "not a real place"
for lon, name in no_place:
    print(f'{lon} : {name}')

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
total_waypoints = 0

for lat, lon, name in dict.items(lat, lon, name):
    print(f'{lat} : {lon} : {name}')

# x = waypoints.get("lat", "lon", "name")