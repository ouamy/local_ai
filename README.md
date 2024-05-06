# Local AI

A local AI for enterprise software development.

## Windows

- Install Ollama (https://ollama.com)
- Install Docker (https://www.docker.com/products/docker-desktop)
- Restart your computer
- Download a model you want to use such as llama3

Paste this in your Command Prompt and wait :
```
ollama run llama3 install
```

- Make sure Ollama is running at : http://localhost:11434
- Open Docker Desktop

Paste this in your Command Prompt :
```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

- Enjoy your Local AI at : http://localhost:3000

## WSL/Linux

Install Windows Subsystem for Linux [Windows Only Steps]
- Open your Command Prompt
- Enter "wsl --install"
- Restart your computer
- Open Ubuntu

