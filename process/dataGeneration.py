import sys
sys.path.append("../")
from libraries.libraries import *

exceptions = []
items = []
transactions = []


class basketData():
    def __init__():
        pass
    
    def exceptionHandling(error):
        exceptions.append({"error": error})

    def jsonLoads():
        if not transactions:
            basketData.exceptionHandling("trasnactions list is empty, please check if groceryitem.csv in data folder")
        else:
            if os.path.exists("data/transactions.json"):
                os.remove("data/transactions.json")
                with open("data/transactions.json", "w") as file:
                    json.dump(transactions, file)
            else:
                    with open("data/transactions.json", "w") as file:
                        json.dump(transactions, file)
    
    def itemCapture():
        if os.path.exists("data/groceryitem.csv"):
            with open("data/groceryitem.csv") as file:
                reader = csv.reader(file)

                for i, row in enumerate(reader):
                    if i > 0:
                        items.append(row[2])
                    else:
                        pass
        else:
            basketData.exceptionHandling("groceryitem.csv file not found")
    
    def generatingData():
        basketData.itemCapture()
        total_transactions = 7500
        max_items = 100

        for i in range(total_transactions):
            transaction_size = random.randint(1, max_items)
            transaction_items = random.choices(items, k=transaction_size)
            transaction_dict = {item: transaction_items.count(item) for item in set(transaction_items)}
            transactions.append({"transaction_id": str(uuid.uuid4()), "items": transaction_dict})
        
        basketData.jsonLoads()