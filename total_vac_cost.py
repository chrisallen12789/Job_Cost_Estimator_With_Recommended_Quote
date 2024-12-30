#Cost for vactor truck during straight time and includes the prompt to select
def cost_of_vactor():
    hours = int(input("Rounding up to the nearest hour, how long will the truck be on the job? "))
    miles = float(input("What are the total miles for this job round trip? "))
    vactor_hourly_cost = float(hours) * 90.00
    fuel_consumption_cost = float(hours) * 60
    mileage_cost = float(miles) * 1.00
    total_vactor_cost = float(vactor_hourly_cost + mileage_cost + fuel_consumption_cost)
    return total_vactor_cost


"""OVERHEAD COST FOR ALL TRUCKS"""
class VehicleExpense:
    days_in_year = 365.25
    vehicles = []
    def __init__(self, vehicle_class: str, monthly_payment: float, terms: int, insurance: float, registration_tax: float, heavy_use_tax: float):

        self.vehicle_class = vehicle_class.upper()  #Vehicle class, A, B, or C
        self.payment = monthly_payment              #Note Amount, rental and purchase
        self.terms = terms                          #Length of note
        self.insurance = insurance                  #6 month insurance policy
        self.registration_tax = registration_tax    #Yearly plate registration
        self.heavy_use_tax = heavy_use_tax          #DOT use tax yearly fee

        #validate inputs
        self.validate_inputs()

        #append vehicle input to list
        VehicleExpense.vehicles.append(self)

        """conditional to return error in event of negative numbers"""
    def validate_inputs(self):
        if any(val < 0 for val in [self.payment, self.insurance, self.registration_tax, self.heavy_use_tax]):
            raise ValueError("Values must be non-negative.")

    """import values from user for class type and vehicle number"""
    def set_vehicle_type(self, weight_class: str, vehicle_num: int):
        # Validate weight class
        if weight_class.upper() not in ['A', 'B', 'C']:
            raise ValueError("Vehicle class types accepted are A, B, and C.")

        # Set class and vehicle number
        self.vehicle_class = weight_class.upper()
        self.vehicle_num = vehicle_num

    """calculating monthly expense with payment and insurance no taxes accounted for"""
    def monthly_truck_expense(self) -> float:
        monthly_total_lease_cost = self.payment + ((self.insurance * 2) / 12) #monthly payment + monthly policy multiplied by 2 and then divided by 12 months
        return monthly_total_lease_cost

    """calculating yearly expense with taxes added"""
    def yearly_truck_expense(self) -> float:
        monthly_cost = self.monthly_truck_expense() #carry over monthly cost to feed into this method.
        """yearly cost figured including yearly tax amounts"""
        yearly_lease_cost = (monthly_cost * 12) + self.registration_tax + self.heavy_use_tax
        return yearly_lease_cost

    """breaking yearly cost into daily expense. Taking yearly cost and dividing it by days in year"""
    def daily_truck_expense(self) -> float:
        daily_cost= self.yearly_truck_expense() / self.days_in_year
        return daily_cost

    """Vehicles detailed together in print out"""
    @classmethod
    def list_all_vehicles(cls):
        print("Vehicle Inventory:")
        for i, vehicle in enumerate(cls.vehicles, start=1):
            print(f"Vehicle {i}:")
            print(f"  Class: {vehicle.vehicle_class}")
            print(f"  Monthly Payment: ${vehicle.payment:.2f}")
            print(f"  Insurance (6 months): ${vehicle.insurance:.2f}")
            print(f"  Registration Tax: ${vehicle.registration_tax:.2f}")
            print(f"  Heavy Use Tax: ${vehicle.heavy_use_tax:.2f}")
            print(f"  Monthly Expense: ${vehicle.monthly_truck_expense():.2f}")
            print(f"  Yearly Expense: ${vehicle.yearly_truck_expense():.2f}")
            print(f"  Daily Expense: ${vehicle.daily_truck_expense():.2f}")
            print("-" * 30)

    """Total expenses for all vehicles in inventory"""
    @classmethod
    def total_expenses(cls):
        total_yearly_cost = sum(vehicle.yearly_truck_expense() for vehicle in cls.vehicles)
        print(f"Total Yearly Expense for All Vehicles: ${total_yearly_cost:.2f}")