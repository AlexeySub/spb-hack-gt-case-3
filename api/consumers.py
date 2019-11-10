def ws_message(message):
    # data = message.content['text']
    print(message.content)
    message.reply_channels.send("test_text")

    
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    
