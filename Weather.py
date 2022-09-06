temperature = int(input("What is the temperature?\n"))

if temperature > 80:
    print("It's too hot!")
    print("Stay inside.")
elif temperature < 60:
    print("It's too cold!")
    print("Stay inside.")
else:
    print("Let's go hiking!")    