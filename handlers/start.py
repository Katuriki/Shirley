from telegram.ext import CommandHandler, Updater

def start(update, context):
    update.effective_message.reply_text(
        "ā Hello !\n\nā I'm Shirley ā¤ !\nMade By @Akira_xD !"
    )
    print("New User ! \nUser ID : " + str(update.message.from_user.id) + "\nUser Name : " + str(update.message.from_user.username))
    

__handlers__ = [
    [
        CommandHandler(
            "start",
            start
        )
    ]
]
