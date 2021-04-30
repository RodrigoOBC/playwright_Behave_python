#language: pt

Funcionalidade: Pesquisar no Google
  Sou um usuario e quero fazer uma pesquisa no google


  Cenario: Pesquisar "Facebook" no google
    Dado que estou na pagina inicial do google
    Quando O usuario digita "Facebook" na caixa de pesquisa e aperta ENTER
    Entao resultados relacionados ao "Facebook" são exibidos