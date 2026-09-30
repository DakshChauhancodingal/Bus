class vehicle:
    def __init__(self,name,speed,mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage
class bus(vehicle):
    pass
obj=bus("super volvo",130,23)
print("Name",obj.name,
      "speed",obj.speed,
      "mileage",obj.mileage)

    