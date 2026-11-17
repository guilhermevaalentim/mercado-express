import os

produtos = [{'nome':'Arroz', 'categoria':'Comida', 'ativo':True},
            {'nome':'Feijão', 'categoria':'Comida', 'ativo':False},
            {'nome':'Queijo', 'categoria':'Comida', 'ativo':False}]

def exibir_nome_app():
    '''Exibe o nome do aplicativo'''
    print("""
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████──────────██████─██████████████─████████████████───██████████████─██████████████─████████████───██████████████─
─██░░██████████████░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██─
─██░░░░░░░░░░░░░░░░░░██─██░░██████████─██░░████████░░██───██░░██████████─██░░██████░░██─██░░████░░░░██─██░░██████░░██─
─██░░██████░░██████░░██─██░░██─────────██░░██────██░░██───██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██──██░░██──██░░██─██░░██████████─██░░████████░░██───██░░██─────────██░░██████░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██──██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░██─────────██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██──██████──██░░██─██░░██████████─██░░██████░░████───██░░██─────────██░░██████░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██──────────██░░██─██░░██─────────██░░██──██░░██─────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██──────────██░░██─██░░██████████─██░░██──██░░██████─██░░██████████─██░░██──██░░██─██░░████░░░░██─██░░██████░░██─
─██░░██──────────██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░████─██░░░░░░░░░░██─
─██████──────────██████─██████████████─██████──██████████─██████████████─██████──██████─████████████───██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─████████──████████─██████████████─████████████████───██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─████░░██──██░░████─██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░██───────────██░░░░██░░░░██───██░░██──██░░██─██░░██────██░░██───██░░██─────────██░░██─────────██░░██─────────
─██░░██████████───████░░░░░░████───██░░██████░░██─██░░████████░░██───██░░██████████─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─────██░░░░░░██─────██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████───████░░░░░░████───██░░██████████─██░░██████░░████───██░░██████████─██████████░░██─██████████░░██─
─██░░██───────────██░░░░██░░░░██───██░░██─────────██░░██──██░░██─────██░░██─────────────────██░░██─────────██░░██─
─██░░██████████─████░░██──██░░████─██░░██─────────██░░██──██░░██████─██░░██████████─██████████░░██─██████████░░██─
─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░██─────────██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─████████──████████─██████─────────██████──██████████─██████████████─██████████████─██████████████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────
""")

def exibir_opçoes():
    '''Exibe as opções do menu'''
    print('1. Cadastrar Produto')
    print('2. Listar Produtos')
    print('3. Alterar Estado do Produto')
    print('4. Sair\n')

def exibir_subtitulo(texto):
    '''Exibe um subtítulo destacado por linhas de asteriscos.

    Args:
        texto (str): texto do subtítulo.o'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''Aguarda uma tecla do usuário e volta ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal. ')
    main()

def finalizar_app():
    '''Exibe a mensagem de encerramento do aplicativo'''
    os.system('cls')
    exibir_subtitulo('Finalizando o app...')

def opcao_invalida():
    '''Exibe opção inválida e retorna ao menu principal'''
    os.system('cls')
    exibir_subtitulo('Opção inválida.')
    voltar_ao_menu_principal()

def cadastrar_produto():
    '''Pede nome e categoria ao usuário e cadastra o produto'''
    os.system('cls')
    exibir_subtitulo('Cadastrar um produto')
    nome_do_produto = input('Digite o nome do produto: ')
    categoria = input(f'Digite o nome da categoria do produto {nome_do_produto}: ')
    dados_do_produto = {'nome':nome_do_produto, 'categoria':categoria, 'ativo':False}
    produtos.append(dados_do_produto)
    print(f'O produto {nome_do_produto} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_produtos():
    '''Exibe todos os produtos com categoria e status'''
    os.system('cls')
    exibir_subtitulo('Listando todos os produtos')
    print(f'{'Produto'.ljust(22)} | {'Categoria'.ljust(20)} | Status\n')
    for produto in produtos:
        nome_produto = produto['nome']
        categoria = produto['categoria']
        ativo = 'Ativado' if produto ['ativo'] else 'Desativado'
        print(f'- {nome_produto.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_produto():
    '''Altera o status de um produto'''
    exibir_subtitulo('Alterando estado do produto')
    nome_produto = input('Digite o nome do produto que deseja alterar o estado: ')
    produto_encontrado = False
    for produto in produtos:
        if nome_produto == produto['nome']:
            produto_encontrado = True
            produto['ativo'] = not produto['ativo']
            mensagem = f'O produto {nome_produto} foi ativado com sucesso' if produto ['ativo'] else f'O produto {nome_produto} foi desativado com sucesso'
            print(mensagem)
    if not produto_encontrado:
        print('O produto não foi encontrado')
    voltar_ao_menu_principal()

def opçao_escolhida():
    '''Lê a opção do usuário e chama a função correspondente'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_produto()
        elif opcao_escolhida == 2:
            listar_produtos()
        elif opcao_escolhida == 3:
            alternar_estado_produto()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()

def main():
    '''Limpa a tela, exibe o nome do app e o menu e lê a opção escolhida'''
    os.system('cls')
    exibir_nome_app()
    exibir_opçoes()
    opçao_escolhida()
    
if __name__ == '__main__':
    main()

