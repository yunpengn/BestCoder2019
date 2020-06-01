import pandas as pd

# Reads the data.
shops = pd.read_csv('data/shops.csv')
orders = pd.read_csv('data/orders.csv')
orders['count'] = 1

# Filters out official shops.
official_shops = shops.loc[shops['shop_type'] == 'Official Shop']
official_shops = official_shops.drop(columns='shop_type')
official_shops['shop_id'] = official_shops['shop_id'].astype(int)

# Finds out the top 3 items for each official shop.
total = official_shops.size
for i, shop in official_shops.iterrows():
    if i % 100 == 0:
        print('Current row: #{} out of {}'.format(i, total))

    # Gets all orders for the current shop.
    shop_orders = orders.loc[orders['shopid'] == shop['shop_id']]

    # Finds top 3 items.
    items_sold = shop_orders.groupby('itemid').count().reset_index()[['itemid', 'count']]
    top_3 = items_sold.sort_values('count', ascending=False).head(3)

    # Concatenates itemIDs together.
    item_IDs = ','.join(top_3['itemid'].astype(str))
    official_shops.at[i, 'Answer'] = item_IDs

# Saves the result.
official_shops.to_csv('output/round1.csv')
