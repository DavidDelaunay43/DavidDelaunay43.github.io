import markdown

# Lire le fichier Markdown
with open('index.md', 'r', encoding='utf-8') as md_file:
    md_text = md_file.read()

# Convertir en HTML
html_text = markdown.markdown(md_text)

# Écrire le fichier HTML
with open('index.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_text)
