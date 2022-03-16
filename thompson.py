
from AnalizadorLexico import *
from Estado import *
import copy
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
        self.paso_base("a") 
        self.paso_base("b") 
        # self.asterisco(self.maquinas.pop())
        # self.paso_base("b")
        # self.asterisco(self.maquinas.pop())
        # self.concatenacion(self.maquinas.pop(), self.maquinas.pop())
        # print(self.maquinas)
        # self.graficar()
        #self.plus(self.maquinas.pop())
        self.OR(self.maquinas.pop(), self.maquinas.pop() )
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



    def asterisco(self, auotomata):
        estados = []
        estado_inicial = Estado("s0",
                                [Transicion("s1","E"),
                                    Transicion("s"+str(len(auotomata.estados)+1),"E")],
                                        1)
        # --------
        estado_final = Estado("s"+str((len(auotomata.estados)+1)),[],3)

        
        auotomata.estados[0].tipo = 2
        auotomata.estados[-1].tipo = 2
        auotomata.estados[-1].transiciones.append(Transicion("s0","E"))
        auotomata.estados[-1].transiciones.append(Transicion("s"+str(len(auotomata.estados)),"E"))

        # -------

        estados.append(estado_inicial)

        for s in auotomata.estados:
            s.etiqueta = "s"+ str((int(s.etiqueta[1])+ 1))
            for t in s.transiciones:
                t.destino = "s" + str((int(t.destino[1])+ 1))
            estados.append(s)

        estados.append(estado_final)
        self.maquinas.append(AFN(estados,[],[]))

    
    def plus(self,automata):
        automata2 = copy.deepcopy(automata)
        self.asterisco(automata)
        self.concatenacion(self.maquinas.pop(),automata2)


    def OR(self,automata1,automata2):
        
        estados = []
        estado_inicial = Estado("s0",[Transicion("s1","E"),Transicion("s"+str(len(automata2.estados)+1),"E")],1)
        estado_final = Estado("s"+str(len(automata1.estados)+len(automata2.estados)+1),[],3)

        automata1.estados[0].tipo = 2 
        automata1.estados[-1].tipo = 2 

        automata2.estados[0].tipo = 2
        automata2.estados[-1].tipo = 2

        estados.append(estado_inicial)
        
        
        for s in automata2.estados:
            s.etiqueta = "s"+ str((int(s.etiqueta[1])+ 1)) 
            for t in s.transiciones:
                t.destino =  "s" + str((int(t.destino[1])+ 1))
            estados.append(s)
        

        estados[-1].transiciones =[Transicion("s"+str(len(automata1.estados)+len(automata2.estados)+1),"E")]

        for i in automata1.estados:
            i.etiqueta = "s"+ str((int(i.etiqueta[1])+len(automata2.estados)+ 1)) 
            for j in i.transiciones:
                j.destino = "s"+ str((int(j.destino[1])+len(automata2.estados)+ 1)) 
            estados.append(i)

        estados[-1].transiciones =[Transicion("s"+str(len(automata1.estados)+len(automata2.estados)+1),"E")]
        estados.append(estado_final)

        self.maquinas.append(AFN(estados,[],[]))

    def interrogacion(self,automata):
        self.paso_base("E")
        self.OR(self.maquinas.pop(),automata)





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



            


        

        



        

        




        
        

    
    
