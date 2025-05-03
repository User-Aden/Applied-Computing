#Ask how much did the customer spend - 03/05/25
x = float(input("How much money did the customer spend  (in £): "))
#Check if the customer spent over £20, if true, print The customer can recvive a  £3 voucher - 03/05/25
if x > 20:
print("The customer qualifys for a £3 voucher")
#Check if the customer spent over £10, if true, print The customer can recvive a  £1 voucher - 03/05/25
elif x > 10:
print("The customer qualifys for a £1 voucher")
#If both false, print they did not spend enough to get a voucher - 03/05/25
else: 
print("The customer did not spend enough today to qualify for a voucher")
