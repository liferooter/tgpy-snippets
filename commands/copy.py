# Copy and send code from message

from app.handlers import handle_message
from app.message_design import get_code


@Command
async def copy():
    reply = await ctx.msg.get_reply_message()
    msg = await client.send_message(reply.chat_id, get_code(reply))
    this = ctx.msg
    await handle_message(msg)
    await this.delete()
