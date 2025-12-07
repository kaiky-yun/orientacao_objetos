from flask import Blueprint, render_template, session

from app.repositories import JSONStorage, TransactionRepository
from app.services import FinanceService
from config import Config
from .auth_controller import login_required
dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')
transactions_storage = JSONStorage(Config.TRANSACTIONS_DB_PATH)
transaction_repository = TransactionRepository(transactions_storage)
finance_service = FinanceService(transaction_repository)
@dashboard_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    user_id = session.get('user_id')
    balance = finance_service.get_balance(user_id)
    return render_template('dashboard.html', balance=balance)

