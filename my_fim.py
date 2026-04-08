import hashlib
import os
import time

# 1. This function creates a cryptographic "fingerprint" (hash) of a file
def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

print("-" * 50)
print("Starting Mini File Integrity Monitor (FIM)...")
print("-" * 50)

# 2. We will create a fake "highly sensitive" file to monitor
target_file = "confidential_data.txt"

if not os.path.exists(target_file):
    with open(target_file, 'w') as f:
        f.write("CONFIDENTIAL: The secret code is 12345.")
    print(f"[*] Created target file: {target_file}")

# 3. Calculate the baseline fingerprint of the file
baseline_hash = get_file_hash(target_file)
print(f"[*] Baseline SHA-256 Fingerprint: {baseline_hash}")
print("[*] Monitoring file for hacker tampering... (Leave this running)")

# 4. Check the file every 2 seconds to see if the fingerprint changes
try:
    while True:
        time.sleep(2) 
        current_hash = get_file_hash(target_file)
        
        # If the fingerprint changes, trigger a massive alert!
        if current_hash != baseline_hash:
            print("\n" + "!" * 50)
            print("[!!!] CRITICAL ALERT: FILE HAS BEEN TAMPERED WITH! [!!!]")
            print("!" * 50)
            print(f"Old Fingerprint: {baseline_hash}")
            print(f"New Fingerprint: {current_hash}")
            break 
            
except KeyboardInterrupt:
    print("\nMonitoring stopped safely.")