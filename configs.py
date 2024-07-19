from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "2092870"))
    API_HASH = getenv("API_HASH", "d7f5fb245e4c0b489cba4f7b45bc4173")
    BOT_TOKEN = getenv("BOT_TOKEN", "7273391027:AAFyB5RRXoFpdBEle5hBQPsKnL7wp0_9v_s")
    FSUB = getenv("FSUB", "Anshuigroha")
    CHID = int(getenv("CHID", "-1000112234"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
