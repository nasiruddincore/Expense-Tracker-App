import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_expenses(num_records=300):
    os.makedirs(os.path.dirname(__file__), exist_ok=True)
    
    categories = ["Food", "Travel", "Rent", "Entertainment", "Utilities", "Shopping"]
    types = ["Expense", "Income"]
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    for _ in range(num_records):
        date = start_date + timedelta(days=random.randint(0, 360))
        t_type = "Income" if random.random() > 0.85 else "Expense"
        
        if t_type == "Income":
            category = "Salary"
            amount = random.randint(3000, 7000)
        else:
            category = random.choice(categories)
            amount = random.randint(10, 500) if category != "Rent" else random.randint(1000, 2000)
            
        data.append({
            "Date": date.strftime("%Y-%m-%d"),
            "Category": category,
            "Amount": amount,
            "Type": t_type
        })
        
    df = pd.DataFrame(data)
    df = df.sort_values(by="Date").reset_index(drop=True)
    
    filepath = os.path.join(os.path.dirname(__file__), "expenses.csv")
    df.to_csv(filepath, index=False)
    print(f"✅ Synthetic data generated successfully at {filepath}")

if __name__ == "__main__":
    generate_expenses()