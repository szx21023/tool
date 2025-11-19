import threading
import time

queue = []

def pub(tid):
    for i in range(5):
        print(f"Thread {tid} - Publishing message {i}")
        queue.append(i)
        time.sleep(1)  # Simulate some work
    print(f"Thread {tid} - Finished publishing messages")

def sub(tid):
    while True:
        if queue:
            message = queue.pop(0)
            print(f"Thread {tid} - Consumed message {message}")
        else:
            print(f"Thread {tid} - No messages to consume")
        time.sleep(2)  # Simulate some work


thread_pub = threading.Thread(target=pub, args=(1,))

thread_sub_1 = threading.Thread(target=sub, args=(2,))
thread_sub_2 = threading.Thread(target=sub, args=(3,))

thread_pub.start()
thread_sub_1.start()
thread_sub_2.start()
thread_pub.join()
thread_sub_1.join()
thread_sub_2.join()