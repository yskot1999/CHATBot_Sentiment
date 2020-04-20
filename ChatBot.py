def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def echo_all(updates):
    #print("echo")
    GREETING_INPUTS = ("Hello Amigo", "Hi", "Greetings","Hey buddy", "Heyy")
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            reply = get_reply(text,chat)
            print(reply)
            if(reply=="None"):
                #send_message(reply, chat)
                send_message(Questions.chooseNextQuestion(reply),chat)
            elif(reply=="NULL"):
                print("NULL")
            elif reply in GREETING_INPUTS:
                send_message(reply+"This is U.r.moodi",chat)
                send_message(Questions.chooseNextQuestion(reply),chat)
            else:
                send_message("Your song is on the way",chat)
                send_message("Tuning in!!",chat)
                str=songs.predict_song(reply)
                str=str.replace("\n","")
                bot.send_audio(chat_id=chat, audio=open(str, 'rb'))
                send_message("Enter /start for trying it again!!",chat)
                send_message("Enter /song for another song ",chat)
        except Exception as e:
            print(e)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def get_reply(text,chat_id):
    print("yash")
    rep=text+str(chat_id)
    print(rep)
    if(Dict.get("chat_id")==None):
        curr=[0,0,0,0,0]
        Dict["chat_id"]={"no_of_questions":0,"current_emo":curr}
        print(Dict)
    
    #return rep
    flag=True
    no_of_questions = Dict["chat_id"]["no_of_questions"]
    current_emo=Dict["chat_id"]["current_emo"]
    GREETING_INPUTS = ("Hello Amigo", "Hi", "Greetings","Hey buddy", "Heyy")
    answer = ''
    user_response = text
    user_response=user_response.lower()
    if(user_response=='/start' or no_of_questions>3 ):
        answer = random.choice(GREETING_INPUTS)
        return answer
    elif(user_response=="/song"):
        send_message("Your next song is on the way",chat_id)
        send_message("Stay tuned",chat_id)
        sentiment=emotion.final_predict(current_emo)
        str1=songs.predict_song(str(sentiment))
        str1=str1.replace("\n","")
        bot.send_audio(chat_id=chat_id, audio=open(str1, 'rb'))
        send_message("Enter /start for trying it again!!",chat_id)
        send_message("Enter /song for another song ",chat_id)
        return "NULL"
    elif(user_response!='bye'):
        current_emo=emotion.predict(no_of_questions,current_emo,user_response)
        Dict["chat_id"]["current_emo"]=current_emo
        #sentiment=emotion.final_predict(current_emo)
        no_of_questions=no_of_questions+1
        if(no_of_questions==3):
            sentiment=emotion.final_predict(current_emo)
            current_mood=str(sentiment)
            Dict["chat_id"]["no_of_questions"]=0
            Dict["chat_id"]["current_emo"]=[0,0,0,0,0]
            return str(sentiment)
        else:
            Dict["chat_id"]["no_of_questions"]=no_of_questions
            return "None"
    """global exitt
    answer = ''
    user_response = text
    user_response=user_response.lower()
    if(user_response=='/start'):
        answer = "Hello Sir! My name is Shanaya. I got to know about your job from XYZ website. I am interested to apply"
        return answer
    if(user_response!='bye'):
        if((user_response in CONV_ENDER_INPUTS) and not(int_asked)):
            #print("When and Where can I come for an interview?")
            answer = "When and Where can I come for an interview?"
            int_asked = True
            return answer
            #user_response = input()
            #print("okay! Thank you Sir")
            #flag=False
            #print("ROBO: You are welcome..")
        elif(int_asked):
            answer = 'Yes, Sir. Will be there. Bye! Nice talking to you'
            exitt = True
            return answer
            #sys.exit()
        else:
            if(greeting(user_response)!=None):
                #print("ROBO: "+greeting(user_response))
                answer = answer + greeting(user_response)
                
            else:
                #print("ROBO: ",end="")
                #print(response(user_response))
                answer = answer + response(user_response)
                sent_tokens.remove(user_response)
    return answer 
"""
def main():
    last_update_id = None
    while(True):
        updates = get_updates(last_update_id)
        print(updates)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    import nltk
    import numpy as np
    import random
    import string
    import sys
    sys.path.append('src')
    import Questions
    import emotion
    import songs
    #Setting it up with Telegram
    import requests
    import json
    import time
    import sys
    import telegram
    bot = telegram.Bot(token='1048652720:AAHmKh2086fO87pyVVaYVrMxSQbwe_WOykk')
    Dict={}
    global mood
    TOKEN = "1048652720:AAHmKh2086fO87pyVVaYVrMxSQbwe_WOykk"
    URL = "https://api.telegram.org/bot{}/".format(TOKEN)  
    print("hell")  
    main()