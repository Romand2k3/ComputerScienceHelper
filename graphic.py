from logic_and_smallgraphic import *


# словари с функциями и их названия для последующей генерации кнопок
Thm1_dict = {
    "Перевод из 10 с/с в 2 с/с": from_10_to_2_8_16,
    "Умножение и деление с \nрезультатом в 2 виде": multiplication_dividing,
    "Перевод из 16 с/с в 2 с/с": from_16_to_10,
    "Перевод из 10 с/с в 2 с/с \nв 3 видах кодирования": types_of_code_3,
    "Перевод из 10 с/с в 2 с/с \nв формате IEEE_754(32-битная)": IEEE_754,
}

Thm2_dict = {
    "Построить таблицу истинности": print_table_by_vector,
    "Построить СДНФ": print_sdnf,
    "Построить СКНФ": print_sknf
}

Thm3_dict = {
    "Сочетания(сколькими способами\n можно выбрать K из N)": combinations,
    "Количество различных паролей": num_passwords,
    "Вероятности": possibilities,
}



class HubFrame:
    """
    основной класс описывающий элементы
    """
    def __init__(self, parent):
        """
        создание всех элементов главного окна
        :param parent:
        """
        # конфигурация главного окна
        parent.title("CSH")
        parent.configure(bg='#F1DCC9')
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1, minsize=300)
        parent.rowconfigure(1, weight=1, minsize=300)
        parent.rowconfigure(2, weight=1, minsize=300)

        # верхняя рамка
        self.TopPanel = tk.Frame(parent, bg='#F1DCC9')
        self.TopPanel.grid(column=0, row=0)

        # средняя рамка
        self.MidllePanel = tk.Frame(parent, bg='#F1DCC9')
        self.MidllePanel.grid(column=0, row=1)

        # нижняя рамка
        self.BottomPanel = tk.Frame(parent, bg='#F1DCC9')
        self.BottomPanel.grid(column=0, row=2)

        # стартовые кнопки
        self.InfoBtn = tk.Button(self.BottomPanel)
        self.InfoBtn.grid(column=0, row=2)
        self.InfoBtn.configure(text="Информация", font=("Bookman Old Style", 25), bg='#6C2D2C', fg="white", relief=tk.RAISED)
        self.InfoBtn['command'] = self.showInfo

        self.Thm1Btn = tk.Button(self.MidllePanel)
        self.Thm1Btn.grid(column=0, row=1, padx=20)
        self.Thm1Btn.configure(text="Математические основы\nвычислительной техники", font=("Bookman Old Style", 15), bg='#42313A', fg="white", relief=tk.RAISED)
        self.Thm1Btn['command'] = self.showThm1

        self.Thm2Btn = tk.Button(self.MidllePanel)
        self.Thm2Btn.grid(column=1, row=1, padx=20)
        self.Thm2Btn.configure(text="Логические основы\nвычислительной техники", font=("Bookman Old Style", 15), bg='#42313A',fg="white", relief=tk.RAISED)
        self.Thm2Btn['command'] = self.showThm2

        self.Thm3Btn = tk.Button(self.MidllePanel)
        self.Thm3Btn.grid(column=2, row=1, padx=20)
        self.Thm3Btn.configure(text="Основы комбинаторики и\nтеории вероятностей", font=("Bookman Old Style", 15), bg='#42313A',fg="white", relief=tk.RAISED)
        self.Thm3Btn['command'] = self.showThm3

        # надпись вверху экрана
        self.GreetLbl = tk.Label(self.TopPanel)
        self.GreetLbl.grid(column=0, row=0)
        self.GreetLbl.configure(text="Welcome to\nComputerScienceHelper", font=("Bookman Old Style", 50), bg='#F1DCC9', padx=20)

        # три появляющихся рамки с темами
        self.MidllePanel_Thm1 = tk.Frame(bg='#F1DCC9')
        self.MidllePanel_Thm1.grid(column=0, row=1)
        self.MidllePanel_Thm1.grid_remove()

        self.MidllePanel_Thm2 = tk.Frame(bg='#F1DCC9')
        self.MidllePanel_Thm2.grid(column=0, row=1)
        self.MidllePanel_Thm2.grid_remove()

        self.MidllePanel_Thm3 = tk.Frame(bg='#F1DCC9')
        self.MidllePanel_Thm3.grid(column=0, row=1)
        self.MidllePanel_Thm3.grid_remove()

        # рамка с информацией
        self.InfoPanel = tk.Frame(bg='#F1DCC9')
        self.InfoPanel.grid(column=0, row=1)
        self.InfoPanel.grid_remove()


    def showThm1(self):
        """
        отображение рамки с первой темой
        :return:
        """
        self.GreetLbl.configure(text="Математические основы\nвычислительной техники")
        self.InfoBtn.configure(text="Назад")
        self.MidllePanel.grid_remove()
        num_of_btn=0
        self.MidllePanel_Thm1.grid()
        for ex_name_Thm1, func_of_ex_Thm1 in Thm1_dict.items():
            self.temp_Btn = tk.Button(self.MidllePanel_Thm1, text=ex_name_Thm1, command=func_of_ex_Thm1,font=("Bookman Old Style", 15 ), bg='#42313A', fg="white", relief=tk.RAISED)
            self.temp_Btn.grid(column=num_of_btn, row=1, padx=20)
            num_of_btn = num_of_btn + 1
        self.InfoBtn['command'] = lambda: self.goBackThm()


    def showThm2(self):
        """
        отображение рамки с второй темой
        :return:
        """
        self.GreetLbl.configure(text="Логические основы\nвычислительной техники")
        self.InfoBtn.configure(text="Назад")
        self.MidllePanel.grid_remove()
        num_of_btn=0
        self.MidllePanel_Thm2.grid()
        for ex_name_Thm2, func_of_ex_Thm2 in Thm2_dict.items():
            self.temp_Btn = tk.Button(self.MidllePanel_Thm2, text=ex_name_Thm2, command=func_of_ex_Thm2,font=("Bookman Old Style", 15 ), bg='#42313A', fg="white", relief=tk.RAISED)
            self.temp_Btn.grid(column=num_of_btn, row=1, padx=20)
            num_of_btn = num_of_btn + 1
        self.InfoBtn['command'] = lambda: self.goBackThm()


    def showThm3(self):
        """
        отображение рамки с третьей темой
        :return:
        """
        self.GreetLbl.configure(text="Основы комбинаторики и\nтеории вероятностей")
        self.InfoBtn.configure(text="Назад")
        self.MidllePanel.grid_remove()
        num_of_btn=0
        self.MidllePanel_Thm3.grid()
        for ex_name_Thm3, func_of_ex_Thm3 in Thm3_dict.items():
            self.temp_Btn = tk.Button(self.MidllePanel_Thm3, text=ex_name_Thm3, command=func_of_ex_Thm3,font=("Bookman Old Style", 15 ), bg='#42313A', fg="white", relief=tk.RAISED)
            self.temp_Btn.grid(column=num_of_btn, row=1, padx=20)
            num_of_btn = num_of_btn + 1
        self.InfoBtn['command'] = lambda: self.goBackThm()


    def showInfo(self):
        """
        отображение рамки с информацией
        :return:
        """
        self.GreetLbl.configure(text="Информация")
        self.InfoBtn.configure(text="Назад")
        self.MidllePanel.grid_remove()
        self.InfoPanel.grid()
        self.lbl_info = tk.Label(self.InfoPanel, text="Данное приложение создано для помощи учащимся\nв изучении основных тем информатики\n\nСоздано Романовским Андреем в 2021",
                                 font=("Bookman Old Style", 15 ), bg='#F1DCC9', padx=20 )
        self.lbl_info.grid(column=0, row=1)
        self.InfoBtn['command'] = lambda: self.goBackThm()

    def goBackThm(self):
        """
        функция возврата на главный экран
        :return:
        """
        self.GreetLbl.configure(text="Welcome to\nComputerScienceHelper")
        self.InfoBtn.configure(text="Информация")
        self.MidllePanel_Thm1.grid_remove()
        self.MidllePanel_Thm2.grid_remove()
        self.MidllePanel_Thm3.grid_remove()
        self.InfoBtn['command'] = self.showInfo
        self.InfoPanel.grid_remove()
        self.MidllePanel.grid(column=0, row=1)