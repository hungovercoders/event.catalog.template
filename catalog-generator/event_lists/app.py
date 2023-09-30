import os
import openai
import requests

def get_latest_architecture_version(dir_path: str):
    files = os.listdir('dir_path')
    return files

def get_filepath(architecture_required : str):
    architecture_required_path = architecture_required.replace(" ","_")
    dir_path = f"{architecture_required_path}/{architecture_required_path}"
    files = os.listdir(dir_path)
    return filepath

def main():
    """
    Main function generates event list
    """

    architecture_required = input()

    openai.api_key = os.getenv("CHATGPT_KEY")

    json_template = """{\"domain\": \"UserManagement\", \"event\": \"UserRegistered\", \"team\": \"RegistrationTeam\"},
    {\"domain\": \"DogManagement\", \"event\": \"DogProfileCreated\", \"team\": \"DogManagementTeam\"},
    {\"domain\": \"DogManagement\", \"event\": \"DogProfileUpdated\", \"team\": \"DogManagementTeam\"},
    {\"domain\": \"WalkManagement\", \"event\": \"WalkRequested\", \"team\": \"WalkTeam\"},
    {\"domain\": \"WalkManagement\", \"event\": \"WalkScheduled\", \"team\": \"SchedulingTeam\"},
    {\"domain\": \"WalkManagement\", \"event\": \"WalkerAssigned\", \"team\": \"SchedulingTeam\"},
    {\"domain\": \"WalkManagement\", \"event\": \"WalkInitiated\", \"team\": \"WalkerTeam\"},
    {\"domain\": \"WalkManagement\", \"event\": \"WalkInProgress\", \"team\": \"WalkerTeam\"},
    {\"domain\": \"WalkManagement\", \"event\": \"WalkCompleted\", \"team\": \"WalkerTeam\"},
    {\"domain\": \"PaymentManagement\", \"event\": \"PaymentMade\", \"team\": \"FinanceTeam\"},
    {\"domain\": \"PaymentManagement\", \"event\": \"PaymentReceived\", \"team\": \"FinanceTeam\"},
    {\"domain\": \"Support\", \"event\": \"SupportTicketRaised\", \"team\": \"CustomerSupportTeam\"},
    {\"domain\": \"Support\", \"event\": \"SupportTicketClosed\", \"team\": \"CustomerSupportTeam\"}"""

    chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user"
    , "content": f"""Return the JSON only in your response for an event catalog that supports a software
    architecture for an {architecture_required} system using this JSON as the example template {json_template}"""}])

    out = chat_completion['choices'][0]['message']['content']

    architecture_required_path = architecture_required.replace(" ","_")

    with open(f"event_lists/{architecture_required_path}/{architecture_required_path}_v2.json", "w") \
    as outfile:
        outfile.write(out)

if __name__ == '__main__':
    main()
