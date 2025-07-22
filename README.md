Seleção Inteligente de Candidatos
✨ Descrição
Projeto desenvolvido como parte de desafio técnico para automação de triagem de candidatos. O sistema:

Recebe uma lista de candidatos em formato JSON

Filtra de acordo com critérios técnicos e culturais definidos

Gera um ranking justificado dos melhores perfis

Produz um feedback construtivo e respeitoso para candidatos não aprovados

🚀 Como executar
Clone o repositório

bash
Copiar
Editar
git clone https://github.com/seuusuario/selecao-inteligente-candidatos.git
cd selecao-inteligente-candidatos
Instale as dependências

bash
Copiar
Editar
pip install openai
Configure a variável de ambiente da sua API Key OpenAI

bash
Copiar
Editar
export OPENAI_API_KEY="sua_api_key_aqui"
Crie ou edite o arquivo candidatos.json com seus candidatos, exemplo:

json
Copiar
Editar
[
  {
    "nome": "Ana",
    "experiencia_anos": 3,
    "skills": ["Python", "SQL", "Comunicação"],
    "cultura": ["Flexibilidade", "Inovação"]
  },
  {
    "nome": "Carlos",
    "experiencia_anos": 5,
    "skills": ["Python", "Java", "SQL"],
    "cultura": ["Flexibilidade", "Liderança"]
  }
]
Execute o programa

bash
Copiar
Editar
python3 desafio_case2.py
💡 Melhorias futuras
Criar interface web para entrada dinâmica de candidatos

Automatizar envio de feedback por e-mail

Visualizar gráficos e métricas avançadas sobre o processo seletivo

🛠️ Tecnologias utilizadas
Python 3

OpenAI API

👤 Autor
Isabelle Costa
