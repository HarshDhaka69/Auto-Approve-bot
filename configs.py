from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "2092870"))
    API_HASH = getenv("API_HASH", "d7f5fb245e4c0b489cba4f7b45bc4173")
    BOT_TOKEN = getenv("BOT_TOKEN", "7273391027:AAFyB5RRXoFpdBEle5hBQPsKnL7wp0_9v_s")
    FSUB = getenv("FSUB", "TestingSuxbot")
    CHID = int(getenv("CHID", "-1002219153273"))
    SUDO = list(map(int, getenv("SUDO", "6288275206").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://itsharshx432:FIdinAchypJomJ8@cluster0.a3fdtex.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
