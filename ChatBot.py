import tkinter as tk
import openai

# Agrega tu clave de API de OpenAI aquí
openai.api_key = "AQUI_TU_API_KEY"

def chatbot_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def send_message():
    prompt = user_input.get()
    response = chatbot_response(prompt)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Humano: " + prompt + "\n")
    chat_log.insert(tk.END, "Bot: " + response + "\n")
    chat_log.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)

root = tk.Tk()
root.title("Chatbot")

chat_log = tk.Text(root, bd=1, bg="white", fg="black", state=tk.DISABLED)
chat_log.pack(fill=tk.BOTH, expand=True)

user_input = tk.Entry(root)
user_input.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
