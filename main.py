import os, ollama, discord
from discord.ext import commands
from discord import Intents
from discord.ui import Button, View

MIKAEL_TOKEN = os.environ["MIKAEL_TOKEN"]

intents = Intents.all()
chat_log = []
client = commands.Bot(command_prefix="!", intents=intents, owner_id=1110526906106904626)

@client.event
async def on_ready() -> None:
    try:
        await client.change_presence(
            activity=discord.Streaming(
                name="Ask me anything!", url="https://twitch.tv/gothamchess"
            )
        )
        print(
            f"----- Mikael is Online -----\nServers: {len(client.guilds)}\nMembers: {len(client.users)}"
        )

    except Exception:
        print(Exception)


@client.event
async def on_message(message):
    if message.author == client.user:
        pass
    elif message.content.startswith("!"):
        pass
    
    else:
        if isinstance(message.channel, discord.DMChannel):
            await message.channel.typing()

            if message.attachments:  
                for attachment in message.attachments:
                    if os.path.splitext(attachment.filename)[1] in [
                        ".png",
                        ".jpg",
                        ".jpeg",
                        ".gif",
                    ]:
                        await message.channel.typing()
                        await attachment.save(attachment.filename)
    
                        response = ollama.generate(
                            model="llava",
                            prompt=message.content,
                            images=[attachment.filename],
                            stream=False
                        )
    
                        await message.channel.send(response['response'])
                        os.remove(attachment.filename)

            else:
                num = 1
                while num != 0:
                    chat_log.append({"role": "user", "content": message.content})
                    chat_call = ollama.chat(model="mistral", messages=chat_log)
                    response = chat_call["message"]["content"]
                    chat_log.append({"role": "assistant", "content": response})
                    
                    await message.channel.send(response)
                    num -= 1
                    if num == 0:
                        break
        else:
            pass
    

    await client.process_commands(message)


@client.event
async def on_guild_join(guild):

    server_button = Button(label="Discord Server", style=discord.ButtonStyle.url, url="https://discord.gg/JX4XgrQSeV")
    github_button = Button(label="GitHub", style=discord.ButtonStyle.url, url="https://github.com/ibnaleem/mikael")
    view = View()
    view.add_item(server_button)
    view.add_item(github_button)
    
    owner = guild.owner
    try:
        await owner.send("I'm Mikael, a Discord chatbot trained on Mistral's 7.3B parameter language and LLaVA's multimodal models. Currently, I can:\n - Outperform Llama 2 13B on all benchmarks\n- Outperform Llama 1 34B on many benchmarks\n- Approach CodeLlama 7B performance on code, while remaining good at English tasks\n- Use Grouped-query attention (GQA) for faster inference\n- Use Sliding Window Attention (SWA) to handle longer sequences at smaller cost\n- Process, interpret and describe images\n\n I am a **chat-only** Discord bot, therefore, I do not have any commands. Feel free to provide me images or text, I can use both! Please place my role at the top of your server for members to easily message me. It does not need permissions. For more information, see my GitHub or join my server.", view=view)
    except discord.Forbidden:
        pass

client.run(MIKAEL_TOKEN)
