customer_name=input("enter customer name: ")

bill_amount= input("enter customer bill amount: ")

tip_percentage= input("enter tip%: ")

GST_percentage= input("enter gst%: ")

tip=(int(tip_percentage)*int(bill_amount))/100

gst=(int(GST_percentage)*int(bill_amount))/100

total_amount=int(bill_amount)+float(tip)+int(gst)

print("total bill    : ",total_amount)

rcvd_payment=input("enter the amount you recieved: ")

return_payment=(int(rcvd_payment)-int(total_amount))
input()

print("-----------------------")
print("Jalander Restuarant")
print("-----------------------")
print("Customer name : ", customer_name)
print("total bill    : ", int(bill_amount))
print("total tip     : ", int(tip))
print("total GST     : ",gst)
print("total bill    : ",total_amount)
print("cash recieved : ",int(rcvd_payment))
print("cash return   : ",return_payment)
print("-----------------------")
print("thank you visit again")
print("-----------------------")