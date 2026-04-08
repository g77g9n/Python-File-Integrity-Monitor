# Cryptographic File Integrity Monitor (FIM)

## Objective
The goal of this project was to engineer a custom File Integrity Monitor using Python to understand how enterprise SIEMs (like Wazuh and Tripwire) detect unauthorized file modifications and potential breaches.

## Skills Learned
- Applied Cryptography utilizing the `hashlib` library to generate SHA-256 hashes.
- Automation of continuous monitoring loops to track file states in real-time.
- Understanding of the core principles of Data Integrity within the CIA Triad.

## Tools Used
- Python 3
- Visual Studio Code

## How It Works
The script calculates a baseline cryptographic SHA-256 hash of a designated target file. It then enters a continuous monitoring loop, recalculating the hash at set intervals. If the live hash deviates from the baseline hash—indicating the file has been modified, tampered with, or corrupted—the script immediately halts and generates a critical alert detailing the cryptographic mismatch.
