from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

@dataclass
class Conjunto:
    elementos: list = []
    nombre: str = ""
    __contador_instancias = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Conjunto.__contador_instancias += 1
        self.__id = Conjunto.__contador_instancias

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e.nombre == elemento.nombre for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        for elemento in self.elementos + otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        return cls(nombre_resultado, elementos_comunes)

    def __str__(self):
        elementos_str = ", ".join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"


elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")


conjunto1 = Conjunto("Conjunto1")
conjunto2 = Conjunto("Conjunto2")


conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)


union_conjuntos = conjunto1 + conjunto2
print(union_conjuntos)


interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print(interseccion)
