def jokenpo(jogada1, jogada2):
    if jogada1 == jogada2:
        return "Empate"
    elif (jogada1 == "Pedra" and jogada2 == "Tesoura") or (jogada1 == "Tesoura" and jogada2 == "Papel") or (jogada1 == "Papel" and jogada2 == "Pedra"):
        return "Jogador 1 vence"
    else:
        return "Jogador 2 vence"
