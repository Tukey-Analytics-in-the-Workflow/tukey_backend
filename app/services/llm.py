def ask_llm(context: dict):
    return {
        "decision": f"Stock more {context['top_products'][0]}",
        "confidence": "High",
        "reason": f"Sales trend is {context['sales_trend']} in {context['time_period']}"
    }
