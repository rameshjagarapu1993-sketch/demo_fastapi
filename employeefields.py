

employees=[
    {
        "id" : 1,
        "name" : "Ramesh",
        "department" : "software",
        "leave_balance" :  25000,
    }
]

def get_all_employees():
    return employees


def get_employee_by_id(employess_id):
    for employee in employees:
        if employee["id"] == employess_id:
            return employee

    return None


def calculate_employee_status(employee, requested_leave):
    if  requested_leave <= employee["leave_balance"]:
        return "Approve the leave"
    else: 
        return "reject the leave"


