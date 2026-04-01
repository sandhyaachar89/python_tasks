import datetime
import json
import os

class SuperMarket:
    BILL_FILE = "bills.json"

    def __init__(self):
        self.products = {
            1: {"name": "Rice (1kg)", "price": 60},
            2: {"name": "Sugar (1kg)", "price": 50},
            3: {"name": "Milk (1L)", "price": 40},
            4: {"name": "Oil (1L)", "price": 150},
            5: {"name": "Soap", "price": 35},
            6: {"name": "Shampoo", "price": 120},
            7: {"name": "Toothpaste", "price": 75},
            8: {"name": "Tea Powder (250g)", "price": 90},
            9: {"name": "Snacks Pack", "price": 30},
            10: {"name": "Biscuits", "price": 25}
        }
        self.cart = []
        self.bills = []
        self.load_bills()

    def load_bills(self):
        if os.path.exists(self.BILL_FILE):
            try:
                with open(self.BILL_FILE, "r") as f:
                    self.bills = json.load(f)
            except json.JSONDecodeError:
                self.bills = []

    def save_bills(self):
        with open(self.BILL_FILE, "w") as f:
            json.dump(self.bills, f, indent=4, default=str)

    def show_products(self):
        print("\n========== AVAILABLE PRODUCTS ==========")
        print("{:<5} {:<25} {:<10}".format("ID", "Product", "Price (₹)"))
        print("-------------------------------------------")
        for pid, info in self.products.items():
            print("{:<5} {:<25} {:<10}".format(pid, info["name"], info["price"]))
        print("-------------------------------------------")

    def add_to_cart(self):
        self.show_products()
        try:
            pid = int(input("Enter Product ID to add: "))
            qty = int(input("Enter Quantity: "))
        except ValueError:
            print(" Invalid input! Try again.")
            return

        if pid not in self.products:
            print(" Product ID not found!")
            return

        product = self.products[pid]
        total_price = qty * product["price"]
        self.cart.append({
            "product_id": pid,
            "product_name": product["name"],
            "quantity": qty,
            "unit_price": product["price"],
            "total_price": total_price
        })

        print(f" {qty} x {product['name']} added to cart successfully!")

    def view_cart(self):
        if not self.cart:
            print("\n Your cart is empty!")
            return

        print("\n========== YOUR CART ==========")
        print("{:<25} {:<10} {:<10} {:<10}".format("Product", "Qty", "Price", "Total"))
        print("----------------------------------------------------")

        total_amount = 0
        for item in self.cart:
            print("{:<25} {:<10} {:<10} {:<10}".format(item["product_name"], item["quantity"], item["unit_price"], item["total_price"]))
            total_amount += item["total_price"]

        print("----------------------------------------------------")
        print(f"Subtotal: ₹{total_amount}")
        print("----------------------------------------------------")

    def generate_bill(self):
        if not self.cart:
            print("\n Cart is empty! Please add items first.")
            return

        customer_name = input("Enter Customer Name: ").strip()
        if not customer_name:
            print(" Customer name cannot be empty!")
            return

        date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        subtotal = sum(item["total_price"] for item in self.cart)
        gst = round(subtotal * 0.05, 2)  
        grand_total = subtotal + gst

        bill_data = {
            "customer_name": customer_name,
            "date": date,
            "items": self.cart,
            "subtotal": subtotal,
            "gst": gst,
            "grand_total": grand_total
        }

        self.bills.append(bill_data)
        self.save_bills()

        print("\n========== FINAL BILL ==========")
        print(f"Customer: {customer_name}")
        print(f"Date: {date}")
        print("-------------------------------------------")
        print("{:<25} {:<10} {:<10} {:<10}".format("Product", "Qty", "Price", "Total"))
        print("-------------------------------------------")
        for item in self.cart:
            print("{:<25} {:<10} {:<10} {:<10}".format(item["product_name"], item["quantity"], item["unit_price"], item["total_price"]))
        print("-------------------------------------------")
        print(f"Subtotal: ₹{subtotal}")
        print(f"GST (5%): ₹{gst}")
        print(f"Grand Total: ₹{grand_total}")
        print("===========================================")
        print(" Bill generated and saved successfully!")

        self.cart = []

    def view_all_bills(self):
        if not self.bills:
            print("\nNo bills found yet!")
            return

        print("\n========== SAVED BILLS ==========")
        for b in self.bills:
            print(f"Customer: {b['customer_name']} | Date: {b['date']} | Total: ₹{b['grand_total']}")
            print("-------------------------------------------")

def main():
    shop = SuperMarket()

    while True:
        print("\n========== SUPERMARKET BILLING SYSTEM ==========")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Generate Bill")
        print("5. View All Bills")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            shop.show_products()
        elif choice == '2':
            shop.add_to_cart()
        elif choice == '3':
            shop.view_cart()
        elif choice == '4':
            shop.generate_bill()
        elif choice == '5':
            shop.view_all_bills()
        elif choice == '6':
            print(" Thank you for shopping with us! Visit again.")
            break
        else:
            print(" Invalid choice! Try again.")


if __name__ == "__main__":
    main()
