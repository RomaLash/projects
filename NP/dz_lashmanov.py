import re
import sys
from function import *
input_file = sys.argv[1]     #аргумент командной строки - входной файл
output_file = sys.argv[2]     #аргумент командной строки - выходной файл
Correct(input_file)           #проверка корректности обрабатываемого файла
Temp = Zapolnenie(Otkritie_faila(input_file)) 
Kolichestvo_ugroz = Temp[0]       #Kolichestvo_ugroz - количество угроз
Meri_beta = Temp[1]     #Meri_beta - массив мер, не обработанный
Null_array_1 = Pustoi(Kolichestvo_ugroz)     #Null_array - пустой массив, размер - количество угроз
Meri_ok = Meri(Meri_beta,Null_array_1,Kolichestvo_ugroz) #Meri_ok - массив мер, обработанный

Comfort_beta = Meri_ok.pop(len(Meri_ok) - 1) #Comfort_beta - массив "неудобств", необработанный
print("Подано на вход: ")
for k in Meri_ok:
        print(k)
Odin_array = Odinochnii(Kolichestvo_ugroz)     #Odin_array - одиночный массив
Null_array_2 = Pustoi(Kolichestvo_ugroz)     #Null_array - пустой массив, размер - количество угроз
Comfort_ok = Comfortable(Meri_ok,Comfort_beta)       #Comfort_ok - массив "неудобств", обработанный

Temp = Algoritm(Odin_array,Meri_ok,Comfort_ok,Null_array_2)
Answer_meri_array = Temp[1]     #Answer_meri_array - массив мер, использованных при решении задачи
Answer_comfort_array = Temp[0]       #Answer_comfort_array - общее неудобство пользователя (меньше - лучше)
print("Используемые меры: ")    
for i in Answer_meri_array:
    print(i)
print("Общий комфорт: ",Answer_comfort_array)
Zapis_v_fail(output_file,Answer_meri_array,Answer_comfort_array)

        
