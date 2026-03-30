from database import create_table
from expenses import add_expense, get_all_expenses, get_total_by_category

def main():
    create_table()
    while True:
        print("\n1. Add Expense  2. View All  3. View by Category  4. Quit")
        choice = input("Choose: ")
        if choice == "1":
            cat = input("Category: ")
            amt = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD): ")
            desc = input("Description (optional): ")
            add_expense(cat, amt, date, desc)
            print("Added!")
        elif choice == "2":
            for row in get_all_expenses():
                print(row)
        elif choice == "3":
            for row in get_total_by_category():
                print(f"{row[0]}: ${row[1]:.2f}")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()