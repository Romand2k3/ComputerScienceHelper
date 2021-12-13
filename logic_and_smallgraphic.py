import math
import tkinter as tk
from math import copysign, fabs, floor, isfinite, modf




def from_10_to_2_8_16():
    """
    окно перевода из 10 системы в 2-8-16
    :return:
    """

    def decimalToBinary(f):
        """
        не мой код, использовал интернет
        :param value:
        :return:
        """
        if not isfinite(f):
            return repr(f)  # inf nan

        sign = '-' * (copysign(1.0, f) < 0)
        frac, fint = modf(fabs(f))  # split on fractional, integer parts
        n, d = frac.as_integer_ratio()  # frac = numerator / denominator
        assert d & (d - 1) == 0  # power of two
        return f'{sign}{floor(fint):b}.{n:0{d.bit_length() - 1}b}'

    def from_10_to_2_8_16_logic():
        """
        функция логики самого перевода из 10 системы в 2-8-16
        :return:
        """
        number_from_10_to_2_8_16 = float(ent_number_from_10_to_2_8_16.get())
        s = str(number_from_10_to_2_8_16)
        after_comm = abs(s.find('.') - len(s)) - 1
        after_comm_new = math.ceil(after_comm*math.log(10,2))
        number_from_10_to_2_8_16_new = decimalToBinary(number_from_10_to_2_8_16)
        len_before_comm = abs(str(number_from_10_to_2_8_16_new).find('.'))+1
        print(len_before_comm, after_comm_new)
        lbl_result_from_10_to_2_8_16["text"] = number_from_10_to_2_8_16_new[:(len_before_comm+after_comm_new)]


    window_from_10_to_2_8_16 = tk.Tk()
    window_from_10_to_2_8_16.title("Перевод из 10 в 2-8-16")
    frame_from_10_to_2_8_16 = tk.Frame(window_from_10_to_2_8_16)
    label_from_10_to_2_8_16 = tk.Label(window_from_10_to_2_8_16, text="Введите положительное число, которые необходимо перевести")
    ent_number_from_10_to_2_8_16 = tk.Entry(frame_from_10_to_2_8_16, width=10)
    btn_convert_from_10_to_2_8_16 = tk.Button(frame_from_10_to_2_8_16, command=from_10_to_2_8_16_logic)
    lbl_result_from_10_to_2_8_16 = tk.Label(frame_from_10_to_2_8_16)

    label_from_10_to_2_8_16.grid(column=0, row=0)
    frame_from_10_to_2_8_16.grid(column=0, row=1)
    ent_number_from_10_to_2_8_16.grid(column=0, row=1)
    btn_convert_from_10_to_2_8_16.grid(column=1, row=1)
    lbl_result_from_10_to_2_8_16.grid(column=2, row=1)


def multiplication_dividing():
    pass

def from_16_to_10():
    pass

def types_of_code_3():
    pass

def IEEE_754():
    pass
