print("name : monalisa.n \n usn : 1AY24AI073 \n section : O ")

def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total += count
    print(f"Total items: {total}")

# Example usage
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1}
display_inventory(inventory)
