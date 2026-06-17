import time
import requests
import logging
from urllib.parse import urlparse
import os



class Downloader:
    def supports_range_requests(self, url):

        response = requests.head(
            url,
            allow_redirects=True
        )

        return (
            response.headers.get(
                "Accept-Ranges"
            )
            == "bytes"
        )
    def download(self, url, filename):
        print("Starting download...")

        response = requests.get(url, stream=True)

        with open(filename, "wb") as file:
           for chunk in response.iter_content(chunk_size=8192):
               if chunk:
                   file.write(chunk)
        logging.info(
            "Download complete"
        )
    def download_chunk(
        self,
        url,
        start,
        end,
        chunk_filename,
        tracker
    ):

        max_retries = 3

        for attempt in range(max_retries):

            try:

                headers = {
                    "Range": f"bytes={start}-{end}"
                }

                response = requests.get(
                    url,
                    headers=headers,
                    timeout=10,
                    stream=True
                )

                response.raise_for_status()

                with open(chunk_filename, "wb") as file:
                    file.write(response.content)

                tracker.update(
                    len(response.content)
                )

                print(
                    f"Downloaded {chunk_filename}"
                )

                return

            except Exception as e:

                print(
                    f"{chunk_filename} failed "
                    f"(attempt {attempt + 1})"
                )

                time.sleep(1)

        print(
            f"{chunk_filename} permanently failed"
        )   
    def get_file_size(self, url):

        response = requests.head(url)

        return int(response.headers["Content-Length"])
    def get_filename(self, url):

        response = requests.head(
            url,
            allow_redirects=True
        )

        content_disposition = response.headers.get(
            "Content-Disposition"
        )

        if content_disposition:

            if "filename=" in content_disposition:

                filename = (
                    content_disposition
                    .split("filename=")[1]
                    .strip('"')
                )

                return filename
        parsed = urlparse(url)

        filename = os.path.basename(
            parsed.path
        )

        if filename:
            return filename
        return "downloaded_file"
