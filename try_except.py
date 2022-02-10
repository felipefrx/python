try:
    print(x)
except:
    print("Error")
else:
    print("All right.")
finally:
    print("End of treatment.")


num = "Felipe"

if not type(num) is int:
    raise Exception("Only whole numbbers.")
else:
    print(num)