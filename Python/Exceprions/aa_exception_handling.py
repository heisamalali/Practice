try:
    print(1/0)
except Exception as e:
    print(e)

try:
    raise ValueError("ValueError")
except Exception as e:
    print(e)
finally:
    print("finally")

try:
    raise Exception("Exception")
except Exception as e:
    print(e)
