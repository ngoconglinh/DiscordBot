import discord
import asyncio

import os
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 852344315421917194  # Thay bằng ID channel của bạn

intents = discord.Intents.default()
intents.message_content = True  # Phải bật nếu muốn đọc nội dung tin nhắn
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Bot đã đăng nhập: {client.user}')

@client.event
async def on_message(message):
    # Chỉ xử lý nếu là tin nhắn từ bot khác và chứa embed, và đúng channel
    if message.channel.id == CHANNEL_ID and message.author.bot and message.embeds:
        embed = message.embeds[0]
        print("\n📥 Embed mới được gửi:")
        if embed.title:
            print(f"🔹 Tiêu đề: {embed.title}")
        if embed.description:
            print(f"🔸 Mô tả: {embed.description}")
        for field in embed.fields:
            print(f"➡ {field.name}: {field.value}")

client.run(TOKEN)
