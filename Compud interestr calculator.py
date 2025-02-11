def accumulated_amount(time, rate, principal):
    
    return principal * ((1 + (rate / 100)) ** time)

print("Welcome to the bank accumulated amount calculator")


principal = float(input("Enter initial principal balance: "))
rate = float(input("Enter interest accumulation rate: "))
time = float(input("Enter time (in years): "))


amount = accumulated_amount(time, rate, principal)


print(f"The accumulated total amount in {time} years is {amount:.2f} Ksh")
