import tkinter as tk
from timeit import default_timer as timer
import random

class SpeedTypingTest:
    def __init__(self,root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("600x450")
        self.sentences = [
    "It is only with the heart that one can see rightly; what is essential is invisible to the eye. – The Little Prince",
    "Not all those who wander are lost. – The Lord of the Rings",
    "It was the best of times, it was the worst of times. – A Tale of Two Cities",
    "Whatever our souls are made of, his and mine are the same. – Wuthering Heights",
    "All we have to decide is what to do with the time that is given us. – The Fellowship of the Ring",
    "It does not do to dwell on dreams and forget to live. – Harry Potter and the Sorcerer’s Stone",
    "Real courage is when you know you're licked before you begin, but you begin anyway. – To Kill a Mockingbird",
    "Tomorrow is always fresh, with no mistakes in it yet. – Anne of Green Gables",
    "So we beat on, boats against the current, borne back ceaselessly into the past. – The Great Gatsby",
    "All animals are equal, but some animals are more equal than others. – Animal Farm",
    "It’s no use going back to yesterday, because I was a different person then. – Alice’s Adventures in Wonderland",
    "You never really understand a person until you consider things from his point of view. – To Kill a Mockingbird",
    "There is some good in this world, and it’s worth fighting for. – The Two Towers",
    "The only way out of the labyrinth of suffering is to forgive. – Looking for Alaska",
    "We accept the love we think we deserve. – The Perks of Being a Wallflower",
    "Even the darkest night will end and the sun will rise. – Les Misérables",
    "It matters not what someone is born, but what they grow to be. – Harry Potter and the Goblet of Fire"
]
    def setup_ui(self):
        self.sentence = random.choice(self.sentences)
        self.label_sentence = tk.Label(self.root,text=self.sentence, font=("Arial",14), wraplength=500)
        self.label_sentence.pack(pady=20)
        self.label_prompt = tk.Label(self.root,text="Type the above sentence:",font=("Arial",12))
        self.label_prompt.pack(pady=10)
        self.entry = tk.Entry(self.root,width=50)
        self.entry.pack(pady=10)
        self.entry.bind("Return",lambda event: self.check__result())
        self.button_done = tk.Button(self.root, text="Done", command=self.check__result,width=12,bg="#1C3144")
        self.button_done.pack(pady=5)
        self.button_retry = tk.Button(self.root, text="Try again ", command=self.reset_test,width=12,bg="#596F62")
        self.button_retry.pack(pady=5)
        self.button_retry = tk.Button(self.root, text="Try Again", command=self.reset_test, width=12, bg="#70161E")
        self.button_retry.pack(pady=5)
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)
        self.start_time = timer()
    def check__result(self):
        typed_test = self.entry.get()
        if typed_test == self.sentence:
            end_time = timer()
            time_taken = round(end_time - self.start_time,2)
            words = len(self.sentence.split())
            wpm = round((words/time_taken)*60,2)
            self.result_label.config(text=f"Time Taken:{time_taken} sec | WPM: {wpm}",fg="#7EA16B")
        else:
            self.result_label.config(text=f"Incorrect TypingTry again!)",fg="#74121d")
    def reset_test(self):
        pass
