# cis6930fa24 -- Assignment 0 -- FBI wanted list

**Name:** Navya Durgam  
**UFID:** 33725389

---

## Overview

This project retrieves data from the FBI's wanted list, either via API or from a local JSON file. The program extracts and formats the following details:
- **Title**: Description of the wanted person/event.
- **Subjects**: The associated subjects or reasons.
- **Field Offices**: The FBI field offices handling the case.

The data is formatted with the thorn character (`þ`) to separate fields. Fields containing multiple values, such as `subjects` or `field_offices`, are separated by commas within them. If a field is missing or empty, it will be left blank with no trailing thorn (`þ`) at the end of the record.

---

## How to install
### 1. Install pipenv:
   Install pipenv using:
   ```bash
   pip install pipenv
   ```
### 2. Install dependencies:
   Required python packages can be installed using:
   ```bash
   pipenv install -e. 
   ```
### 3. Clone the repository:
   This project can be cloned using:
   ```bash
   git clone https://github.com/NavyaDurgam98/cis6930fa24-assignment0.git
   ```

---

## How to run

### Option 1: Get data from the FBI API

To fetch data from a specific page of the FBI API, use:

```bash
pipenv run python main.py --page 1
```

This fetches and formats data from the FBI API's first page.

### Option 2: Load data from local JSON file

To test using a local JSON file, use:

```bash
pipenv run python main.py --file-location fbi_data.json
```

---

## Example Output

Here’s a sample of what the formatted output looks like:  
VICTIM - BETH ELLEN VINSON - RALEIGH, NORTH CAROLINAþViCAP Homicides and Sexual Assaultsþ  
UNKNOWN SUSPECT - UNSOLVED HOMICIDE - AURORA, COLORADOþViCAP Homicides and Sexual Assaultsþ  
UNSOLVED/COLD CASE HOMICIDE - NEBRASKAþViCAP Homicides and Sexual Assaultsþ  
ABDULLAH AL-RIMIþSeeking Information - Terrorismþnewyork  

---
## Functions

### main.py

- **get_data_fromApi(page)**: Retrieves JSON data from the FBI API for the specified page.
- **get_data_fromFile(location)**: Reads JSON data from the local file at the provided location.
- **save_data_toJsonFile(data, fileName)**: Saves the fetched data to a `.json` file with specified filename.
- **format_data(data, outFile)**: Formats data using the thorn (`þ`) delimiter and saves it to a CSV file. It also prints the formatted data to the console.
- **main(page=None, file_location=None)**: Processes command-line arguments to fetch data from either the API or a file, then formats and outputs the data.
---

## Assumptions

- **API Structure**: Assumes the structure of the FBI API remains unchanged. If the structure changes, some fields may not be processed properly.
- **Single Page Support**: Currently supports fetching a single page at a time from the FBI API.

---

## Running tests

The project uses **pytest** for unit testing.

To run all tests:

```bash
pipenv run python -m pytest -v
```

To run a specific test file, such as `test_download.py`:

```bash
pipenv run python -m pytest tests/test_download.py -v
```
---
## Conclusion

This project showcases the functionality of fetching and formatting data from an external FBI API. The primary goal is to extract and format information from the "Most Wanted" list into a structured output using the thorn (`þ`) character as a delimiter. By handling both API data retrieval and local file input, the code provides a versatile solution for data processing.

While the project effectively demonstrates data extraction and formatting, future enhancements could include supporting pagination for handling multiple pages of API data and extending the formatting to accommodate additional fields or requirements.

```
