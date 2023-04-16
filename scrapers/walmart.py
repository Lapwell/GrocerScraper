from requests_html import HTMLSession

produce_url = 'https://www.walmart.ca/browse/grocery/fruits-vegetables/10019-6000194327370?icid=grocery_wm_OGL1_LMagCategory_Tile_Fruits_Veg'
dairy_eggs_url = 'https://www.walmart.ca/browse/grocery/dairy-eggs/10019-6000194327369?icid=homepage_HP_GroceryTiles_Name_DairyEggs'

#Setting up requests-html connection
session = HTMLSession()
payload = {'walmart.nearestPostalCode': 'V9B9Z0'}
walmartSession = session.get(produce_url)
# walmartSession.post('walmart.ca', data=payload)
