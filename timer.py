import time

def timer(seconds):
    """
    A function that counts down from a specified number of seconds.
    """
    while seconds > 0:
        print(f"{seconds} seconds left...")
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# Example usage:
timer(10)