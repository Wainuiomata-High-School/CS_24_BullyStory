import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import from Pillow
import json  # For saving and loading the game state
import os  # For file path checks
import tkinter.filedialog as fd

from Ending_per1 import bully_story
from Ending_vic1 import victim_story


class StoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Story Book Game")
        self.story_text = tk.StringVar()
        self.player_name = tk.StringVar()
        self.story_image = None  # To keep a reference to the image
        self.bind_keys()

        self.stories = {
            'bully': bully_story,
            'victim': victim_story
        }

        self.current_story_key = ''
        self.current_node = 1

        # Set up intro screen and menu
        self.setup_intro_screen()
        self.setup_menu()
        
    def bind_keys(self):
        # Bind "P" key to open pause menu globally
        self.root.bind_all("<p>", lambda event: self.pause_game())
        print("Keys bound")  # Debug to confirm method execution

    def setup_intro_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter your name:").pack(pady=10)
        tk.Entry(self.root, textvariable=self.player_name).pack(pady=50)

        tk.Button(self.root, text="Begin Zach's story", command=lambda: self.start_game('victim')).pack(pady=10)
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
        self.current_node = 1  # Start at the beginning
        self.setup_game_screen()
        self.update_story()  # Ensure story and buttons are set up correctly from the beginning


    def restart_game(self):
        self.current_node = 1  # Reset to the starting node
        self.current_story_key = 'victim'  # Or the key of your starting story
        self.story_text.set("Welcome back! Ready to start Zach's journey again?")  # Reset the displayed text
        self.setup_intro_screen()  # Go back to the introduction screen


    def pause_game(self):
        print("Pause menu triggered")
        # Disable main choice buttons to pause interaction
        self.button1.config(state=tk.DISABLED)
        self.button2.config(state=tk.DISABLED)
        
        # Create a popup window for the pause menu
        pause_popup = tk.Toplevel(self.root)
        pause_popup.title("Game Paused")
        pause_popup.geometry("200x150")  # Set a size for better layout

        pause_label = tk.Label(pause_popup, text="Game is paused.", font=("Arial", 12))
        pause_label.pack(pady=10)

        resume_button = tk.Button(pause_popup, text="Resume", command=lambda: self.resume_game(pause_popup))
        resume_button.pack(pady=5)

        save_button = tk.Button(pause_popup, text="Save", command=self.save_game)
        save_button.pack(pady=5)

        save_button = tk.Button(pause_popup, text="Restart", command=self.restart_game)
        save_button.pack(pady=5)

        quit_button = tk.Button(pause_popup, text="Quit", command=self.quit_game)
        quit_button.pack(pady=5)

        pause_popup.transient(self.root)
        pause_popup.grab_set()
        pause_popup.protocol("WM_DELETE_WINDOW", lambda: self.resume_game(pause_popup))

    def resume_game(self, pause_popup):
        self.button1.config(state=tk.NORMAL)
        self.button2.config(state=tk.NORMAL)
        pause_popup.destroy()

    def save_game(self):
        save_dir = "saves"
        os.makedirs(save_dir, exist_ok=True)
        
        base_filename = os.path.join(save_dir, f"save_{self.player_name.get()}")
        index = 1
        filename = f"{base_filename}_{index}.json"
        while os.path.exists(filename):
            index += 1
            filename = f"{base_filename}_{index}.json"
        
        game_state = {
            "player_name": self.player_name.get(),
            "current_story_key": self.current_story_key,
            "current_node": self.current_node
        }
        
        try:
            with open(filename, "w") as save_file:
                json.dump(game_state, save_file)
            messagebox.showinfo("Save Game", f"Game saved successfully as {filename}.")
        except Exception as e:
            messagebox.showerror("Save Game", f"Failed to save game: {e}")

    def load_game(self):
        save_dir = "saves"
        os.makedirs(save_dir, exist_ok=True)
        
        filename = fd.askopenfilename(
            initialdir=save_dir,
            title="Select Save File",
            filetypes=[("JSON files", "*.json")]
        )
        
        if filename:
            try:
                with open(filename, "r") as save_file:
                    game_state = json.load(save_file)
                
                self.player_name.set(game_state["player_name"])
                self.current_story_key = game_state["current_story_key"]
                self.current_node = game_state["current_node"]
                self.setup_game_screen()
                self.update_story()
                messagebox.showinfo("Load Game", "Game loaded successfully.")
            
            except (FileNotFoundError, KeyError, json.JSONDecodeError) as e:
                messagebox.showwarning("Load Game", f"Failed to load the game: {e}")

    def quit_game(self):
        if messagebox.askyesno("Quit Game", "Do you want to save before quitting?"):
            self.save_game()
        self.root.quit()

    def make_choice(self, choice):
        current_story = self.stories[self.current_story_key]
        current_node_data = current_story.get(self.current_node, {})

        # Check if choice exists for the current node
        if choice in current_node_data.get('choices', {}):
            next_node = current_node_data['choices'][choice]['next_node']

            # Check if the next node exists in the current story
            if isinstance(next_node, int) and next_node in current_story:
                self.current_node = next_node
                self.update_story()
            elif isinstance(next_node, str) and next_node in self.stories:
                # If next_node is a story key, switch stories and start at node 1
                self.current_story_key = next_node
                self.current_node = 1
                self.update_story()
            elif choice == 1 and current_node_data['choices'][1]['text'] == "Restart":
                # Reset game state for a clean restart
                self.current_node = 1
                self.current_story_key = 'victim'  # Or set this to the starting story
                self.setup_intro_screen()
            else:
                # Handle missing node or invalid story key
                messagebox.showerror("Error", "The chosen path does not lead to a valid node. Restarting...")
                self.setup_intro_screen()  # Reset to the intro screen
        else:
            messagebox.showwarning("Invalid Choice", "This choice is not available.")

    def update_story(self):
        current_story = self.stories[self.current_story_key]
        story_data = current_story[self.current_node]
        
        story_text = story_data['text'].format(name=self.player_name.get())
        self.story_text.set(story_text)

        image_path = story_data.get('image', None)
        print(f"Current node: {self.current_node}, Image path: {image_path}")  # Debugging line
        if image_path and os.path.exists(image_path):
            img = Image.open(image_path)
            self.story_image = ImageTk.PhotoImage(img)  # Keep reference to avoid garbage collection
            self.image_label.config(image=self.story_image)
            self.image_label.pack()  # Ensure image label is packed to display
        else:
            self.image_label.config(image='')  # Clear the image if not found
            self.image_label.pack_forget()  # Hide the label if no image

        choices = story_data.get('choices', {})
        self.button1.config(text=choices.get(1, {}).get('text', ""), state=tk.NORMAL if 1 in choices else tk.DISABLED)
        self.button2.config(text=choices.get(2, {}).get('text', ""), state=tk.NORMAL if 2 in choices else tk.DISABLED)
        


# Create the main window
root = tk.Tk()
game = StoryGame(root)

# Run the application
root.mainloop()

