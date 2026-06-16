    import telegram
    from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
    import logging
    import os # Needed to access environment variables

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Get the bot token from environment variable
    # Render will set this when you deploy
    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    def start(update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text('Hi! I am your Football Spyfall Bot. Use /newgame to start.')

    def echo(update, context):
        """Echo the user message."""
        update.message.reply_text(update.message.text)

    def main():
        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        updater = Updater(BOT_TOKEN, use_context=True)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        # Add other command handlers here for /newgame, /join, etc.

        # on non-command Ids - echo the message
        # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo)) # Uncomment if you want echo

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should never happen with Render, as it keeps the process alive.
        updater.idle()

    if __name__ == '__main__':
        if BOT_TOKEN is None:
            print("Error: BOT_TOKEN environment variable not set.")
            # In a real deployment, you might exit or handle this more gracefully
            # For Render, if this happens, your bot won't start.
        else:
            main()
