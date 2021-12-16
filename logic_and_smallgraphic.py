import tkinter as tk # библиотека для графики
from math import copysign, fabs, floor, isfinite, modf, factorial, ceil, log # для усложненных математических действий
import pandas as pd # библиотека для работы с удобными таблицами


def decimalToBinary(value):
    """
    функция для перевода любого числа в двоичную с/с
    :param value: число изначально
    :return: число после перевода
    """
    # !!!не мой код, использовал интернет!!!
    if not isfinite(value):
        return repr(value)  # inf nan
    sign = '-' * (copysign(1.0, value) < 0)
    frac, fint = modf(fabs(value))  # split on fractional, integer parts
    n, d = frac.as_integer_ratio()  # frac = numerator / denominator
    assert d & (d - 1) == 0  # power of two
    return f'{sign}{floor(fint):b}.{n:0{d.bit_length() - 1}b}'
    # !!!конец не моего кода!!!

def numAfterComm(number, number_new):
    """
    функция вычисления количества знаков после запятой после перевода числа из 10 с/с в 2 с/с
    :param number: изначальное число
    :param number_new: число после перевода
    :return: кол-во знаков после запятой
    """
    temp = str(number)
    after_comm = abs(temp.find('.') - len(temp)) - 1
    after_comm_new = ceil(after_comm * log(10, 2))
    len_before_comm = abs(str(number_new).find('.')) + 1
    return len_before_comm+after_comm_new


