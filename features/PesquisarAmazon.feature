#language: pt

Funcionalidade: Pesquisar no Google
  Sou um usuario e quero fazer uma pesquisa no google


  Cenario: Pesquisar "Amazon" no google
    Dado que acesso a pagina do google
    Quando pesquiso por "Amazon"
    Entao resultados relacionados ao "Amazon" são exibidos


  Cenario: Pesquisar "Livro" na Amazon
    Dado que acesso a pagina principal da amazon
    Quando pesquiso "Livro" na Amazon
    Entao livros vendidos são exibidos