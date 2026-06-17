import threading
import itertools
import time
import sys


class Spinner:

    def __init__(self):

        self.running = False
        self.thread = None

    def start(self, message="Downloading"):

        self.running = True

        def animate():

            for frame in itertools.cycle(
                ["|", "/", "-", "\\"]
            ):

                if not self.running:
                    break

                sys.stdout.write(
                    f"\r{message} {frame}"
                )

                sys.stdout.flush()

                time.sleep(0.1)

        self.thread = threading.Thread(
            target=animate
        )

        self.thread.start()

    def stop(self):

        self.running = False

        self.thread.join()

        sys.stdout.write("\r")
        sys.stdout.flush()