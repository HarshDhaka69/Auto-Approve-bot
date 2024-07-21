from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28484147"))
    API_HASH = getenv("API_HASH", "339dbdfab9626dfc5da6dd7c0aba1652")
    BOT_TOKEN = getenv("BOT_TOKEN", "7273391027:AAFyB5RRXoFpdBEle5hBQPsKnL7wp0_9v_s")
    SESSION_STRING = getenv("SESION_STRING", "BAGyojMAjnLbu_1c9LwGqet0oaKPGvkuUsoen2NGJTtzWJetgn0U4wLdsYAjRDoyafE4IZsP5UaqtZxf__6fkh4hoVHkuZ-exl8hyC27K5w0k3fiUawYb6gH9ubz8Qaq29WESma6JYK4yYE7AaKEwy-e1liLZPD3he-6AXgDq7gp4p6qgVPGNVygSZOYV-8C7bMQbSEKnRfHcYFsEEF-rVWMBjJil8T4TXK8-Ar4f1MQ3zlwzGX4yMu_9LMEevmqMUIRNXwvH0R7nN9wqwVUjGeXfZBuN_8MXDJ46b6dQ8p739M3EUHe-AQj9hi0Cvmkw_gHZepZnH68xmSlfojbYNiT_xDWDQAAAAFnuV93AA")
    FSUB = getenv("FSUB", "NiftyPool")
    CHID = int(getenv("CHID", "-1002057997692"))
    SUDO = list(map(int, getenv("SUDO", "6288275206").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://itsharshx432:FIdinAchypJomJ8@cluster0.a3fdtex.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
