import os

restaurantes = [{'nome':'restaurante XP','categoria':'Alimento','ativo':False},
                {'nome':'Santa','categoria':'carne','ativo':True},
                {'nome':'CWB','categoria':'Sushi','ativo':False}] 

def exibir_nome_do_programa():
 print("""Oscar Alho
 """)
def exibir_opcoes():
 '''Essa função é responavel por exibir opções'''
 print('1. Cadastrar restaurante')
 print('2. Listar restaurante')
 print('3. Ativar restaurante')
 print('4. Sair')
 
def finaliza_app():
   '''Essa função finaliza o Aplicativo
   output:
   - Aplicativo Finalizado
   '''
   exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
   '''Essa função é responsavel por fazer voltar ao menu principal1
   '''

   input('\n Digite a tecla "Enter" para voltar ao menu principal')
   main()
   
def opcao_invalida():
   '''Essa função é reponavel por invalidar as opções
   '''

   print('Opção invalida!\n')
   voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsavel '''
    os.system('clear') 
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
   '''Essa função  é responsável por cadastrar um novo restaurante 
   inputs:
   - Nome do restaurante
   - Categoria
   
   Output:
   - Adicionar um novo restaurante à lista de restaurantes
   '''
   
   exibir_subtitulo('Cadastro de novos restaurantes: ')
   nome_do_restaurante = input('Digite o nome do novo restaurante:')
   categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
   dado_do_restaurante ={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
   restaurantes.append(dado_do_restaurante)
   print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
   voltar_ao_menu_principal()

def listar_restaurante():
   '''Essa função é responsavel por listar os restaurantes
   output:
   - Apresenta na tela a lista com os nomes dos rertaurantes
   '''

   exibir_subtitulo('Listando os restaurantes')

   print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
   for restaurante in restaurantes:
      nome_restaurante = restaurante['nome']
      categoria = restaurante['categoria']
      ativo = 'ativado' if restaurante['ativo'] else 'desativado'
      print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

   voltar_ao_menu_principal()   

def alternar_estado_retaurante():
   '''Essa função e responsavel por alterar o estado dos restaurantes
   inputs:
   - nome do retaurante
   - categoria 
   output:
   - Estado do restaurante foi alterado
   '''

   exibir_subtitulo('alternando estado do retaurante')
   nome_restaurante = input ('digite o nome do restaurante que deseja alterar o estado')
   restaurante_encontrado = False

   for retaurante in restaurantes:
       if nome_restaurante == restaurantes['nome']:
         restaurante_encontrado = True
         restaurantes['ativo'] = not restaurantes['ativo'] 
         mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurantes['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
         print(mensagem)

   if not restaurante_encontrado:
       print('o restaurante não foi encontrado')
   voltar_ao_menu_principal()       

def escolher_opcao():
 try:
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurante()
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    elif opcao_escolhida == 4:
       finaliza_app()    
    else:
       opcao_invalida()

 except:
    opcao_invalida()        

def main():
   os.system('clear')
   exibir_nome_do_programa()
   exibir_opcoes()
   escolher_opcao()

if __name__ == '__main__':
    main()