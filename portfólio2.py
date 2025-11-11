import tkinter as tk
import time
import threading
from datetime import datetime
from tkinter import filedialog
from googletrans import Translator

# Inicializa o tradutor
translator = Translator()

# Dicionário de traduções
translations = {
    'pt': {
        'title': 'Vet - Desenvolvedor de Jogos (Builder)',
        'folders': 'Pastas',
        'trash': 'Lixeira limpa e vazia',
        'snake': 'Jogo Snake',
        'score': 'Pontuação',
        'date': 'Data/Hora',
        'change_lang': 'Mudar idioma',
        'upload_icon': 'Enviar ícone'
    },
    'en': {
        'title': 'Vet - Game Developer (Builder)',
        'folders': 'Folders',
        'trash': 'Trash clean and empty',
        'snake': 'Snake Game',
        'score': 'Score',
        'date': 'Date/Time',
        'change_lang': 'Change language',
        'upload_icon': 'Upload icon'
    }
}

# Idioma padrão
lang = 'pt'

# Função para traduzir textos
def t(key):
    return translations.get(lang, {}).get(key, key)

# Criação da janela principal
root = tk.Tk()
root.title(t('title'))
root.configure(bg='black')
root.geometry('800x600')

# Cabeçalho
header = tk.Label(root, text=t('title'), font=('Arial', 18, 'bold'), fg='white', bg='black')
header.pack(pady=10)

# Função para alternar o idioma
def switch_lang():
    global lang
    lang = 'en' if lang == 'pt' else 'pt'
    update_texts()

# Botão para trocar idioma
lang_button = tk.Button(root, text=t('change_lang'), command=switch_lang, bg='white', fg='black')
lang_button.pack(pady=5)

# Label de data/hora
datetime_label = tk.Label(root, text='', font=('Arial', 12), fg='white', bg='black')
datetime_label.pack()

# Atualiza os textos na interface
def update_texts():
    root.title(t('title'))
    header.config(text=t('title'))
    folder_title.config(text=t('folders'))
    lang_button.config(text=t('change_lang'))
    for i, btn in enumerate(upload_buttons):
        btn.config(text=t('upload_icon'))

# Atualiza a hora em tempo real
def update_time():
    while True:
        now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        datetime_label.config(text=f"{t('date')}: {now}")
        time.sleep(1)

# Thread para o relógio
threading.Thread(target=update_time, daemon=True).start()

# Área das pastas
folders_frame = tk.Frame(root, bg='black')
folders_frame.pack(pady=10)

folder_title = tk.Label(folders_frame, text=t('folders'), font=('Arial', 14, 'bold'), fg='white', bg='black')
folder_title.pack()

# Lista de ícones e botões
icons = []
upload_buttons = []

# Função para enviar ícone
def upload_icon(index):
    file = filedialog.askopenfilename(filetypes=[('Imagens', '*.png;*.jpg;*.jpeg;*.gif')])
    if file:
        try:
            img = tk.PhotoImage(file=file)
        except Exception:
            from PIL import Image, ImageTk
            img = Image.open(file)
            img = img.resize((64, 64))
            img = ImageTk.PhotoImage(img)

        icons[index].config(image=img, text='')
        icons[index].image = img  # evita descarte da imagem

# Criação das 3 pastas com botões
for i in range(3):
    frame = tk.Frame(folders_frame, bg='black')
    frame.pack(side='left', padx=10)

    icon = tk.Label(frame, text='📁', font=('Arial', 40), bg='black', fg='white')
    icon.pack()
    icons.append(icon)

    btn = tk.Button(frame, text=t('upload_icon'), command=lambda i=i: upload_icon(i), bg='white', fg='black')
    btn.pack(pady=5)
    upload_buttons.append(btn)

# Inicia o loop principal
root.mainloop()
