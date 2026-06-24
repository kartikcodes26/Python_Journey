laptop = {
    "Ram": 16,
    "Storage": 512,
    "Storage_type": "SSD",
    "Processor": "Intel i5",
    "Display": "LCD",
    "Backlit": True,
    16: 17
}

print(laptop["Storage"])
print(laptop["Display"])
print(laptop["Processor"])


laptop["Ram"] = 32
laptop["Storage"] = 1024

print(laptop)

# .get() the safety net

ram = laptop.get("Ram", 0) # If found ram, return its value, else reutrn 0
print(ram)
camera = laptop.get("Camera", -1)
print(camera)
trackpad = laptop.get("Trachpad") # Reruen None if not found
print(trackpad)

nothing = None
print(nothing)