from time import time


def len_check(pes):
    if len(pes) != 11:
        return True
    return False


def dig_check(pes):
    if not pes.isdigit():
        return True
    return False


def date_check(pes):
    year = str(pes[0:2])
    month = int(str(pes[2:4]))
    day = int(str(pes[4:6]))
    century = month // 20
    month -= 20 * century
    if century == 0:
        year = "19"+year
    elif century == 1:
        year = "20" + year
    elif century == 2:
        year = "21" + year
    elif century == 3:
        year = "22" + year
    elif century == 4:
        year = "18" + year
    year = int(year)
    if month < 1 or month > 12:
        return True
    elif month in (4, 6, 9, 11) and (day < 1 or day > 30):
        return True
    elif month == 2:
        if (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)) and (day < 1 or day > 28):
            return True
        elif day < 1 or day > 29:
            return True
    elif month in (1, 3, 5, 7, 8, 10, 12) and (day < 1 or day > 31):
        return True
    return False


def che_check(pes):
    multi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    c = 0
    for i in range(10):
        c += (int(pes[i]) * multi[i])
    c = (10 - (c % 10)) % 10
    if c != int(pes[10]):
        return True
    return False


s = time()
total = correct = male = female = 0
invalid_length = invalid_digit = invalid_date = invalid_checksum = 0
with open("1e6.dat", "r") as file:
    for pesel in file:
        pesel = pesel.strip()
        if len_check(pesel):
            invalid_length += 1
        elif dig_check(pesel):
            invalid_digit += 1
        elif date_check(pesel):
            invalid_date += 1
        elif che_check(pesel):
            invalid_checksum += 1
        else:
            correct += 1
            if int(pesel[9]) % 2 == 0:
                female += 1
            else:
                male += 1
total = female + male + invalid_length + invalid_digit + invalid_date + invalid_checksum
print(f"{total, correct, female, male}\n"
      f"{invalid_length, invalid_digit, invalid_date, invalid_checksum}\n"
      f"Runtime = {round(time()-s, 2)}s")
