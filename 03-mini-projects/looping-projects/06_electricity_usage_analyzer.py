days=int(input("Enter number of days :"))
if days<=0:
    print("Invalid days ")
    exit()
total_units=0
high_usage_days=0
maximum_usage=0
for i in range(days):
    usage=int(input("Enter usage :"))
    total_units=total_units+usage
    if usage>10:
        high_usage_days=high_usage_days+1
    if usage >maximum_usage:
        maximum_usage=usage
average=total_units/days
if total_units>300:
    print("High Usage!")   
print("Total usage:", total_units)
print("Average usage:", average)
print("Maximum daily usage:", maximum_usage)
print("Days above 10 units:", high_usage_days)