# Détecteur de Contenu Généré par l'IA 🤖

## Description
Application desktop moderne en Python pour détecter si un texte ou une image a été généré par une intelligence artificielle.

## ✨ Nouvelles Fonctionnalités
- 🎨 **Interface graphique moderne** avec design dark mode élégant
- 📝 **Analyse de texte** en temps réel
- 🖼️ **Analyse d'images** pour détecter les générations IA
- 🎭 **Animations et effets visuels** pour une meilleure expérience
- 📊 Métriques détaillées et score de probabilité
- 🌈 **Interface à onglets** pour basculer entre texte et image

## Fonctionnalités

### Analyse de Texte
- 🤖 Détection basée sur plusieurs indicateurs linguistiques
- 📈 Calcul d'entropie du vocabulaire
- 🔍 Détection de phrases formelles et expressions typiques
- 📏 Analyse de la structure et longueur des phrases
- 💡 Interprétation détaillée des résultats

### Analyse d'Images
- 📸 Support des formats: PNG, JPG, JPEG, BMP, GIF
- 🎯 Détection de dimensions suspectes (512x512, 1024x1024, etc.)
- 🌈 Analyse de l'entropie des couleurs
- 🔬 Estimation de la netteté
- 📋 Vérification des métadonnées EXIF
- 📐 Analyse du ratio d'aspect

## Indicateurs d'analyse

### Pour le Texte
1. **Entropie** : Mesure la diversité du vocabulaire
2. **Phrases formelles** : Détecte les expressions typiques de l'IA
3. **Structure** : Analyse la longueur et la complexité des phrases
4. **Mots de liaison** : Identifie les connecteurs logiques
5. **Expressions neutres** : Repère les formulations impersonnelles

### Pour les Images
1. **Dimensions** : Vérifie si ce sont des tailles communes d'IA (512x512, 1024x1024)
2. **Entropie couleur** : Mesure l'uniformité des couleurs
3. **Netteté** : Détecte une netteté artificielle excessive
4. **Métadonnées EXIF** : Les images IA manquent souvent de données EXIF
5. **Ratio d'aspect** : Les carrés parfaits sont suspects

## Installation

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de packages Python)

### Installation des dépendances
```bash
# Installer les dépendances requises
pip install -r requirements.txt

# Sur Linux, si tkinter n'est pas installé :
sudo apt-get install python3-tk
```

### Dépendances
- **Pillow** : Traitement et analyse d'images
- **tkinter** : Interface graphique (généralement inclus avec Python)

## Utilisation

### Lancer l'application
```bash
python ai_content_detector.py
```

### Analyser du Texte
1. Cliquer sur l'onglet **"📝 Analyse de Texte"**
2. Coller ou taper le texte à analyser
3. Cliquer sur **"🔍 ANALYSER"**
4. Consulter les résultats détaillés

### Analyser une Image
1. Cliquer sur l'onglet **"🖼️ Analyse d'Image"**
2. Cliquer sur **"📁 Charger Image"**
3. Sélectionner une image
4. Cliquer sur **"🔍 ANALYSER"**
5. Examiner les métriques et le verdict

### Interprétation des résultats

#### Score IA
- **🤖 60-100%** (Rouge) : Probablement généré par l'IA
- **❓ 40-60%** (Orange) : Incertain, caractéristiques mixtes
- **✍️ 0-40%** (Vert) : Probablement authentique/humain

## 🎨 Interface

L'application dispose d'une interface moderne avec :
- **Dark Mode** élégant avec palette de couleurs cyan/bleu
- **Animations** sur le titre et les boutons
- **Onglets** pour basculer entre les modes d'analyse
- **Barre de statut** pour suivre les opérations
- **Résultats colorés** pour une lecture facile
- **Hover effects** sur les boutons interactifs

## Limitations
⚠️ Cet outil fournit une estimation basée sur des heuristiques et analyses simples. Il ne doit pas être considéré comme une preuve définitive. 

### Facteurs influençant les résultats :
- La longueur et le contexte du texte
- Le style d'écriture personnel de l'auteur
- Le sujet et le registre de langue
- La qualité et la résolution de l'image
- Les modifications post-génération
- Le format et la compression de l'image

## Structure du code

```
ai_content_detector.py
├── Classe AIContentDetector
│   ├── __init__() : Interface graphique avec onglets
│   ├── create_gradient_background() : Effets visuels
│   ├── animate_title() : Animation du titre
│   ├── load_image() : Chargement d'images
│   ├── analyze_text() : Analyse de texte
│   ├── analyze_image() : Analyse d'images
│   ├── calculate_entropy() : Calcul de l'entropie
│   ├── calculate_color_entropy() : Entropie des couleurs
│   ├── estimate_sharpness() : Estimation de netteté
│   ├── analyze_patterns() : Détection des patterns
│   └── clear_all() : Reset complet
```

## Améliorations possibles
- 🧠 Intégration de modèles de machine learning (BERT, CNN)
- 🌐 Analyse d'images via reconnaissance d'artefacts IA
- 📊 Graphiques de visualisation interactifs
- 💾 Export des résultats en PDF/JSON
- 🔄 Analyse par lots de multiples fichiers
- 🌍 Support multilingue
- 🎯 Détection de générateurs spécifiques (Midjourney, DALL-E, etc.)

## Technologies utilisées
- **Python 3.x**
- **Tkinter** : Interface graphique native
- **Pillow (PIL)** : Traitement d'images
- **re** : Expressions régulières pour l'analyse de texte
- **collections.Counter** : Analyse statistique
- **math** : Calculs d'entropie

## Formats supportés

### Images
- PNG
- JPEG / JPG
- BMP
- GIF
- WEBP

### Texte
- Texte brut
- Copier-coller depuis n'importe quelle source

## Captures d'écran

L'interface moderne comprend :
- 🎨 Design dark mode avec accents cyan
- 📑 Système d'onglets pour texte/image
- 🎯 Boutons interactifs avec effets hover
- 📊 Résultats formatés avec couleurs
- 📍 Barre de statut en temps réel

## Auteur
Projet académique - PFA 2025

## Licence
Projet éducatif libre d'utilisation

## Notes techniques

### Performance
- Analyse de texte: instantanée
- Analyse d'image: <2 secondes pour images standard
- Support des grandes images (redimensionnement automatique)

### Compatibilité
- Windows 10/11
- macOS (Catalina et supérieur)
- Linux (Ubuntu, Debian, Fedora, etc.)

## Support
Pour toute question ou amélioration, n'hésitez pas à contribuer au projet!
