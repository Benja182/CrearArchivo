from dataclasses import dataclass


@dataclass
class Depto:
    num_ident: int
    nombre: str
    piso: int
    codigo: int
    monto: int


def to_string(reg):
    linea = '|{:^20}\t|{:^20}\t|{:^20}\t|{:^20}\t|{:^20}|\n'
    linea = linea.format(reg.num_ident, reg.nombre, reg.piso, reg.codigo, reg.monto)
    return linea
