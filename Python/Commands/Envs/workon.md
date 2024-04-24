Instale o pip, o virtualenv e o virtualenvwrapper com os comandos abaixo:

    sudo apt-get install python3-pip
    sudo pip3 install --upgrade pip
    sudo pip3 install virtualenv virtualenvwrapper

Instale o vim: 

    sudo apt-get install vim

Para configurar o VirtualEnvWrapper, abra o arquivo /home/usuario/.bashrc:

    vim /home/lucas/.bashrc

Inclua o conteúdo abaixo no final do arquivo:

    # Python Virtualenvs 
    export WORKON_HOME=/home/usuario/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6 (verificar versao)
    source /usr/local/bin/virtualenvwrapper.sh 
    export PIP_REQUIRE_VIRTUALENV=true  

WORKON_HOME define o local onde ficarão seus envs.
VIRTUALENVWRAPPER_PYTHON define a versão padrão do Python usada na criação dos envs.
PIP_REQUIRE_VIRTUALENV impede que instalação de pacotes fora de um virtualenv.


Feito isso, reinicie o terminal. 
O VirtualEnvWrapper irá gerar os scripts dentro da pasta ~/.virtualenvs.
Para criar o virtualenv use o comando:

    mkvirtualenv projeto

Para fazer o virtualenv direcionar para a pasta do projeto quando for ativado, edite o arquivo postactivate:
Cole o comando para direcionar para a pasta do projeto que foi clonado do Git:

    cd /home/usuario/projetos/projeto

Salve e feche o arquivo.
Para acessar o virtualenv use o comando:
    workon projeto



Para utilizar com zsh:

    sudo vim ~/.zshrc

Copia o conteudo que vc adicionou em vim /home/lucas/.bashrc
e reinicia os terminais