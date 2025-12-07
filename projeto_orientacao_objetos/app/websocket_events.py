from flask import session
from flask_socketio import join_room
from .services import FinanceService
from .repositories import JSONStorage, TransactionRepository
from config import Config
transactions_storage = JSONStorage(Config.TRANSACTIONS_DB_PATH)
transaction_repository = TransactionRepository(transactions_storage)
finance_service = FinanceService(transaction_repository)
def register_websocket_events(socketio):
    @socketio.on('connect')
    def handle_connect():
        if 'user_id' in session:
            user_id = session['user_id']
            join_room(user_id)
            finance_service._emit_balance_update(user_id)
