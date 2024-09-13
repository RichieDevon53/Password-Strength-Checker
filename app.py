import customtkinter
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv("data.csv", on_bad_lines = "skip")
data.dropna(inplace=True)
with open('pickle/model.pkl', 'rb') as file1:
    model = pickle.load(file1)

def word(password):
    character=[]
    for i in password:
        character.append(i)
    return character

x = data["password"]
tdif = TfidfVectorizer(tokenizer=word)
tdif.fit(x)

def button_callback():
    password = entry.get()
    password_list = [password]
    password_trans = tdif.transform(password_list)
    strength = model.predict(password_trans)
    if strength == 0 :
        strength_label = 'Weak'
    elif strength == 1 :
        strength_label = 'Medium'
    elif strength == 2 :
        strength_label = 'Strong'
    label.configure(text=f"Password Strength: {strength_label}")

app = customtkinter.CTk()
app.title("PSC")
app.iconbitmap('password.ico')
app.geometry("300x225")
app.grid_columnconfigure(0, weight=1)

title_label = customtkinter.CTkLabel(app, text="Password Strength Checker", font=("Arial", 20, "bold"))
title_label.grid(row=0, column=0, padx=20, pady=(10,0))

subtitle_label = customtkinter.CTkLabel(app, text="Check the strength of your password.", font=("Arial", 12))
subtitle_label.grid(row=1, column=0, padx=20)

entry = customtkinter.CTkEntry(app, placeholder_text="Enter your password")
entry.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

button = customtkinter.CTkButton(app, text="Check Strength", command=button_callback)
button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

label = customtkinter.CTkLabel(app, text="", font=("Arial", 16, "bold"))
label.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

app.mainloop()

