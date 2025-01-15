class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackVehicle(LandVehicle):
    pass

my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_track_vehicle = TrackVehicle

for obj in [my_vehicle, my_land_vehicle, my_track_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackVehicle]:
        print(isinstance(obj, cls), end='\t')
    print()