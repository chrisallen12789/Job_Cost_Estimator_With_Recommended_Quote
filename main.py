
print("""
This should be easy, and all the math is done for you. 
Just figure out the basics and this software will take care of the rest. 

Enjoy and please feel free to email any
comments to me at Clane@Benkari.Net.
      """)

from total_labor_cost import operator_hourly_rate_includes_overtime, laborer_cost
from total_vac_cost import *
from misc_expense import equipment_special_tool_expense
from total_disposal_cost import disposal_rate

operator_overhead = operator_hourly_rate_includes_overtime()
total_laborer_cost = laborer_cost()
total_vactor_cost = cost_of_vactor()
disposal_total_expense = disposal_rate()
special_tool_cost = equipment_special_tool_expense()
total_overhead_expense = (operator_overhead + total_laborer_cost + total_vactor_cost +
                          disposal_total_expense + special_tool_cost)

quote_recommendation = total_overhead_expense * 1.5
profit_total = quote_recommendation - total_overhead_expense
hourly_profit_total = profit_total / 4


print(f"""
   Total:: {total_overhead_expense}
   Quote:: {quote_recommendation}
   
   Profit Total:: {profit_total}
   Hourly Profit:: {hourly_profit_total}
    
    Operator = {operator_overhead}
    
    Laborer(s) = {total_laborer_cost}
    
    Vactor/Vacall = {total_vactor_cost}
                
    Disposal Cost = {disposal_total_expense}
    
    Special Equipment Total = {special_tool_cost}  
""")