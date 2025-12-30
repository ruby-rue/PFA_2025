import re
from collections import Counter
import math

class AIContentDetectorCLI:
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
    
    def analyze_text(self, text):
        """Analyse le texte et retourne les résultats"""
        if not text.strip():
            return "Erreur: Texte vide"
        
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
            emoji = "🤖"
        elif ai_score >= 40:
            verdict = "INCERTAIN"
            emoji = "❓"
        else:
            verdict = "PROBABLEMENT ÉCRIT PAR UN HUMAIN"
            emoji = "✍️"
        
        # Formater les résultats
        results = f"""
{'='*60}
{emoji} DÉTECTEUR DE CONTENU IA {'='*60}

{emoji} Verdict: {verdict}

📊 Détails de l'analyse:
{'='*60}
• Score IA: {ai_score}%
• Entropie: {entropy:.2f}
• Nombre de mots: {word_count}
• Longueur moyenne des phrases: {patterns['longueur_moyenne']:.1f} mots
• Phrases formelles détectées: {patterns['formalité']}
• Mots de liaison: {patterns['mots_de_liaison']}
• Expressions neutres: {patterns['neutralité']}

💡 Interprétation:
{'='*60}
"""
        
        if ai_score >= 60:
            results += """Le texte présente plusieurs caractéristiques typiques du contenu 
généré par IA: structure formelle, phrases bien construites, 
vocabulaire neutre."""
        elif ai_score >= 40:
            results += """Le texte présente des caractéristiques mixtes. Il pourrait être 
écrit par un humain avec un style formel ou par une IA avec 
quelques ajustements humains."""
        else:
            results += """Le texte semble authentique avec des variations naturelles, 
un style personnel et moins de structures formelles typiques 
de l'IA."""
        
        results += "\n" + "="*60 + "\n"
        
        return results

def main():
    detector = AIContentDetectorCLI()
    
    print("\n" + "="*60)
    print("🤖 DÉTECTEUR DE CONTENU GÉNÉRÉ PAR L'IA")
    print("="*60 + "\n")
    
    # Test avec un exemple de texte IA
    print("📝 TEST 1: Exemple de texte formel (type IA)")
    print("-"*60)
    text_ia = """
    En effet, il est important de noter que l'intelligence artificielle 
    représente aujourd'hui un domaine en pleine expansion. Par ailleurs, 
    de nombreuses applications sont développées dans ce secteur. Ainsi, 
    il convient de mentionner que les progrès réalisés sont significatifs. 
    Toutefois, certains défis demeurent à relever. En conclusion, 
    l'avenir de cette technologie s'annonce prometteur.
    """
    print(detector.analyze_text(text_ia))
    
    # Test avec un exemple de texte humain
    print("\n📝 TEST 2: Exemple de texte naturel (type humain)")
    print("-"*60)
    text_humain = """
    J'ai passé une super journée aujourd'hui! Je suis allé au parc 
    avec mes amis et on a joué au foot. C'était trop cool! 
    Par contre j'ai oublié ma bouteille d'eau... fail total. 
    Bref, je recommence demain peut-être.
    """
    print(detector.analyze_text(text_humain))
    
    # Mode interactif
    print("\n" + "="*60)
    print("✍️  MODE INTERACTIF")
    print("="*60)
    print("Entrez votre texte (tapez 'quit' pour quitter):\n")
    
    user_text = input("> ")
    if user_text.lower() != 'quit':
        print(detector.analyze_text(user_text))

if __name__ == "__main__":
    main()
