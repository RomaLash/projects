import re
import sys
def Otkritie_faila(inputfile):
    file = open(inputfile,"r",encoding='utf-8')
    return file

def Zapis_v_fail(output_file,Answer_meri_array,Answer_comfort_array):
    """Функция записывает в файл данные, появившиеся в результате работы алгоритма"""
    file = open(output_file, "w", encoding='utf-8')
    file.write("Используемые меры: \n")
    for i in Answer_meri_array:
        file.writelines([str(i),"\n"])
    file.writelines(["Общий комфорт: ",str(Answer_comfort_array),"\n"])
    file.close()
    return output_file
    
def Zapolnenie(file):
    """Функция заполняет массивы входными данными для дальнейшей работы алгоритма"""
    Kolichestvo_ugroz = int(file.readline())
    Meri_alpha = []
    Meri_alpha = Meri_alpha[1:]
    for line in file:
        line = line[:(len(line) - 1)]
        Meri_alpha.append(line)
    file.close()
    Meri_beta = []
    for i in Meri_alpha:
        Meri_beta.append(re.split(' ',i))
    return Kolichestvo_ugroz,Meri_beta

def Comfortable(Meri_ok,Comfort_beta):
    """Функция обрабатывает массив удобств пользователя"""
    counter = 0
    Comfort_ok = []
    while counter < len(Meri_ok):
        Comfort_ok.append(int(Comfort_beta[counter]))
        counter = counter + 1
    print("Удобства: ",Comfort_ok)
    return Comfort_ok
    
def Pustoi(a):
    """Функция возвращает пустой массив размера а """
    counter = 0
    Null_array = []
    while counter < a:
        Null_array.append(0)
        counter = counter + 1
    return Null_array

def Odinochnii(a):
    """Функция возвращает единичный массив размера а """
    counter = 0
    Odin_array = []
    while counter < a:
        Odin_array.append(1)
        counter = counter + 1
    return Odin_array

def Meri(Meri_beta,Null_array,Kolichestvo_ugroz):
    """Функция обрабатывает массив мер, поданных на вход"""
    counter_1 = 0
    counter_2 = 0
    while counter_1 < (len(Meri_beta)-1):
        while counter_2 < len(Meri_beta[counter_1]):
            Null_array[int(Meri_beta[counter_1][counter_2])-1] = 1
            counter_2 = counter_2 + 1      
        Meri_beta[counter_1] = Null_array
        Null_array = []
        counter_3 = 0
        while counter_3 < Kolichestvo_ugroz:
            Null_array.append(0)
            counter_3 = counter_3 + 1
        counter_1 = counter_1 + 1
        counter_2 = 0
    return Meri_beta

def Algoritm(Odin_array,Meri_ok,Comfort_ok,Null_array):
    """Основной алгоритм программы"""
    Answer_meri_array = []
    counter_1 = 0
    counter_2 = 0
    kolvo_close_ugroz = 0
    Answer_comfort_array = 0
    best_kolvo_close_ugroz = 0
    best_comfort_ugrozi = 0
    
    while (1 in Odin_array):
        print("Меры: ")
        while (counter_1 < len(Meri_ok)):
            mera = Meri_ok[counter_1]
            comfort_ugrozi = Comfort_ok[counter_1]
            print(mera)        
            while counter_2 < len(mera):
                if (mera[counter_2] == Odin_array[counter_2] and mera[counter_2] == 1):
                    kolvo_close_ugroz = kolvo_close_ugroz + 1
                counter_2 = counter_2 + 1
            if (kolvo_close_ugroz > best_kolvo_close_ugroz or (kolvo_close_ugroz == best_kolvo_close_ugroz and best_comfort_ugrozi > comfort_ugrozi)):
                best_kolvo_close_ugroz = kolvo_close_ugroz
                kolvo_close_ugroz = 0
                best_mera = mera
                best_nomer_ugrozi = counter_1
                best_comfort_ugrozi = comfort_ugrozi
            else:
                kolvo_close_ugroz = 0
            counter_2 = 0
            counter_1 = counter_1 + 1
        print("Лучшая мера: ",best_mera)
        print("Удобство: ",best_comfort_ugrozi)
        Answer_comfort_array += best_comfort_ugrozi 
        print("Сколько угроз закрывает: ",best_kolvo_close_ugroz)
        Answer_meri_array.append(best_mera)    
        while counter_2 < len(best_mera):
            if (best_mera[counter_2] == Odin_array[counter_2] and Odin_array[counter_2] == 1):
                Odin_array[counter_2] = 0
                Null_array[counter_2] = 1
            counter_2 = counter_2 + 1
        print("Осталось закрыть: ", Odin_array)
        print("Мера, которую использовали: ",Meri_ok.pop(best_nomer_ugrozi))
        Comfort_ok.pop(best_nomer_ugrozi)
        
        counter_1 = 0
        kolvo_close_ugroz = 0
        best_mera = []
        best_kolvo_close_ugroz = 0
        best_nomer_ugrozi = 0
        counter_2 = 0
        
    return Answer_comfort_array,Answer_meri_array        

