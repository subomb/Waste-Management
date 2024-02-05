import RPi.GPIO as GPIO
import time

# Use GPIO numbering
GPIO.setmode(GPIO.BOARD)

# Define GPIO pins
TRIG_PIN = 18  # Change as per your connection
ECHO_PIN = 16  # Change as per your connection

# Set up the GPIO channels - one input, one output
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    # Ensure the Trigger pin is low for a clean pulse
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.5)

    # Send 10us pulse to trigger
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)  # 10 microseconds
    GPIO.output(TRIG_PIN, False)

    # Start the timer
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    # Wait for the echo back
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Calculate pulse duration
    pulse_duration = pulse_end - pulse_start

    # Calculate distance
    distance = pulse_duration * 17150  # Speed of sound at sea level is 34300 cm/s
    distance = round(distance, 2)

    return distance

try:
    last_percentage_reported = -10  # Initialize to a value that will not match any calculated percentage
    while True:
        distance = measure_distance()
        print(f"Bin Fill Level: {distance} cm")

        # Calculate the fill percentage based on a 50 cm bin depth
        fill_percentage = round((1 - distance / 50) * 100)

        # Ensure fill percentage is within 0-100%
        fill_percentage = max(0, min(fill_percentage, 100))

        # Check if we need to update the reported percentage
        if fill_percentage // 10 > last_percentage_reported // 10: 
            last_percentage_reported = fill_percentage
            print(f"Bin is approximately {fill_percentage}% full")

        # Stop if bin is nearly full (less than 5 cm remaining)
        if distance <= 8:
            print("Bin is full")
            break

        time.sleep(10)  # Wait for 10 seconds before the next measure

except KeyboardInterrupt:
    print("Measurement stopped by User")
finally:
    GPIO.cleanup()  # Reset the GPIO ports to a safe statepython