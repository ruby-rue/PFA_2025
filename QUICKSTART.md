# 🚀 Guide de Démarrage Rapide

## Installation en 3 Étapes

### 1️⃣ Installation Automatique (Recommandée)
```bash
python setup.py
```

### 2️⃣ Installation Manuelle
```bash
# Installer les dépendances
pip install -r requirements.txt

# Ou directement
pip install Pillow
```

### 3️⃣ Lancer l'Application
```bash
python ai_content_detector.py
```

---

## ⚡ Utilisation Express

### Analyse de Texte (30 secondes)
1. **Lancer** l'application
2. **Onglet** "📝 Analyse de Texte"
3. **Coller** votre texte
4. **Cliquer** sur "🔍 ANALYSER"
5. **Lire** les résultats colorés

### Analyse d'Image (1 minute)
1. **Lancer** l'application
2. **Onglet** "🖼️ Analyse d'Image"
3. **Cliquer** "📁 Charger Image"
4. **Sélectionner** une image
5. **Cliquer** "🔍 ANALYSER"
6. **Examiner** les métriques

---

## 🎯 Tests Rapides

### Tester avec les Exemples Fournis

#### Test 1 : Image IA
```bash
# Chargez test_ai_image.png
# Résultat attendu: Score élevé (60%+)
```

#### Test 2 : Image Naturelle
```bash
# Chargez test_natural_image.png
# Résultat attendu: Score bas (<40%)
```

#### Test 3 : Texte Formel
```
En effet, il est important de noter que l'intelligence 
artificielle représente un domaine en pleine expansion. 
Par ailleurs, de nombreuses applications sont développées.
# Résultat attendu: Score élevé
```

#### Test 4 : Texte Informel
```
Salut! J'ai trop kiffé ce film hier soir. 
C'était ouf, genre vraiment trop bien!
# Résultat attendu: Score bas
```

---

## 📋 Checklist Avant Utilisation

- [ ] Python 3.7+ installé
- [ ] Pillow installé (`pip install Pillow`)
- [ ] Tkinter disponible (généralement inclus)
- [ ] Fichier `ai_content_detector.py` présent

**Vérification rapide:**
```bash
python validate_code.py
```

---

## 🆘 Problèmes Courants

### ❌ "No module named 'tkinter'"
**Solution:**
- Windows: Réinstallez Python avec tcl/tk
- Linux: `sudo apt-get install python3-tk`
- Mac: Inclus avec Python de python.org

### ❌ "No module named 'PIL'"
**Solution:**
```bash
pip install Pillow
```

### ❌ L'application ne démarre pas
**Solution:**
1. Vérifiez Python 3.7+: `python --version`
2. Testez la syntaxe: `python validate_code.py`
3. Consultez `TROUBLESHOOTING.md`

---

## 💡 Raccourcis Clavier

| Action | Raccourci |
|--------|-----------|
| Analyser | `Ctrl+Enter` |
| Effacer | `Ctrl+D` |
| Quitter | `Alt+F4` / `Cmd+Q` |

---

## 📱 Interface en un Coup d'Œil

```
┌─────────────────────────────────────────────┐
│  🤖 DÉTECTEUR DE CONTENU IA                │
│  Analysez du texte ou des images           │
├─────────────────────────────────────────────┤
│ 📝 Analyse de Texte | 🖼️ Analyse d'Image  │
├─────────────────────────────────────────────┤
│                                             │
│  [Zone de texte / Zone d'image]            │
│                                             │
├─────────────────────────────────────────────┤
│     🔍 ANALYSER      🗑️ EFFACER            │
├─────────────────────────────────────────────┤
│  📊 Résultats:                              │
│  • Verdict: [🤖/❓/✍️]                      │
│  • Score IA: XX%                            │
│  • Détails...                               │
├─────────────────────────────────────────────┤
│  Statut: Prêt à analyser                    │
└─────────────────────────────────────────────┘
```

---

## 🎨 Personnalisation Rapide

### Changer la Taille de la Fenêtre
**Ligne 26 dans `ai_content_detector.py`:**
```python
self.root.geometry("1000x750")  # Modifiez ici
```

### Changer les Couleurs
**Ligne 28:**
```python
self.root.configure(bg='#1a1a2e')  # Fond principal
```

---

## 📚 Documentation Complète

| Fichier | Description |
|---------|-------------|
| `README.md` | Documentation détaillée |
| `GUIDE_UTILISATION.md` | Guide visuel complet |
| `TROUBLESHOOTING.md` | Résolution de problèmes |
| Ce fichier | Démarrage rapide |

---

## 🎓 Pour Votre PFA

### Points Clés à Mentionner

1. **Fonctionnalités:**
   - ✅ Analyse de texte multi-critères
   - ✅ Analyse d'images avec métriques
   - ✅ Interface graphique moderne
   - ✅ Système de scoring intelligent

2. **Technologies:**
   - Python 3.x
   - Tkinter (GUI)
   - Pillow (traitement d'images)
   - Heuristiques personnalisées

3. **Améliorations Futures:**
   - Modèles ML (BERT, CNN)
   - Support multilingue
   - Analyse par lots
   - Export des résultats

---

## 📞 Support

**En cas de problème:**
1. Consultez `TROUBLESHOOTING.md`
2. Vérifiez les prérequis
3. Testez avec les exemples fournis
4. Lisez la documentation complète

---

## ✅ Validation

**Tout fonctionne si:**
- ✓ L'application se lance sans erreur
- ✓ Les deux onglets sont visibles
- ✓ Les images de test s'affichent
- ✓ L'analyse produit des résultats
- ✓ Les couleurs s'affichent correctement

---

**Version:** 2.0 avec analyse d'images
**Dernière mise à jour:** Décembre 2025
**Projet:** PFA - Détection de Contenu IA

🎉 **Bon courage pour votre présentation!**
