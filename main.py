import random

def n_input():
    n=1
    try:
        n=int(input("Введите правую границу: "))
        return n
    except:
        print("Введите число!\n")
        n_input()
    return n

print("Добро пожаловать в числовую угадайку")
n=n_input()

num_rand=random.randint(1,n)
ans=0
k=1

while num_rand!=ans:
    try:
        ans=int(input("Отгадайте число от 1 до "+str(n)+": "))
        if ans>100 or ans<1:
            print("Введите число от 1 до", n ,"!\n")
            continue
    except:
        print("Введите число от 1 до", n ,"!\n")
        continue

    if ans>num_rand:
        k+=1
        print("Слишком много, попробуйте еще раз\n")
    elif ans<num_rand:
        k+=1
        print("Слишком мало, попробуйте еще раз\n")
    else:
        print("Вы угадали, поздравляем! Количество попыток: ",k)

