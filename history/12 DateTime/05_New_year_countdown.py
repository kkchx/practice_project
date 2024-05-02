from datetime import datetime

def countdown_to_new_year():
    # Get the current date and time
    now = datetime.now()

    # Set the target date for the next New Year
    new_year_target = datetime(now.year + 1, 1, 1, 0, 0, 0)

    # Calculate the time remaining
    time_remaining = new_year_target - now

    print("New Year Countdown:")
    print(f"Time remaining: {time_remaining.days} days, {time_remaining.seconds // 3600} hours, "
          f"{(time_remaining.seconds % 3600) // 60} minutes, {time_remaining.seconds % 60} seconds.")

# Run the countdown
countdown_to_new_year()