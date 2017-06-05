import time
import threading

# Inherit Thread class
class AsynchWrite(threading.Thread):
    # Override __init__ of Thread class
    def __init__(self, file, text):
        threading.Thread.__init__(self)
        self.file = file
        self.text = text

    # Override the run() method
    def run(self):
        print("Started file write: " + self.file)
        f = open(self.file, "a")  # append
        f. write(self.text + "\n")
        f.close
        time.sleep(5)
        print("File wrtie complete")


message = raw_input("Text: ")
file = "out.txt"
write_thread = AsynchWrite(file, message)
write_thread.start()
print("#############")
write_thread.join()
print("The wait is over!")
