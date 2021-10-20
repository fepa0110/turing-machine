class operaciones_turing():
    caracter_vacio = "$"
    cinta = ""
    indice_cinta = 0
    
    def __init__(self, cinta):
        self.cinta = self.caracter_vacio+cinta+self.caracter_vacio
        #print("CINTA: {}".format(self.cinta))
    
    def get_indice_cinta(self):
        return self.indice_cinta
    
    def get_cinta(self):
        return self.cinta
    
    def get_caracter_vacio(self):
        return self.caracter_vacio
    
    def get_caracter_actual(self):
        return self.cinta[self.indice_cinta]
    
    def right(self):
        if(self.indice_cinta < self.cinta.__len__()-1):
            self.indice_cinta += 1
        else:
            self.indice_cinta += 1
            self.cinta = self.caracter_vacio+self.cinta+self.caracter_vacio

    def left(self):
        if(self.indice_cinta > 0):
            self.indice_cinta= self.indice_cinta-1
        else:
            self.indice_cinta = 0
            self.cinta = self.caracter_vacio+self.cinta+self.caracter_vacio

    def shift_right(self, cinta, indice_cinta):
        self.indice_cinta = self.cinta.__len__()-1
        return self.cinta[self.indice_cinta], self.cinta, self.indice_cinta

    def shift_left(self, cinta, indice_cinta):
        self.indice_cinta = 0
        return self.cinta[self.indice_cinta], self.cinta, self.indice_cinta

    def right_to(self, caracter, cinta, indice_cinta):
        try:
            self.indice_cinta = self.cinta.index(self.caracter, start=self.indice_cinta)
            return self.cinta[self.indice_cinta], self.cinta, self.indice_cinta
        except ValueError as ve:
            return ve

    def left_to(self, caracter, cinta, indice_cinta):
        try:
            self.indice_cinta = self.cinta.index(self.caracter, start=0, end=self.indice_cinta)
            return self.cinta[self.indice_cinta], self.cinta, self.indice_cinta
        except ValueError as ve:
            return ve

    def put(self,caracter):
        self.cinta = self.cinta[0: self.indice_cinta:] + caracter + self.cinta[self.indice_cinta + 1::]

    def operation(self, input_operation):
        operation = input_operation.upper()
        caracter = self.caracter_vacio
        caracter_actual = ""
        if(operation == "R"):
            self.right()
            return "R => caracter: {}".format(self.get_caracter_actual())
        else:
            if(operation == "L"):
                self.left()
                return "L => caracter: {}".format(self.get_caracter_actual())
            else:
                if(input_operation == "-"):
                    return "No hacer nada."
                else:
                    if((input_operation != "") and (input_operation != self.caracter_vacio)):
                        self.put(input_operation)
                        return "escribir --> {}".format(input_operation)
        return "Error en la operación."
