# Delete all messages up to given

@Command
async def purge():
    await smartpurge(lambda m: True)
