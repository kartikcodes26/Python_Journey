import json

class laptop:
    # Place Store all instances of the class
    laptops = []
    count = 0

    def __init__(self, name, ram, rom):
        self.name = name
        self.ram = ram
        self.rom = rom

        # Store the particular instance of the class
        laptop.laptops.append(self)
        laptop.count += 1

    @classmethod
    def getlaptops(cls):
        for ele in cls.laptops:
            print(f"{ele.name}, {ele.ram}, {ele.rom}")

    @classmethod
    def export(cls):
        duplicates = 0

        # In order to append, first get the old data already there
        # First store all the names that are already in the json
        unique_names = set()

        with open("laptops_Export.json", 'r') as f:
            # Read laptop names from the file as we dont want to append them again
            # If the file is empty
            if f.read().strip():
                old_data = json.load(f)
                for ele in old_data:
                    unique_names.add(ele['Name'])
            else:
                old_data = []

        # To store the jsonised version of our data that is not already in the json file
        laptop_json = []

        # Store the jsonised version ignoring dublicates
        for ele in cls.laptops:
            if not ele.name in unique_names:
                laptop_json.append({
                    "Name": ele.name,
                    "Ram": ele.ram,
                    "Rom": ele.rom
                })
                # Another unique name found
                unique_names.add(ele.name)
            else:
                duplicates += 1

        # Appending the new data
        old_data.extend(laptop_json)

        # Finally dumping the new data
        with open("laptops_Export.json", 'w') as f:
            json.dump(old_data, f,indent=4)

        # Log
        if duplicates:
            print(f"Found {duplicates} duplicate values")

        if cls.count - duplicates == 0:
            print("Export of no object is done")
        else:
            print(f"Export of {abs(cls.count - duplicates)} objects is done")


l1 = laptop("asus", 16, 512)
l2 = laptop("apple", 8, 256)
l3 = laptop("lenovo", 24, 1024)

# laptop.getlaptops()

laptop.export()
