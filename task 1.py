from multiprocessing import Process

def message1():
    print("Process 1: Hello from Process 1")

def message2():
    print("Process 2: Hello from Process 2")

def message3():
    print("Process 3: Hello from Process 3")

if __name__ == "__main__":
    p1 = Process(target=message1)
    p2 = Process(target=message2)
    p3 = Process(target=message3)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("All processes completed.")