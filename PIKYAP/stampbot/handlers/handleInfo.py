
async def info(update, context):

    name = update.message.from_user.first_name

    greetigs_text = f'''
    Привет,  {name}! 🤚 \nЯ помогу опознать и расшифроватть заводские клейма\nвремен Великой Отечетвенной войны!
Введи клеймо и я покажу результаты!\nИли отправь мне фотографию и я постораюсь распознать штамп на ней.
Я могу опознать только оной клейммо за раз!

    🧑‍💻 Мой создатель: @antiqueMouse
    '''

    await context.bot.send_message(chat_id=update.effective_chat.id, text=greetigs_text)
    