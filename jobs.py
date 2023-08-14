from create_threads import taskConsumer, taskProducer
from queue import Queue
import time

def print_stuff(message):
    print(message)
    time.sleep(3)

def main():
    task_queue = Queue()
    num_producers = 4
    num_consumers = 3

    inputs = ["input1", "input2", "input3"]

    producers = [taskProducer(task_queue, f"Producer: {i}", inputs) for i in range(num_producers)]
    consumers = [taskConsumer(task_queue, f"Consumer: {i}", print_stuff) for i in range(num_consumers)]

    for producer in producers:
        producer.start()
    
    for consumer in consumers:
        consumer.start()
    
    for _ in range(num_consumers):
        task_queue.put(None)
    
    for consumer in consumers:
        consumer.join()
    
    print("Done!")

if __name__ == "__main__":
    main()