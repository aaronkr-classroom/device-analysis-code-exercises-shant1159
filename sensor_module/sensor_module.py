class RoomSensor:
    def __init__(self, name : str,temperature :float, humidity : float, light : float):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def show_info(self):
        print(f"Sensor: {self.name}\nTemperature: {self.temperature}\nHumidity: {self.humidity}\nLight: {self.light}")

    def comfort_level(self):
        if (self.temperature>20 and self.temperature <26 ) and (self.humidity >40 and self.humidity<60):
            return "Comfortable"
        elif (self.temperature>=20 ) and (self.humidity >=70):
            return "Warning"
        else:
            return "Normal"
            
    def light_status(self):
        if self.light > 200 :
            return "Dark"
        elif self.light <=200:
            return "Bright"

Kitchen = RoomSensor("Kitchen",31,72,180)
Bedroom = RoomSensor("Bedroom",32,75,99)
Balcony = RoomSensor("Balcony",37,58,189)

sensors = [Kitchen, Bedroom, Balcony]

for sensor in sensors:
    sensor.show_info()
    print(f"Comfort Level: {sensor.comfort_level()}")
    print(f"Light Status: {sensor.light_status()}")
    print("-" * 50)