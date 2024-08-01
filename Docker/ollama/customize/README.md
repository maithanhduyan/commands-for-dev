#
> ollama create mario -f ./MarioModel
~~~~
FROM llama3.1
PARAMETER temperature 1
SYSTEM """
You are Mario from super mario bros, acting as an assistant.
"""
~~~~
> ollama run mario

# SaleModel
> docker exec -it ollama  ollama create sales -f "/home/ollama/customize/SaleModel"