# 🧠 Gemini 2.0 Flash Chatbot

This is a simple **AI-powered chatbot** built using **Google’s Gemini 2.0 Flash model**.  
The chatbot allows users to interact with Gemini directly from the command line using the `google-generativeai` Python library.

---

## 🚀 Features

- Interactive terminal-based chatbot  
- Powered by **Google Gemini 2.0 Flash**  
- Handles continuous conversation  
- Graceful error handling and user input validation  

---

## 🛠️ Requirements

Before running the chatbot, make sure you have the following installed:

- **Python 3.8+**
- Required library:
  ```bash
  pip install google-generativeai
  ```

---

## ⚙️ Setup Instructions

1. **Clone this repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Install dependencies:**
   ```bash
   pip install google-generativeai
   ```

3. **Set your Gemini API Key:**
   Replace the existing key in the script with your own:
   ```python
   GEMINI_API_KEY = "YOUR_API_KEY"
   ```

   > 🔒 **Important:** Never upload or share your API key publicly on GitHub.  
   > Instead, store it securely using an environment variable:
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```
   And modify your script like this:
   ```python
   import os
   GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
   ```

4. **Run the chatbot:**
   ```bash
   python 1st.py
   ```

---

## 💬 Usage

- Type your messages to chat with Gemini.
- Type `quit` to end the conversation.
- If you send an empty message, the chatbot will prompt you to type something.

---

## 🧩 Example Interaction

```
You: Hello!
Gemini: Hi there! How can I assist you today?

You: Tell me a joke.
Gemini: Why don’t programmers like nature? It has too many bugs.

You: quit
Goodbye! Thanks for chatting with Gemini 2.0 Flash.
```

---

## ⚠️ Notes

- Keep your API key private.
- This chatbot runs on **Gemini 2.0 Flash**, which is optimized for speed and efficiency.
- You can expand this project into a GUI app or web interface later.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
