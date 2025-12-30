"""
Test simple pour vérifier que le bouton ANALYSER fonctionne
"""
import tkinter as tk
from tkinter import scrolledtext, messagebox

def test_analyze():
    """Fonction de test pour l'analyse"""
    # Récupérer le texte
    text = text_input.get('1.0', tk.END).strip()
    
    print(f"DEBUG: Bouton cliqué!")
    print(f"DEBUG: Texte récupéré: '{text}'")
    print(f"DEBUG: Longueur: {len(text)}")
    
    if not text:
        messagebox.showwarning("Attention", "Veuillez entrer du texte!")
        return
    
    # Simuler une analyse simple
    word_count = len(text.split())
    
    # Afficher les résultats
    results_text.configure(state=tk.NORMAL)
    results_text.delete('1.0', tk.END)
    results_text.insert(tk.END, f"✅ ANALYSE RÉUSSIE!\n\n")
    results_text.insert(tk.END, f"📊 Résultats:\n")
    results_text.insert(tk.END, f"• Nombre de mots: {word_count}\n")
    results_text.insert(tk.END, f"• Texte analysé: {text[:50]}...\n")
    results_text.configure(state=tk.DISABLED)
    
    status_label.config(text="✓ Analyse terminée!")
    print("DEBUG: Résultats affichés!")

# Créer la fenêtre
root = tk.Tk()
root.title("Test Bouton ANALYSER")
root.geometry("600x500")
root.configure(bg='#1a1a2e')

# Titre
title = tk.Label(root, text="TEST DU BOUTON ANALYSER", 
                font=('Arial', 16, 'bold'),
                bg='#1a1a2e', fg='#00d9ff')
title.pack(pady=20)

# Zone de texte
input_frame = tk.LabelFrame(root, text="Tapez du texte ici:",
                           font=('Arial', 10, 'bold'),
                           bg='#16213e', fg='#00d9ff')
input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

text_input = scrolledtext.ScrolledText(input_frame,
                                       font=('Arial', 11),
                                       bg='#1a1a2e',
                                       fg='white',
                                       height=5)
text_input.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
text_input.insert('1.0', "Tapez quelque chose ici puis cliquez sur ANALYSER...")

# Bouton
analyze_btn = tk.Button(root,
                       text="🔍 ANALYSER",
                       command=test_analyze,
                       font=('Arial', 12, 'bold'),
                       bg='#00d9ff',
                       fg='#16213e',
                       padx=30,
                       pady=10,
                       cursor='hand2')
analyze_btn.pack(pady=10)

# Zone de résultats
results_frame = tk.LabelFrame(root, text="Résultats:",
                             font=('Arial', 10, 'bold'),
                             bg='#16213e', fg='#00d9ff')
results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

results_text = scrolledtext.ScrolledText(results_frame,
                                        font=('Arial', 10),
                                        bg='#1a1a2e',
                                        fg='white',
                                        height=5,
                                        state=tk.DISABLED)
results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Barre de statut
status_label = tk.Label(root, text="Prêt à analyser",
                       bg='#0f3460', fg='#94b9ff',
                       font=('Arial', 9),
                       anchor=tk.W,
                       padx=10, pady=5)
status_label.pack(fill=tk.X, padx=20, pady=(0, 10))

print("="*60)
print("TEST DU BOUTON ANALYSER")
print("="*60)
print("1. Tapez du texte dans la zone de texte")
print("2. Cliquez sur le bouton ANALYSER")
print("3. Regardez les résultats s'afficher")
print("="*60)

root.mainloop()
