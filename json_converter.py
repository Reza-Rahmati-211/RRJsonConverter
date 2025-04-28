import os
import pandas as pd

def convert_files_to_json(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if filename.endswith('.csv'):
            try:
                df = pd.read_csv(filepath)
                json_filename = filename.replace('.csv', '.json')
                json_path = os.path.join(directory, json_filename)
                df.to_json(json_path, orient='records', indent=4, force_ascii=False)
                print(f"File {filename} successfully converted to {json_filename}.")
            except Exception as e:
                print(f"Error: {filename} -> {e}")

        elif filename.endswith('.xlsx'):
            try:
                df = pd.read_excel(filepath)
                json_filename = filename.replace('.xlsx', '.json')
                json_path = os.path.join(directory, json_filename)
                df.to_json(json_path, orient='records', indent=4, force_ascii=False)
                print(f"File {filename} successfully converted to {json_filename}.")
            except Exception as e:
                print(f"Error: {filename} -> {e}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    convert_files_to_json(current_directory)
