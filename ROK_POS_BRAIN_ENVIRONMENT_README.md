# ROK_POS Brain Environment

## Useful Links
[Setting up LLAMA3 Locally](https://www.datacamp.com/tutorial/run-llama-3-locally)

[Chroma DB Guide](https://www.datacamp.com/tutorial/chromadb-tutorial-step-by-step-guide)

[Context Aware Chatbot](https://www.datacamp.com/tutorial/building-context-aware-chatbots-leveraging-langchain-framework-for-chatgpt)

[What Is LangChain](https://medium.com/@zshariff70/langchain-simple-llm-chains-in-action-bda6950afc71)
## Pre-requisites
+ [Anaconda for Windows](https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Windows-x86_64.exe) or Use the script below for Linux/WSL, make sure to use the latest version by updating the .sh filename from the [anaconda repo](https://repo.anaconda.com/archive).

    - ```mkdir /tmp/anaconda_install && cd /tmp/anaconda_install; wget -O install.sh "https://repo.anaconda.com/archive/Anaconda3-2024.06-Linux-x86_64.sh"; sudo chmod +x install.sh; ./install.sh```

+ Anaconda environment with python 3.8+
+ [Jupyter Lab](https://jupyter.org/install) (for development)
+ [Ollama](https://ollama.com/download)
## Installation
1. Run the appropriate Ollama installer for your OS
2. Test ollama by running ```ollama run llama3``` from a terminal. When Ollama is ready for input you sould see a prompt like
    ```
    >>> 
    ```
3. In the chatbox from the terminal where ollama was run, type ```Write a proper email to employees about how well the company is doing.```. You should see some output related to this request.
    ```
    >>> Write a proper email to employees about how well the company is doing.
    Subject: Exciting News About Our Company's Progress!

    Dear Team,

    I am thrilled to share with you that our company has been experiencing remarkable growth and success in recent
    months. As we continue to work together towards our goals, I wanted to take a moment to acknowledge and celebrate
    the incredible progress we've made.

    As of [current date], we have:

    * Achieved a 25% increase in revenue compared to this time last year
    * Expanded our customer base by 30%
    * Launched new products/services that have received rave reviews from clients and industry experts alike
    ```
4. Now exit the chatbot by typing ```/bye```
5. Next serve up the llama3 model by running ```ollama serve```. If you see an error like ```Error: listen tcp 127.0.0.1:11434: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted.``` This means Ollama is probably already running. On Windows you can try closing Ollama from the notification tray or task manager. On Linux try finding and killing the process. Then retry the command.
7. Open your Anaconda environment and install the following packages either through PIP or Anaconda
    - ollama-python
    - unstructured
    - langchain
    - langchainhub
    - langchain_community
    - langchain-chroma
    - python-magic-bin

    PIP Command : ```pip install unstructured[docx] langchain langchainhub langchain_community langchain-chroma python-magic-bin```

## Configuration
The development notebook will use a docx file containing all the information the model should have access to for querying. You can use the existing curated file or provide your own by changing the source file in the jupyter notebook. 

The file(s) should go in the same location as the .ipynb file.
## Usage
To start developing you can open the existing jupyter notebook .ipynb file. Opening this and running should connect to the locally running instance of ollama. For production we should have a standalone application and possibly a notebook for validation.