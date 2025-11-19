import threading
import time

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        # with lock:
            temp = counter
            time.sleep(0.00001)  # 強制讓出 CPU，模擬競爭
            counter = temp + 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final counter: {counter}")  # 理論上應該是 200,000，但會小於這個值
