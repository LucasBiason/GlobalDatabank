** Pré requisitos do pyenv:

    sudo apt-get update

    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git

** Instalação do pyenv:

    curl https://pyenv.run | bash

Cole o conteúdo abaixo no final do arquivo '~/.bashrc' ou '~/.zshrc'

    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

** Utilize o comando abaixo para verificar se o seu pyenv esta com todos os pacotes corretos enão tem que instalar alguma dependencia extra:
    
    pyenv doctor

** Para consulta a versão de Python desejada:

    pyenv install -list

** Instale a versão de Python desejada:

    pyenv install X.X.X

** Clone o Projeto deseja e dentro da pasta dele, utilize a versão desejada:

    pyenv shell  X.X.X


** Você pode verificar a versão configurada com:
    pyenv versions

** Criação do ambiente virtual:
    virtualenv .venv
    source .venv/bin/activate


** Notas:

Para facilitar a utilização, você pode criar alias:

    alias workon_PROJETO='cd /path/to/project  && source ./path/to/venv/bin/activate && clear'


** Pyenv + Virtualenv:

Criar:

    pyenv virtualenv 3.5.7 <<nome do ambiente>>

Ativar:

    pyenv activate <<nome do ambiente>>

Desativar

    pyenv deactivate