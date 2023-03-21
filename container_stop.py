
import docker
import time
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread


ending_string="..........All containers are stopped.........."

print(" We are going to listing all the stoped containers with id in your system:--")


class Loader:

    def __init__(self, description="Loading...", end_point="Done!", time_out=0.2):

        self.desc = description
        self.end = end_point
        self.timeout = time_out

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for i in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {i}", flush=True, end="")
            time.sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        self.stop()



client = docker.from_env()

all_container_list = client.containers.list(all=True)

count=1

for container in all_container_list:
            
            if __name__ == "__main__":
                with Loader("Loading for docker..."):
                    for i in range(3):
                        time.sleep(0.25)

                loader = Loader("Loading for container details...", "oohhh!!, That was too fast!", 0.05).start()
                for i in range(3):
                    time.sleep(0.25)

                loader.stop()

            print("\n")

            print("This will be your container number: ",count )
            time.sleep(0.5)

            print("---------",container,"---------")
            time.sleep(0.5)

            count= count+1

            print("This is the container id:- ",container.id)
            container.stop()

print(ending_string.upper())



