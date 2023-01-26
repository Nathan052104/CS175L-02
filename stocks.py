# Nathan Tunnessen
# CS175L-02
# Stocks
Commission_rate=float(input("Please eneter commission rate as a percent (ex. 05)"))
Num_shares= int(input("Please enter number of shares as a whole number:"))
Purchase_price= int(input("Please enter purchase price as a whole number:"))
Selling_price= float(input("Please enter selling price as a whole number:"))
amountPaidForStock = Num_shares*Purchase_price
purchaseCommission= Commission_rate*amountPaidForStock

totalPaid= amountPaidForStock + purchaseCommission
stockSoldFor= Num_shares*Selling_price
sellingCommission=Commission_rate*stockSoldFor
totalRecieved= stockSoldFor - sellingCommission
profitOrLoss = totalRecieved - totalPaid

print(f'Amount paid for stock: ${amountPaidForStock:,.2f}')
print(f'Commission paid on the purchase: ${purchaseCommission:,.2f}')
print(f'Amount the stock sold for: ${stockSoldFor:,.2f}')
print(f'Commission paid on the sale: ${sellingCommission:,.2f}')
print(f'Profit (or loss if negative: ${profitOrLoss:,.2f}')

