import os
import re
import time
import random

# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
# from main import I18n
from zi_i18n import I18n

# en_US.zi.lang (<lang>.zi.lang)
# ------------------------------
# "<!example.test: "This is a test">" -> example.test = "This is a test"
# "<!example.test2: "This also a test">" -> example.test2 = "This also a test"
#
# Dictionary
# ----------
# ! -> Translation type (Might scrap this idea)
# example.test -> Name
# "This is a test" -> Translated Text

class MyTimer():
    def __init__(self):
        self.start = time.time()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        runtime = (end - self.start)*1000
        msg = 'The function took {time} ms to complete'
        print(msg.format(time=runtime))

# with MyTimer():
    # i18n = I18n()
    # print(i18n.translate("example.test"))
    # i18n.change_lang("id_ID")
    # print(i18n.translate("example.test"))
    # print(i18n.latency())
    # i18n.change_lang("fr")
    # i18n.translate("example.test")

i18n = I18n()
print(i18n.translate("example.text"))
i18n.change_lang("id_ID")
print(i18n.translate("example.text"))



# test = ["<!example.test='lmao'>"]

# test2 = "test"

# print(process.extract(test2, test))
# print(fuzz.ratio(test, test2) >= 65)