def Correct(inputfile):
    """ Проверяет наличие ошибок при вводе информации из файла."""
    file = open(inputfile,'r')
    Kolichestvo_ugroz = int(file.readline())
    if (Kolichestvo_ugroz < 1):
        raise Exception('Угрозы отсутствуют!')
    Meri_beta = []
    Meri_beta = Meri_beta[1:]
    for line in file:
        line = line[:(len(line) - 1)]
        Meri_beta.append(line)    
    if (len(Meri_beta) < 2):
        raise Exception('Недостаточно информации!')    
    Meri_ok = []
    for i in Meri_beta:
        Meri_ok.append(re.split(' ',i))
    print(Meri_ok)
    Meri_ok_1 = Meri_ok[:-1]
    for i in Meri_ok_1:
        for j in i:
            if (int(j) > Kolichestvo_ugroz):
                raise Exception('В мерах больше угроз, чем заявлено ранее!')

    Kolichestvo_mer = len(Meri_ok_1)
    Comfort_ok = Meri_ok.pop(len(Meri_ok) - 1)
    if Kolichestvo_mer != len(Comfort_ok):
        raise Exception('Количество весов не совпадает с количеством мер!')
    print("Проверка входного файла завершена. \n")
    file.close()


def input_test(inputfile,Etalon_meri,Etalon_kolichestvo):
    """Входной тест"""
    file = open(inputfile,"r",encoding='utf-8')
    Temp = Zapolnenie(file)
    Kolichestvo_ugroz = Temp[0]
    if Kolichestvo_ugroz != Etalon_kolichestvo:
        raise Exception("Тест не пройден (не совпадает количество угроз)!")
    Null_array = Pustoi(Kolichestvo_ugroz)
    Meri_ok = Meri(Temp[1],Null_array,Kolichestvo_ugroz)   
    i = 0
    j = 0
    while i < len(Meri_ok):
        while j < len(Meri_ok[i]):
            print(Meri_ok)
            print(Etalon_meri)
            if int(Meri_ok[i][j]) != int(Etalon_meri[i][j]):
                raise Exception("Тест не пройден (не совпадают массивы мер и весов)!")
                print(Meri_ok[i][j])
            j = j + 1
        i = i + 1
        j = 0
    print("Тест на вход пройден! Приступаю к тесту основного алгоритма!")    

def algoritm_test(Etalon_meri, Etalon_kolichestvo,Etalon_otvet, Etalon_comfort):
    """Тест алгоритма"""
    Comfort_beta = Etalon_meri.pop(len(Etalon_meri) - 1)
    Comfort_ok = Comfortable(Etalon_meri,Comfort_beta)
    Odin_array = Odinochnii(Etalon_kolichestvo)
    Null_array = Pustoi(Etalon_kolichestvo)
    Temp = Algoritm(Odin_array,Etalon_meri,Comfort_ok,Null_array)
    Answer_meri_array = Temp[1]
    Bool = 1
    for a in Answer_meri_array:
        if a not in Etalon_otvet:
            print("Тест основного алгоритма завершен с ошибкой. Удобство пользователя в идеальном случае - ", Etalon_comfort, ", посчитанное алгоритмом - ", Temp[0])
            Bool = 0
            break
    if Bool:
        print("Тест алгоритма завершен, перехожу к тесту вывода!")
    
def output_test(output_file,Etalon_otvet,Etalon_comfort):
    """Тест выхода"""
    Zapis_v_fail(output_file,Etalon_otvet,Etalon_comfort)
    text_file = open(output_file,"r",encoding='utf-8')
    Meri_beta = []
    for line in text_file:
        line = line[:(len(line) - 1)]
        Meri_beta.append(line)
    Comfort_alpha = Meri_beta[-1]    
    Meri_ok = Meri_beta[1:-1]
    counter_1 = 0
    jump_x3_counter = 1
    counter_2 = 0
    while counter_1 < len(Meri_ok):
        while jump_x3_counter < len(Meri_ok[counter_1]):
            if (int(Meri_ok[counter_1][jump_x3_counter])!= Etalon_otvet[counter_1][counter_2]):
                raise Exception("Запись неудачна (меры)!")
            jump_x3_counter = jump_x3_counter + 3     #python записывает в файл следующим образом - скобка,цифра,запятая,пробел,цифра и т.д.
            counter_2 = counter_2 + 1     #мне нужны только цифры - поэтому таким образом изменяется счетчик
        counter_1 = counter_1 + 1
        jump_x3_counter = 1
        counter_2 = 0
    Comfort_beta = (Comfort_alpha.find(':') + 1)
    Comfort_ok = int(Comfort_alpha[Comfort_beta:])
    if Comfort_ok!=Etalon_comfort:
        raise Exception("Запись неудачна (общее неудобство)!")
    print("Тест пройден!")    

def Correct_test(inputfile):
    """Проверка корректности файла - нанекорректном вхоже программа работать не будет"""
    oshibka = 0
    Correct(inputfile)
    if oshibka == 1:
        print("Тест не пройден - входной файл содержал ошибку, незамеченную программой!")
    
