
from AnalizadorLexico import *
from Estado import *
from transicion import *
from AFN import *
#import graphviz ##

class Thompson:
    def __init__(self, expresion_regular):
        a = AnalizadorLexico(expresion_regular)
        self.maquinas = []
        self.expresion_regular = a.convertir_postfix()
    
    def compilar(self):
        print(self.maquinas) 
        self.paso_base("c")
        self.paso_base("a")
        self.concatenacion(self.maquinas.pop(), self.maquinas.pop())

        

    def concatenacion(self, maquina1, maquina2):
        print(maquina1)
        print(maquina2)

        
        

   

    #paso base
    #ir de estado inicial a final con un caracter
    #t1 iniical, t2 normal, t3 final ok
    def paso_base(self, caracter):
        trans = Transicion("S1", caracter)
        estado1 = Estado("S0", [trans],1)
        estadof = Estado("S1", [], 3)
        self.maquinas.append(AFN([estado1,estadof],[],trans))


    def graficar(self):
        maquina = self.maquinas[0]
        # ---
        afn = graphviz.Digraph('finite_state_machine', filename='AFN.gv')
        afn.attr(rankdir='LR', size='8,5')
        afn.attr('node', shape='doublecircle')
        afn.node('S0')
        afn.node(maquina.estados[-1].etiqueta)

        # --
        for estado in maquina.estados:
            if estado.tipo == 3:
                continue
            for transi in estado.transiciones:
                afn.edge(estado.etiqueta, transi.destino, label=transi.caracter)
        
        afn.view()



            


        

        



        

        




        
        

    
    
