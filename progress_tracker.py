from threading import Lock
import time


class ProgressTracker:

    def __init__(self, total_size):

        self.total_size = total_size
        self.downloaded = 0
        self.lock = Lock()

        self.start_time = time.time()

    def update(self, bytes_downloaded):

        with self.lock:

            self.downloaded += bytes_downloaded

            elapsed = time.time() - self.start_time

            speed = self.downloaded / elapsed

            remaining = self.total_size - self.downloaded

            eta = remaining / speed if speed > 0 else 0

            percentage = (
                self.downloaded
                / self.total_size
            ) * 100

            print(
                f"\nProgress: {percentage:.2f}%"
            )

            print(
                f"Speed: {speed/1024:.2f} KB/s"
            )

            print(
                f"ETA: {eta:.2f} sec"
            )
            print()