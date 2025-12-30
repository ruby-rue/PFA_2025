import tkinter as tk
from tkinter import messagebox

def test_button():
    """Test simple pour vérifier si le bouton fonctionne"""
    messagebox.showinfo("Test", "✓ Le bouton fonctionne!")
    print("Button clicked!")

# Create window
root = tk.Tk()
root.title("Test Bouton")
root.geometry("400x300")

# Add label
label = tk.Label(root, text="Test du bouton Analyser", font=('Arial', 14))
label.pack(pady=20)

# Add text area
text_area = tk.Text(root, height=5, width=40)
text_area.pack(pady=10)
text_area.insert('1.0', "Tapez du texte ici...")

# Add button
button = tk.Button(root, 
                   text="🔍 TEST ANALYSER", 
                   command=test_button,
                   font=('Arial', 12, 'bold'),
                   bg='#00d9ff',
                   fg='#16213e',
                   padx=20,
                   pady=10)
button.pack(pady=20)

# Add instruction
instruction = tk.Label(root, text="Cliquez sur le bouton ci-dessus", font=('Arial', 10, 'italic'))
instruction.pack()

print("Application lancée. Cliquez sur le bouton pour tester.")

root.mainloop()
