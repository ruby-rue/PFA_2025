# 📖 Guide d'Utilisation - Détecteur de Contenu IA

## 🚀 Démarrage Rapide

### Lancement de l'Application
```bash
python ai_content_detector.py
```

## 🎨 Interface Principale

L'application s'ouvre avec une interface moderne en **dark mode** comprenant :

### En-tête
- **Titre animé** : "🤖 DÉTECTEUR DE CONTENU IA" avec effet de couleur cyclique
- **Sous-titre** : Description de la fonction
- **Couleurs** : Palette cyan/bleu sur fond sombre

### Zone de Navigation
- **Deux onglets** :
  - 📝 **Analyse de Texte** (par défaut)
  - 🖼️ **Analyse d'Image**

### Contrôles
- **🔍 ANALYSER** : Bouton principal cyan pour lancer l'analyse
- **🗑️ EFFACER** : Bouton rouge pour tout réinitialiser

### Zone de Résultats
- Affichage formaté avec couleurs
- Code couleur pour les verdicts
- Métriques détaillées

### Barre de Statut
- En bas de l'application
- Affiche les opérations en cours
- Messages de confirmation/erreur

---

## 📝 Mode 1 : Analyse de Texte

### Étape 1 : Saisir le Texte
1. Cliquez dans la **grande zone de texte** sous "📄 Texte à analyser"
2. Collez ou tapez votre texte
3. Le texte peut faire de quelques mots à plusieurs paragraphes

### Étape 2 : Lancer l'Analyse
1. Cliquez sur le bouton **🔍 ANALYSER**
2. La barre de statut affiche "🔄 Analyse du texte en cours..."
3. L'analyse est quasi-instantanée

### Étape 3 : Interpréter les Résultats

#### Verdict (en haut)
- **🤖 PROBABLEMENT GÉNÉRÉ PAR L'IA** (texte rouge)
  - Score ≥ 60%
  - Texte très formel et structuré
  
- **❓ INCERTAIN** (texte orange)
  - Score entre 40-60%
  - Caractéristiques mixtes
  
- **✍️ PROBABLEMENT ÉCRIT PAR UN HUMAIN** (texte vert)
  - Score < 40%
  - Style naturel et varié

#### Détails de l'Analyse
```
📊 Détails de l'analyse:
─────────────────────────────────────────
• Score IA: XX%
• Entropie: X.XX (diversité du vocabulaire)
• Nombre de mots: XXX
• Longueur moyenne des phrases: XX.X mots
• Phrases formelles détectées: X
• Mots de liaison: X
• Expressions neutres: X
```

#### Interprétation
Explication en langage naturel des résultats

### Exemples de Textes à Tester

#### Texte Type IA (Score élevé)
```
En effet, il est important de noter que l'intelligence artificielle 
représente un domaine en pleine expansion. Par ailleurs, de nombreuses 
applications sont développées. Ainsi, il convient de mentionner que 
les progrès sont significatifs. En conclusion, l'avenir s'annonce 
prometteur.
```

#### Texte Type Humain (Score faible)
```
J'ai passé une super journée! Je suis allé au parc avec mes amis 
et on a joué au foot. C'était trop cool! Par contre j'ai oublié 
ma bouteille d'eau... fail total. Bref, je recommence demain.
```

---

## 🖼️ Mode 2 : Analyse d'Image

### Étape 1 : Charger une Image
1. Cliquez sur l'onglet **"🖼️ Analyse d'Image"**
2. Cliquez sur le bouton **"📁 Charger Image"**
3. Sélectionnez une image dans le navigateur de fichiers
4. Formats acceptés : PNG, JPG, JPEG, BMP, GIF

### Étape 2 : Visualiser l'Image
- L'image apparaît dans la zone de prévisualisation
- Elle est automatiquement redimensionnée pour s'adapter
- Le nom du fichier apparaît dans la barre de statut

### Étape 3 : Lancer l'Analyse
1. Cliquez sur **🔍 ANALYSER**
2. La barre de statut affiche "🔄 Analyse de l'image en cours..."
3. L'analyse prend 1-2 secondes

### Étape 4 : Interpréter les Résultats

#### Verdict
- **🤖 PROBABLEMENT GÉNÉRÉ PAR L'IA** (rouge)
  - Score ≥ 60%
  - Dimensions suspectes (512x512, 1024x1024)
  - Absence de métadonnées
  - Couleurs très uniformes
  
- **❓ INCERTAIN** (orange)
  - Score entre 40-60%
  - Quelques indicateurs suspects
  
