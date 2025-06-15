# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20793620"))
    API_HASH = getenv("API_HASH", "a712d2b8486f26c4dee5127cc9ae0615")
    BOT_TOKEN = getenv("BOT_TOKEN", "7610534695:AAETk26NvwYon8Vm0d--22iUpoK0FkhdM6U")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002330243493")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "1720910522 7825330156").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://baskarkass70:<G84z76PCCDuGCmnd@cluster0.u3oyyfa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
