import os

restaurantes = [{'nome':'Girafus e a Dani','categoria': 'Alimento','ativo':False},
                {'nome':'Santa','categoria':'pastel de carne','ativo':True},
                {'nome':'CWB','categoria':'pizza de frango','ativo':False}]

def exibir_nome_do_programa():  
 print("""Oscar Alhos
  """)
def exibir_opcoes():
 print('1. Cadastrar restaurante')
 print('2. Listar restaurante')
 print('3. Ativar restaurante')
 print('4. Sair')

def finalizar_app():
   exibir_subtitulos('Finalizar App')
   
def voltar_ao_menu_principal():
   '''Essa função é responsavel por voltar ao menu principal
   inputs:
   -voltar ao menu principal
   
   output:
   -Volta ao menu principal'''
   input('\n Digite a tecla "Enter" para voltar ao menu pŕincipal')
   main()

def opcao_invalida():
   print('Opção invalida!\n')
   voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    os.system("clear")
    linha = '*' + (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
   '''Essa função é responavel por cadastrar um novo restaurante
    inputs:
    - Nome do restaurante
    - Categoria

    output:
    - Adiciona um novo restaurante à lista de restaurantes
   '''
   

   exibir_subtitulos('Cadastro de novos restaurantes: ')
   nome_do_restaurante = input(f'Digite o nome do novo Restaurante{nome_do_restaurante}:')
   categoria = input(f'Digite a categoria do restaurante {categoria}:')
   dado_do_restaurante ={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
   restaurantes.append(dado_do_restaurante)
   print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
   voltar_ao_menu_principal()

def listar_restaurante():
   '''Essa função é responsavel por listar os restaurantes
   output:
   - Apresenta uma lista dos Restaurantes
   '''


   exibir_subtitulos('Listando os Restaurantes')
   '''Essa função é responsavel por exibir os subtitulos
   output:
   - Exibe o subtitulos
   '''


   print(f'{"Nome do restaurnte".ljust(22)} | {"Categoria".ljust(20)} | Status')
   for restaurante in restaurantes:
      nome_restaurante = restaurante['nome']
      categoria = restaurante['categoria']
      ativo = 'ativado' if restaurante['ativo'] else 'desativado'
      print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

   voltar_ao_menu_principal()
   '''Essa função é responsavel por voltar ao menu
   output:
   - Volta ao menu'''


def alternar_estado_restaurnte():
   '''Essa função é responsavel por alterar o estado do restaurante
   inputs:
   - Nome do restaurante

   output:
   - Altera o estado do restaurante
   '''
   

   exibir_subtitulos('Alternando estado do restaurante')

   nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado:')
   restaurante_encontrado = False

   for restaurante in restaurantes:
     if nome_restaurante == restaurante['nome']:
       restaurante_encontrado = True
       restaurante['ativo'] = not restaurante['nome']
       mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso' 
       print(mensagem)

   if not restaurante_encontrado:
      print('O restaurante não foi encontrado')
   voltar_ao_menu_principal()

def escolher_opcao():
   '''Essa função é responsavel por dar as opções
   output:
   - Opções'''


try:
    opcao_escolhida = int(input('Escolha uma opção: '))
   
    if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
        listar_restaurante()
    elif opcao_escolhida == 3:
        alternar_estado_restaurnte
    elif opcao_escolhida == 4:
       finalizar_app()
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
   
