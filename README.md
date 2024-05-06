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

Enjoy your Local AI at : http://localhost:3000

## WSL/Linux

Install Windows Subsystem for Linux [Windows Only Steps]
- Open your Command Prompt
- Enter "wsl --install"
- Restart your computer
- Open Ubuntu

### WSL & Linux

Run the following commands :
```
sudo apt update
```
```
sudo apt upgrade -y
```
```
sudo apt install curl
```

- Install Ollama :
```
curl -fsSL https://ollama.com/install.sh | sh
```

- And run the following command :
```
ollama run llama3 install
```

- Make sure Ollama is running at : http://localhost:11434

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

- Install Docker :
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

- Install Open WebUI :
```
sudo docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Enjoy your Local AI at : http://localhost:3000
