"""Runs the clsses in the repo"""

from company.IT.Compliance import Compliance
from company.Finance import Finance
from company.forecast import forecast
import company.HR as HR
import supply.Inventory as Inventory


def main():
    """runs the main function"""
    org_functions = [Compliance, Finance, forecast, HR, Inventory]
    for i in org_functions:
        return i

if __name__ == "__main__":
    main()
