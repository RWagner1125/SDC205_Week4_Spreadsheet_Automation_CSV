# Spreadsheet Automation Menu - CSV File Storage
# Student ID: Raywag8025

from datetime import datetime
from pathlib import Path
import csv

# Convert a temperature from Fahrenheit to Celsius.
def convertData(value):
    return (value - 32) * 5 / 9


# Append one comma-separated record to the CSV file, creating it if needed.
def insertData(path, data):
    try:
        with open(path, 'a', newline='', encoding='utf-8') as csvfile:
            csvfile.write(data + '\n')
        return True
    except OSError as error:
        print(f"Error writing to CSV file: {error}")
        return False


# Read the CSV file with minimal permissions and display its contents.
def viewData(path):
    try:
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            print(f"The file {path}")
            reader = csv.reader(csvfile)
            for row in reader:
                print(','.join(row))
    except FileNotFoundError:
        print("Error: ZooData.csv does not exist yet. Choose 1 to add data first.")
    except OSError as error:
        print(f"Error reading CSV file: {error}")


# Ask for temperature entries, convert them, and save each to ZooData.csv.
def getInput(path):
    try:
        entryCount = int(input("How many entries are you inputting?\n"))
        if entryCount < 1:
            print("Please enter a positive number of entries.")
            return
    except ValueError:
        print("Error: Please enter a whole number.")
        return

    for entryNumber in range(entryCount):
        entryDate = input("Enter a date:\n")
        try:
            value = float(input("Enter the highest temp for the inputted date:\n"))
        except ValueError:
            print("Error: Temperature must be a number. Entry skipped.")
            continue
        # Pass a Fahrenheit temperature to convertData; get Celsius in return.
        convertedValue = convertData(value)
        data = f"{entryDate},{value:g},{convertedValue}"
        # Pass the file path and comma-separated record to insertData.
        if insertData(path, data):
            print(f"The following data was saved at {datetime.now()}: {data}")


# Display the menu and run the selected spreadsheet operation.
def main():
    folderPath = Path(r'C:\PythonFiles')
    csvPath = folderPath / 'ZooData.csv'
    try:
        folderPath.mkdir(parents=True, exist_ok=True)
    except OSError as error:
        print(f"Error creating data folder: {error}")
        return

    menuOptions = ['Input Data', 'View Current Data', 'Generate Report']
    print("Raywag8025's Spreadsheet Automation Menu")
    print('Choose a number from the following options')
    for optionNumber, optionText in enumerate(menuOptions, start=1):
        print(f'{optionNumber} {optionText}')

    selection = input()
    print(f'You selected {selection} at {datetime.now()}')
    if selection == '1':
        getInput(csvPath)
    elif selection == '2':
        viewData(csvPath)
    else:
        print('Error: The chosen functionality is not implemented yet')


if __name__ == '__main__':
    main()
