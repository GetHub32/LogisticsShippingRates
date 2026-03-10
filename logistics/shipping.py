# logistics/shipping.py
"""Small shipping calculator library and CLI."""

from __future__ import annotations
import logging
import argparse
from typing import Optional


def calculate_shipping_cost(weight: float, rate: float) -> float:
    """Return shipping cost as weight * rate.

    Raises:
        ValueError: if inputs are invalid (negative or non-finite).
    """
    if not (isinstance(weight, (int, float)) and isinstance(rate, (int, float))):
        raise ValueError("weight and rate must be numbers")
    if weight < 0:
        raise ValueError("weight must be non-negative")
    if rate < 0:
        raise ValueError("rate must be non-negative")
    return weight * rate


def _prompt_float(prompt: str) -> float:
    raw = input(prompt).strip()
    return float(raw)


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Shipping cost calculator")
    parser.add_argument(
        "--weight", type=float, help="package weight in kilograms", required=False
    )
    parser.add_argument(
        "--rate", type=float, help="shipping rate per kilogram", required=False
    )
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    logging.basicConfig(level=logging.INFO)
    args = parse_args(argv)

    try:
        if args.weight is None:
            weight = _prompt_float("Enter the package weight in kilograms: ")
        else:
            weight = args.weight

        if args.rate is None:
            rate = _prompt_float("Enter the shipping rate per kilogram: ")
        else:
            rate = args.rate

        cost = calculate_shipping_cost(weight, rate)
    except ValueError as exc:
        logging.error("Invalid input: %s", exc)
        return 2
    except Exception as exc:
        logging.error("Unexpected error: %s", exc)
        return 3

    # Print with two decimals for readability
    print(f"Shipping Cost: {cost:.2f} USD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())