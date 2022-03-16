
from AnalizadorLexico import *
from Estado import *
from transicion import *
from AFN import *
import graphviz 

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
        self.graficar()
        

    def concatenacion(self, maquina1, maquina2):
        print(maquina1)
        print(maquina2)
        # --
        #maquina2.estados[-1].tipo = 2
        estados = []
        estados = maquina2.estados[:-1]
        punto_referencia = len(maquina2.estados) -1

        for estado in maquina1.estados:

            
            if estado.tipo == 1:
                estado.etiqueta = "s" + str(punto_referencia)
                estado.tipo = 2
            
            else:
                estado.etiqueta = "s" + str((int(estado.etiqueta[1]) + punto_referencia))

            
            for transicion in estado.transiciones:
                transicion.destino = "s" + str((int(transicion.destino[1]) + punto_referencia))

            estados.append(estado)
        
        self.maquinas.append(AFN(estados,[],[]))    



    #paso base
    #ir de estado inicial a final con un caracter
    #t1 iniical, t2 normal, t3 final ok
    def paso_base(self, caracter):
        trans = Transicion("s1", caracter)
        estado1 = Estado("s0", [trans],1)
        estadof = Estado("s1", [], 3)
        self.maquinas.append(AFN([estado1,estadof],[],trans))


    def graficar(self):
        maquina = self.maquinas[0]
        # ---
        afn = graphviz.Digraph('finite_state_machine', filename='AFN.gv')
        afn.attr(rankdir='LR', size='8,5')
        afn.attr('node', shape='doublecircle')
        afn.node('s0')
        afn.node(maquina.estados[-1].etiqueta)

        # --
        for estado in maquina.estados:
            print(estado.tipo)
            if estado.tipo == 3:
                continue
            for transi in estado.transiciones:
                afn.edge(estado.etiqueta, transi.destino, label=transi.caracter)
        
        afn.view()



            


        

        



        

        




        
        

    
    
