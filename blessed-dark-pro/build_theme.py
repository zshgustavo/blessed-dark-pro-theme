import json
import os

# 1. Definição da Paleta de Cores
palette = {
    # --- FUNDO DEFINIDO ---
    "background": "#000000",      # Preto puro (fundo do editor e terminal)
    
    # --- CORES EM ANÁLISE (Placeholders temporários) ---
    "surface": "#111111",         # Fundo das barras laterais
    "border": "#222222",          # Divisórias entre abas e painéis
    "foreground": "#CCCCCC",      # Cor base do texto comum
    "primary_accent": "#555555",  # Cor primária 
    "secondary_accent": "#777777",# Cor secundária 
    "danger": "#FF3333",          # Erros
    "warning": "#FFFF33",         # Alertas e Strings
    "success": "#33FF33"          # Adições (Git)
}

# 2. Mapeamento do Tema
theme = {
    "name": "Blessed Dark Pro",
    "type": "dark",
    "colors": {
        "editor.background": palette["background"],
        "editor.foreground": palette["foreground"],
        "sideBar.background": palette["surface"],
        "sideBar.border": palette["border"],
        "activityBar.background": palette["surface"],
        "activityBar.foreground": palette["primary_accent"],
        "terminal.background": palette["background"],
        "terminal.foreground": palette["foreground"],
        "focusBorder": palette["border"]
    },
    "tokenColors": [
        {
            "name": "Sintaxe Base (Palavras-chave)",
            "scope": ["keyword", "control", "statement", "keyword.other.DML.sql", "keyword.other.DDL.sql"],
            "settings": {
                "foreground": palette["primary_accent"],
                "fontStyle": "bold"
            }
        },
        {
            "name": "Funções e Métodos",
            "scope": ["entity.name.function", "meta.function-call"],
            "settings": {
                "foreground": palette["secondary_accent"]
            }
        },
        {
            "name": "Strings e Marcações",
            "scope": ["string", "punctuation.definition.string", "markup.heading"],
            "settings": {
                "foreground": palette["warning"]
            }
        }
    ]
}

# 3. Execução multiplataforma (Windows/Linux)
def build():
    output_dir = "themes"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "blessed-dark-pro-color-theme.json")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(theme, f, indent=4)
        
    print(f"Tema 'Blessed Dark Pro' gerado com sucesso em: {output_path}")

if __name__ == "__main__":
    build()