# It is easier to ask for forgiveness than permission

class student:
    def study(self):
        print("The Student is studying")
    def relax(self):
        print("The Student is relaxing")

class professional:
    def work(self):
            print("The Professional is working")
    def relax(self):
        print("The Professional is relaxing")

def action(person):
    try:
        person.relax()
        person.study()
    except AttributeError:
        print("Must Be a student")

student = student()
action(student)

prof = professional()
action(prof)

# =============================== Another use case =========================#

# laptop = {'ram':16, 'ssd':512, 'Mic':False}
laptop = {'ram':16, 'ssd':512}

try:
    print(f"The laptop has {laptop['ram']} gb ram and {laptop['ssd']} gb ssd and mic {laptop['Mic']}")
except KeyError as e:
    print(f"{e} key is missing")

