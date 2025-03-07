import json
 
 class CintaUnicaTuring:
 

    def __init__(self, config_file, n):
        with open(config_file, "r") as f:
            config = json.load(f)

        self.estados = config["estados"]
        self.e_ini = config["estado_inicial"]
        self.e_end = config["estados_finales"]
        self.transiciones = config["transiciones"]

        self.es_act = self.e_ini

        # Inicializamos la cinta con el formato: n F(n-2) F(n-1) 
        self.cinta = ["_"] * 10  
        self.cinta[0] = str(n)  
        self.cinta[1] = "1"  
        self.cinta[2] = "1"  
        self.head = 3  

        self.traza = []  