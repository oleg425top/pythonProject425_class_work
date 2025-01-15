class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackVehicle]:
        print(issubclass(cls1, cls2), end='\t')
    print()