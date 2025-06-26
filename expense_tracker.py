import argparse
import json
from pathlib import Path

DATA_FILE = Path('data.json')

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_transaction(tr_type, amount, description):
    data = load_data()
    data.append({'type': tr_type, 'amount': amount, 'description': description})
    save_data(data)

def show_summary():
    data = load_data()
    income = sum(item['amount'] for item in data if item['type'] == 'income')
    expense = sum(item['amount'] for item in data if item['type'] == 'expense')
    balance = income - expense
    print(f"Total income: {income:.2f}")
    print(f"Total expenses: {expense:.2f}")
    print(f"Balance: {balance:.2f}")

def main():
    parser = argparse.ArgumentParser(description='Simple income and expense tracker')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new transaction')
    add_parser.add_argument('--type', choices=['income', 'expense'], required=True, help='Transaction type')
    add_parser.add_argument('--amount', type=float, required=True, help='Amount of the transaction')
    add_parser.add_argument('--description', default='', help='Optional description')

    subparsers.add_parser('summary', help='Show income and expense summary')

    args = parser.parse_args()

    if args.command == 'add':
        add_transaction(args.type, args.amount, args.description)
    elif args.command == 'summary':
        show_summary()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
