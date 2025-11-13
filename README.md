# Sistema Acadêmico Colaborativo com Apoio de IA


Este projeto entrega um sistema Django com:
- Layout idêntico ao modelo (painel lateral azul, área principal clara, bolha amarela no rodapé)
- Login, Cadastro, Dashboard
- Telas: Perfil, Assistente, Matérias, Notas, Cadastro, Frequência, Notificações, Tarefas
- API REST básica (DRF) para Materias, Notas, Tarefas, Frequencias e Notificações
- Assistente IA: endpoint que recebe ações (buscar, ordenar, relatorio). O relatório é exportável em CSV.
- Dockerfile e docker-compose para rodar com Postgres (opcional)