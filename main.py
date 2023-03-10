'3.2'
words = [] #создаем список
while (new_word := str(input())) != "stop":
    words.append(new_word) #есть список вордс и мы к нему добавляем слова из переменной нью вордс

print(" ".join(words)) #вывод списка плюс пробел

'3.3'
def z2():
    words = []
    while(new_word := str(input())) != "stop":
        if "ф" or "Ф" in new_word:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово!")

'3.4'
def z3():

    from random import randint
    t = 0
    f = 0
    while True:
        a = randint(1, 100)
        b = randint(1 , 100)
        print(f"{a}+{b} = ", end="")
        res = input()

        while not res.isdigit() and res != "stop":
            print("Ответ не верный")
            res = input()
        if res == "stop":
            break
        res = int(res)
        if a + b == res:
            t +=1
            print("Правильно!")
        else:
            print("Ответ неверный : ")
            f += 1
        if f >= 3:
            print("Игра окончена.Правильных ответов =", f )
z2(), z3()


