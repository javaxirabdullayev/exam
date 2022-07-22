from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from bs4 import BeautifulSoup
import requests


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user

    update.message.reply_html(
        f"Assalom alaykum, {user.mention_html()}. Url ni jo'nating!"
    )

def url(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    
    URL = "https://stadion.uz/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find("table", class_="items_most_player items_content_exp")
    tbody = table.find("tbody")
    tr_all = tbody.find_all("tr", recursive=false)
    text = ""
        for element in tr_all[:11]:
            
            td_all = element.find_all("td", class_="zentriert")
            
            number = td_all[0].text
            name = element.find("img")["title"]
            age = td_all[1].text

    
    

 
    
    
def main() -> None:

    updater = Updater("5488984715:AAG72RXLULM48fLQVAlyzKabvB-jK4ga0fM")
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, url))

    # Start the Bot
    updater.start_polling()
    updater.idle()



if __name__ == "__main__":

    main()