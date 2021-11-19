# Save message as quote via @NotQuotLyBot

import asyncio

QUOTE_BOT = 'NotQuotLyBot'


@Command
@silent
@reply_or_last
async def quote(orig):
    quoted = await orig.forward_to(QUOTE_BOT)
    await asyncio.sleep(1)
    await quoted.reply('/q rate')

    while True:
        await asyncio.sleep(1)
        async for quote in client.iter_messages(QUOTE_BOT, limit=1):
            if quote.sender.username == QUOTE_BOT and quote.buttons:
                await quote.buttons[0][0].click()
                break
        else:
            continue
        break

    async for msg in client.iter_messages(QUOTE_BOT):
        await msg.delete()
        if msg == quoted:
            break

    await asyncio.sleep(1)

    results = await client.inline_query(QUOTE_BOT, orig.raw_text)
    if results:
        await results[0].click(orig.chat_id)
