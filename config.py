import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "11734178"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "11e86105f12d9121b04afe06adf4d35f")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Kuku:kuku@123@cluster0.fk02aeq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
