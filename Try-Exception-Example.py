# Try & Exception Example Code
try:
    #print("10" + 10)
    print(2+10)
except IOError:
    print("You Have an input/output error!")
except TypeError:
    print("You are using the worng data types!")
except:
    print("you got an error")
else:
    print("Run Successfull without error")
finally:
    print("Your Code run out and final.")