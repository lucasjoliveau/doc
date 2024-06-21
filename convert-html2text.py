import os
import re
from bs4 import BeautifulSoup
import html2text

# Répertoires source et destination
source_dir = './html-doc/lang/fr/applications/finance'
dest_dir = './dist/html'

# Crée le répertoire de destination s'il n'existe pas
os.makedirs(dest_dir, exist_ok=True)
print("Création du répertoire:", dest_dir)

# Fonction pour extraire le contenu de la balise <main> et le convertir en Markdown
def convert_html_to_md(source_file, dest_file):
    # print(f"Conversion du fichier : {source_file} vers {dest_file}")
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier {source_file}: {e}")
        return
    
    main_content = soup.find('main')
    if main_content:
        # print(f"Extraction du contenu de la balise <main> pour le fichier : {source_file}")
        # Remplacer les <span class="guilabel"> par des <b>
        for span in main_content.find_all('span', class_='guilabel'):
            span.name = 'b'
            del span['class']
        
        # Traiter uniquement les alertes
        alerts = main_content.find_all('div', class_='alert')
        alert_placeholders = {}
        
        for i, alert in enumerate(alerts):
            # Remplacer les classes alert-tip par alert-info
            if 'alert-tip' in alert['class']:
                alert['class'] = [cls if cls != 'alert-tip' else 'alert-info' for cls in alert['class']]
            
            # Remplacer les <span class="pre"> et <span class="doc"> par leur contenu
            for span in alert.find_all('span', class_=['pre', 'doc', 'menuselection']):
                span.unwrap()
            
            # Supprimer toutes les classes des balises <code>, <a>, et <ul>
            for code in alert.find_all('code'):
                code.attrs = {}
            for a in alert.find_all('a'):
                a.attrs = {key: a.attrs[key] for key in a.attrs if key != 'class'}
                # Supprimer l'extension .html des attributs href
                if 'href' in a.attrs:
                    a['href'] = a['href'].replace('.html', '')
            for ul in alert.find_all('ul'):
                ul.attrs = {}

            # Remplacer les <strong> par des <b>
            for strong in alert.find_all('strong'):
                strong.name = 'b'

            # Remplacer les alertes par des balises de remplacement
            placeholder = f"ALERT_PLACEHOLDER_{i}"
            alert_placeholders[placeholder] = str(alert)
            alert.replace_with(soup.new_string(placeholder))

        # Convertir le reste en Markdown
        html_content = str(main_content)
        md_content = html2text.html2text(html_content)
        
        # Supprimer le caractère ¶ du contenu Markdown
        md_content = md_content.replace('¶', '')

        # Réinsérer les alertes HTML à leur emplacement d'origine
        for placeholder, alert_html in alert_placeholders.items():
            md_content = md_content.replace(placeholder, alert_html)
        
        # Supprimer l'extension .html des liens Markdown
        md_content = re.sub(r'\(([^)]+)\.html', r'(\1', md_content)
        
        try:
            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(md_content)
        except Exception as e:
            print(f"Erreur lors de l'écriture du fichier {dest_file}: {e}")
    # else:
        # print(f"Pas de balise <main> trouvée dans le fichier : {source_file}")

# Vérifier si le répertoire source contient des fichiers HTML
if not os.path.exists(source_dir):
    print(f"Le répertoire source n'existe pas : {source_dir}")
else:
    html_files = [f for f in os.listdir(source_dir) if f.endswith('.html')]
    if not html_files:
        print(f"Aucun fichier HTML trouvé dans le répertoire : {source_dir}")

# Parcours tous les fichiers HTML dans le répertoire source
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.html'):
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(source_file, source_dir)
            dest_file = os.path.join(dest_dir, os.path.splitext(relative_path)[0] + '.md')

            os.makedirs(os.path.dirname(dest_file), exist_ok=True)
            convert_html_to_md(source_file, dest_file)

print("Conversion terminée.")
