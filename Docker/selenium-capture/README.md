> mkdir chat-bot
> cd chat-bot
> python -m venv .venv
> .venv\Scripts\activate 
or in linux
> source .venv/bin/activate
> pip install -r requirements.txt
> python app.py

### Docker build image
> docker build --pull --rm -f "llms\chat-bot\Dockerfile" -t chatbot:latest "llms\chat-bot" 

> docker logs -f selenium
> docker logs -f chatbot


### Python dependencies
- To ensure app dependencies are ported from your virtual environment/host machine into your container, run 'pip freeze > requirements.txt' in the terminal to overwrite this file

> pip freeze > requirements.txt

- update pip
> python.exe -m pip install --upgrade pip