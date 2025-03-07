import json
 
class CintaUnicaTuring:
 

    def __init__(self, config_file, n):
        with open(config_file, "r") as f:
            config = json.load(f)

        self.estados = config["estados"]
        self.e_ini = config["e_ini"]
        self.e_end = config["e_end"]
        self.transiciones = config["transiciones"]

        self.es_act = self.e_ini

      
        self.cinta = ["_"] * 10  
        self.cinta[0] = str(n)  
        self.cinta[1] = "1"  
        self.cinta[2] = "1"  
        self.head = 3  

        self.traza = []  

    def get_configuracion(self):
            
            return {
                "estado": self.es_act,
                "cinta": " ".join(self.cinta),
                "cabezal": self.head
            }

    def paso(self):
            if self.es_act not in self.transiciones:
                return

            info_estado = self.transiciones[self.es_act]

            
            n = int(self.cinta[0]) if self.cinta[0] != "_" else 0
            f_k_minus_2 = int(self.cinta[1]) if self.cinta[1] != "_" else 0
            f_k_minus_1 = int(self.cinta[2]) if self.cinta[2] != "_" else 0

            
            if "condicion" in info_estado:
                condicion = info_estado["condicion"]
                if condicion == "IF_N_LE_2":
                    self.es_act = info_estado["si_cumple"] if n <= 2 else info_estado["si_no_cumple"]
                elif condicion == "IF_COUNTER_GT_0":
                    self.es_act = info_estado["si_cumple"] if n > 2 else info_estado["si_no_cumple"]

            
            if "accion" in info_estado:
                accion = info_estado["accion"]

                if accion == "SUM_TAPE2_TAPE3_TO_TAPE4":
                    suma = f_k_minus_2 + f_k_minus_1
                    self.cinta[self.head] = str(suma)  

                elif accion == "TAPE2_EQUALS_TAPE3_AND_TAPE3_EQUALS_TAPE4":
                    self.cinta[1] = self.cinta[2]  
                    self.cinta[2] = self.cinta[self.head]  
                    self.cinta[self.head] = "_"  

                elif accion == "COUNTER_MINUS_1":
                    self.cinta[0] = str(n - 1)  
                elif accion == "STOP":
                    pass 

           
            if "siguiente" in info_estado:
                self.es_act = info_estado["siguiente"]

    def run(self):
        
        self.traza.append(self.get_configuracion())

        while self.es_act not in self.e_end:
            self.paso()
            self.traza.append(self.get_configuracion())

        return self.cinta[2], self.traza  


   
config_file = "turing_c.json"
n = 6  
machine = CintaUnicaTuring(config_file, n)
resultado, traza = machine.run()

