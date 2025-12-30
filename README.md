# Détecteur de Contenu Généré par l'IA

## Description
Application desktop simple en Python pour détecter si un texte a été généré par une intelligence artificielle.

## Fonctionnalités
- 🤖 Analyse de texte en temps réel
- 📊 Score de probabilité IA
- 🎨 Interface graphique intuitive
- 📈 Métriques détaillées d'analyse
- 🔍 Détection basée sur plusieurs indicateurs

## Indicateurs d'analyse
L'application analyse plusieurs aspects du texte :

1. **Entropie** : Mesure la diversité du vocabulaire
2. **Phrases formelles** : Détecte les expressions typiques de l'IA
3. **Structure** : Analyse la longueur et la complexité des phrases
4. **Mots de liaison** : Identifie les connecteurs logiques
5. **Expressions neutres** : Repère les formulations impersonnelles

## Installation

### Prérequis
- Python 3.7 ou supérieur
- Bibliothèque tkinter (généralement incluse avec Python)

### Installation des dépendances
```bash
# Tkinter est inclus par défaut avec Python
# Si nécessaire sur Linux :
sudo apt-get install python3-tk
```

## Utilisation

### Lancer l'application
```bash
python ai_content_detector.py
```

### Comment utiliser
1. Coller ou taper le texte à analyser dans la zone de texte
2. Cliquer sur "🔍 Analyser"
3. Consulter les résultats :
   - 🤖 Rouge = Probablement IA
   - ❓ Orange = Incertain
   - ✍️ Vert = Probablement humain
4. Utiliser "🗑️ Effacer" pour recommencer

## Interprétation des résultats

### Score IA
- **0-40%** : Le texte semble écrit par un humain
- **40-60%** : Incertain, caractéristiques mixtes
- **60-100%** : Probablement généré par l'IA

### Métriques
- **Entropie < 3.5** : Vocabulaire répétitif (signe d'IA)
- **Phrases longues** : Style formel et structuré
- **Phrases formelles élevées** : Langage académique typique de l'IA

## Limitations
⚠️ Cet outil fournit une estimation basée sur des heuristiques simples. Il ne doit pas être considéré comme une preuve définitive. Les facteurs suivants peuvent influencer les résultats :

- La longueur du texte
- Le style d'écriture de l'auteur
- Le sujet traité
- La langue et le registre utilisés

## Structure du code

```
ai_content_detector.py
├── Classe AIContentDetector
│   ├── __init__() : Interface graphique
│   ├── calculate_entropy() : Calcul de l'entropie
│   ├── analyze_patterns() : Détection des patterns
│   ├── analyze_text() : Analyse principale
│   └── clear_all() : Reset de l'interface
```

## Améliorations possibles
- 🔄 Ajout de modèles de machine learning
- 📝 Support de plusieurs langues
- 💾 Sauvegarde des résultats
- 📊 Graphiques de visualisation
- 🌐 API pour analyse par lots

## Technologies utilisées
- **Python 3.x**
- **Tkinter** : Interface graphique
- **re** : Expressions régulières
- **collections.Counter** : Analyse statistique
- **math** : Calculs d'entropie

## Auteur
Projet académique - PFA 2025

## Licence
Projet éducatif libre d'utilisation
