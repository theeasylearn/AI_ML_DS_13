#default argument function
def getSeconds(hours,minutes=0,seconds=0):
    print(f"hours = {hours} minutes = {minutes} seconds  = {seconds} ")
    totalSeconds = (hours * 60 * 60) + (minutes * 60) + seconds
    return totalSeconds #function return value 


result = getSeconds(10,9,35) 
print(f"total seconds = {result}")
result = getSeconds(10,9)
print(f"total seconds = {result}")
result = getSeconds(10)
print(f"total seconds = {result}")

