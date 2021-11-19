# Allows to get replied message or last message
# as function argument automatically

def reply_or_last(func):
    async def wrapper():
        orig = await ctx.msg.get_reply_message()
        if orig:
            return await func(orig)
        async for msg in client.iter_messages(ctx.msg.chat_id):
            if msg.id != ctx.msg.id:
                return await func(msg)
    return wrapper
