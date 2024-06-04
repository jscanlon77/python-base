from typing import List
from app.logging.logging_factory import BaseService
from app.repositories.cash_repository import CashRepository
from app.domain.cashtransaction import CashTransaction

class CashService(BaseService):

    def __init__(self, cashrepository: CashRepository) -> None:
        self.cashRepository = cashrepository
        super().__init__()

    def get_cash(self) -> List[CashTransaction]:
        self.logger.info("Getting relevant cash from database")
        return self.cashRepository.get_cash()
        # returns whatever it needs to