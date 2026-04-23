from sensor_module import RoomSensor

Kitchen = RoomSensor("Kitchen", 31, 72, 180)
Bedroom = RoomSensor("Bedroom", 32, 75, 99)
Balcony = RoomSensor("Balcony", 37, 58, 189)

sensors = [Kitchen, Bedroom, Balcony]

comfortable_count = 0
normal_count = 0
warning_count = 0

for sensor in sensors:
    # Get the comfort level using the method
    status = sensor.comfort_level()
    
    # Use conditionals to count categories
    if status == "Comfortable":
        comfortable_count += 1
    elif status == "Normal":
        normal_count += 1
    elif status == "Warning":
        warning_count += 1

print(f"Comfortable: {comfortable_count}")
print(f"Normal: {normal_count}")
print(f"Warning: {warning_count}")
