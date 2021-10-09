import datetime

# Κρατάμε την τιμή της ώρας
current_Hour = datetime.datetime.now().hour

# Ελέγχουμε εάν είναι πρώτος
flag = False

for i in range(2, current_Hour):
    if (current_Hour % i) == 0:
        flag = True
        break

if not flag:
    q = (current_Hour - 1) / 2

    if q % 2 == 1 and q >= 2:
        flag2 = False

        for i in range(2, int(q)):
            if (q % i) == 0:
                flag2 = True
                break

        if not flag2:
            print(current_Hour, " is a safe prime number.")
else:
    print(current_Hour, " is not a prime number")
