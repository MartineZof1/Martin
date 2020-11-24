import random

def get_quest():
   vopros = open("tekst.txt","r",encoding=("utf-8"))
   question_list = vopros.read().splitlines()
   questnum = random.randrange (0,len(question_list))
   questline = str (question_list[questnum])
   for i in range(0,len(questline)):
       if questline[i]==";":
           question = questline[0:i]
           answer = questline[i+1:len(questline)]
           return answer, question

while True:
    initCheck="exit"
    print("Напишите '",initCheck,"' чтоб закончить! Напишите любую букву чтобы начать: ")  
    init=input()
    if init==initCheck:
        break
    
    answer, question = get_quest()
    print(question)
    print()
    view=[]
    check=""
    for i in range (0,len(answer)):
        if answer[i]==" ":
            view.append(" ")
        else:
            view.append(" - ")
    print("".join(view))
    popitki=5
    while popitki>0:
        ans = input("Введите букву или ответ: ")
        if ans.lower() == answer.lower():
            print("Загаданное слово было: {answer}");
            break
        elif (ans.lower() in answer.lower()):
            print("Правельная буква!")
            for i in range(0,len(answer)):
                if answer[i].lower()==ans.lower():
                    if answer[i].isupper():
                        view[i]=ans.upper()
                        check="".join(view)
                    else:
                        view[i]=ans.lower()
                        check="".join(view)
        else:
            print("Не правельная буква! У вас ",popitki-1," попытки.")
            popitki=popitki-1
        if check.lower()==answer.lower():
            print(f"Вы угадали все буквы! Загаданное слово: {answer}");break
        print(check)
        if popitki==0:
            print(f"Игра закончина!  Загаданное слово было: {answer}")