import random

print("\nBem-vindo ao Jogo do Seis! Tente adivinhar o número secreto (de 1 a 10)\n⚠️Mas cuidado! Se for 6, você perde automaticamente!⚠️\n")

tentativas = []  
numero_secreto = random.randint(1, 10)

enquanto = True
while enquanto:
    try:
        palpite = int(input("Digite um número entre 1 e 10: "))
        
        if palpite < 1 or palpite > 10:
            print("⛔ Número inválido! Escolha um entre 1 e 10.")
            continue
        
        else:
            
            tentativas.append(palpite)
            
            if palpite == 6:
                print("💀 Você perdeu! O número 6 é proibido!")
                enquanto = False
            elif palpite == numero_secreto:
                print(f"🎉 Parabéns! Você acertou em {len(tentativas)} tentativa(s). O número era {numero_secreto}.")
                enquanto = False
            else:
                print("❌ Errado! Tente novamente.")
        
    except ValueError:
        print("⛔ Entrada inválida! Digite apenas números inteiros.")
        
print("\n🔚 Fim do jogo! Obrigado por jogar! 😊")
