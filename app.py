from chatbot import ChatBot, Chat

if __name__ == "__main__":
    chatbot = ChatBot()

    chat1 = Chat(chatbot=chatbot)
    chat2 = Chat(chatbot=chatbot)
    chat3 = Chat(chatbot=chatbot)

    bot_reply = chat1.get_reply('hi')
    print("chat1: ", bot_reply)
    bot_reply = chat2.get_reply('hi')
    print("chat2: ", bot_reply)
    bot_reply = chat3.get_reply('hi')
    print("chat3: ", bot_reply)

    bot_reply = chat1.get_reply('how are you?')
    print("chat1: ", bot_reply)
    bot_reply = chat2.get_reply('how are you?')
    print("chat2: ", bot_reply)
    bot_reply = chat3.get_reply('how are you?')
    print("chat3: ", bot_reply)
    
    bot_reply = chat1.get_reply("i'm fine")
    print("chat1: ", bot_reply)
    bot_reply = chat2.get_reply("i'm fine")
    print("chat2: ", bot_reply)
    bot_reply = chat3.get_reply("i'm fine")
    print("chat3: ", bot_reply)

