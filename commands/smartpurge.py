# Filter and delete messages up to given

@silent
async def smartpurge(func):
    orig = await ctx.msg.get_reply_message()
    async for msg in client.iter_messages(orig.chat_id):
        if func(msg):
            await msg.delete()
        if msg == orig:
            break
