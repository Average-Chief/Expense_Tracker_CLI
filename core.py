from datetime import date, datetime
import polars as pl
import json
import os

data_file = "expenses.json"

def _init_file():
    #create the data file if it does not exist
    if not os.path.exists(data_file):
        data = {
            "next_id": 1,
            "expenses": []
        }
        with open(data_file,"w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

def load_data():
    _init_file()
    with open(data_file,"r", encoding="utf-8") as f:
        data = json.load(f)
    
    if "next_id" not in data:
        data["next_id"] = 1
    if "expenses" not in data:
        data["expenses"] = []
    return data

def save_data(data):
    with open(data_file,"w", encoding = "utf-8") as f:
        json.dump(data, f, indent=4)

def add_expense(description:str,amount:float)->int:
    if amount <=0:
        raise ValueError("Amount must be positive.")
    
    data = load_data()
    expenses = data["expenses"]
    next_id = data["next_id"]

    expense = {
        "id": next_id,
        "date": date.today().isoformat(),
        "amount": amount,
        "description": description
    }

    expenses.append(expense)
    data["next_id"] = next_id + 1    
    save_data(data)
    return next_id

def get_all_espenses():
    data = load_data()
    return data["expenses"]

def summary():
    data = load_data()
    expenses = data["expenses"]
    total = sum(e["amount"]for e in expenses)
    return total

def delete_expense(expense_id:int)->bool:
    data = load_data()
    expenses = data["expenses"]
    original_len = len(expenses)
    expenses = [e for e in expenses if e["id"] != expense_id]
    if len(expenses)== original_len:
        return False
    data["expenses"] = expenses
    save_data(data)
    return True

def summary_by_month(month:int)->float:
    data = load_data()
    expenses = data["expenses"]
    filtered = [e for e in expenses if datetime.strptime(e['date'],"%Y-%m-%d").month == month]
    return sum(e["amount"] for e in filtered)

def export_to_csv(filename:str):
    data = load_data()
    expenses = data["expenses"]
    df = pl.DataFrame(expenses)
    df.write_csv(filename)
    return len(expenses)


