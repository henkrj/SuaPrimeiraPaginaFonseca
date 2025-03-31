# 🎮 GameReview

Bem-vindo ao **GameReview**, um site simples e direto para cadastrar jogos, Desenvolvedoras e escrever reviews! Este projeto foi desenvolvido como parte de um curso de Django, focando em aplicar o padrão MTV e os principais recursos da framework.

---

## 💡 O que você encontra aqui:

- Cadastro de **Desenvolvedoras**
- Cadastro de **Jogos**, linkando com a desenvolvedora
- Cadastro de **Reviews** com nota, comentário e autor
- Um campo de busca para encontrar jogos pelo título
- Listagem das Reviews feitas
- Interface bonitinha com Bootstrap
- Painel administrativo via Django Admin

---

## 🧰 Tecnologias usadas

- Python 3.13
- Django 5.1
- SQLite (banco de dados padrão do Django)
- Bootstrap 5 + Bootstrap Icons

---

## ▶️ Como rodar o projeto na sua máquina

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/GameReview.git
   ```

2. Entre na pasta do projeto:
   
   cd ProjetoGameReview
  

3. Ative um ambiente virtual (opcional, mas ajuda):
   
   python -m venv venv
   venv\Scripts\activate
 

4. Instale as dependências:
   
   pip install -r requirements.txt
   

5. Rode as migrações:
   
   python manage.py makemigrations
   python manage.py migrate
   

6. Crie um superusuário:
   python manage.py createsuperuser
   

7. Inicie o servidor:
   python manage.py runserver
   

8. Acesse no navegador:
      http://127.0.0.1:8000/
   

---

## 🧪 Como testar o projeto

1. Vá em **Desenvolvedora** e cadastre uma.
2. Depois vá em **Jogo** e cadastre um jogo, escolhendo a desenvolvedora.
3. Em seguida, cadastre uma **Review** para esse jogo.
4. Veja a lista de reviews já feitas.
5. Teste a busca de jogos pelo título!

---

## 🗂️ Estrutura do projeto

```
ProjetoGameReview/
├── GameApp/
│   ├── templates/GameApp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── ProjetoGameReview/
│   └── settings.py
├── db.sqlite3
└── manage.py
```

---

## Sobre

Projeto criado por Igor Renato da Fonseca Vasques como parte do aprendizado em Python com Django. Código simples, direto, e com carinho!
