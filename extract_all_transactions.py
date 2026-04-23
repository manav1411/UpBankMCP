import os
from dotenv import load_dotenv
from upbankapi import Client

# Load environment variables
load_dotenv()

# Get API token from environment
UP_TOKEN = os.getenv("UP_BANK_API")

def main():
    if not UP_TOKEN:
        print("Error: UP_BANK_API environment variable is not set")
        return

    client = Client(token=UP_TOKEN)
    
    print("Extracting ALL transactions...")
    transactions = client.transactions()
    
    with open("transactions.txt", "w") as f:
        count = 0
        for tx in transactions:
            f.write(f"ID: {tx.id}\n")
            f.write(f"Status: {tx.status}\n")
            f.write(f"Description: {tx.description}\n")
            f.write(f"Amount: {tx.amount} {tx.currency}\n")
            f.write(f"Category: {tx.category.id if tx.category else 'None'}\n")
            f.write(f"Tags: {[tag.id for tag in tx.tags]}\n")
            f.write(f"Created At: {tx.created_at}\n")
            f.write("-" * 40 + "\n")
            
            count += 1
            if count % 100 == 0:
                print(f"Extracted {count} transactions...")

    print(f"Data extraction complete. Total transactions: {count}")

if __name__ == "__main__":
    main()
