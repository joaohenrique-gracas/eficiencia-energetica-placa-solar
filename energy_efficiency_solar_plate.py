while True:
    kw_gasto = float(input('digite a quantidade gasta em kwh/mês: '))
    investimento = float(input('Digite o valor de deseja investir: '))
    taxa_regiao = float(input('Digite o valor do kwh da sua região: '))

    # Calculo de paineis necessários
    energy_dia = (265 * 4.93 * (1 - 0.20)) / 1000  # energia diaria
    energy_mes = energy_dia * 30  # energia mensal
    x_painel = kw_gasto / energy_mes  # painéis necessarios
    # Calculo área minina
    potencia_painel = x_painel * 265  # potencia gerada
    area_min = (potencia_painel / 265) * 2  # area minima
    # Calculo Payback
    payback = (investimento / kw_gasto * 12 * taxa_regiao) / 100  # retorno financeiro

    print('=======================================')

    if x_painel >= 16 and x_painel <= 17:
        print('Quantidade de painéis necessários:', '%.0f' % x_painel, 'com módulos de 400Wp')
        print('Área minima para instalação:', '%.0f' % area_min, 'm2')
    if x_painel >= 19 and x_painel <= 20:
        print('Quantidade de painéis necessários:', '%.0f' % x_painel, 'com módulo de 330 Wp')
        print('Área minima para instalação:', '%.0f' % area_min, 'm2')
    else:
        print('Quantidade de painéis necessários:', '%.0f' % x_painel)
        print('Área minima para instalação:', '%.0f' % area_min, 'm2')

    print('PayBack em anos:', '%.2f' % payback)
    new_conta = input('Deseja realizar outra conta? (sim/nao): ').upper()

    print('=======================================')

    if new_conta == 'NAO':
        break
    while True:
        if new_conta != 'SIM':
            print('Valor Inválido!')
            new_conta = input('Deseja realizar outra conta? (sim/nao): ').upper()
        else:
            break








