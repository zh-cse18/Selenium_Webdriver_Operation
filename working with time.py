from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H")
print("Current Time =", current_time)