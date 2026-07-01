START

DEFINE prices:
    COFFEE_PRICE = 8.50
    TEA_PRICE = 6.00
    SANDWICH_PRICE = 12.00

FUNCTION calculate_total(coffee, tea, sandwich):
    total = (coffee * COFFEE_PRICE) + (tea * TEA_PRICE) + (sandwich * SANDWICH_PRICE)
    RETURN total

FUNCTION print_receipt(customer_name, coffee, tea, sandwich, total):
    PRINT "===== RECEIPT ====="
    PRINT "Customer :", customer_name
    PRINT "Coffee   :", coffee
    PRINT "Tea      :", tea
    PRINT "Sandwich :", sandwich
    PRINT "------------------"
    PRINT "Total = RM", total

MAIN:
    customer_name = ASK "Customer name: "
    coffee = ASK "Coffee quantity: "
    tea = ASK "Tea quantity: "
    sandwich = ASK "Sandwich quantity: "

    total = calculate_total(coffee, tea, sandwich)
    print_receipt(customer_name, coffee, tea, sandwich, total)

END