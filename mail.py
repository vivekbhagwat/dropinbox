import box

def handle_message(message):
   access_token = access_token_from_email(message['From']) 
   if access_token is None:
       send_failure_email(message)
       return
    
    location = message['subject']
    if os.path.isabs(location):
        location = location[1:]

    location = location.split('/')
    for folder in location:
       #TODO check if exists? 
        
    if message['attachments']:
        for attachment in message['attachments']:
            box.put_file(attachment, location)
    
    if message['body']:
        box.put_file(attachment, location)




# TODO reply to message with failure notice
def send_failure_email(message):
