import os
from typing import List
import pyodbc, struct
from azure.identity import DefaultAzureCredential
from app.logging.logging_factory import LoggingFactory
from app.domain.cashtransaction import CashTransaction

connection_string = os.environ["AZURE_SQL_CONNECTIONSTRING"]
class CashRepository():


    def __init__(self, loggingFactory: LoggingFactory) -> None:
        self.loggingFactory = loggingFactory

    
    
    def get_cash(self) -> List[CashTransaction]:
        
        cashTransactions = List[CashTransaction]
        self.loggingFactory.logger.info("Getting relevant cash from database")
        with self.get_conn() as conn:
            cursor = conn.cursor()
            result = cursor.execute("exec usp_GetCashTransactions")
            
            for row in result:
                cashTransaction = CashTransaction()
                cashTransaction.transactionId = row.TransactionId
                cashTransaction.transactionAmount = row.TransactionAmount
                cashTransaction.transactionName = row.TransactionName
                cashTransactions.append(cashTransaction)
                
        return cashTransactions
        
    def get_conn():
        credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
        token_bytes = credential.get_token("https://database.windows.net/.default").token.encode("UTF-16-LE")
        token_struct = struct.pack(f'<I{len(token_bytes)}s', len(token_bytes), token_bytes)
        SQL_COPT_SS_ACCESS_TOKEN = 1256  # This connection option is defined by microsoft in msodbcsql.h
        conn = pyodbc.connect(connection_string, attrs_before={SQL_COPT_SS_ACCESS_TOKEN: token_struct})
        return conn