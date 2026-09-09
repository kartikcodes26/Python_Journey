from collections import namedtuple

labels = namedtuple('Marks', ['English', 'Maths', 'Physics'])
student = labels(Maths=34, English=50, Physics=99)
print(student.Maths)
print(student.English)
print(student.Physics)

