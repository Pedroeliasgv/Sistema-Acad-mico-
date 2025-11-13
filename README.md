# 🧠 Sistema Acadêmico Colaborativo com Apoio de IA

![Django](https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow?style=for-the-badge)

---

## 📘 Sobre o projeto

O **Sistema Acadêmico Colaborativo com Apoio de IA** é uma plataforma web criada com **Django** para facilitar o **gerenciamento acadêmico** de alunos, matérias, notas, frequência e comunicação entre professores e estudantes.

Além das funções básicas de um sistema educacional, o projeto visa incluir uma **IA assistente** integrada, capaz de ajudar alunos e professores em dúvidas e atividades pedagógicas.

---

## 🚀 Funcionalidades

✅ Autenticação completa (Login, Registro e Logout)  
✅ Painel (Dashboard) com visão geral do sistema  
✅ Gestão de matérias, notas e frequência  
✅ Edição de perfil com atualização de senha e dados  
✅ Fórum colaborativo entre alunos e professores  
✅ Sistema de notificações e tarefas  
✅ Biblioteca virtual integrada  
🤖 **(Em breve)** Assistente inteligente com IA

---

## 🛠️ Tecnologias utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| **Backend** | Django (Python) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Banco de Dados** | SQLite |
| **Autenticação** | Django Auth |
| **Template Engine** | Django Templates |

---

## ⚙️ Como executar o projeto localmente

```bash
# 1️⃣ Clone o repositório
git clone https://github.com/seuusuario/sistema-academico.git
cd chatbot_academic

# 2️⃣ Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate   # (no Windows)

# 3️⃣ Instale as dependências
pip install -r requirements.txt

# 4️⃣ Execute as migrações
python manage.py migrate

# 5️⃣ Inicie o servidor
python manage.py runserver

