"""
# Let's Build a Vendor Availability system

## Problem

We need to know if a vendor (restaurant) is available to deliver a meal. 
So given a list of upcoming meals, build a function that will tell us if 
the vendor (restaurant) is available to take the order.

## Requirements

- input: take a vendor_id and a date
- output: True if the vendor is available, False if not
- A vendor is available if:
  - They have enough drivers for a concurrent delivery
  - As long as the delivery blackout period doesn't overlap (30 minutes before, 10 minutes after)
"""
import pytest
from datetime import datetime, timedelta
import re

check_date=(datetime.now()+timedelta(days=1)).strftime("%Y-%m-%d")
check_date2=(datetime.now()+timedelta(days=2)).strftime("%Y-%m-%d")

# A list of meals to be delivered
meals = {
    "results": [
    {
        "vendor_id": 1,                    # Vendor 1 will be serving
        "client_id": 10,                   # Client 10 on
        "datetime": check_date+" 13:30:00"  # January 1st, 2017 at 1:30 pm
    },
    {
        "vendor_id": 1,
        "client_id": 40,
        "datetime": check_date2+" 14:30:00"
    },
    {
        "vendor_id": 2,
        "client_id": 20,
        "datetime": check_date+" 13:30:00"
    },
    {
        "vendor_id": 3,
        "client_id": 50,
        "datetime": check_date+" 13:30:00"
    },
        {
        "vendor_id": 3,
        "client_id": 60,
        "datetime": check_date+" 13:30:00"
    },
        {
        "vendor_id": 3,
        "client_id": 70,
        "datetime": check_date+" 13:30:00"
    }
  ]
}

# Driver information per vendor.
vendors = {
    "results": [
    {
        "vendor_id": 1,
        "drivers": 1
    },
    {
        "vendor_id": 2,
        "drivers": 3
    },
    {
        "vendor_id": 3,
        "drivers": 3
    }
  ]
}


# you can write the function here.
def is_vendor_available(vendor_id, date_time):
    vendors_drivers = {v["vendor_id"]: v["drivers"] for v in vendors["results"]}
    
    if vendor_id in vendors_drivers:
        drivers_available = vendors_drivers[vendor_id]
    else:
        raise ValueError("This vendor is not exist")
    
    if type(date_time)!=str:
        raise TypeError("The input date has a wrong type")
    
    if re.search(r"\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d", date_time) is not None:
        date_time=datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
    else:
        raise ValueError("The input date should have a valid format")
    
    if date_time<datetime.now()+timedelta(minutes=30):
        raise ValueError("It is impossible to choose the past time")    
    
    for order in meals["results"]:
        if order["vendor_id"] == vendor_id:
            order_time = datetime.strptime(order["datetime"], "%Y-%m-%d %H:%M:%S")
            if date_time>=order_time-timedelta(minutes=30) and date_time<=order_time+timedelta(minutes=10):
                drivers_available-=1
                if drivers_available == 0:
                    return False
    return True


"""
Here's some tests to get you started
"""


def test_vendor_is_not_exist():
    with pytest.raises(ValueError):
        is_vendor_available(5, check_date+" 13:30:00")

def test_wrong_date_type():
    with pytest.raises(TypeError):
        is_vendor_available(1, 3)

def test_wrong_date_format():
    with pytest.raises(ValueError):
        is_vendor_available(1, "17-01-01 13:30:00")

def test_date_less_than_now():
    with pytest.raises(ValueError):
        is_vendor_available(1, "2020-01-01 13:30:00")



def test_unavailable_vendor():
    assert is_vendor_available(1, check_date+" 13:30:00") == False
    
def test_available_vendor():
    assert is_vendor_available(1, check_date+" 14:30:00") == True

def test_unavailable_vendor_time_interval():
    assert is_vendor_available(1, check_date+" 13:00:00") == False
    assert is_vendor_available(1, check_date+" 12:59:00") == True
    assert is_vendor_available(1, check_date+" 13:40:00") == False
    assert is_vendor_available(1, check_date+" 13:41:00") == True

def test_available_vendor_many_drivers():
    assert is_vendor_available(2, check_date+" 13:30:00") == True

def test_available_vendor_many_drivers_runout():
    assert is_vendor_available(3, check_date+" 13:30:00") == False

"""
Sanity tests
""" 
def test_exceptions_get_caught():
    with pytest.raises(Exception) as e_info:
        x = 1 / 0

def test_sanity():
    assert 2 + 2 == 4
    
pytest.main()


