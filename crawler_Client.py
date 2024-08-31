import json
import requests
import time
import csv

url = "http://a.4cdn.org/boards.json"
previous_data = None
out_file_name = f"{int(time.time())}-boards.csv"


print("Vivek added some line of code herere")
while True:
    response = requests.get(url)
    parsed_response = response.json()

    current_data = parsed_response['boards']
    print('yashwant')
    print('vivek')
    list = [1,2,3]
    list.sort()
    
    
    
    ####################################----------------------------------code written by Vivek Raj-------------############################################
    
    
    
    def search_in_array(arr, key):
        for index, value in enumerate(arr):
            if value == key:
                return index 
        return -1  

        # Example usage:
    arr = [10, 20, 30, 40, 50]
    key_to_search = 30

    result = search_in_array(arr, key_to_search)

    if result != -1:
        print(f"{key_to_search} found at index {result}.")
    else:
        print(f"{key_to_search} not found in the array.")

    
    print("saharshini")
    
    
    
    
    
    
    
    
    
    
    
    
    #####--------------------------------------------------------------------------------------------------------------------------------------#####

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
