import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

# Create a thread
t = threading.Thread(target=print_numbers)

# Start the thread
t.start()

# Continue with the main thread
print("Main thread continues...")



def print_hello():
    for _ in range(3):
        print("Hello")
        time.sleep(1)

def print_world():
    for _ in range(3):
        print("World")
        time.sleep(1)

t1 = threading.Thread(target=print_hello)
t2 = threading.Thread(target=print_world)

t1.start()
t2.start()

t1.join()  # Wait for t1 to finish
t2.join()  # Wait for t2 to finish

print("Both threads finished.")

print("new branch add main")