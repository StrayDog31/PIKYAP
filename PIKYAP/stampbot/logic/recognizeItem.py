from typing import List
from logic.checkers.tokenCheck import token_check
from logic.checkers.stampCheck import waa_check

from logic.stamps_structures.stampRecognize import waa_recognize
from logic.stamps_structures.token.tokenRecognize import token_recognize


async def type_check(text: List [str], update, context):


    if await waa_check(text):

        await context.bot.send_message(chat_id=update.effective_chat.id,  text="Распознано клеймо приемки военного имущества!")
        await waa_recognize(text, update, context)

    elif await token_check(text):

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Распознан солдатский жетон (ЛОЗ)!")
        await token_recognize(text, update, context)

    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Тип клейма неопознан!")




