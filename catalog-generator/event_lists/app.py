import os
import openai
import requests
import json

def get_latest_architecture_version(dir_path: str):
    """Gets latest architecture version from directory

    Args:
        dir_path (str): The directory path to search

    Returns:
        str: The architecture version
    """
    int_version = 1
    if(os.path.exists(dir_path)):
        files = os.listdir(dir_path)
        for file in files:
            version = file.split('_')[-1].replace(".json","")
            int_version = int(version) + 1
        version_str = str(int_version)
    version_str = version_str.rjust(3, '0') 
    return version_str

def get_filepath(architecture_required : str):
    """Returns filepath for events architecture

    Args:
        architecture_required (str): The system of he software architecture required

    Returns:
        _type_: The filepath for the event architecture
    """
    architecture_path = architecture_required.replace(" ","_")
    isExist = os.path.exists(architecture_path)
    if not isExist:
        os.makedirs(architecture_path)
        print("The new directory is created!")
    version = get_latest_architecture_version(architecture_path)
    file_path = f"{architecture_path}/{architecture_path}_{version}.json"
    return file_path

def get_event_list(architecture_required : str, template_version: int):
    """
    Main function generates event list
    """
    
    openai.api_key = os.getenv("CHATGPT_KEY")
    template_version_str = str(template_version).rjust(3, '0') 
    
    with open(f'template/template_{template_version_str}.json') as template_file:
        json_template = json.load(template_file)
    
    answers = []
    
    for i in range(1,4):

        print(f"Calling API {i} time to get the json architecture for {architecture_required}...")
        chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user"
        , "content": f"""Return the JSON only in your response for an event catalog that supports a software
        architecture for an {architecture_required} system using this JSON as the example template {json_template} to inform your choices
        for the software architecture."""}])
        out = chat_completion['choices'][0]['message']['content']
        print(f"Called API {i} times to get the json architecture for {architecture_required}.")
        answers.append(out)
        
    print(f"Calling API to ask which is the best json architecture for {architecture_required}...")
    chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user"
    , "content": f"""Return the JSON only in your response of the best json representation of the software architecture for {architecture_required} that is found in {answers} given the template {json_template}."""}])
    final_answer = chat_completion['choices'][0]['message']['content']
    print(f"Called API to ask which is the best json architecture for {architecture_required}...")
    
    return final_answer
    
def write_event_list(architecture_required  : str, event_list : str):
    
    file_path = get_filepath(architecture_required)
    print(f"The event list json will write out to {file_path}.")

    print(f"Writing out file to {file_path}...")
    with open(file_path, "w") \
    as outfile:
        outfile.write(event_list)
    print(f"Written out file to {file_path}.")
    
def main():
    print('Enter the software architecture you require:')
    architecture_required = input()
    print('JSON template version required:')
    template_version = input()
    event_list = get_event_list(architecture_required, template_version)
    write_event_list(architecture_required, event_list)

if __name__ == '__main__':
    main()
