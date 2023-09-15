from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

elemento1 = Elemento("A")
elemento2 = Elemento("B")

if elemento1 == elemento2:
    print("Los elementos son iguales.")
else:
    print("Los elementos son diferentes.")

elemento3 = Elemento("A")

if elemento1 == elemento3:
    print("Los elementos son iguales.")
else:
    print("Los elementos son diferentes.")
