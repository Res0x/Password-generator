from random import sample

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
hz = 'il1Lo0O'

def is_correct(txt):
    if txt == 'да' or txt == 'нет':
        return True
    return False
def check_d(y):
    while not is_valid(y):
        print('Введите число')
        y = input()

def is_valid(num):
    if num.isdigit():
        return True
    else:
        return False

def to_tf (txt):
    while True:
        if is_correct(txt):
            return True
        else:
            while not is_correct(txt):
                print('Введите да или нет')
                txt = input()

def create_chars (dg, uc, lc, pu, ns):
    chars = []
    if dg == True:
        chars.extend(digits)
    if uc == True:
        chars.extend(uppercase_letters)
    if lc == True:
        chars.extend(lowercase_letters)
    if pu == True:
        chars.extend(punctuation)
    if ns == False:
        chars.extend(hz)
    return chars
def generate(n, ln, chars):
    for i in range(int(n)):
        print(*sample(chars, int(ln)), sep='')

print('Сколько паролей нужно?')
num = input()
check_d(num)
print('Какая длина пароля?')
length = input()
check_d(length)
print('Включать ли цифры?')
digit = to_tf(input().lower())
print('Включать ли прописные буквы?')
upper = to_tf(input().lower())
print('Включать ли строчные буквы?')
lower = to_tf(input().lower())
print('Включать ли символы?')
symbols = to_tf(input().lower())
print('Исключать ли неоднозначные символы il1Lo0O?')
similar_symbols = to_tf(input().lower())
ch = create_chars(digit, upper, lower, symbols, similar_symbols)
generate(num, length, ch)