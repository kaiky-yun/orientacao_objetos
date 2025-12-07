#!/bin/bash
VENV_PATH="./venv"
PYTHON_EXEC="$VENV_PATH/bin/python"
RUN_FILE="run.py"
PORT=8000

if [ ! -d "$VENV_PATH" ]; then
    echo "Erro: Ambiente virtual '$VENV_PATH' não encontrado."
    echo "Por favor, crie-o com 'python3 -m venv venv' e instale as dependências."
    exit 1
fi

if [ ! -f "$PYTHON_EXEC" ]; then
    echo "Erro: Executável Python do venv não encontrado em $PYTHON_EXEC."
    echo "Certifique-se de que o venv está criado corretamente."
    exit 1
fi

echo "Iniciando servidor Flask/SocketIO na porta $PORT em background..."
nohup $PYTHON_EXEC $RUN_FILE > server.log 2>&1 &

echo $! > flask_server.pid

echo "Servidor iniciado com PID: $!"
