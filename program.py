nome = input ('Digite seu nome aqui: ')
idade = int (input('Digite sua idade aqui: '))

if (idade < 18) : {
    print ('Você não tem permissão para acessar este conteudo')
}
elif (idade >= 18) : {
    print ('Seja muito Bem-Vindo' , nome + '!')
}
