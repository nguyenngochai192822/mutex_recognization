FA_LPR = dict(FA_ALPHABET='abcddefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
              FA_DIGITS='0123456789')

FA_DOCS = dict(FA_ALPHABET='abcddefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
               FA_DIGITS='_#,.-%',
               SYMBOLS='_#,.-%',
               EN_DIGITS='0123456789')

ALPHABETS = dict(FA_LPR=FA_LPR, FA_DOCS=FA_DOCS)


ALPHABETS = {k: "".join(list(v.values())) for k, v in ALPHABETS.items()}
