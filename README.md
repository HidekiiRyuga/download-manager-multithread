# Multi-Threaded Download Manager

A high-performance download manager built in Python that accelerates file transfers using concurrent chunk-based downloading, HTTP Range Requests, and thread synchronization.

## Author

**Stuti**

---

## Overview

This project implements a multi-threaded download manager capable of downloading files in parallel by splitting them into multiple chunks and assigning each chunk to a separate worker thread.

The downloaded chunks are then reassembled into the original file while preserving the correct file extension.

The project demonstrates important Software Engineering and Systems Programming concepts such as:

* Concurrency
* Multi-threading
* Synchronization
* Thread Safety
* Fault Tolerance
* Networking
* Object-Oriented Design

---

## Features

* Concurrent downloads using `ThreadPoolExecutor`
* HTTP Range Request support
* Automatic file size detection
* Dynamic chunk allocation
* Thread-safe progress tracking using `Lock`
* Download speed estimation
* ETA (Estimated Time Remaining)
* Automatic filename detection
* Extension preservation during renaming
* Retry mechanism for failed downloads
* Automatic cleanup of temporary chunk files
* Logging support
* Modular object-oriented architecture

---

## Project Structure

```text
download-manager/

├── main.py
├── downloader.py
├── chunk_manager.py
├── file_assembler.py
├── progress_tracker.py
├── spinner.py
├── requirements.txt
└── README.md
```

---

## Architecture

```text
User URL
    │
    ▼
Downloader
    │
    ▼
HEAD Request
    │
    ▼
File Size Detection
    │
    ▼
Chunk Manager
    │
    ▼
Chunk Generation
    │
    ▼
ThreadPoolExecutor
 ┌──┼──┬──┐
 ▼  ▼  ▼  ▼
T1 T2 T3 T4
 │  │  │  │
 ▼  ▼  ▼  ▼
chunk_0.part
chunk_1.part
chunk_2.part
chunk_3.part
    │
    ▼
FileAssembler
    │
    ▼
Final File
```

---

## Technologies Used

* Python
* Requests
* ThreadPoolExecutor
* Threading
* Logging
* HTTP Range Requests
* Object-Oriented Programming

---

## Concurrency Concepts Demonstrated

* Multi-threading
* Thread Pools
* Synchronization
* Shared State Management
* Race Condition Prevention
* Mutual Exclusion using Locks

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd download-manager
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the application:

```bash
python main.py
```

The program will prompt for:

```text
Enter URL:
```

Example:

```text
https://proof.ovh.net/files/100Mb.dat
```

Then:

```text
Workers [8]:
```

Press Enter to use the default value or specify your own worker count.

You will then see:

* Detected filename
* File size
* Download progress
* Download speed
* ETA
* Completion status

---

## Example Output

```text
Detected filename: 100Mb.dat

Progress: 25.00%
Speed: 2.80 MB/s
ETA: 26 sec

Progress: 50.00%
Speed: 3.10 MB/s
ETA: 15 sec

Progress: 75.00%
Speed: 3.00 MB/s
ETA: 8 sec

Progress: 100.00%

All chunks downloaded successfully.
Assembled: 100Mb.dat
Temporary chunk files deleted
```

---

## Sample Test URLs

```text
https://proof.ovh.net/files/10Mb.dat
https://proof.ovh.net/files/100Mb.dat
https://proof.ovh.net/files/1Gb.dat
```

---

## Learning Outcomes

This project helped explore:

* Concurrent Programming
* Synchronization Mechanisms
* HTTP Protocol Fundamentals
* Range Requests
* Fault-Tolerant Design
* File System Operations
* Software Design Principles
* Object-Oriented Programming

---

## Future Improvements

* Pause / Resume Downloads
* Download Queue Management
* SHA256 Integrity Verification
* GUI Version
* Adaptive Chunk Sizing
* Download History Tracking

---

## License

This project is open-source and available for educational and learning purposes.
