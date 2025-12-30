"""
Générateur de Rapport PDF - Détecteur de Contenu IA
Ce script génère un rapport PDF professionnel à partir des résultats d'analyse
"""

from datetime import datetime
import os

def generate_pdf_report(results_text, analysis_type="TEXTE", image_path=None, output_path=None):
    """
    Génère un rapport PDF professionnel
    
    Args:
        results_text: Texte des résultats à inclure
        analysis_type: "TEXTE" ou "IMAGE"
        image_path: Chemin vers l'image analysée (si applicable)
        output_path: Chemin du fichier PDF à créer
    """
    try:
        # Tentative d'import de reportlab
        try:
            from reportlab.lib.pagesizes import letter, A4
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak
            from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
            from reportlab.lib import colors
        except ImportError:
            print("⚠️  reportlab n'est pas installé")
            print("   Installez avec: pip install reportlab")
            return generate_html_report(results_text, analysis_type, image_path, output_path)
        
        # Définir le nom du fichier si non spécifié
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"rapport_analyse_ia_{timestamp}.pdf"
        
        # Créer le document PDF
        doc = SimpleDocTemplate(output_path, pagesize=A4)
        story = []
        styles = getSampleStyleSheet()
        
        # Style personnalisé pour le titre
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#00d9ff'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        # Style pour les sous-titres
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#0f3460'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        )
        
        # Style pour le corps du texte
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=11,
            alignment=TA_JUSTIFY,
            spaceAfter=10
        )
        
        # Titre principal
        title = Paragraph("🤖 DÉTECTEUR DE CONTENU IA", title_style)
        story.append(title)
        story.append(Spacer(1, 0.2*inch))
        
        # Sous-titre
        subtitle = Paragraph("Rapport d'Analyse Automatique", styles['Heading2'])
        story.append(subtitle)
        story.append(Spacer(1, 0.3*inch))
        
        # Informations générales
        info_text = f"""
        <b>Date de génération:</b> {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}<br/>
        <b>Type d'analyse:</b> {analysis_type}<br/>
        """
        
        if image_path and analysis_type == "IMAGE":
            info_text += f"<b>Fichier analysé:</b> {os.path.basename(image_path)}<br/>"
        
        story.append(Paragraph(info_text, body_style))
        story.append(Spacer(1, 0.3*inch))
        
        # Ligne de séparation
        story.append(Spacer(1, 0.1*inch))
        
        # Résultats
        heading = Paragraph("📊 RÉSULTATS DE L'ANALYSE", heading_style)
        story.append(heading)
        story.append(Spacer(1, 0.2*inch))
        
        # Formater les résultats
        formatted_results = results_text.replace('\n', '<br/>')
        formatted_results = formatted_results.replace('•', '&bull;')
        
        results_para = Paragraph(formatted_results, body_style)
        story.append(results_para)
        story.append(Spacer(1, 0.3*inch))
        
        # Pied de page
        story.append(Spacer(1, 0.5*inch))
        footer_text = """
        <i>Ce rapport a été généré automatiquement par le Détecteur de Contenu IA v2.0<br/>
        Projet PFA 2025 - Génie Informatique et Réseaux</i>
        """
        footer = Paragraph(footer_text, styles['Italic'])
        story.append(footer)
        
        # Construire le PDF
        doc.build(story)
        
        print(f"✓ Rapport PDF généré: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"✗ Erreur lors de la génération du PDF: {e}")
        # Fallback vers HTML
        return generate_html_report(results_text, analysis_type, image_path, output_path)


def generate_html_report(results_text, analysis_type="TEXTE", image_path=None, output_path=None):
    """
    Génère un rapport HTML professionnel (fallback si PDF impossible)
    """
    try:
        # Définir le nom du fichier
        if not output_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"rapport_analyse_ia_{timestamp}.html"
        else:
            output_path = output_path.replace('.pdf', '.html')
        
        html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport d'Analyse IA</title>
    <style>
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #00d9ff;
            text-align: center;
            font-size: 32px;
            margin-bottom: 10px;
        }}
        h2 {{
            color: #0f3460;
            border-bottom: 2px solid #00d9ff;
            padding-bottom: 10px;
            margin-top: 30px;
        }}
        .info-box {{
            background: #f0f8ff;
            padding: 20px;
            border-left: 4px solid #00d9ff;
            margin: 20px 0;
        }}
        .results {{
            background: #fafafa;
            padding: 20px;
            border-radius: 5px;
            line-height: 1.8;
            white-space: pre-wrap;
            font-family: 'Consolas', monospace;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            color: #666;
            font-style: italic;
        }}
        .emoji {{
            font-size: 24px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1><span class="emoji">🤖</span> DÉTECTEUR DE CONTENU IA</h1>
        <p style="text-align: center; color: #666; font-size: 18px;">
            Rapport d'Analyse Automatique
        </p>
        
        <div class="info-box">
            <p><strong>📅 Date de génération:</strong> {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}</p>
            <p><strong>📝 Type d'analyse:</strong> {analysis_type}</p>
            {f'<p><strong>📁 Fichier analysé:</strong> {os.path.basename(image_path)}</p>' if image_path and analysis_type == "IMAGE" else ''}
        </div>
        
        <h2>📊 RÉSULTATS DE L'ANALYSE</h2>
        
        <div class="results">{results_text}</div>
        
        <div class="footer">
            <p>Ce rapport a été généré automatiquement par le Détecteur de Contenu IA v2.0</p>
            <p>Projet PFA 2025 - Génie Informatique et Réseaux</p>
        </div>
    </div>
</body>
</html>
        """
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✓ Rapport HTML généré: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"✗ Erreur lors de la génération du rapport: {e}")
        return None


if __name__ == "__main__":
    # Test
    test_results = """
🤖 Verdict: PROBABLEMENT GÉNÉRÉ PAR L'IA

📊 Détails de l'analyse:
• Score IA: 65%
• Entropie: 3.2
• Nombre de mots: 150
• Longueur moyenne des phrases: 18.5 mots

💡 Interprétation:
Le texte présente plusieurs caractéristiques typiques du contenu
généré par IA: structure formelle, phrases bien construites.
    """
    
    print("Test de génération de rapport...")
    result = generate_html_report(test_results, "TEXTE")
    if result:
        print(f"✓ Rapport de test créé: {result}")
