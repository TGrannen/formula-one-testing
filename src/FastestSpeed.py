from matplotlib import pyplot as plt
import fastf1.plotting
import fastf1
from prettytable import PrettyTable


def sortBySpeed(e):
    return e[2]


fastf1.plotting.setup_mpl()

session = fastf1.get_session(2023, 'Brazil', 'SS')
session.load()
cars = []
for (carNumber, data) in session.car_data.items():
    name = session.get_driver(carNumber).FullName
    cars.append((carNumber, name, data['Speed'].max()))


cars.sort(reverse=True, key=sortBySpeed)

x = PrettyTable()
x.field_names = ["Car Number", "Name", "Top Speed"]
x.add_rows(cars)
print(x)
