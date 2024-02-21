# Mikael
An advanced multimodal model hosted as a Discord bot that synergizes [Mistral](https://mistral.ai) as the language model and [LLaVA (Large Language and Vision Assistant)](https://llava-vl.github.io) as the vision model. Together, they comprise a potent combination, incorporating a vision encoder and Vicuna for comprehensive visual and language understanding. This configuration empowers Mikael with remarkable chat capabilities, mirroring the versatility of the multimodal GPT-4. 

<div align="center">
   <img src="https://github.com/ibnaleem/mikael/blob/main/assets/showcase.gif?raw=true", alt="Showcase of Mikael Discord Bot">
</div>

## Invite Mikael
Mikael does not require any permissions, it is a **chat-only** Discord bot:
```
https://discord.com/api/oauth2/authorize?client_id=1202687794213036112&permissions=0&scope=bot
```
## Purpose
To combine [Mistral's LLM](https://mistral.ai) and [LLaVA multimodal model](https://llava-vl.github.io) into a Discord bot for users to chat with similar to ChatGPT.
## Benchmarks
Currently, Mistral's 7.3B parameter LLM can:
- Outperform Llama 2 13B on all benchmarks
- Outperform Llama 1 34B on many benchmarks
- Approach CodeLlama 7B performance on code, while remaining good at English tasks
- Use Grouped-query attention (GQA) for faster inference
- Use Sliding Window Attention (SWA) to handle longer sequences at smaller cost

([Mistral AI, 2024](https://mistral.ai/news/announcing-mistral-7b/))
## Running locally
Mikael can be self-hosted by following these steps:
### Install Ollama
For Linux:
```
$ curl https://ollama.ai/install.sh | sh
```
For MacOS:
```
https://ollama.ai/download/Ollama-darwin.zip
```
### Run the following terminal commands:
1. ```
   $ ollama pull mistral
   ```
2. ```
   $ ollama pull llava
   ```
Mistral needs 4.7 GB, while llava requires 4.1 GB of space.
### Install Requirements
```
$ pip install discord.py ollama
```
### Set Mikael's Token
```
$ nvim /path/to/bash-or-zsh
```
```
$ export MIKAEL_TOKEN="TOKEN HERE"
```
```
$ source /path/to/bash-or-zsh
```
Mikael should run correctly; [open an issue](https://github.com/ibnaleem/mikael/issues) if it does not.
## Future Plans
- Incorporate [Dolphin-Mixtral-8x7b](https://huggingface.co/cognitivecomputations/dolphin-2.5-mixtral-8x7b) as Mikael's main LLM.

## Privacy
- Mikael ***temporarily*** downloads all images it's sent to be fed into LLaVA's multimodal model; after successfully finishing its task, your images are immediately deleted from the server. ([L39-L59](https://github.com/ibnaleem/mikael/blob/main/main.py#L39C13-L59C1))
- Mikael only stores your chats in random access memory (RAM) ([L63-L66](https://github.com/ibnaleem/mikael/blob/main/main.py#L63-L66)).

## Acknowledgements
- [LLaVA](https://llava-vl.github.io)
- [Mistral AI](https://mistral.ai)
- [ollama/ollama-python](https://github.com/ollama/ollama-python)

## Support Server
```
https://discord.gg/JX4XgrQSeV
```
