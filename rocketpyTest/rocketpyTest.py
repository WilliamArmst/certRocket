from rocketpy import Environment, SolidMotor, Rocket, Flight
import datetime

env = Environment(latitude=39.01549201631338, longitude=-105.71103788653403, elevation=2962) # Hartsel Launch Site
today = datetime.data.today();

env.set_date(today.year, today.month, today.day, 12)
env.set_atmospheric_model(type="Forecast", file="GFS")

print(env.info())
