import json

file_path = 'my_datas.json'

# Function to append a dictionary to a JSON file
def append_to_json_file(new_data) -> None:
    # Read existing data from the file, if any
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
            
    except FileNotFoundError:
        existing_data = []
    
    
        
    
    # Append the new data to the existing data
    existing_data.append(new_data)

    # Write the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=2)

def read_json_file() -> json or None:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{file_path}'.")
        return None
    
def get_all_posts() -> list[dict] :
    return read_json_file()

def creat_new_post(new_post:dict) -> dict:
    data_dict:dict = {
        "id":read_json_file()[-1]["id"]+1,
        
    }
    data_dict.update(new_post)
    append_to_json_file(data_dict)
    return data_dict
    
    
    


        