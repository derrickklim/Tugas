kata = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def terbilang(n):
    if n < 10:
        return kata[n]
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' billion ' + (terbilang(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + ' million ' + (terbilang(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
        if n // 1_000 == 1:
            return " one thousand " + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
        else:
            return terbilang(n // 1_000) + " thousand " + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
        if n // 100 == 1:
            return ' one hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
        else:
            return terbilang(n // 100) + ' hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
    elif n >= 20:
        if n // 10 == 2:
            return ' twenty ' + (terbilang(n % 20) if n % 20 != 0 else '')
        elif n // 10 == 3:
            return ' thirty ' + (terbilang(n % 20) if n % 30 != 0 else '')
        elif n // 10 == 4:
            return ' forty ' + (terbilang(n % 20) if n % 40 != 0 else '')
        elif n // 10 == 5:
            return ' fifty ' + (terbilang(n % 20) if n % 50 != 0 else '')
        elif n // 10 == 8:
            return ' eighty ' + (terbilang(n % 20) if n % 80 != 0 else '')
        else:
            return terbilang(n // 10) + 'ty ' + (terbilang(n % 10) if n % 10 != 0 else '')

    else:
        if n == 10:
            return ' ten '
        elif n == 11:
            return ' eleven '
        elif n == 12:
            return ' twelve '
        elif n == 13:
            return ' thirteen '
        elif n == 14:
            return ' fourteen '
        elif n == 15:
            return ' fifteen '
        elif n == 16:
            return ' sixteen '
        elif n == 17:
            return ' seventeen '
        elif n == 18:
            return ' eighteen '
        elif n == 19:
            return ' nineteen '
        else:
            return terbilang(n % 10)

#test
import os
while True:
    os.system('cls')
    try:
        n = int(input('angka ? '))
        print(f'{n:,} = {terbilang(n)}')
    except:
        print('data input anda tidak benar ...')
    os.system('pause')