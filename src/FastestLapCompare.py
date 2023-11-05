from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting

fastf1.plotting.setup_mpl()

session = fastf1.get_session(2023, 'Brazil', 'Q')

session.load()
lec_car_data = session.laps.pick_driver('LEC').pick_fastest().get_car_data()
nor_car_data = session.laps.pick_driver('NOR').pick_fastest().get_car_data()

# The rest is just plotting
fig, ax = plt.subplots()
ax.plot(lec_car_data['Time'], lec_car_data['Speed'], label='LEC')
ax.plot(nor_car_data['Time'], nor_car_data['Speed'], label='NOR')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Leclerc/Norris')
ax.legend()
plt.show()
