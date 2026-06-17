from concurrent.futures import ThreadPoolExecutor
from progress_tracker import ProgressTracker
from downloader import Downloader
from chunk_manager import ChunkManager
from file_assembler import FileAssembler
import logging
import os
from pathlib import Path
from spinner import Spinner

def main():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s"
    )

    url = input("Enter URL: ").strip()

    downloader = Downloader()

    # Verify server supports range requests
    if not downloader.supports_range_requests(url):
        raise Exception(
            "Server does not support HTTP Range Requests."
        )

    # Determine worker count
    default_workers = min(
        8,
        (os.cpu_count() or 4) * 2
    )

    user_input = input(
        f"Workers [{default_workers}]: "
    ).strip()

    workers = (
        int(user_input)
        if user_input
        else default_workers
    )

    # Detect filename
    detected_name = downloader.get_filename(url)

    print(
        f"Detected filename: {detected_name}"
    )

    # Allow rename while preserving extension
    stem = Path(detected_name).stem
    suffix = Path(detected_name).suffix

    custom_name = input(
        f"Filename [{detected_name}]: "
    ).strip()

    if custom_name:
        output_name = custom_name + suffix
    else:
        output_name = detected_name

    # File size
    file_size = downloader.get_file_size(url)

    print(
        f"File Size: {file_size:,} bytes"
    )

    # Progress tracker
    tracker = ProgressTracker(file_size)

    # Use worker count as chunk count
    manager = ChunkManager(
        file_size=file_size,
        num_chunks=workers
    )

    chunks = manager.create_chunks()

    logging.info(
        f"Created {len(chunks)} chunks"
    )
    spinner = Spinner()
    spinner.start()

    # Concurrent downloads
    with ThreadPoolExecutor(
        max_workers=workers
    ) as executor:

        futures = []

        for index, (start, end) in enumerate(chunks):

            futures.append(
                executor.submit(
                    downloader.download_chunk,
                    url,
                    start,
                    end,
                    f"chunk_{index}.part",
                    tracker
                )
            )

        # Surface exceptions
        for future in futures:
            future.result()

    logging.info(
        "All chunks downloaded successfully."
    )
    spinner.stop()

    # Assemble file
    assembler = FileAssembler()

    assembler.assemble(
        output_name,
        len(chunks)
    )

    logging.info(
        f"File saved as: {output_name}"
    )
    


if __name__ == "__main__":
    main()