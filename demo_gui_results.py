"""
DÉMONSTRATION - Les Résultats S'Affichent dans la GUI
======================================================

Ce fichier montre exactement comment les résultats apparaissent
dans l'interface graphique (pas dans le terminal).
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox

def analyze_sample_text():
    """Analyse un texte exemple et affiche les résultats dans la GUI"""
    
    # Récupérer le texte
    text = text_input.get('1.0', tk.END).strip()
    
    if not text:
        messagebox.showwarning("Attention", "Veuillez entrer du texte!")
        return
    
    # Simuler une analyse
    word_count = len(text.split())
    
    # Déterminer un verdict simple
    if word_count > 20:
        verdict = "PROBABLEMENT GÉNÉRÉ PAR L'IA"
        color = 'red'
        emoji = "🤖"
        score = 70
    elif word_count > 10:
        verdict = "INCERTAIN"
        color = 'orange'
        emoji = "❓"
        score = 50
    else:
        verdict = "PROBABLEMENT ÉCRIT PAR UN HUMAIN"
        color = 'green'
        emoji = "✍️"
        score = 25
    
    # AFFICHER LES RÉSULTATS DANS LA GUI (pas le terminal!)
    results_text.configure(state=tk.NORMAL)
    results_text.delete('1.0', tk.END)
    
    # Verdict
    results_text.insert(tk.END, f"\n{emoji} Verdict: ", 'title')
    results_text.insert(tk.END, f"{verdict}\n\n", 'verdict')
    results_text.tag_config('verdict', foreground=color, font=('Arial', 12, 'bold'))
    
    # Détails
    results_text.insert(tk.END, "📊 Détails de l'analyse:\n", 'title')
    results_text.insert(tk.END, "─" * 50 + "\n")
    results_text.insert(tk.END, f"• Score IA: {score}%\n")
    results_text.insert(tk.END, f"• Nombre de mots: {word_count}\n")
    results_text.insert(tk.END, f"• Texte: {text[:30]}...\n\n")
    
    # Interprétation
    results_text.insert(tk.END, "💡 Interprétation:\n", 'title')
    results_text.insert(tk.END, "─" * 50 + "\n")
    if score >= 60:
        results_text.insert(tk.END, "Le texte semble généré par une IA.\n")
    elif score >= 40:
        results_text.insert(tk.END, "Résultat incertain.\n")
    else:
        results_text.insert(tk.END, "Le texte semble écrit par un humain.\n")
    
    results_text.configure(state=tk.DISABLED)
    
    # Mettre à jour la barre de statut
    status_label.config(text="✓ Analyse terminée - Résultats affichés ci-dessus!")

# Créer la fenêtre
root = tk.Tk()
root.title("DÉMONSTRATION - Résultats dans la GUI")
root.geometry("700x600")
root.configure(bg='#1a1a2e')

# Titre
title = tk.Label(root, 
                text="LES RÉSULTATS S'AFFICHENT ICI DANS LA FENÊTRE\n(Pas dans le terminal!)", 
                font=('Arial', 14, 'bold'),
                bg='#1a1a2e', 
                fg='#00d9ff',
                pady=15)
title.pack()

# Zone de texte
input_frame = tk.LabelFrame(root, 
                           text="📝 Entrez du texte à analyser:",
                           font=('Arial', 11, 'bold'),
                           bg='#16213e', 
                           fg='#00d9ff',
                           padx=10,
                           pady=10)
input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

text_input = scrolledtext.ScrolledText(input_frame,
                                       font=('Arial', 11),
                                       bg='#1a1a2e',
                                       fg='white',
                                       height=5,
                                       wrap=tk.WORD)
text_input.pack(fill=tk.BOTH, expand=True)
text_input.insert('1.0', "Tapez votre texte ici...\n\n"
                         "Exemple: En effet, il est important de noter que "
                         "l'intelligence artificielle représente un domaine "
                         "en pleine expansion.")

# Bouton ANALYSER
analyze_btn = tk.Button(root,
                       text="🔍 ANALYSER",
                       command=analyze_sample_text,
                       font=('Arial', 13, 'bold'),
                       bg='#00d9ff',
                       fg='#16213e',
                       padx=40,
                       pady=12,
                       cursor='hand2')
analyze_btn.pack(pady=15)

# Zone de RÉSULTATS (où tout s'affiche!)
results_frame = tk.LabelFrame(root, 
                             text="📊 RÉSULTATS (s'affichent ici dans la fenêtre!):",
                             font=('Arial', 11, 'bold'),
                             bg='#16213e', 
                             fg='#00d9ff',
                             padx=10,
                             pady=10)
results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

results_text = scrolledtext.ScrolledText(results_frame,
                                        font=('Consolas', 10),
                                        bg='#1a1a2e',
                                        fg='white',
                                        height=10,
                                        wrap=tk.WORD,
                                        state=tk.DISABLED)
results_text.pack(fill=tk.BOTH, expand=True)
results_text.tag_config('title', foreground='#00d9ff', font=('Arial', 11, 'bold'))

# Message initial
results_text.configure(state=tk.NORMAL)
results_text.insert('1.0', "Cliquez sur ANALYSER pour voir les résultats s'afficher ici!\n\n"
                           "Les résultats apparaîtront dans cette zone,\n"
                           "PAS dans le terminal/console.")
results_text.configure(state=tk.DISABLED)

# Barre de statut
status_label = tk.Label(root, 
                       text="Prêt à analyser - Les résultats s'afficheront dans la fenêtre ci-dessus",
                       bg='#0f3460', 
                       fg='#94b9ff',
                       font=('Arial', 9),
                       anchor=tk.W,
                       padx=10, 
                       pady=5)
status_label.pack(fill=tk.X, padx=20, pady=(0, 10))

# Instructions
print("="*70)
print("DÉMONSTRATION - RÉSULTATS DANS LA GUI")
print("="*70)
print()
print("1. Tapez ou modifiez le texte dans la zone en haut")
print("2. Cliquez sur le bouton ANALYSER")
print("3. LES RÉSULTATS S'AFFICHENT DANS LA FENÊTRE (zone en bas)")
print("4. PAS dans ce terminal!")
print()
print("="*70)

root.mainloop()
