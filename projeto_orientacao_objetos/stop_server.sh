#!/bin/bash
# Script para parar qualquer serviço rodando na porta 8000

PORT=8000

echo "Procurando processos rodando na porta $PORT..."

# Encontra o PID do processo que está usando a porta 8000
PID=$(lsof -t -i :$PORT)

if [ -z "$PID" ]; then
    echo "Nenhum processo encontrado rodando na porta $PORT."
else
    echo "Processo(s) encontrado(s) com PID(s): $PID"
    echo "Encerrando processo(s)..."
    # Mata o processo
    kill -9 $PID
    echo "Processo(s) encerrado(s) com sucesso."
fi
