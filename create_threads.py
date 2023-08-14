import threading
#from queue import Queue

class taskProducer(threading.Thread):
    def __init__(self, queue, name, task_inputs):
        super().__init__()
        self.queue = queue
        self.name = name
        self.task_inputs = task_inputs

    def run(self):
        for input in self.task_inputs:
            self.queue.put(input)
            print(f"putting {input} in queue")
        print(f"{self.name} finished producing")

class taskConsumer(threading.Thread):
    def __init__(self, queue, name, process_function):
        super().__init__()
        self.queue = queue
        self.name = name
        self.process_function = process_function

    def run(self):
        while True:
            task_inputs = self.queue.get()
            if task_inputs is None:
                print(f"{self.name} exiting")
                break
            print(f"{self.name} consuming: {task_inputs}")
            self.process_function(task_inputs)
            self.queue.task_done()
        print(f"{self.name} finished consuming")