- **📷 PROBABLEMENT AUTHENTIQUE** (vert)
  - Score < 40%
  - Dimensions naturelles
  - Métadonnées présentes
  - Variation naturelle des couleurs

#### Métriques Analysées
```
📊 Analyse de l'image:
─────────────────────────────────────────
• Score IA: XX%
• Dimensions: XXX x XXX pixels
• Format: PNG/JPEG/etc.
• Mode couleur: RGB/L/etc.
• Ratio d'aspect: X.XX
• Dimensions suspectes: Oui/Non
• Données EXIF: Présentes/Absentes
• Entropie des couleurs: X.XX
• Netteté estimée: X.XX
```

### Indicateurs Clés pour les Images

#### 🚩 Signes d'Image IA
1. **Dimensions parfaites** : 512x512, 1024x1024, 768x768
2. **Absence d'EXIF** : Pas de métadonnées caméra
3. **Entropie faible** : Couleurs trop uniformes (< 6.0)
4. **Netteté élevée** : Trop net pour être naturel (> 0.7)
5. **Ratio carré parfait** : 1:1 exactement

#### ✅ Signes de Photo Authentique
1. **Dimensions irrégulières** : 1920x1080, 4032x3024
2. **Métadonnées EXIF** : Info caméra, GPS, date
3. **Entropie élevée** : Variations naturelles des couleurs
4. **Netteté variable** : Naturellement imparfaite
5. **Ratio non-standard** : 16:9, 4:3, 3:2

---

## 🎯 Conseils d'Utilisation

### Pour le Texte
- **Minimum** : 50 mots pour une analyse fiable
- **Optimal** : 100-500 mots
- **Langues** : Français principalement
- Testez avec différents styles d'écriture

### Pour les Images
- **Résolution** : Aucune restriction (redimensionnement auto)
- **Taille fichier** : Toutes tailles acceptées
- **Formats** : PNG recommandé pour préserver les détails
- Comparez plusieurs images pour comprendre les patterns

### Limitations
⚠️ L'outil est **indicatif**, pas définitif :
- Les résultats sont basés sur des heuristiques
- Un score élevé ne prouve pas à 100% une génération IA
- Un score faible ne garantit pas l'authenticité
- Utilisez votre jugement critique

---

## 🎨 Fonctionnalités de l'Interface

### Effets Visuels
- **Animation du titre** : Changement de couleur cyclique
- **Hover effects** : Boutons qui changent au survol
- **Onglets** : Navigation intuitive entre modes
- **Barre de statut** : Feedback en temps réel

### Raccourcis
- **Analyser** : Clic ou Entrée dans les zones de texte
- **Effacer** : Bouton rouge ou raccourci clavier
- **Charger image** : Double-clic sur la zone d'image

### Personnalisation
Le design dark mode est optimisé pour :
- ✅ Réduire la fatigue oculaire
- ✅ Mise en évidence des résultats
- ✅ Expérience moderne et professionnelle

---

## 🧪 Tests Recommandés

### Test 1 : Texte Formel vs Informel
Comparez un email professionnel avec un message texte

### Test 2 : Images Standard
Testez une capture d'écran vs une photo de smartphone

### Test 3 : Contenu Mixte
Analysez un texte partiellement édité par un humain

### Test 4 : Images Traitées
Comparez une photo originale avec une version retouchée

---

## ❓ Résolution de Problèmes

### L'image ne se charge pas
- Vérifiez le format de fichier
- Essayez de convertir en PNG/JPG
- Vérifiez que le fichier n'est pas corrompu

### L'analyse est trop rapide
- C'est normal! L'analyse texte est instantanée
- L'analyse image prend 1-2 secondes

### Les résultats semblent incorrects
- Souvenez-vous : c'est une estimation
- Essayez avec un échantillon plus large
- Comparez plusieurs textes/images similaires

### L'application ne démarre pas
```bash
# Vérifiez les dépendances
pip install -r requirements.txt --break-system-packages

# Sur Linux
sudo apt-get install python3-tk
```

---

## 💡 Astuces Pro

1. **Combinez les analyses** : Analysez texte ET images d'un même projet
2. **Gardez des références** : Créez une collection de cas connus
3. **Documentez** : Notez les patterns que vous observez
4. **Comparez** : Testez plusieurs versions du même contenu
5. **Contextualisez** : Prenez en compte le contexte d'utilisation

---

## 📞 Support

Pour toute question :
1. Consultez le README.md
2. Vérifiez les exemples fournis
3. Testez avec les images de test incluses
4. Expérimentez avec différents contenus

---

**Version** : 2.0 (avec analyse d'images)
**Dernière mise à jour** : 2025
**Projet** : PFA - Détection de Contenu IA
