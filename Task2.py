import threading
import time
import queue
import random
import json
from datetime import datetime

# ==========================================
# STEP 1: GLOBAL STATE & CONFIGURATION
# ==========================================
# Thread-safe queue for incoming background transactions
data_queue = queue.Queue()

# Default budget caps for categories
BUDGET_CAPS = {
    "Food": 150.0,
    "Cloud-Server": 200.0,
    "Marketing": 300.0,
    "Utilities": 100.0
}

# FILE STORAGE CONFIG
DATA_FILE = "live_expenses.json"

# ==========================================
# STEP 2: BACKGROUND REAL-TIME DATA STREAM
# ==========================================
def simulated_transaction_stream():
    """Simulates live incoming transaction events from an external API feed."""
    live_categories = ["Cloud-Server", "Marketing", "Utilities", "Office-Supplies"]
    while True:
        # Generate an incoming expense transaction every 5 to 10 seconds
        time.sleep(random.randint(5, 10))
        
        mock_transaction = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "category": random.choice(live_categories),
            "amount": round(random.uniform(10.0, 85.0), 2)
        }
        # Push to the thread-safe queue
        data_queue.put(mock_transaction)

# ==========================================
# STEP 3: CORE STORAGE AND FILE I/O LOGIC
# ==========================================
def save_state_to_disk(expenses, ledger):
    """Persists current memory data structures into a clean JSON file."""
    payload = {
        "expenses": expenses,
        "ledger": ledger
    }
    with open(DATA_FILE, "w") as f:
        json.dump(payload, f, indent=4)

def load_state_from_disk():
    """Restores data on initialization to prevent losing previous progress."""
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return data.get("expenses", {}), data.get("ledger", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return {}, [] # Return blank initial structures if no file exists

# ==========================================
# STEP 4: REAL-TIME STATE ACCUMULATION WORKER
# ==========================================
def process_incoming_queue(expenses, ledger):
    """
    Flushes the transaction queue instantly.
    Accumulates data into structures and evaluates budget limits on the fly.
    """
    new_data_processed = False
    
    while not data_queue.empty():
        transaction = data_queue.get()
        cat = transaction["category"]
        amt = transaction["amount"]
        
        # 1. Update Cumulative Totals
        expenses[cat] = expenses.get(cat, 0.0) + amt
        
        # 2. Append to Historical Record Ledger
        ledger.append(transaction)
        new_data_processed = True
        
        # 3. Budget Alert Logic Evaluation
        if cat in BUDGET_CAPS and expenses[cat] > BUDGET_CAPS[cat]:
            overdraft = expenses[cat] - BUDGET_CAPS[cat]
            print(f"\n🚨 [BUDGET WARNING]: Category '{cat}' has exceeded budget limit by ${overdraft:.2f}!")
            
    if new_data_processed:
        save_state_to_disk(expenses, ledger)
        print("\n📥 [SYSTEM]: New live background transactions accumulated and saved.")

# ==========================================
# STEP 5: ANALYTICS RUNTIME ENGINE
# ==========================================
def display_analytics(expenses, ledger):
    """Calculates granular real-time statistics out of the accumulated state."""
    if not expenses:
        print("\n📂 No transactions recorded yet to extract analytics.")
        return
        
    total_spent = sum(expenses.values())
    top_category = max(expenses, key=expenses.get)
    avg_transaction = total_spent / len(ledger) if ledger else 0.0
    
    print("\n" + "="*40)
    print("        📊 REAL-TIME METRICS DASHBOARD     ")
    print("="*40)
    for category, amount in expenses.items():
        percentage = (amount / total_spent) * 100
        cap_status = f"/ ${BUDGET_CAPS[category]}" if category in BUDGET_CAPS else "(No Cap)"
        print(f"• {category:<15}: ${amount:>7.2f} {cap_status:<10} ({percentage:.1f}%)")
        
    print("-"*40)
    print(f"Total Combined Spending : ${total_spent:,.2f}")
    print(f"Average Transaction Size: ${avg_transaction:,.2f}")
    print(f"Peak Operational Cost   : {top_category} (${expenses[top_category]:.2f})")
    print("="*40)

# ==========================================
# STEP 6: MAIN INTERACTIVE UI LOOP
# ==========================================
def main():
    # Load previously saved state from file system
    expenses, ledger = load_state_from_disk()
    
    # Spin up background data engine thread
    bg_thread = threading.Thread(target=simulated_transaction_stream, daemon=True)
    bg_thread.start()
    
    while True:
        # Check background worker changes right before drawing UI menu
        process_incoming_queue(expenses, ledger)
        
        print("\n--- MENU ---")
        print("1. Refresh & View Live Metrics Dashboard")
        print("2. Log a Manual Expense")
        print("3. View Historical Audit Ledger Logs")
        print("4. Safe Shutdown & Exit")
        
        choice = input("\nSelect Option (1-4): ").strip()
        
        # Flush queue immediately after input blocking delay ends
        process_incoming_queue(expenses, ledger)
        
        if choice == '1':
            display_analytics(expenses, ledger)
            
        elif choice == '2':
            cat = input("Enter Category: ").strip().capitalize()
            if not cat: continue
            try:
                amt = float(input(f"Enter Amount for '{cat}': "))
                if amt <= 0: raise ValueError
            except ValueError:
                print("❌ Invalid numerical amount.")
                continue
                
            # Manual Transaction Assembly
            manual_tx = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "category": cat,
                "amount": amt
            }
            
            # State accumulation execution
            expenses[cat] = expenses.get(cat, 0.0) + amt
            ledger.append(manual_tx)
            
            # Check budgets for manual inputs
            if cat in BUDGET_CAPS and expenses[cat] > BUDGET_CAPS[cat]:
                print(f"🚨 [BUDGET WARNING]: '{cat}' went over budget by ${expenses[cat] - BUDGET_CAPS[cat]:.2f}!")
                
            save_state_to_disk(expenses, ledger)
            print("✅ Transaction manually processed successfully.")
            
        elif choice == '3':
            print("\n" + "-"*50)
            print(f"{'TIMESTAMP':<22} | {'CATEGORY':<15} | {'AMOUNT':<10}")
            print("-"*50)
            for tx in ledger[-10:]: # Displays the last 10 transactions for readability
                print(f"{tx['timestamp']:<22} | {tx['category']:<15} | ${tx['amount']:<10.2f}")
            print("-"*50)
            
        elif choice == '4':
            save_state_to_disk(expenses, ledger)
            print("\nData structures cleanly flushed to persistent storage. Goodbye!")
            break
        else:
            print("❌ Invalid menu choice.")

if __name__ == "__main__":
    main()
    