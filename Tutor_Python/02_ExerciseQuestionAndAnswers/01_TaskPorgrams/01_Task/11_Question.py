# 11. A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in hundreds, find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.

amt = int(input("Enter the Amount to be Withdrawn :"))
hundred = amt//100
amt = amt%100
fifty = amt//50
amt = amt%50
ten = amt//10
print("No of Hundred Notes :",hundred)
print("No of Fifty Notes :",fifty)
print("No of Ten Notes :",ten)