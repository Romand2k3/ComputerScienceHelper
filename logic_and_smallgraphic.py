import math
import tkinter as tk
from math import copysign, fabs, floor, isfinite, modf


def decimalToBinary(value):
    """
    не мой код, использовал интернет
    :param value: число изначально
    :return: число после перевода
    """
    if not isfinite(value):
        return repr(value)  # inf nan

    sign = '-' * (copysign(1.0, value) < 0)
    frac, fint = modf(fabs(value))  # split on fractional, integer parts
    n, d = frac.as_integer_ratio()  # frac = numerator / denominator
    assert d & (d - 1) == 0  # power of two
    return f'{sign}{floor(fint):b}.{n:0{d.bit_length() - 1}b}'


def numAfterComm(number, number_new):
    """
    функция вычисления количества знаков после запятой после перевода
    :param number: изначальное число
    :param number_new: число после перевода
    :return: кол-во знаков после запятой
    """
    temp = str(number)
    after_comm = abs(temp.find('.') - len(temp)) - 1
    after_comm_new = math.ceil(after_comm * math.log(10, 2))
    len_before_comm = abs(str(number_new).find('.')) + 1
    return len_before_comm+after_comm_new


def from_10_to_2_8_16():
    """
    окно перевода из 10 системы в 2-8-16
    :return:
    """

    def from_10_to_2_8_16_logic():
        """
        функция логики самого перевода из 10 системы в 2-8-16
        :return:
        """
        number_from_10_to_2_8_16 = float(ent_number_from_10_to_2_8_16.get())
        number_from_10_to_2_8_16_new = decimalToBinary(number_from_10_to_2_8_16)
        after_comm = numAfterComm(number_from_10_to_2_8_16,number_from_10_to_2_8_16_new)
        lbl_result_from_10_to_2_8_16["text"] = number_from_10_to_2_8_16_new[:(after_comm)]


    window_from_10_to_2_8_16 = tk.Tk()
    window_from_10_to_2_8_16.title("Перевод из 10 в 2-8-16")
    frame_from_10_to_2_8_16 = tk.Frame(window_from_10_to_2_8_16)
    label_from_10_to_2_8_16 = tk.Label(window_from_10_to_2_8_16, text="Введите положительное число, которые необходимо перевести")
    ent_number_from_10_to_2_8_16 = tk.Entry(frame_from_10_to_2_8_16, width=10)
    btn_convert_from_10_to_2_8_16 = tk.Button(frame_from_10_to_2_8_16,width=5, text="=", command=from_10_to_2_8_16_logic)
    lbl_result_from_10_to_2_8_16 = tk.Label(frame_from_10_to_2_8_16)

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
        функция умножения двух чисел
        :return:
        """
        number_deviding_1 = float(ent_number_multiplication_dividing.get())
        number_deviding_2 = float(ent_number_multiplication_dividing_2.get())
        number_result = decimalToBinary(number_deviding_1 * number_deviding_2)
        after_comm = max(numAfterComm(number_deviding_1, number_result), numAfterComm(number_deviding_2, number_result))
        lbl_result_multiplication_dividing["text"] = number_result[:(after_comm)]

    def dividing():
        """
        функция деления двух чисел
        :return:
        """
        number_deviding_1 = float(ent_number_multiplication_dividing_second.get())
        number_deviding_2 = float(ent_number_multiplication_dividing_second_2.get())
        number_result = decimalToBinary(number_deviding_1 / number_deviding_2)
        after_comm = max(numAfterComm(number_deviding_1, number_result), numAfterComm(number_deviding_2, number_result))
        lbl_result_multiplication_dividing_second["text"] = number_result[:(after_comm)]



    window_multiplication_dividing = tk.Tk()
    window_multiplication_dividing.title("Перевод из 10 в 2-8-16")
    frame_multiplication_dividing = tk.Frame(window_multiplication_dividing)
    label_multiplication_dividing = tk.Label(window_multiplication_dividing,
                                       text="Введите числа в 10м формате, которые необходимо умножить/поделить")

    ent_number_multiplication_dividing = tk.Entry(frame_multiplication_dividing, width=10)
    ent_number_multiplication_dividing_2 = tk.Entry(frame_multiplication_dividing, width=10)
    btn_convert_multiplication_dividing = tk.Button(frame_multiplication_dividing,text="=", command=multiplication)
    lbl_sign_multiplication_dividing = tk.Label(frame_multiplication_dividing, text="*")
    lbl_result_multiplication_dividing = tk.Label(frame_multiplication_dividing)

    ent_number_multiplication_dividing_second = tk.Entry(frame_multiplication_dividing, width=10)
    ent_number_multiplication_dividing_second_2 = tk.Entry(frame_multiplication_dividing, width=10)
    btn_convert_multiplication_dividing_second = tk.Button(frame_multiplication_dividing,text="=", command=dividing)
    lbl_sign_multiplication_dividing_second = tk.Label(frame_multiplication_dividing, text="/")
    lbl_result_multiplication_dividing_second = tk.Label(frame_multiplication_dividing)

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
        функция перевода числа из 16 системы в 2 и перевод из дополнительного в прямой код
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


    window_from_10_to_16 = tk.Tk()
    window_from_10_to_16.title("Перевод из 10 в 2-8-16")
    frame_from_10_to_16 = tk.Frame(window_from_10_to_16)
    label_from_10_to_16 = tk.Label(window_from_10_to_16,
                                       text="Введите 16ричное число, которые необходимо перевести")
    ent_number_from_10_to_16 = tk.Entry(frame_from_10_to_16, width=10)
    btn_convert_from_10_to_16 = tk.Button(frame_from_10_to_16, width=5, text="=",
                                              command=convert_from_10_to_16)
    lbl_result_from_10_to_16 = tk.Label(frame_from_10_to_16)

    lbl_type_dop = tk.Label(frame_from_10_to_16, text="в дополнительном коде:")
    lbl_result_from_10_to_16_dop = tk.Label(frame_from_10_to_16)

    label_from_10_to_16.grid(column=0, row=0)
    frame_from_10_to_16.grid(column=0, row=1)
    ent_number_from_10_to_16.grid(column=0, row=1)
    btn_convert_from_10_to_16.grid(column=1, row=1)
    lbl_result_from_10_to_16.grid(column=2, row=1)
    lbl_type_dop.grid(column=0, row=2)
    lbl_result_from_10_to_16_dop.grid(column=2,row=2)


def types_of_code_3():
    """
    окно перевода чсила из 10 в 2 в прямой, обратный и дополнительный код
    :return:
    """
    def convert_types_of_code_3():
        """
        функция логики перевода числа из 10 в 2 в прямой, обратный и дополнительный коды
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




    window_types_of_code_3 = tk.Tk()
    window_types_of_code_3.title("Перевод из 10 в прямой, обратный и дополнительный код")
    frame_types_of_code_3 = tk.Frame(window_types_of_code_3)
    label_types_of_code_3 = tk.Label(window_types_of_code_3,
                                   text="Введите число, которые необходимо перевести в 3 вида кода")
    ent_number_types_of_code_3 = tk.Entry(frame_types_of_code_3, width=10)
    btn_convert_types_of_code_3 = tk.Button(frame_types_of_code_3, width=5, text="=",
                                          command=convert_types_of_code_3)

    lbl_types_of_code_3_real = tk.Label(frame_types_of_code_3, text="Прямой:")
    lbl_types_of_code_3_invert = tk.Label(frame_types_of_code_3, text="Обратный:")
    lbl_types_of_code_3_dop = tk.Label(frame_types_of_code_3, text="Дополнительный:")

    lbl_result_types_of_code_3_real= tk.Label(frame_types_of_code_3)
    lbl_result_types_of_code_3_invert = tk.Label(frame_types_of_code_3)
    lbl_result_types_of_code_3_dop = tk.Label(frame_types_of_code_3)

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

    :return:
    """
    def convert_IEEE_754():
        number_IEEE_754 = float(ent_number_IEEE_754.get())
        number_IEEE_754_new = decimalToBinary(float(number_IEEE_754))
        if int(number_IEEE_754) < 0:
            number_IEEE_754_sign = 1
        else:
            number_IEEE_754_sign = 0
        if number_IEEE_754 >= 1:
            number_IEEE_754_exp = decimalToBinary(str(number_IEEE_754_new).find(".")-1+127)
            number_IEEE_754_mantis = number_IEEE_754_new[1:]
        if number_IEEE_754 < 1:
            number_IEEE_754_exp = decimalToBinary(-str(number_IEEE_754_new).find("1") + 128)
            number_IEEE_754_mantis = number_IEEE_754_new[str(number_IEEE_754_new).find("1")+1:]
        lbl_result_IEEE_754_sign["text"] = number_IEEE_754_sign
        print(len(number_IEEE_754_exp))
        lbl_result_IEEE_754_exp["text"] =("0"*(10 - len(number_IEEE_754_exp)) + str(number_IEEE_754_exp))[:8]
        number_IEEE_754_mantis = number_IEEE_754_mantis.replace(".","" )
        lbl_result_IEEE_754_mantis["text"] = number_IEEE_754_mantis[:23]




    window_IEEE_754 = tk.Tk()
    window_IEEE_754.title("Перевод из 10 в в IEEE_754")
    frame_IEEE_754 = tk.Frame(window_IEEE_754)
    label_IEEE_754 = tk.Label(window_IEEE_754,
                                     text="Введите число, которые необходимо перевести в IEEE_754")
    ent_number_IEEE_754 = tk.Entry(frame_IEEE_754, width=10)
    btn_convert_IEEE_754 = tk.Button(frame_IEEE_754, width=5, text="=",
                                       command=convert_IEEE_754)

    lbl_IEEE_754_sign = tk.Label(frame_IEEE_754, text="Знак:")
    lbl_IEEE_754_exp = tk.Label(frame_IEEE_754, text="Экспонента:")
    lbl_IEEE_754_mantis = tk.Label(frame_IEEE_754, text="Мантисса:")

    lbl_result_IEEE_754_sign = tk.Label(frame_IEEE_754)
    lbl_result_IEEE_754_exp = tk.Label(frame_IEEE_754)
    lbl_result_IEEE_754_mantis = tk.Label(frame_IEEE_754)

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
