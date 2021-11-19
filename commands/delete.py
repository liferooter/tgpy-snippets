# Delete last or replied message

@Command
@silent
@reply_or_last
async def delete(msg):
    await msg.delete()
