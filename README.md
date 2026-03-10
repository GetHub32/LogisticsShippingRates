# LogisticsShippingRates

Simple project for calculating shipping cost.

## Quickstart

1. Create a virtualenv
   python -m venv .venv
   source .venv/bin/activate
2. Install
   pip install -r requirements.txt
3. Run tests
   pytest
4. Use the module:
   from src.logistics.shipping import calculate_shipping_cost
   print(calculate_shipping_cost(2.0, 3.5))  # 7.0

Command-line:
   python -m src.logistics.shipping
