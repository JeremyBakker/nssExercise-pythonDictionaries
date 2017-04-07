stockDict = { 'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':"Eastman Kodak", 'GE':"General Electric" }

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ), ( 'CAT', 100, '1-apr-1999', 24 ), 
( 'GE', 200, '1-jul-1998', 56 ) ]

for purchase in purchases:
	ticker_symbol = purchase[0]
	number_of_shares = purchase[1]
	purchase_price = purchase [3]
	total_price = number_of_shares * purchase_price
	company_name = stockDict[ticker_symbol]
	print("I purchased {} shares of {} stock for ${}".format(number_of_shares, company_name, total_price)+".")

portfolio = dict()

for purchase in purchases:
	ticker = purchase[0]
	company_name = stockDict[ticker]

	number_of_shares=purchase[1]
	purchase_price=purchase[3]
	full_purchase_price = number_of_shares * purchase_price

	try:
		portfolio[ticker].append(purchase) # Append the purchase to the ticker list
	except KeyError:
		portfolio[ticker]=list() # If the key doesn't exist yet, create it
		portfolio[ticker].append(purchase)

	print("I purchased {} stock for ${}".format(company_name, full_purchase_price))

for ticker, purchases in portfolio.items():
	print("------ {} ------".format(ticker))
	total_portfolio_stock_value = 0
	for purchase in purchases:
		total_portfolio_stock_value += purchase[1]*purchase[3]
		print(purchase)
	print("Total value of stock in portfolio: ${}\n\n".format(total_portfolio_stock_value))


