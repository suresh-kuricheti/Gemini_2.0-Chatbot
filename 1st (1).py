import google.generativeai as genai


GEMINI_API_KEY = "AIzaSyCn0syMz62wbBPIAxdZEXNQKxi4pPIsB9Y"  

# Configure Gemini with the API key
genai.configure(api_key=GEMINI_API_KEY)

# Create the generative model
model = genai.GenerativeModel('gemini-2.0-flash')

# Start chat session
chat = model.start_chat(history=[])

print("here the AB chatbot is ready")


while True:
    user_input = input("You: ").strip()
    
    if not user_input:
        print("Gemini needs some input to respond!")
        continue

    if user_input.lower() == "quit":
        print("\nGoodbye! Thanks for chatting with Gemini 2.0 Flash.")
        break

    try:
        response = chat.send_message(user_input, stream=True)
        print("Gemini:", end=" ")
        for chunk in response:
            print(chunk.text, end="")
        print("\n")
    except Exception as e:
        print(f"Gemini encountered an error: {e}\n")
