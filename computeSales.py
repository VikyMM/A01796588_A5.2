# pylint: disable=invalid-name
"""Compute sales totals from a product catalogue and sales record."""

import json
import sys
import time


def load_json_file(file_path):
    """Load and parse a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as err:
        print(f"Error: File '{file_path}' is not valid JSON. {err}")
        sys.exit(1)
    return data


def build_price_catalogue(products):
    """Build a dictionary mapping product title to price."""
    catalogue = {}
    for product in products:
        try:
            title = product["title"]
            price = float(product["price"])
            catalogue[title] = price
        except (KeyError, ValueError, TypeError) as err:
            print(f"Warning: Invalid product entry skipped. {err}")
    return catalogue


def compute_sales(catalogue, sales):
    """Compute total sales and return detailed results."""
    grand_total = 0.0
    sale_totals = {}
    errors = []

    for record in sales:
        try:
            sale_id = record["SALE_ID"]
            product_name = record["Product"]
            quantity = record["Quantity"]
        except (KeyError, TypeError) as err:
            error_msg = f"Error: Invalid sale record skipped: {err}"
            print(error_msg)
            errors.append(error_msg)
            continue

        if product_name not in catalogue:
            error_msg = (
                f"Error: Product '{product_name}' in SALE {sale_id} "
                f"not found in catalogue. Record skipped."
            )
            print(error_msg)
            errors.append(error_msg)
            continue

        if not isinstance(quantity, (int, float)):
            error_msg = (
                f"Error: Invalid quantity ({quantity}) for "
                f"'{product_name}' in SALE {sale_id}. Record skipped."
            )
            print(error_msg)
            errors.append(error_msg)
            continue

        price = catalogue[product_name]
        line_total = price * quantity
        grand_total += line_total

        if sale_id not in sale_totals:
            sale_totals[sale_id] = 0.0
        sale_totals[sale_id] += line_total

    return grand_total, sale_totals, errors


def format_results(grand_total, sale_totals, elapsed_time, errors):
    """Format results into a human-readable string."""
    lines = []
    lines.append("=" * 50)
    lines.append("         SALES RESULTS REPORT")
    lines.append("=" * 50)
    lines.append("")

    for sale_id in sorted(sale_totals.keys()):
        total = sale_totals[sale_id]
        lines.append(f"  SALE {sale_id:>4}:  ${total:>12,.2f}")

    lines.append("")
    lines.append("-" * 50)
    lines.append(f"  GRAND TOTAL:  ${grand_total:>12,.2f}")
    lines.append("-" * 50)

    if errors:
        lines.append("")
        lines.append("WARNINGS/ERRORS DURING PROCESSING:")
        for error in errors:
            lines.append(f"  - {error}")

    lines.append("")
    lines.append(f"Time elapsed: {elapsed_time:.4f} seconds")
    lines.append("=" * 50)

    return "\n".join(lines)


def main():
    """Main function to compute sales from JSON files."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py "
              "priceCatalogue.json salesRecord.json")
        sys.exit(1)

    catalogue_file = sys.argv[1]
    sales_file = sys.argv[2]

    start_time = time.time()

    products = load_json_file(catalogue_file)
    catalogue = build_price_catalogue(products)

    sales = load_json_file(sales_file)

    grand_total, sale_totals, errors = compute_sales(catalogue, sales)

    elapsed_time = time.time() - start_time

    results = format_results(
        grand_total, sale_totals, elapsed_time, errors
    )

    print(results)

    with open("SalesResults.txt", 'w', encoding='utf-8') as out_file:
        out_file.write(results + "\n")

    print("\nResults saved to SalesResults.txt")


if __name__ == "__main__":
    main()
