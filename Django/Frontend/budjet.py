import matplotlib.pyplot as plt

def get_float(msg):
    try:
        return float(input(msg) or 0)
    except:
        print("Invalid number. Enter again.")
        return get_float(msg)

print("\n============================")
print("      BUDGET PLANNER")
print("============================\n")

# -----------------------------
# USER INCOME
# -----------------------------
income = get_float("Enter your Total Monthly Income: ₹ ")

nec_limit = income * 0.50
needs_limit = income * 0.30
save_limit = income * 0.20

# -----------------------------
# NECESSITIES (50%)
# -----------------------------
print("\n--- Necessities (50%) ---")

rent = get_float("Rent: ₹ ")
utilities = get_float("Utilities (EB, Water,Recharge, etc): ₹ ")
groceries = get_float("Groceries: ₹ ")
medical = get_float("Medical Essentials: ₹ ")
nec_others = get_float("Others: ₹ ")

nec_total = rent + utilities + groceries + medical + nec_others

# -----------------------------
# NEEDS (30%)
# -----------------------------
print("\n--- Needs (30%) ---")

shopping = get_float("Shopping: ₹ ")
subscriptions = get_float("Subscriptions: ₹ ")
eatout = get_float("Eat-out: ₹ ")
needs_others = get_float("Others: ₹ ")

needs_total = shopping + subscriptions + eatout + needs_others

# -----------------------------
# SAVINGS (20%)
# -----------------------------
print("\n--- Savings (20%) ---")

invest = get_float("Investment (FD/Gold/Stocks): ₹ ")
save_others = get_float("Others: ₹ ")

save_total_without_emergency = invest + save_others

# Emergency fund = remaining from 20% limit
emergency_fund = save_limit - save_total_without_emergency
if emergency_fund < 0:
    emergency_fund = 0

save_total = save_total_without_emergency + emergency_fund

# -----------------------------
# VALIDATION
# -----------------------------
print("\n============================")
print("          RESULTS")
print("============================")

if nec_total > nec_limit:
    print(f"❗ Necessities exceeded limit! (Allowed: ₹{nec_limit:.2f})")

if needs_total > needs_limit:
    print(f"❗ Needs exceeded limit! (Allowed: ₹{needs_limit:.2f})")

if save_total > save_limit:
    print(f"❗ Savings exceeded limit! (Allowed: ₹{save_limit:.2f})")

print("\nBreakdown:")
print(f"Necessities Total: ₹{nec_total:.2f}")
print(f"Needs Total: ₹{needs_total:.2f}")
print(f"Savings Total: ₹{save_total:.2f}")
print(f"Emergency Fund Auto-Added: ₹{emergency_fund:.2f}")

# -----------------------------
# PIE CHART
# -----------------------------
plt.figure(figsize=(4,4))  # small pie chart
labels = ['Necessities', 'Needs', 'Savings']
values = [nec_total, needs_total, save_total]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Budget Distribution")
plt.show()
