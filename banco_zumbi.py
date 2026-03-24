nome = input ('qual seu nome?')
print (f'olá {nome}, seu saldo: R$: 0,00')
extrato = []
saldo = 0
escolha = ''
while escolha != '4':
    print ('[1] Depositar')
    print ('[2] Sacar')
    print ('[3] Ver extrato')
    print ('[4] Sair')
    escolha = input ('Opção:')
    if escolha == '1':
        valor = float(input ('valor:'))
        if valor > 0:
            saldo = saldo + valor
            extrato.append(f'depósito R$:{valor:.2f}')
            print (f'valor depositado R$:{valor:.2f}')
        else:
            print ("valor invalido!")
    elif escolha == '2':
        valor = float (input ('valor:'))
        if valor > 0:
            if valor <= saldo:
                saldo = saldo - valor
                extrato.append (f'saque RS{valor:.2f}')
                print (f'Você sacou R$:{valor:.2f}')
            else:
                print (f'saldo insuficiente.')
        else:
            print (f'valor invalido!')
            
    elif escolha == '3':
        print ('===EXTRATO===')
        for item in extrato:
            print (item)
        print (f'seu saldo atual: {saldo:.2f}')

    elif escolha == '4':
        print (f'Até logo {nome}')
    else:
        print ('opção invalida!')
