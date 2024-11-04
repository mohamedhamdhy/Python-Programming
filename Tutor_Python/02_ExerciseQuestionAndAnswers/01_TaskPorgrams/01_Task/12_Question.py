# 12. If the total selling price of 15 items and the total profit earned on them is input through the keyboard, write a program to find the cost price of one item.

sp = float(input("Enter the Selling Price :"))
profit = float(input("Enter the Profit :"))
cp = sp - profit
cp = cp // 15
print("Cost Price of Per Item :",cp)