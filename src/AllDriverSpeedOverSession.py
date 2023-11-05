from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2023, 'Brazil', 'SS')

session.load()
lec_car_data = session.car_data
# The rest is just plotting
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Fast')
ax.legend()


# For each race in the season
for (carNumber, data) in session.car_data.items():
    ax.plot(data['Time'], data['Speed'], label=carNumber)

plt.show()
