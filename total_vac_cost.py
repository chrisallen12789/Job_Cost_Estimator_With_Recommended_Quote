#Cost for vactor truck during straight time and includes the prompt to select
def cost_of_vactor():
    hours = int(input("Rounding up to the nearest hour, how long will the truck be on the job? "))
    miles = float(input("What are the total miles for this job round trip? "))
    vactor_hourly_cost = float(hours) * 90.00
    fuel_consumption_cost = float(hours) * 60
    mileage_cost = float(miles) * 1.00
    total_vactor_cost = float(vactor_hourly_cost + mileage_cost + fuel_consumption_cost)
    return total_vactor_cost