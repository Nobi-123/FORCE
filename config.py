# ==========================================================
# Group Manager Bot
# Author: learning_bots (https://github.com/learning_bots)
# Support: https://t.me/learning_bots
# Channel: https://t.me/learningbots79
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ==========================================================

import os

# Required configurations (loaded from environment variables)
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

# Owner and bot details
OWNER_ID = int(os.getenv("OWNER_ID", ""))
BOT_USERNAME = os.getenv("BOT_USERNAME", "RafinGroupBot")

# Links and visuals
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/TNCmeetup")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "https://t.me/TechNodeCoders")
START_IMAGE = os.getenv("START_IMAGE", "https://files.catbox.moe/j2yhce.jpg")
