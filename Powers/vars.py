from os import getcwd, path

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])
is_env = path.isfile(env_file)


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default="6808170222:AAEy7kiRfRoppFJMCW8c2a-3D4yYlzJ5D6E")
    API_ID = int(config("API_ID", default=17596251))
    API_HASH = config("API_HASH", default="e58343b4c0193e293e391daf97603fcd")
    OWNER_ID = int(config("OWNER_ID", default=7552579717))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-1001603822916))  # if not given owner id will be msg dump :)
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="7552579717",
        ).split(None)
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="7552579717",
        ).split(None)
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="7552579717"
        ).split(None)
    ]
    # CHROME_BIN = config("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    # CHROME_DRIVER = config("CHROME_DRIVER", default="/app/.chromedriver/bin/chromedriver")
    GENIUS_API_TOKEN = config("GENIUS_API", default=None)
    # AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API", default="iXkrY3xWBKvi6dJcfCLrRxp5")
    DB_URI = config("DB_URI", default="mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = config("DB_NAME", default="zara")
    BDB_URI = config("BDB_URI", default="mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="AloneXSupport")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="AloneUpdates")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE", default='Asia/Kolkata')
    BOT_USERNAME = "AloneXRobot"  # Leave it as it is
    BOT_ID = "6392016724"  # Leave it as it is
    BOT_NAME = "Alone"  # Leave it as it is


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6808170222:AAEy7kiRfRoppFJMCW8c2a-3D4yYlzJ5D6E"
    API_ID = "17596251"  # Your APP_ID from Telegram
    API_HASH = "e58343b4c0193e293e391daf97603fcd"  # Your APP_HASH from Telegram
    OWNER_ID = 7552579717  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001603822916  # Your Private Group ID for logs if not passed your owner id will be msg dump
    DEV_USERS = []
    SUDO_USERS = []
    WHITELIST_USERS = []
    DB_URI = "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "zara"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    RMBG_API = "iXkrY3xWBKvi6dJcfCLrRxp5"
    PREFIX_HANDLER = ["!", "/", "$"]
    SUPPORT_GROUP = "SUPPORT_GROUP"
    SUPPORT_CHANNEL = "SUPPORT_CHANNEL"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority"
    WORKERS = 8
    # CHROME_BIN = "/app/.apt/usr/bin/google-chrome"
    # CHROME_DRIVER = "/app/.chromedriver/bin/chromedriver"
