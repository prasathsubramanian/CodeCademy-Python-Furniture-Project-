# Item 1

item_1_name = "Bradbury - Aurelio Study Set"

item_1_description = """ Love your desk job! The Bradbury Desk and 
Aurelio Study Chair make the perfect pair for your study or home office
The Bradbury Desk and Aurelio Study Chair are also both available individually
Dimensions : 53"l x 27.5"b X 30"h
For indoor use only """

item_1_price = 25499.00

# Item 2

item_2_name = "Ayana Curtain - Set Of 2"

item_2_description = """ Heartfelt, handcrafted. A tribute to things timeless, 
these delightful curtains are a contemporary take on traditional block print motifs. 
Every design is lovingly, painstakingly printed by hand on soft, 
breathable cotton. Hang them up and shut out the world!
Material: 100% cotton
Hand block printed
Top band: Stainless steel eyelets
Dimensions: 54” x 84”
Set of 2 curtains """

item_2_price = 2000.155551

# Item 3

item_3_name = "Snoozy Pet Handtufted Carpet"

item_3_description = """ Pet love. Transform the mood of your room with this fun, 
bright hand tufted carpet. For dog lovers who don’t have a dog or are away from theirs, 
here’s a rug with a life-size snoozing dog. Once placed under a coffee table, 
it gives the illusion of your pet sleeping under the table. It’s your reminder to slow down, 
relax and snooze a little.
Hand tufted
Made from wool with a canvas backing
Non reversible
Caring for your carpet: Vacuum regularly. Dry cleaning recommended. Avoid exposure to sunlight. """

item_3_price = 3999.21212


# orders

customer_name = "prasath"
customer_order_no = 1

purchase_item1 = item_2_name
purchase_quantity1 = 2
purchase_description1 = item_2_description
purchase_price1: float = item_2_price * purchase_quantity1

purchase_item2 = item_3_name
purchase_quantity2 = 3
purchase_description2 = item_3_description
purchase_price2: float = item_3_price * purchase_quantity2

GST : float = 0.28

customer1_total = purchase_price1 + purchase_price2 + GST



#receipt design

print("---------------------------------------------------------------------------------------------------------------------------")

print("Customer Name :" + customer_name + "                                                                                " + "Order No :" + str(customer_order_no))
print('\n')
print("S.no" + "      " + "Item" + "                                     " + "Quantity" + "                                       " + "Amount" )
print('\n')
print("---------------------------------------------------------------------------------------------------------------------------")

print('\n')

print("1" + "      " + purchase_item1 + "                             " + str(purchase_quantity1) + "                                 " + str(purchase_price1) )

print('\n')

print("  Description: " + purchase_description1 + "   " )

print('\n')

print("---------------------------------------------------------------------------------------------------------------------------")
print('\n')

print("2" + "      " + purchase_item2 + "                             " + str(purchase_quantity2) + "                                 " +  str(purchase_price2) )

print('\n')

print("  Description: " + purchase_description2 + "   " )

print('\n')

print("---------------------------------------------------------------------------------------------------------------------------")


print("                                                                  Gross Total Including GST 28%  = "  + str(customer1_total) )


print("---------------------------------------------------------------------------------------------------------------------------")

print('\n')