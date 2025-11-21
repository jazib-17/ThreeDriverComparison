# ThreeDriverComparison
A Python tool that generates a clear, side-by-side laptime comparison table for three Formula 1 drivers within a single race session.
The script uses FastF1 to load race data, extracts laptimes for the selected drivers, and displays:
- Each driver’s lap time from a chosen lap range
- The lap-by-lap time difference relative to a reference driver
- The average delta over the selected stint
- A fully styled matplotlib table with customizable team colors, fonts, and chart size

This tool is useful for doing race-pace analysis, stint comparisons, and driver performance breakdowns in an intuitive, visual format.
Simply modify the variables at the top (drivers, race, lap range, colors) and run the script to generate the comparison table.
