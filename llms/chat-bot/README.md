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