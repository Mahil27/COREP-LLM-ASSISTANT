def validate_output(data):
    flags = []

    if not data.amount:
        flags.append("Missing capital amount")

    if "200%" in data.risk_weight:
        flags.append("Risk weight unusually high")

    return flags
