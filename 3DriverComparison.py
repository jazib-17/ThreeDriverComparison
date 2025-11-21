'''
Driver Laptime Comparison Maker

Compare the laptimes of 2 (or more with some edits) to drivers in a single race

Author: Jazib Ahmed
'''
from fastf1.plotting import get_driver_abbreviation
import fastf1
import matplotlib.pyplot as plt
from datetime import timedelta

fastf1.Cache.enable_cache('fastf1_cache')

#-----------------------------------
# Change the variables here for different races/different drivers
session = fastf1.get_session(2024, 'Singapore', 'Race') # Set race here
session.load(telemetry=False,weather=False,messages=False)
startlap = 40 #Which lap to start getting laptimes from
endlap = 58 #Which lap to end getting laptimes from

driver1 = "Piastri" # First driver (Laps will be compared to this driver)
driver2 = "Leclerc" # Second driver
driver3 = "Verstappen" # Third driver

# What color the columns should be set for each driver (their team color)
team_color = {
# Two colors:  [Text color, background color]
'Driver1Team': ['black','orange'],
'Driver2Team': ['white','red'],
'Driver3Team': ['white','blue']
}
# Set the title and chart/font size for the analysis
chart_title = "Ferrari's True Pace at Singapore 24 (Part 2: In Open Air)"
chartsize = (20,6) #((width, height))
fontsize = 20
#------------------------------------

def format_lap(laptime):
    # Format the average difference with a '+' or '-' sign at the front
    if laptime < timedelta(0):
        # If negative, format it with a '-' sign
        formatted_diff = "-" + f"{abs(laptime)}"[14:19]
    else:
        # If positive or zero, format it with a '+' sign
        formatted_diff = "+" + f"{laptime}"[14:19]
    return formatted_diff

# Get lap data for drivers
driver1laps = session.laps.pick_drivers(get_driver_abbreviation(driver1, session))['LapTime']
driver2laps = session.laps.pick_drivers(get_driver_abbreviation(driver2, session))['LapTime']
driver3laps = session.laps.pick_drivers(get_driver_abbreviation(driver3, session))['LapTime']

# Calculate differences on each lap
differences,differences2 = [],[]
for i in range(startlap-1,endlap-1):
    differences.append(list(driver2laps)[i]-list(driver1laps)[i])
    differences2.append(list(driver3laps)[i]-list(driver1laps)[i])

# Calculate the total sum of differences
total_diff1 = sum(differences, timedelta())
total_diff2 = sum(differences2, timedelta())

# Calculating the average difference and formatting it
average_diff1 = total_diff1 / len(differences)
average_diff2 = total_diff2 / len(differences2)
formatted_avg_diff = format_lap(average_diff1)
formatted_avg_diff2 = format_lap(average_diff2)

# Formatting the time for each driver on each lap
driver1lapsformat = list(driver1laps.astype(str).str[-11:-3])[startlap-1:endlap-1]
driver2lapsformat = list(driver2laps.astype(str).str[-11:-3])[startlap-1:endlap-1]
driver3lapsformat = list(driver3laps.astype(str).str[-11:-3])[startlap-1:endlap-1]

# Laps column text
row = ["Lap " + str(i) for i in range(startlap,endlap)]

lap_data = list(zip(row,driver1lapsformat,driver2lapsformat,driver3lapsformat))  # Zipped lap identifiers and lap times
# Adding the average difference row to bottom of chart
lap_data.append(["Avg. Difference to " + driver1,'±0.000',formatted_avg_diff, formatted_avg_diff2])
# Create a figure and axis
fig, ax = plt.subplots(figsize=chartsize)

# Column names
column = ["Lap",driver1, driver2, driver3]

# Extra settings for the chart
ax.axis("off")
fig.patch.set_facecolor('#2e2e2e')
fig.suptitle(chart_title,color="white",fontsize = fontsize)
# Create the table
table = ax.table(cellText=lap_data, colLabels=column, loc='center', cellLoc='center')
table.scale(xscale=1, yscale=2)
table.set_fontsize(fontsize)

# Set colors for specific columns
for (i, j), cell in table.get_celld().items():
    if j == 0:  # Lap number column
        cell.set_text_props( color='white')  # Text properties
        cell.set_facecolor('black')  # Background color
    elif j == 1:  # Driver 1's column
        cell.set_text_props( color=team_color['Driver1Team'][0])  # Text properties
        cell.set_facecolor(team_color['Driver1Team'][1])  # Background color
    elif j == 2:  # Driver 2's column
        cell.set_text_props( color=team_color['Driver2Team'][0])  # Text properties
        cell.set_facecolor(team_color['Driver2Team'][1])  # Background color
    elif j == 3:  # Driver 3's column
        cell.set_text_props( color=team_color['Driver3Team'][0])  # Text properties
        cell.set_facecolor(team_color['Driver3Team'][1])  # Background color


plt.tight_layout()
# Show the plot
plt.show()