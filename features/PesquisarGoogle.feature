#language: pt

Funcionalidade: Pesquisar no Google
  Sou um usuario e quero fazer uma pesquisa no google


  Cenario: Pesquisar "Amazon" no google
    Dado que estou na pagina inicial do google
    Quando O usuario digita "Amazon" na caixa de pesquisa e aperta ENTER
    Entao resultados relacionados ao "Amazon" são exibidos


  Cenario: Pesquisar "Livro" na Amazon
    Dado estou na pagina principal da amazon
    Quando O usuario digita "Livro" na caixa de pesquisa e aperta ENTER
    Entao livros vendidos são exibidos