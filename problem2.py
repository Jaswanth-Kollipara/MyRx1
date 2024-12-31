from datetime import date
from typing import List

class Employee:
    name: str
    employee_id: str
    date_of_join: date
    address: List[str]

if __name__=="__main__":
    address1="address1"
    address2="address2"
    employee= Employee(
        "Jaswanth",
        "1",
        date(2022,1,1),
        [address1,address2]
    )
