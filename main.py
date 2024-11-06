import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import from Pillow
import os  # To check for file existence

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

        # Initialize main widgets
        self.story_label = tk.Label(self.root, textvariable=self.story_text, wraplength=400)
        self.image_label = tk.Label(self.root)  # Image display label
        self.button1 = tk.Button(self.root, text="", command=lambda: self.make_choice(1))
        self.button2 = tk.Button(self.root, text="", command=lambda: self.make_choice(2))

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
        try:
            next_node = current_story[self.current_node]['choices'][choice]['next_node']
            if isinstance(next_node, int):
                self.current_node = next_node
            else:
                self.current_story_key = next_node
                self.current_node = 1
            self.update_story()
        except KeyError:
            messagebox.showerror("Error", f"Choice {choice} not available at this node.")
            return

    def update_story(self):
        # Get the current story and node
        try:
            current_story = self.stories[self.current_story_key]
            story_data = current_story[self.current_node]
        except KeyError:
            messagebox.showerror("Error", f"Could not load story node {self.current_node}.")
            return

        # Update the story text
        story_text = story_data['text'].format(name=self.player_name.get())
        self.story_text.set(story_text)

        print(f"Current story text: {story_text}")  # Debugging print for story text

        # Load and display image if it exists for the current node
        image_path = story_data.get('image', None)
        if image_path and os.path.exists(image_path):
            img = Image.open(image_path)
            self.story_image = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.story_image)
            self.image_label.pack(pady=10)  # Ensure image_label is packed
        else:
            self.image_label.config(image='')  # Clear image if none for this node
            self.image_label.pack_forget()  # Ensure image_label is hidden if no image

        # Get and display choices for the current node
        choices = story_data.get('choices', {})
        print(f"Choices for node {self.current_node}: {choices}")  # Debugging print for choices

        # Update button1 for the first choice
        if 1 in choices:
            self.button1.config(text=choices[1]['text'], command=lambda: self.make_choice(1))
            self.button1.pack(side=tk.LEFT, padx=20, pady=10)
        else:
            self.button1.config(text="")  # Clear button1 text if no choice

        # Update button2 for the second choice if it exists
        if 2 in choices:
            self.button2.config(text=choices[2]['text'], command=lambda: self.make_choice(2))
            self.button2.pack(side=tk.RIGHT, padx=20, pady=10)
        else:
            self.button2.pack_forget()  # Hide button2 if only one choice

        # Print the packed widget structure for debugging layout
        for widget in self.root.pack_slaves():
            print(widget)  # Check widget order and visibility



# Create the main window
root = tk.Tk()
game = StoryGame(root)

# Run the application
root.mainloop()
