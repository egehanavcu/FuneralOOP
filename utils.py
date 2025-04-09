import random

def random_condolence_message():
    messages = [
        "My deepest condolences.",
        "May they rest in peace.",
        "I'm truly sorry for your loss.",
        "Wishing you strength and comfort during this difficult time.",
        "You are in my thoughts and prayers.",
        "Sending love and support to you and your family."
    ] # Those messages are from ChatGPT :)
    
    return random.choice(messages)