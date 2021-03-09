print("==============================================")
print("")
print("Exercise 8-9 Messages")

messages= ['Hello thais', 'How are you doing', 'I miss you', 'I love you', "What's up?"]

def showMessages(msg):
    for m in msg:
       result = print(f"Content: {m}")
    return result

showMessages(messages)

print("==============================================")
print("")
print("Exercise 8-10 Sending Messages")

messages2= ['Hello thais', 'How are you doing', 'I miss you', 'I love you', "What's up?"]
sent_messages = []

def send_messages(msg):
    for m in msg:
        result = print(f"Content: {m}")
        sent_messages.append(m)
        print(f"Sent messages: {sent_messages}")
    return result

send_messages(messages2)


print("==============================================")
print("")
print("Exercise 8-11 Archived Messages")

messageSafe = ['ae', 'falou']
mm = []

def send_messages2(msg):
    mm.append(messageSafe)
    for m in mm:
        result = print(f"Content: {m}")
        sent_messages.append(m)
        print(f"Sent messages: {mm}")
        print(f"Saved messages: {mm}")
    return result

send_messages2(messageSafe)