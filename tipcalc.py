def main ():
    dollar = dollars_to_float(input("How much was the meal? "))
    percent= percent_to_float(input("What percent would you like to tip? "))
    tip = percent * dollar
    print(f"leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.replace("$", ""))


def percent_to_float(p):
    return float(p.replace("%", "")) / 100

main()