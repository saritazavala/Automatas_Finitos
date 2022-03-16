class Estado:
    def __init__(self estado_inicial, estado_final):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final

class Transicion:
    def __init__(self, punto_inicio, transicion, final):
        self.punto_inicio = punto_inicio
        self.transicion = transicion
        self.final = final