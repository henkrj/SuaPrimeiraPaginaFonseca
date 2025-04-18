# 🎮 GameReview

Bem-vindo ao GameReview, uma plataforma web para cadastro de jogos, reviews e perfis de usuários. Este projeto foi desenvolvido em Django com foco em aprendizado e prática dos principais conceitos do framework, incluindo autenticação, herança de templates, CBVs, CRUD completo, mensagens entre usuários e muito mais.


---

## 📌 Funcionalidades

- Cadastro de Desenvolvedoras
- Cadastro de Jogos (verifica duplicidade por título e ano)
- Cadastro de Reviews com nota, jogo e comentário
- Página inicial com resumo e últimos jogos adicionados
- Página "Sobre Mim"
- Sistema de autenticação com registro, login, logout
- Perfis de usuários com edição de avatar, bio e data de nascimento
- Envio de mensagens entre usuários com caixa de entrada e saída
- Proteção de visualizações com login obrigatório
- Templates personalizados com Bootstrap 5 e ícones

---


## 🧰 Tecnologias usadas

- Python 3.13
- Django 5.1
- SQLite
- Bootstrap 5
- CKEditor (para campos de texto ricos)
- HTML, CSS

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
GameReview/
│
├── GameApp/                  # App principal
│   ├── templates/            # Templates HTML
│   ├── static/               # Arquivos estáticos (imagens, css, etc.)
│   ├── models.py             # Modelos (Jogo, Desenvolvedora, Review, Mensagem, Profile)
│   ├── views.py              # Views (com CBVs e FBVs)
│   ├── forms.py              # Formulários
│   └── urls.py               # URLs da aplicação
│
├── GamingReview/             # Projeto Django
│   ├── settings.py           # Configurações do Django (inclui MEDIA e STATIC)
│   └── urls.py               # URLs principais
│
├── media/                    # Avatares de usuários (ignorado no git)
├── db.sqlite3                # Banco de dados (ignorado no git)
├── requirements.txt          # Dependências do projeto
└── README.md                 # Você está aqui :)
```

---

## Sobre

Projeto criado por Igor Renato da Fonseca Vasques como parte do aprendizado em Python com Django. Código simples, direto, e com carinho!
