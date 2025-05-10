print("name : monalisa.n \n usn : 1AY24AI073\n section : O ")

def print_table(headers, rows):
    col_widths = [max(len(str(cell)) for cell in column) for column in zip(headers, *rows)]
    row_format = " | ".join(f"{{:<{width}}}" for width in col_widths)

    print(row_format.format(*headers))
    print("-+-".join("-" * width for width in col_widths))

    for row in rows:
        print(row_format.format(*row))

# Example usage
if __name__ == "__main__":
    headers = ["Name", "Age", "City"]
    data = [
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"]
    ]
    print_table(headers, data)