def from_10_to_2_8_16():
    """
    окно перевода из 10 с/с в 2-8-16 с/с
    :return:
    """

    def from_10_to_2_8_16_logic():
        """
        функция перевода числа из 10 с/с в 2-8-16 с/с
        :return:
        """
        number_from_10_to_2_8_16 = float(ent_number_from_10_to_2_8_16.get())
        number_from_10_to_2_8_16_new = decimalToBinary(number_from_10_to_2_8_16)
        after_comm = numAfterComm(number_from_10_to_2_8_16,number_from_10_to_2_8_16_new)
        lbl_result_from_10_to_2_8_16["text"] = number_from_10_to_2_8_16_new[:(after_comm)]

    # создание нового окна и его основных элементов
    window_from_10_to_2_8_16 = tk.Tk()
    window_from_10_to_2_8_16.title("Перевод из 10 в 2-8-16")
    window_from_10_to_2_8_16.configure(bg='#F1DCC9')
    frame_from_10_to_2_8_16 = tk.Frame(window_from_10_to_2_8_16, bg='#F1DCC9')
    label_from_10_to_2_8_16 = tk.Label(window_from_10_to_2_8_16, text="Введите положительное число, которые необходимо перевести", font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_from_10_to_2_8_16 = tk.Entry(frame_from_10_to_2_8_16, width=10, font=("Bookman Old Style", 15))
    btn_convert_from_10_to_2_8_16 = tk.Button(frame_from_10_to_2_8_16,width=5, text="=", command=from_10_to_2_8_16_logic, font=("Bookman Old Style", 10), bg='#42313A', fg="white")
    lbl_result_from_10_to_2_8_16 = tk.Label(frame_from_10_to_2_8_16, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')

    # закрепление элементов окна
    label_from_10_to_2_8_16.grid(column=0, row=0)
    frame_from_10_to_2_8_16.grid(column=0, row=1)
    ent_number_from_10_to_2_8_16.grid(column=0, row=1)
    btn_convert_from_10_to_2_8_16.grid(column=1, row=1)
    lbl_result_from_10_to_2_8_16.grid(column=2, row=1)


def multiplication_dividing():
    """
    окно умножения двух чисел в двоичной системе
    :return:
    """
    def multiplication():
        """
        функция умножения двух чисел и вывод их
        :return:
        """
        number_deviding_1 = float(ent_number_multiplication_dividing.get())
        number_deviding_2 = float(ent_number_multiplication_dividing_2.get())
        number_result = decimalToBinary(number_deviding_1 * number_deviding_2)
        after_comm = max(numAfterComm(number_deviding_1, number_result), numAfterComm(number_deviding_2, number_result))
        lbl_result_multiplication_dividing["text"] = number_result[:(after_comm)]

    def dividing():
        """
        функция деления двух чисел и вывод их
        :return:
        """
        number_deviding_1 = float(ent_number_multiplication_dividing_second.get())
        number_deviding_2 = float(ent_number_multiplication_dividing_second_2.get())
        number_result = decimalToBinary(number_deviding_1 / number_deviding_2)
        after_comm = max(numAfterComm(number_deviding_1, number_result), numAfterComm(number_deviding_2, number_result))
        lbl_result_multiplication_dividing_second["text"] = number_result[:(after_comm)]

    # создание нового окна и его основных элементов
    window_multiplication_dividing = tk.Tk()
    window_multiplication_dividing.title("Перевод из 10 в 2-8-16")
    window_multiplication_dividing.configure(bg='#F1DCC9')
    frame_multiplication_dividing = tk.Frame(window_multiplication_dividing, bg='#F1DCC9')
    label_multiplication_dividing = tk.Label(window_multiplication_dividing,
                                       text="Введите числа в 10м формате, которые необходимо умножить/поделить", font=("Bookman Old Style", 15), bg='#F1DCC9')

    ent_number_multiplication_dividing = tk.Entry(frame_multiplication_dividing, width=10, font=("Bookman Old Style", 15))
    ent_number_multiplication_dividing_2 = tk.Entry(frame_multiplication_dividing, width=10, font=("Bookman Old Style", 15))
    btn_convert_multiplication_dividing = tk.Button(frame_multiplication_dividing,text="=", command=multiplication, width=5, font=("Bookman Old Style", 10), bg='#42313A', fg="white")
    lbl_sign_multiplication_dividing = tk.Label(frame_multiplication_dividing, text="*", font=("Bookman Old Style", 15),  bg='#F1DCC9' )
    lbl_result_multiplication_dividing = tk.Label(frame_multiplication_dividing, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')

    ent_number_multiplication_dividing_second = tk.Entry(frame_multiplication_dividing, width=10, font=("Bookman Old Style", 15))
    ent_number_multiplication_dividing_second_2 = tk.Entry(frame_multiplication_dividing, width=10, font=("Bookman Old Style", 15))
    btn_convert_multiplication_dividing_second = tk.Button(frame_multiplication_dividing,text="=", command=dividing, width=5, font=("Bookman Old Style", 10), bg='#42313A', fg="white" )
    lbl_sign_multiplication_dividing_second = tk.Label(frame_multiplication_dividing, text="/", font=("Bookman Old Style", 15),  bg='#F1DCC9' )
    lbl_result_multiplication_dividing_second = tk.Label(frame_multiplication_dividing, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')

    # закрепление элементов окна
    label_multiplication_dividing.grid(column=0, row=0)
    frame_multiplication_dividing.grid(column=0, row=1)
    ent_number_multiplication_dividing.grid(column=0, row=1)
    lbl_sign_multiplication_dividing.grid(column=1,row=1)
    ent_number_multiplication_dividing_2.grid(column=2, row=1)
    btn_convert_multiplication_dividing.grid(column=3, row=1)
    lbl_result_multiplication_dividing.grid(column=4, row=1)
    ent_number_multiplication_dividing_second.grid(column=0, row=2)
    lbl_sign_multiplication_dividing_second.grid(column=1, row=2)
    ent_number_multiplication_dividing_second_2.grid(column=2, row=2)
    btn_convert_multiplication_dividing_second.grid(column=3, row=2)
    lbl_result_multiplication_dividing_second.grid(column=4, row=2)


def from_16_to_10():
    """
    окно перевода из 16 в 2 и работа с дополнительным кодом
    :return:
    """

    #словарь перевода из 16 с/с в 2 с/с
    dict_of_16 = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
    }

    def convert_from_10_to_16():
        """
        функция перевода числа из 16 системы в 2 и перевод из дополнительного в прямой код и вывод его
        :return:
        """

        number_from_10_to_16 = ent_number_from_10_to_16.get()
        number_from_10_to_16_new = "".join(dict_of_16[letter] for letter in number_from_10_to_16)
        lbl_result_from_10_to_16["text"] = number_from_10_to_16_new
        if number_from_10_to_16_new[0] == "0":
            lbl_result_from_10_to_16_dop["text"] = number_from_10_to_16_new
        if number_from_10_to_16_new[0] == "1":
            number_from_10_to_16_new = int(number_from_10_to_16_new, 2) - 1
            number_from_10_to_16_new = str(decimalToBinary(number_from_10_to_16_new))
            number_from_10_to_16_new = number_from_10_to_16_new.replace("0", "2")
            number_from_10_to_16_new = number_from_10_to_16_new.replace("1", "0")
            number_from_10_to_16_new = number_from_10_to_16_new.replace("2", "1")
            number_from_10_to_16_new = number_from_10_to_16_new.replace("0", "1", 1)
            lbl_result_from_10_to_16_dop["text"] = number_from_10_to_16_new[:(len(number_from_10_to_16_new)-2)]

    # создание нового окна и его основных элементов
    window_from_10_to_16 = tk.Tk()
    window_from_10_to_16.title("Перевод из 10 в 2-8-16")
    window_from_10_to_16.configure(bg='#F1DCC9')
    frame_from_10_to_16 = tk.Frame(window_from_10_to_16, bg='#F1DCC9')
    label_from_10_to_16 = tk.Label(window_from_10_to_16,
                                       text="Введите 16ричное число, которые необходимо перевести", font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_from_10_to_16 = tk.Entry(frame_from_10_to_16, width=10, font=("Bookman Old Style", 15))
    btn_convert_from_10_to_16 = tk.Button(frame_from_10_to_16, width=5, text="=",
                                              command=convert_from_10_to_16, font=("Bookman Old Style", 10), bg='#42313A', fg="white")
    lbl_result_from_10_to_16 = tk.Label(frame_from_10_to_16, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')

    lbl_type_dop = tk.Label(frame_from_10_to_16, text="если было в дополнительном коде:", font=("Bookman Old Style", 15),  bg='#F1DCC9')
    lbl_result_from_10_to_16_dop = tk.Label(frame_from_10_to_16, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')

    # закрепление элементов окна
    label_from_10_to_16.grid(column=0, row=0)
    frame_from_10_to_16.grid(column=0, row=1)
    ent_number_from_10_to_16.grid(column=0, row=1)
    btn_convert_from_10_to_16.grid(column=1, row=1)
    lbl_result_from_10_to_16.grid(column=2, row=1)
    lbl_type_dop.grid(column=0, row=2)
    lbl_result_from_10_to_16_dop.grid(column=2,row=2)


def types_of_code_3():
    """
    окно перевода числа из 10 в 2 в прямой, обратный и дополнительный код
    :return:
    """

    def convert_types_of_code_3():
        """
        функция логики перевода числа из 10 в 2 в прямой, обратный и дополнительный коды и вывод его
        :return:
        """

        number_types_of_code_3_real = [0]*16
        number_types_of_code_3_invert = [0]*16
        number_types_of_code_3_dop = [0]*16
        number_types_of_code_3 = ent_number_types_of_code_3.get()
        number_types_of_code_3_bin = str(decimalToBinary(int(number_types_of_code_3)))[:len(str(decimalToBinary(int(number_types_of_code_3))))-2]
        if int(number_types_of_code_3) < 0:
            number_types_of_code_3_real[0] = 1
            number_types_of_code_3_invert[0] = 1
            number_types_of_code_3_dop[0] = 1
            number_types_of_code_3_bin = number_types_of_code_3_bin[1:]

        q = 0
        for i in range((len(number_types_of_code_3_real)-len(number_types_of_code_3_bin)), len(number_types_of_code_3_real)):
            number_types_of_code_3_real[i] = int(number_types_of_code_3_bin[q])
            q = q+1
        if int(number_types_of_code_3) < 0:
            q = 0
            for i in range((len(number_types_of_code_3_invert) - len(number_types_of_code_3_bin)),len(number_types_of_code_3_invert)):
                number_types_of_code_3_invert[i] = int(number_types_of_code_3_bin[q])
                q = q + 1
            for i in range(1, len(number_types_of_code_3_invert)):
                if number_types_of_code_3_invert[i] == 0:
                    number_types_of_code_3_invert[i] = 2
            for i in range(1, len(number_types_of_code_3_invert)):
                if number_types_of_code_3_invert[i] == 1:
                    number_types_of_code_3_invert[i] = 0
            for i in range(1, len(number_types_of_code_3_invert)):
                if number_types_of_code_3_invert[i] == 2:
                    number_types_of_code_3_invert[i] = 1


            number_types_of_code_3_dop = [i for i in number_types_of_code_3_invert]

            for i in range(len(number_types_of_code_3_dop)-1, 1, -1):
                if number_types_of_code_3_dop[i] == 0:
                    number_types_of_code_3_dop[i] = 1
                    for j in range(i+1, len(number_types_of_code_3_dop)):
                        number_types_of_code_3_dop[j] = 0
                    break

            lbl_result_types_of_code_3_real["text"] = number_types_of_code_3_real
            lbl_result_types_of_code_3_invert["text"] = number_types_of_code_3_invert
            lbl_result_types_of_code_3_dop["text"] = number_types_of_code_3_dop
        else:
            lbl_result_types_of_code_3_real["text"] = number_types_of_code_3_real
            lbl_result_types_of_code_3_invert["text"] = number_types_of_code_3_real
            lbl_result_types_of_code_3_dop["text"] = number_types_of_code_3_real



    # создание нового окна и его основных элементов
    window_types_of_code_3 = tk.Tk()
    window_types_of_code_3.title("Перевод из 10 в прямой, обратный и дополнительный код")
    window_types_of_code_3.configure(bg='#F1DCC9')
    frame_types_of_code_3 = tk.Frame(window_types_of_code_3, bg='#F1DCC9')
    label_types_of_code_3 = tk.Label(window_types_of_code_3,
                                   text="Введите число, которые необходимо перевести в 3 вида кода", font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_types_of_code_3 = tk.Entry(frame_types_of_code_3, width=10, font=("Bookman Old Style", 15))
    btn_convert_types_of_code_3 = tk.Button(frame_types_of_code_3, width=5, text="=",
                                          command=convert_types_of_code_3, font=("Bookman Old Style", 10), bg='#42313A', fg="white")

    lbl_types_of_code_3_real = tk.Label(frame_types_of_code_3, text="Прямой:", font=("Bookman Old Style", 15),  bg='#F1DCC9')
    lbl_types_of_code_3_invert = tk.Label(frame_types_of_code_3, text="Обратный:", font=("Bookman Old Style", 15),  bg='#F1DCC9')
    lbl_types_of_code_3_dop = tk.Label(frame_types_of_code_3, text="Дополнительный:", font=("Bookman Old Style", 15),  bg='#F1DCC9')

    lbl_result_types_of_code_3_real= tk.Label(frame_types_of_code_3, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_result_types_of_code_3_invert = tk.Label(frame_types_of_code_3, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_result_types_of_code_3_dop = tk.Label(frame_types_of_code_3, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')

    # закрепление элементов окна
    label_types_of_code_3.grid(column=0, row=0)
    frame_types_of_code_3.grid(column=0, row=1)
    ent_number_types_of_code_3.grid(column=0, row=1)
    btn_convert_types_of_code_3.grid(column=1, row=1)
    lbl_types_of_code_3_real.grid(column=0, row=3)
    lbl_types_of_code_3_invert.grid(column=0, row=4)
    lbl_types_of_code_3_dop.grid(column=0, row=5)
    lbl_result_types_of_code_3_real.grid(column=1, row=3)
    lbl_result_types_of_code_3_invert.grid(column=1, row=4)
    lbl_result_types_of_code_3_dop.grid(column=1, row=5)


def IEEE_754():
    """
    окно перевода числа из 10 чистемы в 2 в формате IEEE_754
    :return:
    """

    def convert_IEEE_754():
        """
        функция логики перевода числа из 10 чистемы в 2 в формате IEEE_754 и вывод его
        :return:
        """

        number_IEEE_754 = float(ent_number_IEEE_754.get())
        number_IEEE_754_new = decimalToBinary(float(number_IEEE_754))
        if int(number_IEEE_754) < 0:
            number_IEEE_754_sign = 1
            number_IEEE_754_new = number_IEEE_754_new[1:]
        else:
            number_IEEE_754_sign = 0


        if number_IEEE_754 >= 1 or number_IEEE_754 <=-1 :
            number_IEEE_754_exp = decimalToBinary(str(number_IEEE_754_new).find(".")-1+127)
            number_IEEE_754_mantis = number_IEEE_754_new[1:]
        if number_IEEE_754 < 1 and number_IEEE_754 > -1:
            number_IEEE_754_exp = decimalToBinary(-str(number_IEEE_754_new).find("1") + 128)
            number_IEEE_754_mantis = number_IEEE_754_new[str(number_IEEE_754_new).find("1")+1:]
        lbl_result_IEEE_754_sign["text"] = number_IEEE_754_sign
        lbl_result_IEEE_754_exp["text"] =("0"*(10 - len(number_IEEE_754_exp)) + str(number_IEEE_754_exp))[:8]
        number_IEEE_754_mantis = number_IEEE_754_mantis.replace(".","" )
        lbl_result_IEEE_754_mantis["text"] = (number_IEEE_754_mantis+"0000000000000000000000")[:23]



    # создание нового окна и его основных элементов
    window_IEEE_754 = tk.Tk()
    window_IEEE_754.title("Перевод из 10 в в IEEE_754")
    window_IEEE_754.configure(bg='#F1DCC9')
    frame_IEEE_754 = tk.Frame(window_IEEE_754, bg='#F1DCC9')
    label_IEEE_754 = tk.Label(window_IEEE_754,
                                     text="Введите число, которые необходимо перевести в IEEE_754", font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_IEEE_754 = tk.Entry(frame_IEEE_754, width=10, font=("Bookman Old Style", 15))
    btn_convert_IEEE_754 = tk.Button(frame_IEEE_754, width=5, text="=",
                                       command=convert_IEEE_754, font=("Bookman Old Style", 10), bg='#42313A', fg="white")

    lbl_IEEE_754_sign = tk.Label(frame_IEEE_754, text="Знак:", font=("Bookman Old Style", 15),  bg='#F1DCC9')
    lbl_IEEE_754_exp = tk.Label(frame_IEEE_754, text="Экспонента:", font=("Bookman Old Style", 15),  bg='#F1DCC9')
    lbl_IEEE_754_mantis = tk.Label(frame_IEEE_754, text="Мантисса:", font=("Bookman Old Style", 15),  bg='#F1DCC9')

    lbl_result_IEEE_754_sign = tk.Label(frame_IEEE_754, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_result_IEEE_754_exp = tk.Label(frame_IEEE_754, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_result_IEEE_754_mantis = tk.Label(frame_IEEE_754, font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')

    # закрепление элементов окна
    label_IEEE_754.grid(column=0, row=0)
    frame_IEEE_754.grid(column=0, row=1)
    ent_number_IEEE_754.grid(column=0, row=1)
    btn_convert_IEEE_754.grid(column=1, row=1)
    lbl_IEEE_754_sign.grid(column=0, row=3)
    lbl_IEEE_754_exp.grid(column=0, row=4)
    lbl_IEEE_754_mantis.grid(column=0, row=5)
    lbl_result_IEEE_754_sign.grid(column=1, row=3)
    lbl_result_IEEE_754_exp.grid(column=1, row=4)
    lbl_result_IEEE_754_mantis.grid(column=1, row=5)


table_truth = pd.DataFrame(
        [
        [0,0,0,0,0],
        [0,0,0,1,0],
        [0,0,1,0,0],
        [0,0,1,1,0],
        [0,1,0,0,0],
        [0,1,0,1,0],
        [0,1,1,0,0],
        [0,1,1,1,0],
        [1,0,0,0,0],
        [1,0,0,1,0],
        [1,0,1,0,0],
        [1,0,1,1,0],
        [1,1,0,0,0],
        [1,1,0,1,0],
        [1,1,1,0,0],
        [1,1,1,1,0]
        ],
        columns=["A", "B", "C", "D", 'F']
    )





def print_table_by_vector():
    """
    окно создания таблицы истинности по вектору функции
    :return:
    """
    #макет таблицы истинности для СДНФ
    table_sknf = table_truth


    def print_table_by_vector_logic():
        """
        функция обработки вектора логической функции, построения таблицы истинности и вывода
        :return:
        """

        number_table_by_vector = ent_number_table_by_vector.get()
        if len(number_table_by_vector) != 16:
            lbl_result_table_by_vector["text"] = "Пожалуйста введите ровно 16 символов"
        if len(number_table_by_vector) == 16:
            for i in range(16):
                table_sknf.loc[i]["F"] = int(number_table_by_vector[i])
            lbl_result_table_by_vector["text"] = table_sknf

    # создание нового окна и его основных элементов
    window_table_by_vector = tk.Tk()
    window_table_by_vector.title("Построение СДНФ")
    window_table_by_vector.configure(bg='#F1DCC9')
    frame_table_by_vector = tk.Frame(window_table_by_vector, bg='#F1DCC9')
    label_table_by_vector = tk.Label(window_table_by_vector,
                                text="Введите 16 цифр, соответствующих функции(вектор функции)",
                                font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_table_by_vector = tk.Entry(frame_table_by_vector, width=20, font=("Bookman Old Style", 15))
    btn_table_by_vector = tk.Button(frame_table_by_vector, width=5, text="=",
                               command=print_table_by_vector_logic, font=("Bookman Old Style", 10), bg='#42313A', fg="white")
    lbl_result_table_by_vector = tk.Label(frame_table_by_vector, font=("Bookman Old Style", 15), width=40, bg='#F1DCC9')

    # закрепление элементов окна
    label_table_by_vector.grid(column=0, row=0)
    frame_table_by_vector.grid(column=0, row=1)
    ent_number_table_by_vector.grid(column=0, row=1)
    btn_table_by_vector.grid(column=1, row=1)
    lbl_result_table_by_vector.grid(column=0, row=2)






def print_sdnf():
    """
    окно создания таблицы истинности и скнф по вектору функции
    :return:
    """
    #макет таблицы истинности для СДНФ
    table_sdnf = table_truth


    def print_sdnf_logic():
        """
        функция обработки вектора логической функции, построения таблицы истинности и СДНФ и их вывода
        :return:
        """

        number_print_sdnf = ent_number_print_sdnf.get()
        number_print_sdnf_func = []
        if len(number_print_sdnf) != 16:
            lbl_result_print_sdnf_table["text"] = "Пожалуйста введите ровно 16 символов"
        if len(number_print_sdnf) == 16:
            for i in range(16):
                table_sdnf.loc[i]["F"] = int(number_print_sdnf[i])
            lbl_result_print_sdnf_table["text"] = table_sdnf
            number_print_sdnf_only1 = (table_sdnf.loc[table_sdnf["F"] == 1])
            for i in range(len(number_print_sdnf_only1)):
                number_print_sdnf_func.append("*(")
                if number_print_sdnf_only1.iloc[i]["A"] == 0:
                    number_print_sdnf_func.append("!A")
                else:
                    number_print_sdnf_func.append("A")
                if number_print_sdnf_only1.iloc[i]["B"] == 0:
                    number_print_sdnf_func.append("+!B")
                else:
                    number_print_sdnf_func.append("+B")
                if number_print_sdnf_only1.iloc[i]["C"] == 0:
                    number_print_sdnf_func.append("+!C")
                else:
                    number_print_sdnf_func.append("+C")
                if number_print_sdnf_only1.iloc[i]["D"] == 0:
                    number_print_sdnf_func.append("+!D")
                else:
                    number_print_sdnf_func.append("+D")
                number_print_sdnf_func.append(")")
            lbl_result_print_sdnf_func["text"] = ("".join(number_print_sdnf_func))[1:]

    # создание нового окна и его основных элементов
    window_print_sdnf = tk.Tk()
    window_print_sdnf.title("Построение СДНФ")
    window_print_sdnf.configure(bg='#F1DCC9')
    frame_print_sdnf = tk.Frame(window_print_sdnf, bg='#F1DCC9')
    label_print_sdnf = tk.Label(window_print_sdnf,
                              text="Введите 16 цифр, соответствующих функции(вектор функции)", font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_print_sdnf = tk.Entry(frame_print_sdnf, width=20, font=("Bookman Old Style", 15))
    btn_print_sdnf = tk.Button(frame_print_sdnf, width=5, text="=",
                                     command=print_sdnf_logic, font=("Bookman Old Style", 10), bg='#42313A', fg="white")
    lbl_result_print_sdnf_table = tk.Label(frame_print_sdnf, font=("Bookman Old Style", 15), width=40, bg='#F1DCC9')
    lbl_result_print_sdnf_func = tk.Label(frame_print_sdnf, font=("Bookman Old Style", 15), bg='#F1DCC9')

    # закрепление элементов окна
    label_print_sdnf.grid(column=0, row=0)
    frame_print_sdnf.grid(column=0, row=1)
    ent_number_print_sdnf.grid(column=0, row=1)
    btn_print_sdnf.grid(column=1, row=1)
    lbl_result_print_sdnf_table.grid(column=0, row=2)
    lbl_result_print_sdnf_func.grid(column=1, row=2)



def print_sknf():
    """
    окно создания таблицы истинности и скнф по вектору функции
    :return:
    """

    #макет таблицы истинности для СДНФ
    table_sknf = table_truth

    def print_sknf_logic():
        """
        функция обработки вектора логической функции, построения таблицы истинности и СДНФ и их вывода
        :return:
        """

        number_print_sknf = ent_number_print_sknf.get()
        number_print_sknf_func = []
        if len(number_print_sknf) != 16:
            lbl_result_print_sknf_table["text"] = "Пожалуйста введите ровно 16 символов"
        if len(number_print_sknf) == 16:
            for i in range(16):
                table_sknf.loc[i]["F"] = int(number_print_sknf[i])
            lbl_result_print_sknf_table["text"] = table_sknf
            number_print_sknf_only0 = (table_sknf.loc[table_sknf["F"] == 0])
            for i in range(len(number_print_sknf_only0)):
                number_print_sknf_func.append("+(")
                if number_print_sknf_only0.iloc[i]["A"] == 1:
                    number_print_sknf_func.append("!A")
                else:
                    number_print_sknf_func.append("A")
                if number_print_sknf_only0.iloc[i]["B"] == 1:
                    number_print_sknf_func.append("*!B")
                else:
                    number_print_sknf_func.append("+B")
                if number_print_sknf_only0.iloc[i]["C"] == 1:
                    number_print_sknf_func.append("*!C")
                else:
                    number_print_sknf_func.append("*C")
                if number_print_sknf_only0.iloc[i]["D"] == 1:
                    number_print_sknf_func.append("*!D")
                else:
                    number_print_sknf_func.append("*D")
                number_print_sknf_func.append(")")
            lbl_result_print_sknf_func["text"] = ("".join(number_print_sknf_func))[1:]

    # создание нового окна и его основных элементов
    window_print_sknf = tk.Tk()
    window_print_sknf.title("Построение СКНФ")
    window_print_sknf.configure(bg='#F1DCC9')
    frame_print_sknf = tk.Frame(window_print_sknf, bg='#F1DCC9')
    label_print_sknf = tk.Label(window_print_sknf,
                              text="Введите 16 цифр, соответствующих функции(вектор функции)", font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_print_sknf = tk.Entry(frame_print_sknf, width=20, font=("Bookman Old Style", 15))
    btn_print_sknf = tk.Button(frame_print_sknf, width=5, text="=",
                                     command=print_sknf_logic, font=("Bookman Old Style", 10), bg='#42313A', fg="white")
    lbl_result_print_sknf_table = tk.Label(frame_print_sknf, font=("Bookman Old Style", 15), width=40, bg='#F1DCC9')
    lbl_result_print_sknf_func = tk.Label(frame_print_sknf, font=("Bookman Old Style", 15), bg='#F1DCC9')

    # закрепление элементов окна
    label_print_sknf.grid(column=0, row=0)
    frame_print_sknf.grid(column=0, row=1)
    ent_number_print_sknf.grid(column=0, row=1)
    btn_print_sknf.grid(column=1, row=1)
    lbl_result_print_sknf_table.grid(column=0, row=2)
    lbl_result_print_sknf_func.grid(column=1, row=2)

def combinations():
    """
    окно подсчета сочетании(сколькими способами можно выбрать K из N)
    :return:
    """

    def combinations_logic():
        """
        функция подсчета сочетании и вывод
        :return:
        """

        number_combinations_N = int(ent_number_combinations_N.get())
        number_combinations_K = int(ent_number_combinations_K.get())
        number_combinations_result = factorial(number_combinations_N) /(factorial(number_combinations_N-
                                                number_combinations_K)*factorial(number_combinations_K))
        lbl_result_combinations["text"] = number_combinations_result

    # создание нового окна и его основных элементов
    window_combinations = tk.Tk()
    window_combinations.title("Сочетания")
    window_combinations.configure(bg='#F1DCC9')
    frame_combinations = tk.Frame(window_combinations, bg='#F1DCC9')
    label_combinations = tk.Label(window_combinations,
                                       text="Введите два числа: количество всех вариантов и сколько нужно выбрать",
                                       font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_combinations_N = tk.Entry(frame_combinations, width=10, font=("Bookman Old Style", 15))
    ent_number_combinations_K = tk.Entry(frame_combinations, width=10, font=("Bookman Old Style", 15))
    btn_convert_combinations = tk.Button(frame_combinations, width=5, text="=",
                                              command=combinations_logic, font=("Bookman Old Style", 10), bg='#42313A', fg="white")
    lbl_combinations_N = tk.Label(frame_combinations,text="Все варианты (N)", font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_combinations_K = tk.Label(frame_combinations,text="Сколько выбрать(K)", font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_result_combinations = tk.Label(frame_combinations, font=("Bookman Old Style", 15), width=30,
                                            bg='#F1DCC9')

    # закрепление элементов окна
    label_combinations.grid(column=0, row=0)
    frame_combinations.grid(column=0, row=1)
    lbl_combinations_N.grid(column=0, row=1)
    lbl_combinations_K.grid(column=0, row=2)
    ent_number_combinations_N.grid(column=1, row=1)
    ent_number_combinations_K.grid(column=1, row=2)
    btn_convert_combinations.grid(column=2, row=1)
    lbl_result_combinations.grid(column=2, row=2)



def num_passwords():
    """
    окно подсчета количества различных паролей, при заданном количестве букв и цифр в пароле
    :return:
    """

    def num_passwords_logic():
        """
        функция подсчета количества различных паролей, при заданном количестве букв и цифр в пароле
        :return:
        """

        N = int(ent_number_num_passwords_N.get())
        M = int(ent_number_num_passwords_M.get())
        K = int(ent_number_num_passwords_K.get())
        number_num_passwords_result = (((K*2)**N * (10**M)) - (K*(2**N))) * (factorial(N+M)/(factorial(N)*factorial(M)))
        lbl_result_num_passwords["text"] = number_num_passwords_result

    # создание нового окна и его основных элементов
    window_num_passwords = tk.Tk()
    window_num_passwords.title("Сочетания")
    window_num_passwords.configure(bg='#F1DCC9')
    frame_num_passwords = tk.Frame(window_num_passwords, bg='#F1DCC9')
    label_num_passwords = tk.Label(window_num_passwords,
                                       text="Введите три числа: количество букв в пароле,\n количество цифр в пароле и мощность алфавита",
                                       font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_num_passwords_N = tk.Entry(frame_num_passwords, width=10, font=("Bookman Old Style", 15))
    ent_number_num_passwords_M = tk.Entry(frame_num_passwords, width=10, font=("Bookman Old Style", 15))
    ent_number_num_passwords_K = tk.Entry(frame_num_passwords, width=10, font=("Bookman Old Style", 15))
    btn_convert_num_passwords = tk.Button(frame_num_passwords, width=5, text="=",
                                              command=num_passwords_logic, font=("Bookman Old Style", 10), bg='#42313A', fg="white")
    lbl_num_passwords_N = tk.Label(frame_num_passwords,text="Количество букв (N)", font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_num_passwords_M = tk.Label(frame_num_passwords,text="Количество цифр (M)", font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_num_passwords_K = tk.Label(frame_num_passwords,text="Количество букв в алфавите (K)", font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_result_num_passwords = tk.Label(frame_num_passwords, font=("Bookman Old Style", 15), width=30,
                                            bg='#F1DCC9')

    # закрепление элементов окна
    label_num_passwords.grid(column=0, row=0)
    frame_num_passwords.grid(column=0, row=1)
    lbl_num_passwords_N.grid(column=0, row=1)
    lbl_num_passwords_M.grid(column=0, row=2)
    lbl_num_passwords_K.grid(column=0, row=3)
    ent_number_num_passwords_N.grid(column=1, row=1)
    ent_number_num_passwords_M.grid(column=1, row=2)
    ent_number_num_passwords_K.grid(column=1, row=3)
    btn_convert_num_passwords.grid(column=2, row=1)
    lbl_result_num_passwords.grid(column=2, row=2)





def possibilities():
    """
    окно подсчета трех видов вероятностей: "хотя бы один", "только два", "не менее двух"
    :return:
    """

    def possibilities_logic():
        """
        функция подсчета трех видов вероятностей: "хотя бы один", "только два", "не менее двух"
        :return:
        """

        P1 = float(ent_number_possibilities_P1.get())
        P2 = float(ent_number_possibilities_P2.get())
        P3 = float(ent_number_possibilities_P3.get())
        number_possibilities_result_1 = 1 - ((1-P1) * (1-P2) * (1-P3))
        number_possibilities_result_2 = (P1 * P2 * (1-P3)) + (P1 * (1-P2) * P3) + ((1-P1) * P2 * P3)
        number_possibilities_result_3 = number_possibilities_result_2 + (P1 * P2 * P3)
        lbl_result_possibilities_1["text"] = round(number_possibilities_result_1, 5)
        lbl_result_possibilities_2["text"] = round(number_possibilities_result_2, 5)
        lbl_result_possibilities_3["text"] = round(number_possibilities_result_3, 5)

    # создание нового окна и его основных элементов
    window_possibilities = tk.Tk()
    window_possibilities.title("Вероятности")
    window_possibilities.configure(bg='#F1DCC9')
    frame_possibilities = tk.Frame(window_possibilities, bg='#F1DCC9')
    label_possibilities = tk.Label(window_possibilities,
                                       text="Введите три числа: вероятности первого, второго\n и третьего событии",
                                       font=("Bookman Old Style", 15), bg='#F1DCC9')
    ent_number_possibilities_P1 = tk.Entry(frame_possibilities, width=10, font=("Bookman Old Style", 15))
    ent_number_possibilities_P2 = tk.Entry(frame_possibilities, width=10, font=("Bookman Old Style", 15))
    ent_number_possibilities_P3 = tk.Entry(frame_possibilities, width=10, font=("Bookman Old Style", 15))
    btn_convert_possibilities = tk.Button(frame_possibilities, width=5, text="=",
                                              command=possibilities_logic, font=("Bookman Old Style", 10), bg='#42313A', fg="white")
    lbl_possibilities_P1 = tk.Label(frame_possibilities,text="Вероятность первого события (P1)", font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_possibilities_P2 = tk.Label(frame_possibilities,text="Вероятность второго события (P2)", font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_possibilities_P3 = tk.Label(frame_possibilities,text="Вероятность третьего события (P3)", font=("Bookman Old Style", 15), width=30, bg='#F1DCC9')
    lbl_result_possibilities_1_name = tk.Label(frame_possibilities, font=("Bookman Old Style", 15), width=15,
                                            bg='#F1DCC9', text="хотя бы одно:")
    lbl_result_possibilities_2_name = tk.Label(frame_possibilities, font=("Bookman Old Style", 15), width=15,
                                            bg='#F1DCC9', text="только два:")
    lbl_result_possibilities_3_name = tk.Label(frame_possibilities, font=("Bookman Old Style", 15), width=15,
                                            bg='#F1DCC9', text="не менее двух:")
    lbl_result_possibilities_1 = tk.Label(frame_possibilities, font=("Bookman Old Style", 15), width=15,
                                               bg='#F1DCC9')
    lbl_result_possibilities_2 = tk.Label(frame_possibilities, font=("Bookman Old Style", 15), width=15,
                                               bg='#F1DCC9')
    lbl_result_possibilities_3 = tk.Label(frame_possibilities, font=("Bookman Old Style", 15), width=15,
                                               bg='#F1DCC9')

    # закрепление элементов окна
    label_possibilities.grid(column=0, row=0)
    frame_possibilities.grid(column=0, row=1)
    lbl_possibilities_P1.grid(column=0, row=1)
    lbl_possibilities_P2.grid(column=0, row=2)
    lbl_possibilities_P3.grid(column=0, row=3)
    ent_number_possibilities_P1.grid(column=1, row=1)
    ent_number_possibilities_P2.grid(column=1, row=2)
    ent_number_possibilities_P3.grid(column=1, row=3)
    btn_convert_possibilities.grid(column=2, row=2)
    lbl_result_possibilities_1_name.grid(column=3, row=1)
    lbl_result_possibilities_2_name.grid(column=3, row=2)
    lbl_result_possibilities_3_name.grid(column=3, row=3)
    lbl_result_possibilities_1.grid(column=4, row=1)
    lbl_result_possibilities_2.grid(column=4, row=2)
    lbl_result_possibilities_3.grid(column=4, row=3)