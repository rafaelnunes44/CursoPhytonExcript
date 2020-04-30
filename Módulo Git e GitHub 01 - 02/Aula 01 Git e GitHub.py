
#===========================================================================================================
""" GIT E GITHUB COMO USAR EM MEU PROJETO?
Blog
https://haylson.com.br/como-usar-o-git-e-o-github/

Video Aula Git e GitHub
https://www.youtube.com/watch?v=aEGkYK6AVRg
https://www.youtube.com/watch?v=SOxafinthys&t=535s
"""
#===========================================================================================================
""" Instalação do GIT e usando o GitBash 
 
GIT >> Software de Versionamento
GitBash >>Propmt de comando do GIT

Fazer download - https://git-scm.com/downloads

"""
#===========================================================================================================
""" Git Bash
-------Configuracao Inicial
git --version
git config --global user.name "seu nome aqui"



-------

Apos localizar a pasta do projeto - Criar um repositorio local 
git init

Verificar Arquivos
git status

Gerenciar todos arquivos
git add .

git commit -m "aqui adicionar uma mensagem"


-------

"""
#===========================================================================================================

"""GitHub - Software que hospeda o projeto e compartilha

* Criar uma conta no - https://github.com/ 
* Escolher o plano free


Passo 1 ao 3 para criar chave 
1.Digitar o comando no Git Bash
ssh-keygen -t rsa -b 4096 -C "rafaelnunes44@gmail.com"
2.Verificar se está rodando!!! 
eval "$(ssh-agent -s)"
3.Identificar
ssh-add .ssh/id_rsa

Copiar Chave
4. 
clip < .ssh/id_rsa.pub

5. Logar no site github (e adicionar chave com control+V)

6. Conectar no hitHub
ssh -T git@github.com

"""
#===========================================================================================================