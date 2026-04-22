import random
from datetime import datetime
 
HISTORY_FILE="history.txt"

responses={
    "greeting":[
        "hello! 😊",
        "hi there! ",
        "hey ✋",
        "assalamualaikum! 🤝"
    ],
    "how are you":[
        "i'am doing great 😀 what about you ?",
        "all good here! 📺",
        "feeling smart today 😎",
        "running perfectly as always!"
    ],
    "jokes":[
        "why don't programmer like nature? too many bugs 🤣",
        "i told my computer a joke ... it crashed 😅",
        "why did python go to school? to become a smart snake 🐍",
        "debugging: removing the needles from the haystack 🧠"
    ],
    "goodbye":[
        "goodbye! 👋",
        "see you later!",
        "Allah hafiz! 🤲",
        "take care!"
    ],
    "thanks":[
        "your welcome! 😀",
        "no proble !",
        "anytime!",
        "glad to help"
    ],
    "name":[
        "i'm your chatbot 🤖",
        "you can call me smartbot 😎",
        "i'm your assistant"
    ],
    "help":[
        "you can ask me for jokes, time, or just chat!",
        "try typing 'joke', 'time', or 'hi' ",
        "i'm still learning, but i can help a bit 😊"
    ],
    "time":[
        "let me check the time for you ⌚"
    ],
    "date":[
        "let me check today's date 📆"
    ],
    "unknown":[
        "hmm... i don't understand that 🧐",
        "can you say that differently?",
        "i'm still learning 😅"
    ]
}

def store_history(user,responses):
    now=datetime.now()
    timestamp=now.strftime("%d-%m-%y %H:%M:%S")

    with open(HISTORY_FILE,'a',encoding='utf-8') as file:

      file.write(f"{user}\n responses:{responses}\n-{timestamp}\n")
      file.close()

while True:
    user=input("Ask chatbot: ").lower()
    store_history(user,responses)

 
    if any (word in user for word in ['hi','hello','hey']):
        response=random.choice(responses['greeting'])
         

    elif "how are you " in user:
        response=random.choice(responses["how are you"])
    
    elif any(word in user for word in['jokes','laugh','funny']):
        response=random.choice(responses["jokes"])

    elif any(word in user for word in['bye','exit','goodbye']):
        response=random.choice(responses["goodbye"])
        print(responses)
        break

    elif any(word in user for word in['thankyou','thanks']):
        response=random.choice(responses["thanks"])

    elif "your name" in user:
        response=random.choice(responses["name"])

    
    elif "help" in user:
        response=random.choice(responses["help"])
        

    elif "time" in user:
        now=datetime.now()
        response=now.strftime("%H:%M:%S")

    elif "date" in user:
        now=datetime.now()
        response=now.strftime("%d-%m-%y")

    else:
        response=random.choice(responses["unknown"])

 
    print(response)

    
