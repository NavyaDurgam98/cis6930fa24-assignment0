import json
import argparse
import csv
import sys
import requests

# delimiter
THORN = 'þ'

# url
BASE_URL = "https://api.fbi.gov/wanted/v1/list?page="

# get data from API
def get_data_fromApi(page):
    url = f"{BASE_URL}{page}"
    result = requests.get(url)
    result.raise_for_status()
    return result.json()

# get data from a local JSON file
def get_data_fromFile(location):
    with open(location, 'r') as file:
        return json.load(file)

# save api data to a JSON file
def save_data_toJsonFile(data, fileName='fbi_data.json'):
    with open(fileName, 'w') as json_file:
        json.dump(data, json_file, indent=2)
    #print(f"JSON data saved to {fileName}")

# Format data with thorn delimiter and save to CSV file
def format_data(data, outFile='FBIMostWanted.csv'):
    with open(outFile, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=THORN)
        writer.writerow(['Title', 'Subjects', 'Field Offices'])

        for item in data['items']:
            title = item.get('title', '')

            subjects = item.get('subjects', [])
            field_offices = item.get('field_offices', [])

            if not isinstance(subjects, list):
                subjects = [subjects] if subjects else []
            if not isinstance(field_offices, list):
                field_offices = [field_offices] if field_offices else []

            subjects_str = ', '.join(subjects)
            field_offices_str = ', '.join(field_offices)

            # Write to CSV
            writer.writerow([title, subjects_str, field_offices_str])
            
            print(f"{title}{THORN}{subjects_str}{THORN}{field_offices_str}")

# Main function to handle command-line arguments
def main(page=None, file_location=None):
    if page:
        data = get_data_fromApi(page)
        save_data_toJsonFile(data)  
    elif file_location:
        data = get_data_fromFile(file_location)
    else:
        print("Error: You should specify either --page or --file-location.")
        sys.exit(1)

    format_data(data)
    #print("Output data has been saved to FBIMostWanted.csv")

# Command-line argument parsing
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get, Format & Save FBI wanted data.")
    parser.add_argument("--page", type=int, required=False, help="The page number to fetch from the FBI API.")
    parser.add_argument("--file-location", type=str, required=False, help="The file location of the JSON data for testing.")

    args = parser.parse_args()

    if args.page and args.file_location:
        print("Error: Only one of --page or --file-location should be specified.")
        sys.exit(1)
    
    main(page=args.page, file_location=args.file_location)
