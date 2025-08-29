def saudacao(nome, cidade):
    if cidade.lower() == "rio de janeiro":
        print(f"{nome}, Seja Bem-vindo à Cidade Maravilhosa!")
    else:
        print(f"{nome}, você está em {cidade}.")

nome = input('Digite seu nome: ')
cidade = input('Digite a cidade de onde vc está falando: ')

saudacao(nome, cidade)