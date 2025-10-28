import json
nome_arq = 'catalogo.json'
def carregar_dados():
    try:
        with open(nome_arq, "r", encoding='utf-8') as file:
            dados = json.load(file)
            return dados
    except FileNotFoundError:
        dados = []
        return dados
    except json.JSONDecodeError:
        dados = []
        return dados

def salva_dados(dados):
    try:
        with open(nome_arq, "w", encoding='utf-8') as file:
            json.dump(dados, file, indent=4)
    except IOError as e:
        print(e)

def listar_itens():
    meu_catalogo = carregar_dados()
    if not meu_catalogo:
        print("Catalogo Vazio")
    else:
        for i, itens in enumerate(meu_catalogo):
            print(f'{i}- {itens}')

def adicionar_item():
    meu_catalogo = carregar_dados()
    novo_item = {}
    novo_item['titulo'] = input('   Digite o titulo do item: ')
    novo_item['genero'] = input('   Digite o genero do item: ')
    meu_catalogo.append(novo_item)
    salva_dados(meu_catalogo)
    print("Item adicionado com sucesso!")

def buscar_item():
    meu_catalogo = carregar_dados()
    genero = input('    Qual genero deseja buscar? ').lower()
    resultados = []
    for i, itens in enumerate(meu_catalogo):
        if itens['genero'].lower() == genero:
            resultados.append( (i, itens) )
    if resultados:
        print(f'Os itens do genero {genero} são:')
        for i, itens in resultados:
            print(f'{i}- {itens}')
    else:
        print(f'Não foi encotrado nenhum item do genero {genero}')

def excluir_item():
    meu_catalogo = carregar_dados()
    alvo_item = input('    Qual é o titulo do item que deseja excluir? ').lower()
    novo_catalogo = []
    item_encontrado = False
    for itens in meu_catalogo:
        if itens['titulo'].lower() != alvo_item:
            novo_catalogo.append(itens)
        else:
            item_encontrado = True
    if item_encontrado:
        salva_dados(novo_catalogo)
        print("Item excluido com sucesso!")
    else:
        print(f"Não foi encotrado nenhum item com o titulo {alvo_item}")

def menu_principal():
    while True:
        print("""Qual ação deseja realizar?
        [1] - Adicionar
        [2] - Listar
        [3] - Buscar item por genero
        [4] - Excluir
        [0] - Sair""")
        opcao = input()
        if opcao == '1':
            print('Opção 1 selecionada')
            adicionar_item()
        elif opcao == '2':
            print('Opção 2 selecionada, aqui esta a lista dos itens')
            listar_itens()
        elif opcao == '3':
            print('Opção 3 selecionada')
            buscar_item()
        elif opcao == '4':
            print('Opção 4 selecionada')
            excluir_item()
        elif opcao == '0':
            break
        else:
            print('opcao invalida, Tente novamente')
menu_principal()




