from datetime import datetime, timedelta
import time
import sys

def countdown_to_new_year():
    # Get the current date and time
    now = datetime.now()

    # Set the target date for the next New Year
    new_year_target = datetime(now.year + 1, 1, 1, 0, 0, 0)

    while True:
        # Calculate the time remaining
        time_remaining = new_year_target - datetime.now()

        # Format the countdown string
        countdown_str = f"Time remaining: {time_remaining.days} days, {time_remaining.seconds // 3600} hours, " \
                        f"{(time_remaining.seconds % 3600) // 60} minutes, {time_remaining.seconds % 60} seconds."

        # Use sys.stdout.write to print without a new line
        sys.stdout.write('\r' + countdown_str)
        sys.stdout.flush()

        # Wait for 1 second before updating the countdown
        time.sleep(1)

try:
    # Run the countdown until the user cancels
    countdown_to_new_year()
except KeyboardInterrupt:
    print("\nCountdown canceled by the user.")