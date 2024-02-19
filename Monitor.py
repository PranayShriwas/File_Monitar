import os
import time
from datetime import datetime
def monitor_directory(directory):
    print("Monitoring directory:", directory)
    try:
        files_before = set(os.listdir(directory))
    except FileNotFoundError:
        print("Directory not found:", directory)
        return

    while True:
        try:
            files_after = set(os.listdir(directory))
            new_files = files_after - files_before

            if new_files:
                for file_name in new_files:
                    file_path = os.path.join(directory, file_name)
                    print(f"New file created: {file_path} at {datetime.now()}")

                # Update the files_before set for the next iteration
                files_before = files_after

            time.sleep(1)  # Check every second
        except FileNotFoundError:
            print("Directory not found:", directory)
            break

if __name__ == "__main__":
    directory_to_monitor = r"C:\File_Monitar"  # directory path
    monitor_directory(directory_to_monitor)
