laptop = {'ram':16, 'ssd':512}

try:
    print(f"The laptop has {laptop['ram']} gb ram and {laptop['ssd']} gb ssd and mic {laptop['Mic']}")
except KeyError as e:
    print(f"{e} key is missing")