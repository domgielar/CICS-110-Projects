# Author   : Dominik Gielarowiec    
# Email    : dgielarowiec@umass.edu
# Spire ID : 35150500


def stop(traffic_light, pedestrian):
    return traffic_light == "Red" or pedestrian

def move_forward(traffic_light, pedestrian):
    return traffic_light != "Red" and (not pedestrian)

def turn_left(traffic_light, pedestrian, cars_opposite):
    return traffic_light == "Green" and (not pedestrian) and (not cars_opposite)
