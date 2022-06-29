from random import choice, randint, shuffle
from config import HASH_TAGS_BASE, PREFIX_LIST

# Can't send emojis through selenium 😢

# EMOJI_LIST = ['😀', '😁', '🤣', '😃', '😄', '😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘', '😗']

# def random_emojis():
#     emojis = ""
#     for _ in range(randint(1, 5)):
#         emojis += choice(EMOJI_LIST)
#     return emojis


def random_prefix() -> str:
    return choice(PREFIX_LIST)

def gen_hashtags(topic: str) -> str:
    no_space = topic.replace(" ", "")
    hashtags = HASH_TAGS_BASE.copy()
    hashtags.append(f"#{no_space}")
    shuffle(hashtags)
    return " ".join(hashtags)