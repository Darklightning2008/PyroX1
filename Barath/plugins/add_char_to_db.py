from config import HANDLER, OWNER_ID, BARATH
from pyrogram import filters
import pymongo
from Barath import barath
import asyncio

# Initialize MongoDB client
mongo_client = pymongo.MongoClient("mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority")
db = mongo_client["your_database"]
collection = db["Event_Collection"]
sent_characters_collection = db["sent_characters"]

# Command to send data from collection
@barath.on_message(filters.command("addchar", HANDLER) & filters.me)
async def send_data(client, message):
    cursor = collection.find({})
    for document in cursor:
        character_id = document["_id"]
        if not sent_characters_collection.find_one({"character_id": character_id}):
            img_url = document["img_url"]
            name = document["name"]
            name_new = name.replace(" ", "-")

            anime = document["anime"]
            anime_new = anime.replace(" ", "-")
            rarity = document["rarity"]
            if rarity == "⛄ Winters[S]":
                new_rarity = 1
            elif rarity == "🧧 New Year[LE]":
                new_rarity = 2
            
            # Sending data
            sent_message = await client.send_photo(chat_id=message.chat.id, photo=img_url, caption=f"/event {img_url} {name_new} {anime_new} {new_rarity}")
            
            # Recording sent character's ID in collection
            sent_characters_collection.insert_one({"character_id": character_id, "sent_message_id": sent_message.message_id})
            asyncio.sleep(3)


