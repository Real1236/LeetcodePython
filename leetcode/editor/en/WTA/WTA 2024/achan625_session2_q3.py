# Question 3 - Hash Maps
# Given a dictionary that contains mapping of employee and his manager as a number of (employee, manager) pairs, write a function to get no of employees under each manager in the hierarchy not just their direct reports. It may be assumed that an employee directly reports to only one manager. The root node/ceo is listed as reporting to himself. The output should be a dictionary that contains a mapping of the total number of employees working under each manager.

# Example:
# Input: 
# dic = {
# "A": "C" ,
# "B": "C",
# "C": "F",
# "D": "E",
# "E": "F",
# "F": "F"
# }
# Output:
# result = {
# A: 0,  
# B: 0,
# C: 2,
# D: 0,
# E: 1,
# F: 5
# } 
# Explanation:
# In this example C is manager of A, C is also manager of B, F is manager of C and so on.  A and B report to C, so C has 2 employees below them. D reports to E, so E has 1 person below them. C and E report to F, so F has the 2 employees directly reporting to them, plus the employees reporting to C, plus the employees reporting to E. F reports to themself to indicate that they are the ceo.

def count_employees_under_manager(employee_manager_map: dict) -> dict:
        direct_reports = dict()
        for key, value in employee_manager_map.items():
            if(key==value):
                continue
            if key not in direct_reports:
                direct_reports[key] = []
            if value not in direct_reports:
                direct_reports[value] = [key]
            else:
                direct_reports[value].append(key)
                
        count = dict()
        for manager in direct_reports:
            count[manager] = len(direct_reports[manager])
            for employee in direct_reports[manager]:
                count[manager] += len(direct_reports[employee])
        return count

dic = {
    "A": "C",
    "B": "C",
    "C": "F",
    "D": "E",
    "E": "F",
    "F": "F"
}
print(count_employees_under_manager(dic))

dic1 = {
    "X": "Y",
    "Y": "Z",
    "Z": "Z"
}
print(count_employees_under_manager(dic1))

dic2 = {
    "G": "H",
    "H": "I",
    "I": "J",
    "J": "K",
    "K": "K"
}
print(count_employees_under_manager(dic2))

# It first constructs a direct_reports dictionary to map each manager to their direct reports. Then, it calculates the total count of direct and indirect reports for each manager by iterating through the direct_reports dictionary.