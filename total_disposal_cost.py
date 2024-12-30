#disposal rate calculation
from unittest import skipIf


def disposal_rate():
    disposal_location = str(input("Will you be dumping at the Valicor in Inkster, MI or Dearborn, MI? ")).lower()
    disposal_rate_expectation = int(input("How much disposal in yards do you think will be accumulated from this job? "))
    dump_travel = int(input("How many miles will the dump add for travel? "))
    miles_rate_for_dump_per_mile = 1.00
    dump_travel_cost = dump_travel * miles_rate_for_dump_per_mile
    valicor_inkster_disposal = 74.00
    valicor_dearborn_disposal = 168.00
    environmental_fee = 0.01149
    minimal_disposal_fee = 400.00

    inkster_total_min_expense = 0
    inkster_total_expense = 0
    dearborn_total_min_expense = 0
    dearborn_total_expense = 0
    while disposal_location == "":
        try:
            if disposal_location == ["neither", "no", "none"]:
                inkster_total_expense = 0

            if disposal_location == "inkster":
                if disposal_rate_expectation <= 2:
                    inkster_total_min_expense = minimal_disposal_fee + dump_travel_cost
                elif disposal_rate_expectation > 2:
                    inkster_total_expense = (valicor_inkster_disposal * disposal_rate_expectation) * (1 + environmental_fee) + dump_travel_cost
                else:
                    inkster_total_expense = 0
            if disposal_location == "dearborn":
                if disposal_rate_expectation <= 2:
                    dearborn_total_min_expense = minimal_disposal_fee + dump_travel_cost
                elif disposal_rate_expectation > 2:
                    dearborn_total_expense = (valicor_dearborn_disposal * disposal_rate_expectation) * (1 + environmental_fee) + dump_travel_cost
                else:
                    dearborn_total_expense = 0
        except ValueError:
            print("You need to enter Inkster, Dearborn, or None for shop disposal.")
    disposal_total_expense = inkster_total_min_expense + inkster_total_expense + dearborn_total_min_expense + dearborn_total_expense
    return disposal_total_expense