import json
import requests
import time
import csv

url = "http://a.4cdn.org/boards.json"
previous_data = None
out_file_name = f"{int(time.time())}-boards.csv"

while True:
    response = requests.get(url)
    parsed_response = response.json()

    current_data = parsed_response['boards']

    if previous_data is None:
        
        # If this is the first fetch, write the data to CSV
        with open(out_file_name, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            header = current_data[0].keys()
            csvwriter.writerow(header)
            for board in current_data:
                csvwriter.writerow(board.values())
                
        print(f"Initial data saved to {out_file_name}")
        
    elif current_data != previous_data:
        
        # ----------------------------------------------------- update the CSV
        with open(out_file_name, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            header = current_data[0].keys()
            csvwriter.writerow(header)
            for board in current_data:
                csvwriter.writerow(board.values())
        print(f"Data updated and saved to {out_file_name} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print(f"No change in data at {time.strftime('%Y-%m-%d %H:%M:%S')}")

    
    previous_data = current_data

    # sleep for 1 second
    time.sleep(1)
