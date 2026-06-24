is_on = True
app_running = False

if is_on == True and app_running == True:
    print("The device is on and App is running")
    
elif is_on == True and app_running == False:
    print("The device is on but app is not running")

elif not is_on:
    print("The device is not on")
    
    
x = 10
if 10 <= x < 20:
    print("The Number is between 10 and 20")