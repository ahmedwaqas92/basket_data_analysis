import sys
sys.path.append("../")

from libraries.libraries import *
from process.dataGeneration import *

errors = []
transactions = []

class aPriori():
    def __init__():
        pass

    def exceptionHandling(error):
        errors.append({"error": error})

    def gettingData():
        if os.path.exists("data/transactions.json"):
            basketData.generatingData()
            with open("data/transactions.json") as file:
                data = json.load(file)
                return data
        else:
            aPriori.exceptionHandling("Transactions json does not exist ")
            basketData.generatingData()
            with open("data/transactions.json") as file:
                data = json.load(file)
                return data
            
    def algorithm():
        data = aPriori.gettingData()
        for transaction in data:
            items = []
            for item, count in transaction["items"].items():
                items.extend([item] * count)
            transactions.append(items)

        te = TransactionEncoder()
        te_ary = te.fit(transactions).transform(transactions)
        df = pd.DataFrame(te_ary, columns=te.columns_)
        frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
        frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)
        frequent_itemsets['itemsets'] = frequent_itemsets['itemsets'].apply(lambda x: ', '.join(list(x)))

        plt.figure(figsize=(14, 8))
        sns.barplot(x='support', y='itemsets', data=frequent_itemsets, palette='viridis', hue="itemsets")
        plt.title('Support of Frequent Itemsets')
        plt.xlabel('Support')
        plt.ylabel('Itemsets')

        plt.show()
