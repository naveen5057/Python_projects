# Program to display the time in different countries

import datetime
import pytz

country_map = ["India", "Singapore", "Japan", "France"]
print(country_map)

print("Select the country for which you want to see the time:")
country_input = input()

country_time_zone_mapping = {"India": "Asia/Calcutta", "Japan": "Asia/Tokyo", "France": "Europe/Paris",
                             "Singapore": "Asia/Singapore"}

# time zone list : https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568

timezone = country_time_zone_mapping.get(country_input)

tz = pytz.timezone(timezone)

current_time = datetime.datetime.now(tz=tz)
print(f"Current time in {country_input} is : {current_time}.")

print("To check whether it prints correct time, google it and find it by your self.")
