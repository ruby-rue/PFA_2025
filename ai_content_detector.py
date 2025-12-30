import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from PIL import Image, ImageTk, ImageEnhance, ImageFilter
import re
from collections import Counter
import math
import os
from datetime import datetime

class AIContentDetector:
    def __init__(self, root):
        self.root = root
        self.root.title("Détecteur de Contenu IA - AI Content Detector")
        self.root.geometry("1000x750")
        self.root.configure(bg='#1a1a2e')
        
        # Variables
        self.current_image = None
        self.current_image_path = None
        self.animation_running = False
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Create gradient background
        self.create_gradient_background()
        
        # Main container with border
        container = tk.Frame(root, bg='#16213e', bd=2, relief=tk.FLAT)
        container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Header with gradient
        header_frame = tk.Frame(container, bg='#0f3460', height=100)
        header_frame.pack(fill=tk.X, padx=10, pady=(10, 5))
        header_frame.pack_propagate(False)
        
        # Animated title
        title_frame = tk.Frame(header_frame, bg='#0f3460')
        title_frame.pack(expand=True)
        
        self.title_label = tk.Label(title_frame, 
                                    text="🤖 DÉTECTEUR DE CONTENU IA", 
                                    font=('Segoe UI', 26, 'bold'), 
                                    bg='#0f3460', 
                                    fg='#00d9ff')
        self.title_label.pack()
        
        subtitle = tk.Label(title_frame, 
                           text="Analysez du texte ou des images pour détecter l'IA", 
                           font=('Segoe UI', 11, 'italic'), 
                           bg='#0f3460', 
                           fg='#94b9ff')
        subtitle.pack()
        
        # Tab control for Text/Image modes
        tab_frame = tk.Frame(container, bg='#16213e')
        tab_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(tab_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Configure notebook style
        style.configure('TNotebook', background='#16213e', borderwidth=0)
        style.configure('TNotebook.Tab', 
                       background='#0f3460', 
                       foreground='white',
                       padding=[20, 10],
                       font=('Segoe UI', 11, 'bold'))
        style.map('TNotebook.Tab',
                 background=[('selected', '#00d9ff')],
                 foreground=[('selected', '#16213e')])
        
        # TEXT TAB
        text_tab = tk.Frame(self.notebook, bg='#16213e')
        self.notebook.add(text_tab, text='📝 Analyse de Texte')
        
        # Input frame for text
        input_frame = tk.LabelFrame(text_tab, 
                                   text="  📄 Texte à analyser  ", 
                                   font=('Segoe UI', 12, 'bold'), 
                                   bg='#16213e', 
                                   fg='#00d9ff',
                                   bd=2,
                                   relief=tk.GROOVE)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(15, 10))
        
        # Text input with custom styling
        text_container = tk.Frame(input_frame, bg='#0f3460', bd=2, relief=tk.SUNKEN)
        text_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.text_input = scrolledtext.ScrolledText(text_container, 
                                                    wrap=tk.WORD, 
                                                    font=('Consolas', 11), 
                                                    bg='#1a1a2e',
                                                    fg='#ffffff',
                                                    insertbackground='#00d9ff',
                                                    selectbackground='#0f3460',
                                                    selectforeground='#ffffff',
                                                    height=10,
                                                    bd=0,
                                                    relief=tk.FLAT)
        self.text_input.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # IMAGE TAB
        image_tab = tk.Frame(self.notebook, bg='#16213e')
        self.notebook.add(image_tab, text='🖼️ Analyse d\'Image')
        
        # Image upload frame
        upload_frame = tk.LabelFrame(image_tab, 
                                    text="  📸 Image à analyser  ",
                                    font=('Segoe UI', 12, 'bold'),
                                    bg='#16213e',
                                    fg='#00d9ff',
                                    bd=2,
                                    relief=tk.GROOVE)
        upload_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(15, 10))
        
        # Image display area
        self.image_canvas = tk.Canvas(upload_frame, 
                                     bg='#0f3460', 
                                     highlightthickness=2,
                                     highlightbackground='#00d9ff',
                                     height=300)
        self.image_canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Placeholder text
        self.placeholder_text = self.image_canvas.create_text(
            300, 150,
            text="📸 Cliquez sur 'Charger Image' pour sélectionner une image",
            font=('Segoe UI', 12, 'italic'),
            fill='#94b9ff'
        )
        
        # Upload button
        upload_btn_frame = tk.Frame(upload_frame, bg='#16213e')
        upload_btn_frame.pack(pady=10)
        
        self.upload_btn = tk.Button(upload_btn_frame, 
                                    text="📁 Charger Image", 
                                    command=self.load_image,
                                    font=('Segoe UI', 11, 'bold'), 
                                    bg='#00d9ff',
                                    fg='#16213e',
                                    padx=25,
                                    pady=10,
                                    cursor='hand2',
                                    relief=tk.FLAT,
                                    activebackground='#00b8d4',
                                    activeforeground='#16213e')
        self.upload_btn.pack()
        
        # Button frame - common for both tabs
        button_frame = tk.Frame(container, bg='#16213e')
        button_frame.pack(pady=15)
        
        # Analyze button with gradient effect
        self.analyze_btn = tk.Button(button_frame, 
                                     text="🔍 ANALYSER", 
                                     command=self.analyze_content,
                                     font=('Segoe UI', 13, 'bold'), 
                                     bg='#00d9ff',
                                     fg='#16213e',
                                     padx=40,
                                     pady=12,
                                     cursor='hand2',
                                     relief=tk.FLAT,
                                     activebackground='#00b8d4',
                                     activeforeground='#16213e',
                                     state=tk.NORMAL)
        self.analyze_btn.pack(side=tk.LEFT, padx=5)
        self.analyze_btn.bind('<Enter>', lambda e: self.on_hover(self.analyze_btn, '#00b8d4'))
        self.analyze_btn.bind('<Leave>', lambda e: self.on_leave(self.analyze_btn, '#00d9ff'))
        
        # Clear button
        self.clear_btn = tk.Button(button_frame, 
                                   text="🗑️ EFFACER", 
                                   command=self.clear_all,
                                   font=('Segoe UI', 13, 'bold'), 
                                   bg='#e74c3c',
                                   fg='white',
                                   padx=40,
                                   pady=12,
                                   cursor='hand2',
                                   relief=tk.FLAT,
                                   activebackground='#c0392b',
                                   activeforeground='white',
                                   state=tk.NORMAL)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        self.clear_btn.bind('<Enter>', lambda e: self.on_hover(self.clear_btn, '#c0392b'))
        self.clear_btn.bind('<Leave>', lambda e: self.on_leave(self.clear_btn, '#e74c3c'))
        
        # Export button
        self.export_btn = tk.Button(button_frame, 
                                    text="💾 EXPORTER", 
                                    command=self.export_results,
                                    font=('Segoe UI', 13, 'bold'), 
                                    bg='#2ecc71',
                                    fg='white',
                                    padx=40,
                                    pady=12,
                                    cursor='hand2',
                                    relief=tk.FLAT,
                                    activebackground='#27ae60',
                                    activeforeground='white',
                                    state=tk.NORMAL)
        self.export_btn.pack(side=tk.LEFT, padx=5)
        self.export_btn.bind('<Enter>', lambda e: self.on_hover(self.export_btn, '#27ae60'))
        self.export_btn.bind('<Leave>', lambda e: self.on_leave(self.export_btn, '#2ecc71'))
        
        # Results frame with modern design
        results_frame = tk.LabelFrame(container, 
                                     text="  📊 Résultats de l'analyse  ",
                                     font=('Segoe UI', 12, 'bold'),
                                     bg='#16213e',
                                     fg='#00d9ff',
                                     bd=2,
                                     relief=tk.GROOVE)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 10))
        
        # Results display with custom styling
        results_container = tk.Frame(results_frame, bg='#0f3460', bd=2, relief=tk.SUNKEN)
        results_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.results_text = scrolledtext.ScrolledText(results_container, 
                                                     wrap=tk.WORD,
                                                     font=('Consolas', 10),
                                                     bg='#1a1a2e',
                                                     fg='#ffffff',
                                                     height=8,
                                                     bd=0,
                                                     relief=tk.FLAT,
                                                     state=tk.DISABLED)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Configure tags for colored text with better colors
        self.results_text.tag_configure('ai', foreground='#ff6b6b', font=('Consolas', 11, 'bold'))
        self.results_text.tag_configure('human', foreground='#51cf66', font=('Consolas', 11, 'bold'))
        self.results_text.tag_configure('uncertain', foreground='#ffd43b', font=('Consolas', 11, 'bold'))
        self.results_text.tag_configure('title', foreground='#00d9ff', font=('Consolas', 11, 'bold'))
        self.results_text.tag_configure('info', foreground='#94b9ff', font=('Consolas', 10))
        
        # Status bar
        self.status_bar = tk.Label(container, 
                                  text="Prêt à analyser", 
                                  bg='#0f3460', 
                                  fg='#94b9ff',
                                  font=('Segoe UI', 9),
                                  anchor=tk.W,
                                  padx=10,
                                  pady=5)
        self.status_bar.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        # Start title animation
        self.animate_title()
    
    def create_gradient_background(self):
        """Create a subtle gradient effect"""
        # Simply set the background color - gradient canvas caused issues
        pass
    
    def on_hover(self, button, color):
        """Change button color on hover"""
        button.config(bg=color)
    
    def on_leave(self, button, color):
        """Restore button color on leave"""
        button.config(bg=color)
    
    def animate_title(self):
        """Animate the title with color cycling"""
        colors = ['#00d9ff', '#00b8d4', '#0096aa', '#00b8d4', '#00d9ff']
        
        def cycle_colors(index=0):
            if self.animation_running:
                return
            self.title_label.config(fg=colors[index % len(colors)])
            self.root.after(1000, lambda: cycle_colors((index + 1) % len(colors)))
        
        cycle_colors()
    
    def load_image(self):
        """Load an image file"""
        file_path = filedialog.askopenfilename(
            title="Sélectionner une image",
            filetypes=[
                ("Images", "*.png *.jpg *.jpeg *.bmp *.gif"),
                ("Tous les fichiers", "*.*")
            ]
        )
        
        if file_path:
            try:
                # Load and display image
                image = Image.open(file_path)
                self.current_image_path = file_path
                
                # Resize image to fit canvas
                canvas_width = self.image_canvas.winfo_width()
                canvas_height = self.image_canvas.winfo_height()
                
                if canvas_width <= 1:
                    canvas_width = 600
                if canvas_height <= 1:
                    canvas_height = 300
                
                image.thumbnail((canvas_width - 20, canvas_height - 20), Image.Resampling.LANCZOS)
                
                # Convert to PhotoImage
                photo = ImageTk.PhotoImage(image)
                self.current_image = photo
                
                # Display on canvas
                self.image_canvas.delete("all")
                self.image_canvas.create_image(
                    canvas_width // 2,
                    canvas_height // 2,
                    image=photo,
                    anchor=tk.CENTER
                )
                
                self.status_bar.config(text=f"✓ Image chargée: {os.path.basename(file_path)}")
                
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de charger l'image:\n{str(e)}")
                self.status_bar.config(text="✗ Erreur lors du chargement de l'image")
    
    def analyze_content(self):
        """Analyze either text or image based on active tab"""
        try:
            current_tab = self.notebook.index(self.notebook.select())
            
            self.status_bar.config(text="🔄 Démarrage de l'analyse...")
            self.root.update_idletasks()
            
            if current_tab == 0:  # Text tab
                self.analyze_text()
            else:  # Image tab
                self.analyze_image()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'analyse:\n{str(e)}")
            self.status_bar.config(text=f"✗ Erreur: {str(e)}")
    
    def analyze_image(self):
        """Analyze an image for AI generation indicators"""
        if not self.current_image_path:
            messagebox.showwarning("Attention", "Veuillez d'abord charger une image!")
            return
        
        self.status_bar.config(text="🔄 Analyse de l'image en cours...")
        self.root.update()
        
        try:
            image = Image.open(self.current_image_path)
            
            # Analyze image properties
            width, height = image.size
            format_type = image.format
            mode = image.mode
            
            # Calculate various metrics
            ai_score = 0
            indicators = {}
            
            # 1. Check for perfect dimensions (AI often generates specific sizes)
            common_ai_sizes = [(512, 512), (1024, 1024), (768, 768), (256, 256)]
            if (width, height) in common_ai_sizes:
                ai_score += 25
                indicators['dimensions_suspectes'] = True
            else:
                indicators['dimensions_suspectes'] = False
            
            # 2. Analyze color distribution
            if mode == 'RGB':
                pixels = list(image.getdata())
                if len(pixels) > 1000:
                    sample = pixels[::len(pixels)//1000]
                else:
                    sample = pixels
                
                # Calculate color entropy
                r_values = [p[0] for p in sample]
                g_values = [p[1] for p in sample]
                b_values = [p[2] for p in sample]
                
                r_entropy = self.calculate_color_entropy(r_values)
                g_entropy = self.calculate_color_entropy(g_values)
                b_entropy = self.calculate_color_entropy(b_values)
                
                avg_entropy = (r_entropy + g_entropy + b_entropy) / 3
                indicators['entropie_couleur'] = avg_entropy
                
                # Very uniform colors might indicate AI
                if avg_entropy < 6.0:
                    ai_score += 20
            
            # 3. Check for noise patterns (AI images often have less noise)
            try:
                enhancer = ImageEnhance.Sharpness(image)
                sharpness = self.estimate_sharpness(image)
                indicators['netteté'] = sharpness
                
                if sharpness > 0.7:  # Very sharp images
                    ai_score += 15
            except:
                indicators['netteté'] = "N/A"
            
            # 4. Check metadata (AI images often lack EXIF data)
            exif_data = image.getexif() if hasattr(image, 'getexif') else {}
            if len(exif_data) == 0:
                ai_score += 20
                indicators['exif'] = False
            else:
                indicators['exif'] = True
            
            # 5. Aspect ratio analysis
            aspect_ratio = width / height
            if abs(aspect_ratio - 1.0) < 0.01:  # Perfect square
                ai_score += 10
            
            indicators['ratio_aspect'] = round(aspect_ratio, 2)
            
            # Determine verdict
            if ai_score >= 60:
                verdict = "PROBABLEMENT GÉNÉRÉ PAR L'IA"
                verdict_tag = 'ai'
                emoji = "🤖"
            elif ai_score >= 40:
                verdict = "INCERTAIN"
                verdict_tag = 'uncertain'
                emoji = "❓"
            else:
                verdict = "PROBABLEMENT AUTHENTIQUE"
                verdict_tag = 'human'
                emoji = "📷"
            
            # Display results
            self.results_text.configure(state=tk.NORMAL)
            self.results_text.delete('1.0', tk.END)
            
            self.results_text.insert(tk.END, f"\n{emoji} Verdict: ", 'title')
            self.results_text.insert(tk.END, f"{verdict}\n\n", verdict_tag)
            
            self.results_text.insert(tk.END, "📊 Analyse de l'image:\n", 'title')
            self.results_text.insert(tk.END, "─" * 70 + "\n", 'info')
            self.results_text.insert(tk.END, f"• Score IA: {ai_score}%\n", 'info')
            self.results_text.insert(tk.END, f"• Dimensions: {width} x {height} pixels\n", 'info')
            self.results_text.insert(tk.END, f"• Format: {format_type}\n", 'info')
            self.results_text.insert(tk.END, f"• Mode couleur: {mode}\n", 'info')
            self.results_text.insert(tk.END, f"• Ratio d'aspect: {indicators['ratio_aspect']}\n", 'info')
            self.results_text.insert(tk.END, f"• Dimensions suspectes: {'Oui' if indicators['dimensions_suspectes'] else 'Non'}\n", 'info')
            self.results_text.insert(tk.END, f"• Données EXIF: {'Présentes' if indicators['exif'] else 'Absentes'}\n", 'info')
            
            if 'entropie_couleur' in indicators:
                self.results_text.insert(tk.END, f"• Entropie des couleurs: {indicators['entropie_couleur']:.2f}\n", 'info')
            
            if indicators['netteté'] != "N/A":
                self.results_text.insert(tk.END, f"• Netteté estimée: {indicators['netteté']:.2f}\n", 'info')
            
            self.results_text.insert(tk.END, "\n💡 Interprétation:\n", 'title')
            self.results_text.insert(tk.END, "─" * 70 + "\n", 'info')
            
            if ai_score >= 60:
                self.results_text.insert(tk.END,
                    "L'image présente plusieurs caractéristiques typiques du contenu généré\n"
                    "par IA: dimensions standards, absence de métadonnées, uniformité des\n"
                    "couleurs, netteté élevée.\n", 'info')
            elif ai_score >= 40:
                self.results_text.insert(tk.END,
                    "L'image présente des caractéristiques mixtes. Elle pourrait être une\n"
                    "photo retouchée ou une génération IA modifiée.\n", 'info')
            else:
                self.results_text.insert(tk.END,
                    "L'image semble authentique avec des métadonnées présentes, des dimensions\n"
                    "naturelles et des variations typiques d'une vraie photographie.\n", 'info')
            
            self.results_text.configure(state=tk.DISABLED)
            self.status_bar.config(text="✓ Analyse de l'image terminée")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'analyse:\n{str(e)}")
            self.status_bar.config(text="✗ Erreur lors de l'analyse")
    
    def calculate_color_entropy(self, values):
        """Calculate entropy for color channel"""
        if not values:
            return 0
        
        # Group values into bins
        bins = {}
        for val in values:
            bin_key = val // 16  # 16 bins
            bins[bin_key] = bins.get(bin_key, 0) + 1
        
        total = len(values)
        entropy = 0
        
        for count in bins.values():
            probability = count / total
            entropy -= probability * math.log2(probability)
        
        return entropy
    
    def estimate_sharpness(self, image):
        """Estimate image sharpness"""
        try:
            # Convert to grayscale
            gray = image.convert('L')
            # Apply edge detection
            edges = gray.filter(ImageFilter.FIND_EDGES)
            # Calculate mean edge intensity
            pixels = list(edges.getdata())
            if pixels:
                return sum(pixels) / (len(pixels) * 255)
            return 0
        except:
            return 0
    
    def calculate_entropy(self, text):
        """Calcule l'entropie du texte"""
        words = text.lower().split()
        if len(words) == 0:
            return 0
        
        word_counts = Counter(words)
        total_words = len(words)
        entropy = 0
        
        for count in word_counts.values():
            probability = count / total_words
            entropy -= probability * math.log2(probability)
        
        return entropy
    
    def analyze_patterns(self, text):
        """Analyse les patterns caractéristiques de l'IA"""
        ai_indicators = {
            'phrases_formelles': [
                r'\ben effet\b', r'\bpar ailleurs\b', r'\bainsi\b', r'\btoutefois\b',
                r'\bcependant\b', r'\bnéanmoins\b', r'\bde plus\b', r'\ben outre\b'
            ],
            'structures_repetitives': r'\b(\w+)\s+(?:\w+\s+){0,5}\1\b',
            'phrases_longues': len(re.findall(r'[.!?]', text)),
            'mots_de_liaison': [
                r'\bpremièrement\b', r'\bdeuxièmement\b', r'\btroisièmement\b',
                r'\ben conclusion\b', r'\bfinalement\b', r'\bpour conclure\b'
            ],
            'phrases_neutres': [
                r'\bil est important de noter\b', r'\bil convient de\b',
                r'\bon peut observer\b', r'\bil est possible de\b'
            ]
        }
        
        scores = {}
        
        # Compter les phrases formelles
        formal_count = sum(len(re.findall(pattern, text, re.IGNORECASE)) 
                          for pattern in ai_indicators['phrases_formelles'])
        scores['formalité'] = formal_count
        
        # Compter les mots de liaison
        liaison_count = sum(len(re.findall(pattern, text, re.IGNORECASE))
                           for pattern in ai_indicators['mots_de_liaison'])
        scores['mots_de_liaison'] = liaison_count
        
        # Compter les phrases neutres
        neutral_count = sum(len(re.findall(pattern, text, re.IGNORECASE))
                           for pattern in ai_indicators['phrases_neutres'])
        scores['neutralité'] = neutral_count
        
        # Analyser la longueur des phrases
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        if sentences:
            avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
            scores['longueur_moyenne'] = avg_sentence_length
        else:
            scores['longueur_moyenne'] = 0
        
        return scores
    
    def analyze_text(self):
        """Analyse le texte et affiche les résultats"""
        text = self.text_input.get('1.0', tk.END).strip()
        
        if not text:
            messagebox.showwarning("Attention", "Veuillez entrer du texte à analyser!")
            return
        
        self.status_bar.config(text="🔄 Analyse du texte en cours...")
        self.root.update()
        
        try:
            # Calculs
            entropy = self.calculate_entropy(text)
            word_count = len(text.split())
            patterns = self.analyze_patterns(text)
            
            # Score de probabilité IA (simplifié)
            ai_score = 0
            
            # Entropie faible = plus susceptible d'être IA
            if entropy < 3.5:
                ai_score += 25
            
            # Beaucoup de phrases formelles
            if patterns['formalité'] > word_count * 0.05:
                ai_score += 20
            
            # Phrases très structurées
            if patterns['mots_de_liaison'] > 2:
                ai_score += 15
            
            # Phrases neutres
            if patterns['neutralité'] > 1:
                ai_score += 20
            
            # Longueur des phrases
            if patterns['longueur_moyenne'] > 15:
                ai_score += 20
            
            # Déterminer le verdict
            if ai_score >= 60:
                verdict = "PROBABLEMENT GÉNÉRÉ PAR L'IA"
                verdict_tag = 'ai'
                emoji = "🤖"
            elif ai_score >= 40:
                verdict = "INCERTAIN"
                verdict_tag = 'uncertain'
                emoji = "❓"
            else:
                verdict = "PROBABLEMENT ÉCRIT PAR UN HUMAIN"
                verdict_tag = 'human'
                emoji = "✍️"
            
            # Afficher les résultats
            self.results_text.configure(state=tk.NORMAL)
            self.results_text.delete('1.0', tk.END)
            
            self.results_text.insert(tk.END, f"\n{emoji} Verdict: ", 'title')
            self.results_text.insert(tk.END, f"{verdict}\n\n", verdict_tag)
            
            self.results_text.insert(tk.END, "📊 Détails de l'analyse:\n", 'title')
            self.results_text.insert(tk.END, "─" * 70 + "\n", 'info')
            self.results_text.insert(tk.END, f"• Score IA: {ai_score}%\n", 'info')
            self.results_text.insert(tk.END, f"• Entropie: {entropy:.2f}\n", 'info')
            self.results_text.insert(tk.END, f"• Nombre de mots: {word_count}\n", 'info')
            self.results_text.insert(tk.END, f"• Longueur moyenne des phrases: {patterns['longueur_moyenne']:.1f} mots\n", 'info')
            self.results_text.insert(tk.END, f"• Phrases formelles détectées: {patterns['formalité']}\n", 'info')
            self.results_text.insert(tk.END, f"• Mots de liaison: {patterns['mots_de_liaison']}\n", 'info')
            self.results_text.insert(tk.END, f"• Expressions neutres: {patterns['neutralité']}\n\n", 'info')
            
            self.results_text.insert(tk.END, "💡 Interprétation:\n", 'title')
            self.results_text.insert(tk.END, "─" * 70 + "\n", 'info')
            if ai_score >= 60:
                self.results_text.insert(tk.END, 
                    "Le texte présente plusieurs caractéristiques typiques du contenu généré\n"
                    "par IA: structure formelle, phrases bien construites, vocabulaire neutre.\n", 'info')
            elif ai_score >= 40:
                self.results_text.insert(tk.END,
                    "Le texte présente des caractéristiques mixtes. Il pourrait être écrit par\n"
                    "un humain avec un style formel ou par une IA avec quelques ajustements.\n", 'info')
            else:
                self.results_text.insert(tk.END,
                    "Le texte semble authentique avec des variations naturelles, un style\n"
                    "personnel et moins de structures formelles typiques de l'IA.\n", 'info')
            
            self.results_text.configure(state=tk.DISABLED)
            self.status_bar.config(text="✓ Analyse du texte terminée")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'analyse du texte:\n{str(e)}")
            self.status_bar.config(text="✗ Erreur lors de l'analyse")
    
    def clear_all(self):
        """Efface tout le contenu"""
        self.text_input.delete('1.0', tk.END)
        self.results_text.configure(state=tk.NORMAL)
        self.results_text.delete('1.0', tk.END)
        self.results_text.configure(state=tk.DISABLED)
        
        # Clear image
        if self.current_image_path:
            self.image_canvas.delete("all")
            canvas_width = self.image_canvas.winfo_width()
            canvas_height = self.image_canvas.winfo_height()
            if canvas_width <= 1:
                canvas_width = 600
            if canvas_height <= 1:
                canvas_height = 300
            self.image_canvas.create_text(
                canvas_width // 2, canvas_height // 2,
                text="📸 Cliquez sur 'Charger Image' pour sélectionner une image",
                font=('Segoe UI', 12, 'italic'),
                fill='#94b9ff'
            )
            self.current_image = None
            self.current_image_path = None
        
        self.status_bar.config(text="Prêt à analyser")
    
    def export_results(self):
        """Exporte les résultats de l'analyse"""
        
        # Vérifier qu'il y a des résultats à exporter
        results_content = self.results_text.get('1.0', tk.END).strip()
        
        if not results_content or len(results_content) < 10:
            messagebox.showwarning("Attention", "Aucun résultat à exporter!\nVeuillez d'abord analyser du contenu.")
            return
        
        try:
            from tkinter import filedialog
            from datetime import datetime
            
            # Demander où sauvegarder
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            default_filename = f"analyse_ia_{current_time}.txt"
            
            filepath = filedialog.asksaveasfilename(
                title="Sauvegarder les résultats",
                defaultextension=".txt",
                initialfile=default_filename,
                filetypes=[
                    ("Fichiers texte", "*.txt"),
                    ("Fichiers Markdown", "*.md"),
                    ("Tous les fichiers", "*.*")
                ]
            )
            
            if filepath:
                # Préparer le contenu à exporter
                export_content = "=" * 70 + "\n"
                export_content += "DÉTECTEUR DE CONTENU IA - RAPPORT D'ANALYSE\n"
                export_content += "=" * 70 + "\n\n"
                export_content += f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
                
                # Ajouter le type d'analyse
                current_tab = self.notebook.index(self.notebook.select())
                if current_tab == 0:
                    export_content += "Type d'analyse: TEXTE\n"
                else:
                    export_content += "Type d'analyse: IMAGE\n"
                    if self.current_image_path:
                        export_content += f"Fichier analysé: {os.path.basename(self.current_image_path)}\n"
                
                export_content += "\n" + "=" * 70 + "\n"
                export_content += "RÉSULTATS DE L'ANALYSE\n"
                export_content += "=" * 70 + "\n\n"
                
                # Ajouter les résultats
                export_content += results_content
                
                export_content += "\n\n" + "=" * 70 + "\n"
                export_content += "Généré par: Détecteur de Contenu IA v2.0\n"
                export_content += "=" * 70 + "\n"
                
                # Sauvegarder le fichier
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(export_content)
                
                messagebox.showinfo("Succès", f"✓ Résultats exportés avec succès!\n\nFichier: {os.path.basename(filepath)}")
                self.status_bar.config(text=f"✓ Résultats exportés: {os.path.basename(filepath)}")
                
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'exporter les résultats:\n{str(e)}")
            self.status_bar.config(text="✗ Erreur lors de l'export")

def main():
    root = tk.Tk()
    app = AIContentDetector(root)
    root.mainloop()

if __name__ == "__main__":
    main()