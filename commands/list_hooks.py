# List your hooks and their code

from app.hooks import Hook


@Command
async def list_hooks():
    res = ""
    for hook in hooks:
        res += '\n\n\n'
        res += f'Hook "{hook}":\n'
        res += '\n'
        res += Hook.load(hook).code
    return res
