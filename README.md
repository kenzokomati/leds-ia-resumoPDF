# 📄 ResumoPDF - Agentes Inteligentes para Leitura e Resumo de Documentos PDF

*Bem-vindo ao ResumoPDF!* 👋

Este projeto tem como objetivo desenvolver uma solução baseada em agentes utilizando o framework **CrewAI** para processar documentos em formato PDF. A solução gera resumos dos documentos lidos e apresenta o conteúdo em um formato adequado para publicação em um blog.

## 🎯 Objetivo Geral

Desenvolver uma aplicação que seja capaz de:

- 📖 Ler documentos PDF de forma eficiente.
- 📝 Gerar resumos curtos e informativos.
- 🖋️ Formatar o texto gerado no estilo de um post de blog.

## 🛠️ Arquitetura de Agentes

A aplicação é composta por diferentes agentes, cada um responsável por uma etapa do processo:

1. **Agente de Leitura de PDF**: Responsável por extrair o texto bruto do arquivo PDF.
2. **Agente de Análise e Extração de Informação**: Identifica as informações mais importantes do texto.
3. **Agente de Resumo**: Utiliza um modelo de linguagem (ex.: GPT) para criar resumos curtos e coerentes.
4. **Agente de Formatação**: Formata o resumo no estilo de um post de blog, incluindo título, subtítulos e uma conclusão.

## 🚀 Como Executar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/kenzokomati/leds-ia-resumoPDF.git
   ```

2. **Navegue até o diretório do projeto**:

   ```bash
   cd leds-ia-resumoPDF/pdf_resumo_app
   ```

3. **Instale as dependências**:

   Certifique-se de ter o Python instalado em sua máquina. Então, instale as dependências necessárias:

   ```bash
   uv pip install -r pyproject.toml
   ```

4. **Modifique a pasta de output**:

   Substituir o path na variável "output_file" na task de formatação para markdown no arquivo crew.py 

5. **Colocar chave e modelo de LLM**:

   ```bash
   MODEL= <LLM-MODEL>
   LLM_API_KEY= <LLM-API-KEY>
   ```   
   
6. **Execute a aplicação**:

   Utilize o comando abaixo para iniciar o processamento dos PDFs:

   ```bash
   crewai run
   ```

## 📂 Estrutura de Diretórios

A estrutura principal do projeto é a seguinte:

```
leds-ia-resumoPDF/
├── data/
│   ├── pdfs/
│   └── outputs/
├── pdf_resumo_app/
│   ├── crew.py
│   └── tools/
│       └── pdf_text_reader.py
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
├── requirements.txt
└── README.md
```

- **data/pdfs/**: Diretório onde os arquivos PDF a serem processados devem ser colocados.
- **data/outputs/**: Diretório onde os resumos gerados serão armazenados.
- **pdf_resumo_app/crew.py**: Arquivo principal que define os agentes e tarefas utilizando o CrewAI.
- **pdf_resumo_app/tools/pdf_text_reader.py**: Ferramenta para extração de texto dos PDFs.
- **config/agents.yaml**: Configurações dos agentes.
- **config/tasks.yaml**: Configurações das tarefas.

## 📝 Configuração dos Agentes e Tarefas

As configurações dos agentes e tarefas estão localizadas nos arquivos `agents.yaml` e `tasks.yaml`, respectivamente, dentro do diretório `config/`. Certifique-se de ajustar essas configurações conforme necessário para atender às especificidades do seu projeto.

## 🛡️ Qualidade e Logs

Para monitorar o desempenho dos agentes e garantir a qualidade dos resumos gerados, a aplicação utiliza logs e indicadores de progresso. Esses logs auxiliam na identificação de possíveis melhorias e na manutenção do sistema.
