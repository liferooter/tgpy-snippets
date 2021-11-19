# Delete message after evaluating

def silent(func):
    async def wrapper(*args, **kwargs):
        await func(*args, **kwargs)
        await ctx.msg.delete()
    return wrapper
