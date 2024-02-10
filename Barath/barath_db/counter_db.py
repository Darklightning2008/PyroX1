from Barath import cli

counters_collection = cli["Kira_DB"]["Counters_DB"]

# Function to increment a counter by 1
async def increment_counter(counter_name):
    # Update the counter by incrementing its value by 1
    await counters_collection.update_one(
        {"counter_name": counter_name},
        {"$inc": {"count": 1}},
        upsert=True  # Create a new document if the counter doesn't exist
    )

# Function to list all counter names and their values
async def list_counters():
    # Find all documents in the counters collection
    cursor = counters_collection.find()

    # Initialize a dictionary to store counter names and values
    counters = {}

    # Iterate over the cursor and populate the counters dictionary
    async for document in cursor:
        counter_name = document["counter_name"]
        counter_value = document["count"]
        counters[counter_name] = counter_value

    return counters

# Function to get the counter value for a specific counter name
async def get_counter(counter_name):
    # Find the document in the counters collection based on the counter name
    counter_doc = await counters_collection.find_one({"counter_name": counter_name})

    if counter_doc:
        # If the counter document exists, return the counter value
        return counter_doc["count"]
    else:
        # If the counter document does not exist, return None
        return None
