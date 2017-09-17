# whaddup?
# yo
# hello world
# get it cuz you're my world
import re
from unicode_dict import EMOJI_UNICODE


smiley = "\U0001f600"
frowny = "\U00002639"

# input_text = input("What do you want to emojify?\n")
input_text = open("text_to_translate.txt", "r").read()


def get_emoji(word):
    word = word.group(0)
    word_alphanum = re.sub(r"[^a-zA-Z0-9_]", "", word)
    if word_alphanum != "":
        if word_alphanum.lower() in EMOJI_UNICODE.keys():
            return re.sub(r"([\w]+)", EMOJI_UNICODE[word_alphanum.lower()] + " ", word)
        # Handle plurals
        elif word_alphanum[-1]=="s" and word_alphanum.lower()[:-1] in EMOJI_UNICODE.keys():
            return re.sub(
                r"([\w]+)", EMOJI_UNICODE[word_alphanum.lower()[:-1]]*2 + " ", word
                )
        else:
            return word
    else:
        return word


def sub_emoji_text(text):
    return re.sub(r"([^\s]+)", get_emoji, text)


output_text = sub_emoji_text(input_text)

print(output_text)