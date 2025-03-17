import asyncio  # Import asyncio for asynchronous programming
import logging  # Import logging for structured logs
from asyncua import Client  # Import Client from asyncua for OPC UA communication

# 🔹 Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Step 1: Define the server URL (Make sure this matches your actual server)
SERVER_URL = "opc.tcp://localhost:4840"  # Change if needed

# Step 2: Define the main function (It handles connecting, reading, and disconnecting)
async def main():
    logging.info("Starting OPC UA Client...")

    # Step 3: Create an async client session and connect to the server
    async with Client(url=SERVER_URL) as client:
        logging.info(f"Connected to OPC UA Server at {SERVER_URL}")

        # Step 4: Get a reference to the "Server Status" node (standard node i=85)
        node = client.get_node("i=85")  # i=85 is a standard OPC UA node

        try:
            # Step 5: Read the value of the node asynchronously
            value = await node.read_value()

            # Step 6: Log the retrieved server status
            logging.info(f"Server Status: {value}")

        except Exception as e:
            logging.error(f"Error reading node value: {e}")

# Step 7: Run the asynchronous function using asyncio
if __name__ == "__main__":
    asyncio.run(main())
