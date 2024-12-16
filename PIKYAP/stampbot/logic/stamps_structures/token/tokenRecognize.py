from typing import List
from logic.stamps_structures.token.tokenMethods import responseGenerator, extract_info, blood_check, exception_check


class Token:
    def __init__(self, stamp: List[str]):
        self.stamp = stamp
        self.dstamp = stamp.copy()
        self.number = None
        self.blood = None
        self.info = []
        self.response = ""

    async def responseGenerator(self):
        await responseGenerator(self)

    async def extract_info(self):
        await extract_info(self)

    async def blood_check(self):
        await blood_check(self)

    async def exception_check(self):
        await exception_check(self)


async def token_recognize(text: List[str], update, context):
    token = Token(text)
    await token.blood_check()
    await token.exception_check()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=token.stamp)
    await token.extract_info()
    await token.responseGenerator()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=token.response)
    del token







