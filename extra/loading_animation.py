import time


def loading_animation():
    print("Loading", end="")
    for _ in range(5):
        time.sleep(0.5)  # Delay of 0.5 seconds
        print(".", end="", flush=True)
    print("\nGame Started! Let's play.")


loading_animation()
