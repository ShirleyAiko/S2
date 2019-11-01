TicketType = input("Enter Tickect Type: ")
while TicketType != 'E' and TicketType != 'S':
    TicketType = input("Enter Tickect Type: ")
BaggageWeight = int(input("Enter Tickect Type: "))
if TicketType == 'E':
    BaggageAllowance = 16
    ChargeRate = 3.5
else:
    BaggageAllowance = 20
    ChargeRate = 5.75
ExcessWeight = BaggageWeight - BaggageAllowance
if ExcessWeight > 0:
    Charge = ExcessWeight * ChargeRate
else:
    Charge = 0
print(Charge)