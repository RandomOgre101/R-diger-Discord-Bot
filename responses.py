import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hallo!'
    
    if p_message == 'roll':
        return str(random.randint(1,6))
    
    if p_message == 'random':
        return str(random.randint(0,1000))
    
    if p_message == '!help':
        return '`Getting started with Rudiger-Bot:\nType hello to get a response\nType roll to get a dice roll from 1-6\nType random to get a random number between 1-1000\n Use \'?\' before any command to get response to your DM`'
    

