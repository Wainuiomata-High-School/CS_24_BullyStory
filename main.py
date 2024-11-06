import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import from Pillow
import json  # For saving and loading the game state
import os  # For file path checks

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

        # Set up intro screen and menu
        self.setup_intro_screen()
        self.setup_menu()

    def setup_intro_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter your name:").pack(pady=10)
        tk.Entry(self.root, textvariable=self.player_name).pack(pady=50)

        tk.Button(self.root, text="Play as Bully", command=lambda: self.start_game('bully')).pack(pady=10)
        tk.Button(self.root, text="Play as Victim", command=lambda: self.start_game('victim')).pack(pady=10)
        tk.Button(self.root, text="Load Game", command=self.load_game).pack(pady=10)
        tk.Button(self.root, text="Quit", command=self.quit_game).pack(pady=10)

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

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        
        # Game menu
        game_menu = tk.Menu(menubar, tearoff=0)
        game_menu.add_command(label="Pause", command=self.pause_game)
        game_menu.add_command(label="Save", command=self.save_game)
        game_menu.add_command(label="Load", command=self.load_game)
        game_menu.add_separator()
        game_menu.add_command(label="Quit", command=self.quit_game)
        menubar.add_cascade(label="Game", menu=game_menu)
        
        # Attach the menubar to the root window
        self.root.config(menu=menubar)

    def start_game(self, story_key):
        if not self.player_name.get():
            messagebox.showwarning("Input Required", "Please enter your name.")
            return
        self.current_story_key = story_key
        self.current_node = 1
        self.setup_game_screen()
        self.update_story()

    def pause_game(self):
        # Disable buttons to pause interaction
        self.button1.config(state=tk.DISABLED)
        self.button2.config(state=tk.DISABLED)
        
        # Popup window for resume
        pause_popup = tk.Toplevel(self.root)
        pause_popup.title("Game Paused")
        tk.Label(pause_popup, text="Game is paused.").pack(pady=10)
        
        # Resume button
        tk.Button(pause_popup, text="Resume", command=lambda: self.resume_game(pause_popup)).pack(pady=10)

    def resume_game(self, pause_popup):
        # Enable buttons to resume interaction
        self.button1.config(state=tk.NORMAL)
        self.button2.config(state=tk.NORMAL)
        
        # Close pause popup
        pause_popup.destroy()

    def save_game(self):
        # Prepare the game state dictionary
        game_state = {
            "player_name": self.player_name.get(),
            "current_story_key": self.current_story_key,
            "current_node": self.current_node
        }
        # Save to JSON file
        with open("game_save.json", "w") as save_file:
            json.dump(game_state, save_file)
        messagebox.showinfo("Save Game", "Game saved successfully.")

    def load_game(self):
        try:
            # Load game state from file
            with open("game_save.json", "r") as save_file:
                game_state = json.load(save_file)
            # Restore game state
            self.player_name.set(game_state["player_name"])
            self.current_story_key = game_state["current_story_key"]
            self.current_node = game_state["current_node"]
            self.setup_game_screen()
            self.update_story()
            messagebox.showinfo("Load Game", "Game loaded successfully.")
        except (FileNotFoundError, KeyError):
            messagebox.showwarning("Load Game", "No saved game found.")

    def quit_game(self):
        if messagebox.askyesno("Quit Game", "Do you want to save before quitting?"):
            self.save_game()
        self.root.quit()

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
        story_data = current_story[self.current_node]
        
        # Update the story text
        story_text = story_data['text'].format(name=self.player_name.get())
        self.story_text.set(story_text)

        # Load and display image if it exists for the current node
        image_path = story_data.get('image', None)
        if image_path and os.path.exists(image_path):
            img = Image.open(image_path)
            self.story_image = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.story_image)
            self.image_label.pack(pady=10)
        else:
            self.image_label.config(image='')
            self.image_label.pack_forget()

        # Get and display choices for the current node
        choices = story_data.get('choices', {})
        if 1 in choices:
            self.button1.config(text=choices[1]['text'], command=lambda: self.make_choice(1))
            self.button1.pack(side=tk.LEFT, padx=20, pady=10)
        else:
            self.button1.config(text="")

        if 2 in choices:
            self.button2.config(text=choices[2]['text'], command=lambda: self.make_choice(2))
            self.button2.pack(side=tk.RIGHT, padx=20, pady=10)
        else:
            self.button2.pack_forget()

# Create the main window
root = tk.Tk()
game = StoryGame(root)

# Run the application
root.mainloop()
