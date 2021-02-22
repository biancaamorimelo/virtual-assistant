# Virtual Assistant

Este repositório contém um projeto privado de uma assistente virtual. O objetivo é construir uma guia inteligente para uma empresa local de João Pessoa, que possa responder perguntas específicas, sem interação humana.

This is a private virtual assistant project. The goal is to build a smart guide to answer and guide people from a local company based in Joao Pessoa, with specific questions and no human interaction.
 
# Instalação
1. Baixe ou clone o repositório.
2. Baixe e instale o [Python 3.8.5](https://www.python.org/downloads/release/python-385/). (__Windows__: lembre de de adicionar às variáveis de ambiente (_$PATH_))
3. Abra o terminal e digite os seguintes comandos para instalar as bibliotecas necessárias:
    ```sh
    $ pip install SpeechRecognition
    $ pip install pyttsx3
    $ pip install pywhatkit
    ```
4. Baixe e instale a [Leticiaf123](https://f123.org/leticia/download/Windows/RHVoice-Brazilian-Portuguese-voice-Leticia-F123-v4.6.11-setup.exe)
5. Baixe e instale o PyAudio de acordo com a versão do Python instalada. Neste caso, estamos utilizando a versão 3.8.5 (PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl), então baixe a versão do [PyAudio38](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

#### Execução

> __Nota:  É obrigatório seguir as ordens da seção "Instalação" antes de executar__.

1. Abra o terminal e navegue até o diretório onde você clonou o código:
    - __Windows__:
    ```sh
    $ cd caminho/virtual-assistant
    ```
2. Execute o seguinte comando:
    ```sh
    $ py main.py
    ```
3. Caso não apresente nenhum erro, o programa estará em execução, não será mostrada nenhuma mensagem. Pode iniciar seu diálogo com a assistente virtual!

### Atividades

- [x] Receber entrada de voz em Português
- [x] Transformar entrada de voz para texto
- [x] Buscar API de voz do Google
- [x] Fazer busca pelo Wikipédia
- [x] Fazer busca pelo Google
- [x] Fazer busca pelo Youtube
- [ ] Criar uma base de dados de perguntas aplicadas
- [ ] Responder as perguntas do contexto
- [ ] Testar
- [ ] Melhorar voz robotizada
- [ ] Implementar interface gráfica



