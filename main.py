import tkinter as tk
from tkinter import messagebox

from Ending_per1 import bully_story
from Ending_vic1 import victim_story

class StoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Story Book Game")
        self.story_text = tk.StringVar()
        self.player_name = tk.StringVar()
        self.story_image = None  # To keep a reference to the image

        self.stories = {
            'bully': bully_story,
            'victim': victim_story
        }

        self.current_story_key = ''
        self.current_node = 1

        self.setup_intro_screen()

    def setup_intro_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter your name:").pack(pady=10)
        tk.Entry(self.root, textvariable=self.player_name).pack(pady=50)

        tk.Button(self.root, text="Play as Bully", command=lambda: self.start_game('bully')).pack(pady=10)
        tk.Button(self.root, text="Play as Victim", command=lambda: self.start_game('victim')).pack(pady=10)

    def start_game(self, story_key):
        if not self.player_name.get():
            messagebox.showwarning("Input Required", "Please enter your name.")
            return
        self.current_story_key = story_key
        self.current_node = 1
        self.setup_game_screen()
        self.update_story()

    def setup_game_screen(self):
        self.clear_screen()

        self.story_label = tk.Label(self.root, textvariable=self.story_text, wraplength=400)
        self.story_label.pack(pady=20)

        self.image_label = tk.Label(self.root)  # Image display label
        self.image_label.pack(pady=10)

        self.button1 = tk.Button(self.root, text="", command=lambda: self.make_choice(1))
        self.button1.pack(side=tk.LEFT, padx=20, pady=10)

        self.button2 = tk.Button(self.root, text="", command=lambda: self.make_choice(2))
        self.button2.pack(side=tk.RIGHT, padx=20, pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def make_choice(self, choice):
        current_story = self.stories[self.current_story_key]
        next_node = current_story[self.current_node]['choices'][choice]['next_node']
        if isinstance(next_node, int):
            self.current_node = next_node
            self.update_story()
        else:
            self.current_story_key = next_node
            self.current_node = 1
            self.update_story()

    def update_story(self):
        current_story = self.stories[self.current_story_key]
        story_text = current_story[self.current_node]['text'].format(name=self.player_name.get())
        self.story_text.set(story_text)

        # Load and display image if it exists for the current node
        image_path = current_story[self.current_node].get('image', None)
        if image_path:
            self.story_image = tk.PhotoImage(file=image_path)
            self.image_label.config(image=self.story_image)
        else:
            self.image_label.config(image='')  # Clear image if none for this node

        choices = current_story[self.current_node]['choices']
        if len(choices) == 1:
            self.button1.config(text=choices[1]['text'], command=lambda: self.make_choice(1))
            self.button2.pack_forget()
        else:
            self.button1.config(text=choices[1]['text'], command=lambda: self.make_choice(1))
            self.button2.config(text=choices[2]['text'], command=lambda: self.make_choice(2))
            self.button2.pack(side=tk.RIGHT, padx=20, pady=10)
