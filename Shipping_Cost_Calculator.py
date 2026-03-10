# Shipping_Cost_Calculator.py
"""Backwards-compatible entrypoint for the original script."""
from logistics.shipping import main

if __name__ == "__main__":
    raise SystemExit(main())
