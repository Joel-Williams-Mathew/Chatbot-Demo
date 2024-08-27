import random
import json

# Load existing learned data from JSON file
def load_learned_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save learned data to JSON file
def save_learned_data(filename, learned_data):
    with open(filename, 'w') as file:
        json.dump(learned_data, file, indent=4)

def chatbot_response(user_input, learned_data):
    if user_input in learned_data:
        return learned_data[user_input]
    else:
        return "I'm still learning. Can you tell me more?"

# Main interaction loop
def main():
    learned_data = load_learned_data('knowledge_base.json')

    print("ChatBot: Hi there! I'm here to learn from you. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye!")
            break

        response = chatbot_response(user_input, learned_data)
        print("ChatBot:", response)

        if user_input not in learned_data:
            new_response = input("ChatBot: Oops, I didn't know that! What should I have said? ")
            learned_data[user_input] = new_response
            save_learned_data('knowledge_base.json', learned_data)
            print("ChatBot: Thanks for teaching me!")

if __name__ == "__main__":
    main()
