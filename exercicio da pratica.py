def menu_de_opçoes ():
    print ('Menu de Opções: ')
    print ("    1. Submenu de Salas")
    print ("    2. Submenu de Filmes")
    print ("    3. Submenu de Sessões")
    print ("    4. Sair")

def menu_de_opçoes_de_submenus ():
    print ("Menu de Opções de Salas")
    print ("    1. Incluir")
    print ("    2. Alterar")
    print ("    3. Imprimir")
    print ("    4. Excluir")
    print ("    5. Exibir")
   

def submenu_de_salas ():
    opçao_de_submenu = int(input("Digite o número da opção desejada: "))
    if opçao_de_submenu == 1:
        a = {}
        aux = {}
        codigo = int(input("Digite o codigo: "))
        nome = input("Digite o nome: ")
        tipo_de_exebiçao = input("Digite o tipo de exibição: ")
        acessivel = input("É acessível?: ")
        aux ['Nome'] = nome
        aux ['tipo de exebiçao'] = tipo_de_exebiçao
        aux ['acessivel'] = acessivel
        a [codigo] = aux
    return a
    if opçao_de_submenu == 2:
        a = {}
        aux = {}
        codigo = int(input("Digite o codigo: "))
        nome = input("Digite o nome: ")
        tipo_de_exebiçao = input("Digite o tipo de exibição: ")
        acessivel = input("É acessível?: ")
        aux ['Nome'] = nome
        aux ['tipo de exebiçao'] = tipo_de_exebiçao
        aux ['acessivel'] = acessivel
        a [codigo] = aux
    return a
        
        
        
            
        
        
        
        
        


def opçoes ():
    opçao_de_menu = int(input(" Digite uma das opções acima (digite o número) :"))
    if opçao_de_menu == 1:
        print ("Submenu de salas")
        menu_de_opçoes_de_submenus ()
        sala = submenu_de_salas ()
        print (sala)
    if opçao_de_menu == 2:
        submenu_de_filmes ()
        print ("Submenu de filmes")
        menu_de_opçoes_de_submenus ()
    if opçao_de_menu == 3:
        print ("Submenu de sessões")
        menu_de_opçoes_de_submenus ()
    if opçao_de_menu == 4:
        print ("Sair")
    


# Menu Principal
menu_de_opçoes ()
opçoes ()

    
    
