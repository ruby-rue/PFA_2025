#!/usr/bin/env python3
"""
Script d'installation automatique pour le Détecteur de Contenu IA
"""

import subprocess
import sys
import os

def print_header():
    """Affiche l'en-tête"""
    print("\n" + "="*70)
    print("🤖 DÉTECTEUR DE CONTENU IA - Installation")
    print("="*70 + "\n")

def check_python_version():
    """Vérifie la version de Python"""
    print("1️⃣  Vérification de la version Python...")
    version = sys.version_info
    
    if version.major >= 3 and version.minor >= 7:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} détecté")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor} détecté")
        print("   ⚠️  Python 3.7+ est requis")
        return False

def check_tkinter():
    """Vérifie si tkinter est disponible"""
    print("\n2️⃣  Vérification de tkinter...")
    try:
        import tkinter
        print("   ✅ tkinter est installé")
        return True
    except ImportError:
        print("   ❌ tkinter n'est pas installé")
        print("\n   📝 Instructions d'installation:")
        
        if sys.platform.startswith('linux'):
            print("   Sur Ubuntu/Debian:")
            print("   sudo apt-get install python3-tk")
        elif sys.platform.startswith('darwin'):
            print("   Sur macOS:")
            print("   brew install python-tk")
        else:
            print("   Sur Windows:")
            print("   Réinstallez Python et cochez 'tcl/tk and IDLE'")
        
        return False

def install_dependencies():
    """Installe les dépendances Python"""
    print("\n3️⃣  Installation des dépendances Python...")
    
    if not os.path.exists('requirements.txt'):
        print("   ⚠️  requirements.txt non trouvé")
        print("   Installation manuelle de Pillow...")
        packages = ['Pillow']
    else:
        print("   📦 Installation depuis requirements.txt...")
        packages = None
    
    try:
        if packages:
            for package in packages:
                print(f"   Installing {package}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        
        print("   ✅ Dépendances installées avec succès")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Erreur lors de l'installation: {e}")
        print("\n   💡 Essayez manuellement:")
        print("   pip install Pillow")
        return False

def verify_installation():
    """Vérifie que tout est installé correctement"""
    print("\n4️⃣  Vérification de l'installation...")
    
    all_ok = True
    
    # Vérifier Pillow
    try:
        from PIL import Image
        print("   ✅ Pillow (PIL) fonctionne")
    except ImportError:
        print("   ❌ Pillow (PIL) non disponible")
        all_ok = False
    
    # Vérifier le fichier principal
    if os.path.exists('ai_content_detector.py'):
        print("   ✅ ai_content_detector.py trouvé")
    else:
        print("   ❌ ai_content_detector.py manquant")
        all_ok = False
    
    # Vérifier la syntaxe
    if os.path.exists('validate_code.py'):
        try:
            result = subprocess.run([sys.executable, 'validate_code.py'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                print("   ✅ Code validé syntaxiquement")
            else:
                print("   ⚠️  Avertissements de validation")
        except:
            print("   ⚠️  Validation ignorée")
    
    return all_ok

def create_launcher():
    """Crée un script de lancement"""
    print("\n5️⃣  Création du script de lancement...")
    
    if sys.platform.startswith('win'):
        # Windows .bat
        launcher_content = """@echo off
echo Lancement du Detecteur de Contenu IA...
python ai_content_detector.py
pause
"""
        launcher_name = "lancer.bat"
    else:
        # Linux/Mac .sh
        launcher_content = """#!/bin/bash
echo "Lancement du Detecteur de Contenu IA..."
python3 ai_content_detector.py
"""
        launcher_name = "lancer.sh"
    
    try:
        with open(launcher_name, 'w') as f:
            f.write(launcher_content)
        
        if not sys.platform.startswith('win'):
            os.chmod(launcher_name, 0o755)
        
        print(f"   ✅ Script de lancement créé: {launcher_name}")
        return True
    except Exception as e:
        print(f"   ⚠️  Impossible de créer le lanceur: {e}")
        return False

def print_summary(success):
    """Affiche le résumé"""
    print("\n" + "="*70)
    print("📊 RÉSUMÉ DE L'INSTALLATION")
    print("="*70)
    
    if success:
        print("\n✅ Installation réussie!")
        print("\n🚀 Pour lancer l'application:")
        
        if sys.platform.startswith('win'):
            print("   • Double-cliquez sur lancer.bat")
            print("   • Ou tapez: python ai_content_detector.py")
        else:
            print("   • Tapez: ./lancer.sh")
            print("   • Ou tapez: python3 ai_content_detector.py")
        
        print("\n📚 Documentation disponible:")
        print("   • README.md - Documentation complète")
        print("   • GUIDE_UTILISATION.md - Guide d'utilisation")
        print("   • TROUBLESHOOTING.md - Guide de dépannage")
        
        print("\n🎨 Fonctionnalités:")
        print("   • Analyse de texte pour détecter l'IA")
        print("   • Analyse d'images pour détecter l'IA")
        print("   • Interface moderne avec dark mode")
        print("   • Résultats détaillés et colorés")
    else:
        print("\n⚠️  Installation incomplète")
        print("\n📝 Actions requises:")
        print("   1. Installez Python 3.7+ depuis python.org")
        print("   2. Installez tkinter (voir TROUBLESHOOTING.md)")
        print("   3. Installez Pillow: pip install Pillow")
        print("   4. Relancez ce script: python setup.py")
    
    print("\n" + "="*70 + "\n")

def main():
    """Fonction principale"""
    print_header()
    
    success = True
    
    # Vérifications
    if not check_python_version():
        success = False
    
    tkinter_ok = check_tkinter()
    if not tkinter_ok:
        print("\n   ⚠️  Continuons quand même...")
    
    # Installation
    if not install_dependencies():
        success = False
    
    # Vérification
    if not verify_installation():
        success = False
    
    # Création du lanceur
    create_launcher()
    
    # Résumé
    print_summary(success and tkinter_ok)
    
    return 0 if success else 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Installation interrompue par l'utilisateur")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {e}")
        sys.exit(1)
