import os

class Config:
    API_ID = os.environ.get("API_ID", "21513517")
    API_HASH = os.environ.get("API_HASH", "838d3451485b95722878921877f12066")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7123612475:AAH5T6k6W253HuK2wb8kHPQtui4NQn-XcD8") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://sumit333:sumit333@cluster0.emqf08v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '5904348755').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
 
