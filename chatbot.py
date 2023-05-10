from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class ChatBot:
  def __init__(self, model_name='microsoft/DialoGPT-large'):
    self.model, self.tokenizer = self.load_model(model_name)    
    
  def load_model(self, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return model, tokenizer

  def get_reply(self, user_message: str, chat_history_ids=None):   
    # encode the new user message to be used by our model
    message_ids = self.tokenizer.encode(user_message + self.tokenizer.eos_token, return_tensors='pt')

    # append the encoded message to the past history so the model is aware of past context
    if chat_history_ids is not None:
      message_ids = torch.cat([chat_history_ids, message_ids], dim=-1)

    # generated a response by the bot 
    chat_history_ids = self.model.generate(
      message_ids,
      pad_token_id=self.tokenizer.eos_token_id, 
      do_sample=True, 
      max_length=200,
      top_k=100, 
      top_p=0.95,
      temperature=0.8,
    )
    
    decoded_message = self.tokenizer.decode(
      chat_history_ids[:, message_ids.shape[-1]:][0], 
      skip_special_tokens=True
    )
    
    return decoded_message, chat_history_ids


class Chat:
    def __init__(self, chatbot: ChatBot):
        self.chatbot = chatbot
        self.chat_history_ids = None


    def get_reply(self, user_message: str) -> str:
        bot_reply, chat_history_ids = self.chatbot.get_reply(user_message, self.chat_history_ids)
        self.chat_history_ids = chat_history_ids
        print(self.chat_history_ids)

        return bot_reply