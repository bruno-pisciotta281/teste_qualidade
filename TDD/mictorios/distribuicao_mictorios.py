def calcular_mijoes_nao_constrangedores(ocupacao_inicial):
    mijoes_nao_constrangedores = 0
    mictorios_vazios = 0
    consecutivo_ocupado = False

    for c in ocupacao_inicial:
        if c == 'X':
            if consecutivo_ocupado:

                mijoes_nao_constrangedores += mictorios_vazios
                mictorios_vazios = 0
            consecutivo_ocupado = True
        elif c == '.':
            mictorios_vazios += 1
            consecutivo_ocupado = False

    if consecutivo_ocupado:
        mijoes_nao_constrangedores += mictorios_vazios

    return mijoes_nao_constrangedores
