Source Code Structure

waste_management.py
This is the main script of the project. It controls the ultrasonic sensor attached to the Raspberry Pi and calculates the fill level of the waste bin. Here's a breakdown of its structure:

Imports and GPIO Setup: The script starts by importing necessary libraries and setting up GPIO pins for communication with the ultrasonic sensor.
Function measure_distance: This function triggers the ultrasonic sensor and reads the distance measurement, converting it into a fill level percentage.
Main Loop: The main execution loop of the script continuously measures the waste bin's fill level and prints the status to the terminal. It also checks for when the bin is considered full and breaks the loop.
Cleanup: Proper GPIO cleanup is handled in a finally block to ensure the GPIO pins are reset when the script is stopped.

How to Use the Prototype
Setting Up the Hardware
1. Sensor Mounting: Mount the HC-SR04 ultrasonic sensor to the undersideof your bin's lid, facing downward.
2. Wiring: Connect the sensor to the Raspberry Pi using GPIO pins. Use GPIO 18 for TRIG and GPIO 16 for ECHO.
3. Power: Ensure the Raspberry Pi is powered and connected to a display or accessible via SSH.

Running the Software
1. Access the Raspberry Pi: Connect to your Raspberry Pi via SSH or open its terminal directly.
2. Navigate to the Script: Use the command line to navigate to the directory containing waste_management.py.
3. Execute the Script: Run the script by typing python3 waste_management.py in the terminal.
4. Observe Output: The script will output the fill level of the bin in the terminal. It updates this information periodically.

Stopping the Script
- To stop the script, simply press Ctrl + C in the terminal. This will trigger a cleanup routine that safely resets the GPIO pins.

Link to the demo:
https://youtube.com/shorts/DRbtLne5NVY