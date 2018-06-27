from telethon import TelegramClient, events
import datetime
import socks

# Use your own values here
api_id = 223471
api_hash = '35e5fd598146bd69a2225b5402ab706c'

client = TelegramClient('AutoGram', api_id, api_hash, update_workers=1, spawn_read_thread=False)

client.start(phone='+79273235411')
print('done')
user = client.get_me()
#--------------------------------------------------------------------

dialogs = client.get_dialogs()
black_rose = client.get_entity(1134379539)
black_rose_id = 1134379539
master_bot_id = 614493767
bot_str = "⚔️🌹 \n🛡🌹"

def send(tower):
    client.send_message('ChatWarsBot', tower)

@client.on(events.NewMessage)
def my_event_handler(event):
    channel = client.get_entity(event.original_update.message.to_id.channel_id)
    target = event.raw_text[2]
    if channel.id == 1134379539 and event.original_update.message.from_id == 614493767:
        if target == '🌹':
            client.send_message('ChatWarsBot', '🛡Защита')
        elif target == "🖤":
            send('🖤')
            print("Атакую Скалу")
        elif target == '☘':
            send('☘️')
            print("Атакую Оплот")
        elif target == '🐢':
            send('🐢')
            print("Атакую Тортугу")
        elif target == '🦇':
            send('🦇')
            print("Атакую Мыш")
        elif target == '🍁':
            send('🍁')
            print("Атакую Амбер")
        elif target == '🍆':
            send('🍆')
            print("Атакую Ферму")


        print(event.original_update.message.from_id, event.raw_text)
        #print(event.original_update.message.to_id.channel_id)


client.idle()

