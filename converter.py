import os
import glob

def replace_characters_in_files():
    # Get all .csv files in the current directory
    csv_files = glob.glob("*.csv")
    
    for file_name in csv_files:
        print(f"Processing file: {file_name}")
        
        # Read the file content
        with open(file_name, 'r') as file:
            content = file.read()
        
        # Replace ',' with '&' and '|' with ','
        modified_content = content.replace(',', '&').replace('|', ',')
        
        # Write the modified content back to the file
        with open(file_name, 'w') as file:
            file.write(modified_content)
        
        print(f"Finished processing file: {file_name}")

if __name__ == "__main__":
    replace_characters_in_files()
