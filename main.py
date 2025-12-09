import argparse
from datetime import date
from core import add_expense, get_all_espenses, summary, delete_expense, summary_by_month, export_to_csv

def cmd_add(args):
    
    description = args.description
    amount = args.amount

    try:
        exp_id = add_expense(description, amount)
    except ValueError as ve:
        print(f"[!] Error adding expense: {ve}")
        return
    
    print(f"[+] Expense added with ID: {exp_id}")
    

def cmd_list(args):
    expenses = get_all_espenses()
    if not expenses:
        print("[!] No expenses recorded.")
        return
    
    print("ID  Date        Description          Amount")
    print("--  ----------  -------------------  ------")
    for e in expenses:
        print(
            f"{e['id']:<3} {e['date']}  "
            f"{e['description'][:19]:<19}  "
            f"${e['amount']}"
        )

def cmd_total(args):
    total = summary()
    print(f"Total Expenses: ${total}")

def cmd_delete(args):
    try:
        exp_id = int(args.id)
    except ValueError:
        print("[!] Invalid ID. It must be an integer.")
        return
    success = delete_expense(exp_id)
    if success:   
        print(f"[+] Expense with ID {exp_id} deleted.") 
    else:
        print(f"[!] No expense found with ID {exp_id}.")

def cmd_summary_month(args):
    month = args.month
    total = summary_by_month(month)
    print(f"Total Expenses for month {month}: ${total}")

def cmd_export(args):
    filename = args.filename
    count = export_to_csv(filename)
    print(f"[+] Exported {count} expenses to {filename}.")


def build_parser():
    parser = argparse.ArgumentParser(
        prog = 'ExpenseTracker',
        description = 'A simple CLI Expense Tracker.'
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    #add command
    p_add = subparsers.add_parser("add", help="Add a new expense.")
    p_add.add_argument(
        "--description", "-d",
        required=True,
        help="Description of the expense."
    )
    p_add.add_argument(
        "--amount", "-a",
        type = float,
        required=True,
        help="Amount of the expense."
    )
    p_add.set_defaults(func=cmd_add)

    #list command
    p_list = subparsers.add_parser("list", help="List all expenses.")
    p_list.set_defaults(func=cmd_list)

    #total command
    p_total = subparsers.add_parser("total", help="Show total expenses.")
    p_total.set_defaults(func=cmd_total)

    #delete command
    p_delete = subparsers.add_parser("delete", help="Delete an expense by ID.")
    p_delete.add_argument(
        "--id",
        help="ID of the expense to delete."
    )
    p_delete.set_defaults(func=cmd_delete)

    #summary by month command
    p_summary_month = subparsers.add_parser("summary", help="Show total expenses for a specific month.")
    p_summary_month.add_argument(
        "--month", "-m",
        type=int,
        choices=range(1,13),
        required=True,
        help="Month (1-12) to summarize expenses for."
    )
    p_summary_month.set_defaults(func=cmd_summary_month)

    #export command
    p_export = subparsers.add_parser("export", help="Export expenses to a CSV file.")
    p_export.add_argument(
        "--filename", "-f",
        required=True,
        help="Filename for the exported CSV."
    )
    p_export.set_defaults(func=cmd_export)

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()