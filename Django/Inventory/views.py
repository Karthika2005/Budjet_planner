from django.shortcuts import render

def budget_planner(request):
    data = {}

    if request.method == "POST":
        income = float(request.POST.get("income", 0))

        # NECESSITIES
        rent = float(request.POST.get("rent", 0))
        groceries = float(request.POST.get("groceries", 0))
        transport = float(request.POST.get("transport", 0))
        utilities = float(request.POST.get("utilities", 0))
        medical = float(request.POST.get("medical", 0))
        nec_others = float(request.POST.get("nec_others", 0))

        necessity_total = rent + groceries + transport + utilities + medical + nec_others

        # NEEDS
        shopping = float(request.POST.get("shopping", 0))
        entertainment = float(request.POST.get("entertainment", 0))
        eatout = float(request.POST.get("eatout", 0))
        needs_others = float(request.POST.get("needs_others", 0))

        needs_total = shopping + entertainment + eatout + needs_others

        # SAVINGS
        insurance = float(request.POST.get("insurance", 0))
        investment = float(request.POST.get("investment", 0))
        sav_others = float(request.POST.get("sav_others", 0))

        savings_total = insurance + investment + sav_others

        # TOTAL EXPENSES
        total_expenses = necessity_total + needs_total + savings_total
        leftover = income - total_expenses
        emergency_fund = leftover if leftover > 0 else 0

        # LIMITS
        limit_nec = income * 0.50
        limit_need = income * 0.30
        limit_sav = income * 0.20

        # LIMIT CHECK MESSAGES
        nec_msg = "✔ Within 50% limit"
        needs_msg = "✔ Within 30% limit"
        sav_msg = "✔ Within 20% limit"

        if necessity_total > limit_nec:
            nec_msg = "❌ Overspending on Necessities!"

        if needs_total > limit_need:
            needs_msg = "❌ Overspending on Needs!"

        if savings_total > limit_sav:
            sav_msg = "❌ Overspending on Savings!"

        data = {
            "total_expenses": total_expenses,
            "leftover": leftover,
            "emergency_fund": emergency_fund,

            "necessity_total": necessity_total,
            "needs_total": needs_total,
            "savings_total": savings_total,

            "limit_nec": limit_nec,
            "limit_need": limit_need,
            "limit_sav": limit_sav,

            "nec_msg": nec_msg,
            "needs_msg": needs_msg,
            "sav_msg": sav_msg,
        }

    return render(request, "index.html", data)
