#!/usr/bin/env python3

from rocketpy import Environment, SolidMotor, Rocket, Flight
import datetime


# return environment class
def setEnvironment():
  #set location
  env = Environment(latitude=39.01549201631338, longitude=-105.71103788653403, elevation=2962) # Hartsel Launch Site

  # set date
  tomorrow = datetime.date.today() + datetime.timedelta(days=1)
  env.set_date(
      (tomorrow.year, tomorrow.month, tomorrow.day, 12)
  )  # Hour given in UTC time

  # get and display weather forecast
  env.set_atmospheric_model(type="Forecast", file="GFS")
  # print(env.info()) # print

  return env

def main():
  env = setEnvironment()

  print("Environment Setup Complete.\n")

  Pro75M1670 = SolidMotor(
    thrust_source="Cesaroni_M1670.eng",
    dry_mass=1.815,
    dry_inertia=(0.125, 0.125, 0.002),
    nozzle_radius=33 / 1000,
    grain_number=5,
    grain_density=1815,
    grain_outer_radius=33 / 1000,
    grain_initial_inner_radius=15 / 1000,
    grain_initial_height=120 / 1000,
    grain_separation=5 / 1000,
    grains_center_of_mass_position=0.397,
    center_of_dry_mass_position=0.317,
    nozzle_position=0,
    burn_time=3.9,
    throat_radius=11 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
  )

  calisto = Rocket(
    radius=127 / 2000,
    mass=14.426,
    inertia=(6.321, 6.321, 0.034),
    power_off_drag="powerOffDragCurve.csv",
    power_on_drag="powerOnDragCurve.csv",
    center_of_mass_without_motor=0,
    coordinate_system_orientation="tail_to_nose",
  )

  calisto.add_motor(Pro75M1670, position=-1.255)

  rail_buttons = calisto.set_rail_buttons(
    upper_button_position=0.0818,
    lower_button_position=-0.6182,
    angular_position=45,
  )

  nose_cone = calisto.add_nose(
    length=0.55829, kind="von karman", position=1.278
  )

  fin_set = calisto.add_trapezoidal_fins(
    n=4,
    root_chord=0.120,
    tip_chord=0.060,
    span=0.110,
    position=-1.04956,
    cant_angle=0.5,
    airfoil=("NACA0012-radians.txt","radians"),
  )

  tail = calisto.add_tail(
      top_radius=0.0635, bottom_radius=0.0435, length=0.060, position=-1.194656
  )

  main = calisto.add_parachute(
    name="main",
    cd_s=10.0,
    trigger=800,      # ejection altitude in meters
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
  )

  drogue = calisto.add_parachute(
      name="drogue",
      cd_s=1.0,
      trigger="apogee",  # ejection at apogee
      sampling_rate=105,
      lag=1.5,
      noise=(0, 8.3, 0.5),
  )

  # calisto.plots.static_margin()
  # calisto.draw()

  test_flight = Flight(
    rocket=calisto, environment=env, rail_length=5.2, inclination=85, heading=0
  )

  # test_flight.prints.maximum_values()
  test_flight.export_kml(
    file_name="trajectory.kml",
    extrude=True,
    altitude_mode="relative_to_ground",
  )

if __name__ == "__main__":
  main()
