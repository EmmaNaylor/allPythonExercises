from datetime import datetime

now = datetime.now()
time = now.strftime("%H:%M")


def check_shift():
    if "00:00" <= time <= "08:00":
        shift = "nights"
    elif "08:00" <= time <= "16:00":
        shift = "days"
    else:
        shift = "evenings"
    return shift
