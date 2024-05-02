from datetime import datetime, timedelta
import time

def get_timer_duration():
    try:
        minutes = int(input("Enter the duration of the timer in minutes: "))
        return minutes * 60  # Convert minutes to seconds
    except ValueError:
        print("Invalid input. Please enter a valid number of minutes.")
        return get_timer_duration()

print("Welcome to the Countdown Timer!")

timer_duration = get_timer_duration()
target_time = datetime.now() + timedelta(seconds=timer_duration)

while True:
    current_time = datetime.now()
    time_remaining = max(target_time - current_time, timedelta(0))

    if time_remaining == timedelta(0):
        print("\nTimer complete. Time's up!")
        break

    minutes, seconds = divmod(time_remaining.seconds, 60)
    milliseconds = time_remaining.microseconds // 1000

    print(f"\rTime remaining: {minutes:02}:{seconds:02}.{milliseconds:03}", end='', flush=True)
    time.sleep(0.001)  # Adjust the sleep time for smoother display (0.1 seconds in this case)