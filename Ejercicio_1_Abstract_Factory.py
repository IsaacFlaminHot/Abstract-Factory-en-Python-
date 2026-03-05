from abc import ABC, abstractmethod

#Fabrica Abstracta#
class MaterialFactory(ABC):

    @abstractmethod
    def crear_guia(self):
        pass

    @abstractmethod
    def crear_examen(self):
        pass

#Productos Abstractos#

class Guia(ABC):

    @abstractmethod
    def mostrar(self):
        pass

class Examen(ABC):
    
    @abstractmethod
    def aplicar(self):
        pass

#Productos concretos (Presencial)#

class GuiaImpresa(Guia):

    def mostrar(self):
        print("Mostrando guia impresa")

class ExamenImpreso(Examen):

    def aplicar(self):
        print("Aplicando examen en papel")

#Productos concretos (Virtual)#

class GuiaPDF(Guia):

    def mostrar(self):
        print("Mostrando guia en formato PDF")

class ExamenOnline(Examen):

    def aplicar(self):
        print("Se aplica el examen en Linea")

#Tarea - Productos concretos (Mixto)#
class GuiaMixta(Guia):
    
    def mostrar(self):
        print("Mostrando guia en formato PDF e impresa")

class ExamenMixto(Examen):
    
    def aplicar(self):
        print("Aplicando examen en papel y en Linea")

#Fabrica concreta#

class MaterialPresencialFactory(MaterialFactory):

    def crear_guia(self):
        return GuiaImpresa()

    def crear_examen(self):
        return ExamenImpreso()

class MaterialVirtualFactory(MaterialFactory):

    def crear_guia(self):
        return GuiaPDF()

    def crear_examen(self):
        return ExamenOnline()

class MaterialMixtoFactory(MaterialFactory):
    
    def crear_guia(self):
        return GuiaMixta()

    def crear_examen(self):
        return ExamenMixto()

if __name__ == "__main__":

    fabrica = MaterialPresencialFactory()

    guia = fabrica.crear_guia()
    examen = fabrica.crear_examen()

    guia.mostrar()
    examen.aplicar()

    print()

    fabrica = MaterialVirtualFactory()

    guia = fabrica.crear_guia()
    examen = fabrica.crear_examen()

    guia.mostrar()
    examen.aplicar()

    print()

    fabrica = MaterialMixtoFactory()

    guia = fabrica.crear_guia()
    examen = fabrica.crear_examen()

    guia.mostrar()
    examen.aplicar()