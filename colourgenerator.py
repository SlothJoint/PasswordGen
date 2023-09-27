import random
import tkinter as tk

# Function to generate a random output
def generate_output():
    random_number = random.randint(0, 2000)
    random_colour = random.choice(colors)
    random_colour2 = random.choice(colors)
    output = f'{random_colour}.{random_colour2}{random_number}'
    result_label.config(text=output)

# Create the main window
window = tk.Tk()
window.title("Random Output Generator")

# Create a label to display the random output
result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

# Create a button to generate the random output
generate_button = tk.Button(window, text="Generate", command=generate_output)
generate_button.pack()

# List of colors
colors = [
    'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown',
    'gray', 'black', 'white', 'cyan', 'magenta', 'lime', 'teal', 'olive',
    'navy', 'maroon', 'gold', 'indigo', 'turquoise', 'lavender', 'beige',
    'coral', 'violet', 'crimson', 'fuchsia', 'mint', 'ruby', 'emerald',
    'sapphire', 'amber', 'scarlet', 'ivory', 'lemon', 'peach', 'plum', 'taupe',
    'sienna', 'aquamarine', 'bronze', 'copper', 'rose', 'orchid', 'salmon',
    'tan', 'teal', 'rust', 'periwinkle', 'khaki', 'slate', 'mauve', 'azure',
    'chartreuse', 'silver', 'turquoise', 'pumpkin', 'lavender', 'charcoal',
    'sepia', 'burgundy', 'celadon', 'cerulean', 'champagne', 'cobalt',
    'crimson', 'cyan', 'emerald', 'garnet', 'indigo', 'magenta', 'maroon',
    'obsidian', 'olive', 'opalescent', 'pearl', 'periwinkle', 'platinum',
    'rose', 'sapphire', 'scarlet', 'topaz', 'ultramarine', 'vermilion',
    'vermillion', 'viridian', 'amethyst', 'aqua', 'aquamarine', 'auburn',
    'avocado', 'cerulean', 'champagne', 'cobalt', 'fandango', 'fern', 'fuchsia',
    'goldenrod', 'lilac', 'magenta', 'obsidian', 'persimmon', 'sepia', 'tangerine'
]

# Start the Tkinter main loop
window.mainloop()
