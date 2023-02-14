from cadastros.models import Reserva
from pprint import pprint


def test():

    horarioMarcados = []
    horariosDisponiveis = []
    data = []
    local = []
    print("tttt"*50)

    

    for i in Reserva.objects.all():
        horarioMarcados.append((i.horario, i.horario))

    for j in Reserva.horario.field.choices:

        if j not in horarioMarcados:
            horariosDisponiveis.append(j)

    # pprint(horarioMarcados)
    # print("#"*50)
    pprint(horariosDisponiveis)

    return horariosDisponiveis
