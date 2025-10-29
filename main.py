import tkinter as tk
from timeit import default_timer as timer
import random
class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("600x350")

        self.sentences = [
    "It is only with the heart that one can see rightly; what is essential is invisible to the eye",
    "Not all those who wander are lost",
    "It was the best of times, it was the worst of times",
    "Whatever our souls are made of, his and mine are the same",
    "So it goes",
    "All we have to decide is what to do with the time that is given us",
    "It does not do to dwell on dreams and forget to live",
    "Stay gold, Ponyboy, stay gold",
    "Real courage is when you know you're licked before you begin, but you begin anyway",
    "Tomorrow is always fresh, with no mistakes in it yet",
    "So we beat on, boats against the current, borne back ceaselessly into the past",
    "All animals are equal, but some animals are more equal than others",
    "It’s no use going back to yesterday, because I was a different person then",
    "You never really understand a person until you consider things from his point of view",
    "There is some good in this world, and it’s worth fighting for",
    "Call me Ishmael",
    "The only way out of the labyrinth of suffering is to forgive",
    "We accept the love we think we deserve",
    "Even the darkest night will end and the sun will rise",
    "It matters not what someone is born, but what they grow to be"
        ]
        
        self.start_time = None
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the UI components."""
        self.sentence = random.choice(self.sentences)
        
        self.label_sentence = tk.Label(self.root, text=self.sentence, font=("Arial", 14), wraplength=500)
        self.label_sentence.pack(pady=20)
        
        self.label_prompt = tk.Label(self.root, text="Type the above sentence:", font=("Arial", 12))
        self.label_prompt.pack()
        
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.check_result())  # Allow Enter key to submit
        
        self.button_done = tk.Button(self.root, text="Done", command=self.check_result, width=12, bg="#C2F8CB")
        self.button_done.pack(pady=5)
        
        self.button_retry = tk.Button(self.root, text="Try Again", command=self.reset_test, width=12, bg="#C2F8CB")
        self.button_retry.pack(pady=5)
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)
        
        self.start_time = timer() 

    def check_result(self):
        typed_text = self.entry.get()
        if typed_text == self.sentence:
            end_time = timer()
            time_taken = round(end_time - self.start_time, 2)
            words = len(self.sentence.split())
            wpm = round((words / time_taken) * 60, 2)  # Words per minute calculation
            self.result_label.config(text=f"Time: {time_taken} sec | WPM: {wpm}", fg="#206F3D")
        else:
            self.result_label.config(text="Incorrect typing. Try again!", fg="#91171f")

    def reset_test(self):
        self.sentence = random.choice(self.sentences)
        self.label_sentence.config(text=self.sentence)
        self.entry.delete(0, tk.END)  
        self.result_label.config(text="")
        self.start_time = timer()  

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()