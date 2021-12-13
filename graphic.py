from logic_and_smallgraphic import *

Thm1_dict = {
    "from_10_to_2_8_16": from_10_to_2_8_16,
    "multiplication_dividing": multiplication_dividing,
    "from_16_to_10": from_16_to_10,
    "3_types_of_code": types_of_code_3,
    "IEEE_754": IEEE_754,
}

Thm2_dict = {
    "from_10_to_2_8_16": from_10_to_2_8_16,
    "multiplication_dividing": multiplication_dividing,
    "from_16_to_10": from_16_to_10,
    "3_types_of_code": types_of_code_3,
    "IEEE_754": IEEE_754,
}

Thm3_dict = {
    "from_10_to_2_8_16": from_10_to_2_8_16,
    "multiplication_dividing": multiplication_dividing,
    "from_16_to_10": from_16_to_10,
    "3_types_of_code": types_of_code_3,
    "IEEE_754": IEEE_754,
}



class HubFrame:
    """

    """
    def __init__(self, parent):
        """

        :param parent:
        """
        parent.title("CSH")
        parent.configure(bg='#F1DCC9')

        self.TopPanel = tk.Frame(parent, bg='#1E0000')
        self.TopPanel.grid(column=0, row=0)


        self.MidllePanel = tk.Frame(parent, bg='#500805')
        self.MidllePanel.grid(column=0, row=1)

        self.BottomPanel = tk.Frame(parent, bg='#9D331F')
        self.BottomPanel.grid(column=0, row=2)

        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1, minsize=300)
        parent.rowconfigure(1, weight=1, minsize=300)
        parent.rowconfigure(2, weight=1, minsize=300)


        self.InfoBtn = tk.Button(self.BottomPanel)
        self.InfoBtn.grid(column=0, row=2)
        self.InfoBtn.configure(text="gggg")

        self.Thm1Btn = tk.Button(self.MidllePanel)
        self.Thm1Btn.grid(column=0, row=1)
        self.Thm1Btn.configure(text="gogogo")
        self.Thm1Btn['command'] = self.showThm1

        self.Thm2Btn = tk.Button(self.MidllePanel)
        self.Thm2Btn.grid(column=1, row=1)
        self.Thm2Btn.configure(text="gogogo")
        self.Thm2Btn['command'] = self.showThm2

        self.Thm3Btn = tk.Button(self.MidllePanel)
        self.Thm3Btn.grid(column=2, row=1)
        self.Thm3Btn.configure(text="gogogo")
        self.Thm3Btn['command'] = self.showThm3

        self.GreetLbl = tk.Label(self.TopPanel)
        self.GreetLbl.grid(column=0, row=0)
        self.GreetLbl.configure(text="Welcome to\nComputerScienceHelper")

        self.MidllePanel_Thm1 = tk.Frame()
        self.MidllePanel_Thm1.grid(column=0, row=1)
        self.MidllePanel_Thm1.grid_remove()

        self.MidllePanel_Thm2 = tk.Frame()
        self.MidllePanel_Thm2.grid(column=0, row=1)
        self.MidllePanel_Thm2.grid_remove()

        self.MidllePanel_Thm3 = tk.Frame()
        self.MidllePanel_Thm3.grid(column=0, row=1)
        self.MidllePanel_Thm3.grid_remove()


    def showThm1(self):
        """

        :return:
        """
        self.GreetLbl.configure(text="Математические основы\nвычислительной техники")
        self.MidllePanel.grid_remove()
        num_of_btn=0
        self.MidllePanel_Thm1.grid()
        for ex_name_Thm1, func_of_ex_Thm1 in Thm1_dict.items():
            self.temp_Btn = tk.Button(self.MidllePanel_Thm1, text=ex_name_Thm1, command=func_of_ex_Thm1)
            self.temp_Btn.grid(column=num_of_btn, row=1)
            num_of_btn = num_of_btn + 1
        self.InfoBtn['command'] = lambda: self.goBackThm()


    def showThm2(self):
        """

        :return:
        """
        self.GreetLbl.configure(text="Логические основы\nвычислительной техники")
        self.MidllePanel.grid_remove()
        num_of_btn=0
        self.MidllePanel_Thm2.grid()
        for ex_name_Thm2, func_of_ex_Thm2 in Thm2_dict.items():
            self.temp_Btn = tk.Button(self.MidllePanel_Thm2, text=ex_name_Thm2, command=func_of_ex_Thm2)
            self.temp_Btn.grid(column=num_of_btn, row=1)
            num_of_btn = num_of_btn + 1
        self.InfoBtn['command'] = lambda: self.goBackThm()


    def showThm3(self):
        """

        :return:
        """
        self.GreetLbl.configure(text="Основы комбинаторики и\nтеории вероятностей")
        self.MidllePanel.grid_remove()
        num_of_btn=0
        self.MidllePanel_Thm3.grid()
        for ex_name_Thm3, func_of_ex_Thm3 in Thm3_dict.items():
            self.temp_Btn = tk.Button(self.MidllePanel_Thm3, text=ex_name_Thm3, command=func_of_ex_Thm3)
            self.temp_Btn.grid(column=num_of_btn, row=1)
            num_of_btn = num_of_btn + 1
        self.InfoBtn['command'] = lambda: self.goBackThm()


    def goBackThm(self):
        """

        :return:
        """
        self.GreetLbl.configure(text="Welcome to\nComputerScienceHelper")
        self.MidllePanel_Thm1.grid_remove()
        self.MidllePanel_Thm2.grid_remove()
        self.MidllePanel_Thm3.grid_remove()
        self.MidllePanel.grid(column=0, row=1)





















