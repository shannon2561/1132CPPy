class BankAccount:
    def __init__(self, account_id, initial_balance):
        self.account_id = account_id
        self.balance = initial_balance
        self.is_closed = False

    def deposit(self, amount):
        # TODO: Add the amount to the balance
        self.balance+=amount

    def withdraw(self, amount):
        # TODO: Check if the balance is sufficient and subtract the amount
        self.balance-=amount

    def apply_interest(self,current_year,current_month,year,month):
        # TODO: Add 1% interest to the balance (truncate to integer)
        while year>current_year or (year==current_year and month>current_month):
            self.balance=int(self.balance*1.01)
            current_month+=1    
            if current_month>12:
                current_month=1
                current_year+=1
        return current_year,current_month

    def close(self):
        # TODO: Mark the account as closed
        self.is_closed=True

    def is_active(self):
        # TODO: Return whether the account is still active
        return not self.is_closed
        # ==
        # if self.is_closed==True:
        #     return False
        # else:
        #     return True

    def get_balance(self):
        # TODO: Return the current balance
        return self.balance

#--------------------------------------------------------------------------
#Functions

def transfer(from_account:BankAccount,to_account:BankAccount,amount:int):      #type hint
    from_account.withdraw(amount)
    to_account.deposit(amount)

def open_accounts(account,amount):
    if account not in Accounts:
        Accounts[account]=BankAccount(account,amount)
    return Accounts[account]

# def acc_active(acc_id):
#     return acc_id in Accounts and Accounts[acc_id].is_active()

#------------------------------------------------------------------------
#ErrorMsg

class DuplicateAccountError(Exception):
    def __str__(self):      #是Python特別用來定義「這個物件變成字串時要印什麼」的函式
        return "Account ID already exists"

class AccountNotFoundError(Exception):
    def __str__(self):
        return "Account not found"

class InvalidAmountError(Exception):
    def __str__(self):
        return "Invalid transaction amount"
    
class InsufficientBalanceError(Exception):
    def __str__(self):
        return "Insufficient balance"

#----------------------------------------------------------------------
#Main Code

if __name__ == "__main__":
    Accounts={}
    FirstData=True
    Last_Interest={}

    while True:
        Input=input()
        if Input=="q":
            break
        
        #input
        List_Data=Input.split(" ")      #[2023-11-30,OPEN,P1,1000]
        Date=List_Data[0].split("-")      #[2023,11,30]
        Operation=List_Data[1]
        Year=int(Date[0])
        Month=int(Date[1])

        if FirstData==True:
            Current_Year=int(Date[0])
            Current_Month=int(Date[1])
            FirstData=False
        
        for Acc_ID,Acc in Accounts.items():
            if Acc.is_active(): 
                Last_Year,Last_Month=Last_Interest.get(Acc_ID,(Current_Year,Current_Month))
                New_Year,New_Month=Acc.apply_interest(Last_Year,Last_Month,Year,Month)
                Last_Interest[Acc_ID]=(New_Year,New_Month)

        Current_Year=Year
        Current_Month=Month

        if Operation=="OPEN":
            Account=List_Data[2]
            Amount_str=(List_Data[3])
            try:
                #帳戶已存在
                if Account in Accounts:
                    raise DuplicateAccountError()
                #金額不是整數或為負數
                try:
                    Amount=int(Amount_str)
                    if Amount<0:
                        raise InvalidAmountError()
                except ValueError:
                    raise InvalidAmountError()
                
                s=open_accounts(Account,Amount)

            except (DuplicateAccountError,InvalidAmountError) as ErrorMsg:
                print(ErrorMsg)
                continue

        elif Operation in ["DEPOSIT","WITHDRAW"]:
            Account=List_Data[2]
            Amount_str=List_Data[3]

            if Operation=="DEPOSIT":
                try:
                    #帳戶不存在或已關閉
                    if Account not in Accounts:
                        raise AccountNotFoundError()
                    s=Accounts[Account]
                    if s.is_active()==False:
                        raise AccountNotFoundError()
                    
                    #金額不是整數或為負數
                    try:
                        Amount=int(Amount_str)
                        if Amount<0:
                            raise InvalidAmountError()
                    except ValueError:
                        raise InvalidAmountError()

                    s.deposit(Amount)

                except (AccountNotFoundError,InvalidAmountError) as ErrorMsg:
                    print(ErrorMsg)
                    continue
            
            if Operation=="WITHDRAW":
                try:
                    #帳戶不存在或已關閉
                    if Account not in Accounts:
                        raise AccountNotFoundError()
                    s=Accounts[Account]
                    if s.is_active()==False:
                        raise AccountNotFoundError()
                    
                    #金額不是整數或為負數
                    try:
                        Amount=int(Amount_str)
                        if Amount<0:
                            raise InvalidAmountError()
                        #餘額不足
                        if Amount>s.get_balance():
                            raise InsufficientBalanceError()
                    except ValueError:
                        raise InvalidAmountError()
                    
                    s.withdraw(Amount)

                except (AccountNotFoundError,InvalidAmountError,InsufficientBalanceError) as ErrorMsg:
                    print(ErrorMsg)
                    continue
                
        elif Operation=="TRANSFER":
            From_Account=List_Data[2]
            To_Account=List_Data[3]
            Amount_str=(List_Data[4])

            try:
                #From，To帳戶不存在
                Invalid_Count=0

                #From帳戶不存在
                if From_Account not in Accounts:
                    Invalid_Count+=1
                else:
                    s=Accounts[From_Account]
                    if s.is_active()==False:
                        Invalid_Count+=1

                #To帳戶不存在
                if To_Account not in Accounts:
                    Invalid_Count+=1
                else:
                    s=Accounts[To_Account]
                    if s.is_active()==False:
                        Invalid_Count+=1

                if Invalid_Count==2:
                    print("Account not found")
                    print("Account not found")
                    continue
                if Invalid_Count==1:
                    raise AccountNotFoundError()
                
                
                #金額不是整數或為負數
                try:
                    Amount=int(Amount_str)
                    if Amount<0:
                        raise InvalidAmountError()
                    #From帳戶餘額不足
                    s=Accounts[From_Account]
                    if Amount>s.get_balance():
                        raise InsufficientBalanceError()
                except ValueError:
                    raise InvalidAmountError()

                transfer(Accounts[From_Account],Accounts[To_Account],Amount)
            
            except (AccountNotFoundError,InvalidAmountError,InsufficientBalanceError) as ErrorMsg:
                print(ErrorMsg)
                continue
        


        elif Operation=="BALANCE":
            Account=List_Data[2]
            try:
                #帳戶不存在或已關閉
                if Account not in Accounts:
                    raise AccountNotFoundError()
                s=Accounts[Account]
                if s.is_active()==False:
                    raise AccountNotFoundError()
            
                print(Account,s.get_balance())

            except AccountNotFoundError as ErrorMsg:
                print(ErrorMsg)
                continue

        
        elif Operation=="CLOSE":
            Account=List_Data[2]
            try:
                #帳戶不存在或已關閉
                if Account not in Accounts:
                    raise AccountNotFoundError()
                s=Accounts[Account]
                if s.is_active()==False:
                    raise AccountNotFoundError()
            
                s.close()

            except AccountNotFoundError as ErrorMsg:
                print(ErrorMsg)
                continue





#---------------------------------------------------------------------

# | 錯誤情況編號 | 觸發情境             | 建議 Exception 類別名稱          | 對應錯誤訊息                       | 優先順序   | 補充說明                           |
# | ------ | ---------------- | -------------------------- | ---------------------------- | ------ | ------------------------------ |
# | ❶      | **帳戶 ID 重複開戶**   | `DuplicateAccountError`    | `Account ID already exists`  | 第 1 順位 | OPEN 指令時帳號已存在                  |
# | ❷      | **帳戶不存在或已關閉**    | `AccountNotFoundError`     | `Account not found`          | 第 2 順位 | 所有操作都需檢查                       |
# | ❸      | **轉帳雙方帳戶有任一不存在** | 兩次 `AccountNotFoundError`  | `Account not found` ×2       | 第 3 順位 | 若兩個都不存在，要印兩次                   |
# | ❹      | **金額為負或非整數**     | `InvalidAmountError`       | `Invalid transaction amount` | 第 4 順位 | 所有金額輸入需檢查                      |
# | ❺      | **餘額不足提款/轉帳**    | `InsufficientBalanceError` | `Insufficient balance`       | 第 5 順位 | 檢查 `withdraw()` / `transfer()` |



#-------------------------------------------------------------------

# 我現在還沒做錯誤訊息指正，但想先試試看如果全部是正確訊息跑不跑得動。
# 這是原本的範例input：
# 2023-11-30 OPEN P1 1000
# 2023-12-01 WITHDRAW P1 800
# 2023-12-01 BALANCE P1
# 2023-12-15 TRANSFER P1 P2 500
# 2023-12-15 DEPOSIT P1 200
# 2023-12-15 BALANCE P1
# q
# 範例output：
# P1 210
# Account not found
# P1 410
# 請幫我用這種格式給我一個沒有錯誤版本的讓我跑看看



#-----------------------------------------------------------
#可以跑

# class BankAccount:
#     def __init__(self, account_id, initial_balance):
#         self.account_id = account_id
#         self.balance = initial_balance
#         self.is_closed = False

#     def deposit(self, amount):
#         # TODO: Add the amount to the balance
#         self.balance+=amount

#     def withdraw(self, amount):
#         # TODO: Check if the balance is sufficient and subtract the amount
#         self.balance-=amount

#     def apply_interest(self,current_year,current_month,year,month):
#         # TODO: Add 1% interest to the balance (truncate to integer)
#         while year>current_year or (year==current_year and month>current_month):
#             self.balance=int(self.balance*1.01)
#             current_month+=1    
#             if current_month>12:
#                 current_month=1
#                 current_year+=1
#         return current_year,current_month

#     def close(self):
#         # TODO: Mark the account as closed
#         self.is_closed=True

#     def is_active(self):
#         # TODO: Return whether the account is still active
#         return not self.is_closed
#         # ==
#         # if self.is_closed==True:
#         #     return False
#         # else:
#         #     return True

#     def get_balance(self):
#         # TODO: Return the current balance
#         return self.balance

# #--------------------------------------------------------------------------
# #Functions

# def transfer(from_account:BankAccount,to_account:BankAccount,amount:int):      #type hint
#     from_account.withdraw(amount)
#     to_account.deposit(amount)

# def open_accounts(account,amount):
#     if account not in Accounts:
#         Accounts[account]=BankAccount(account,amount)
#     return Accounts[account]

# # def acc_active(acc_id):
# #     return acc_id in Accounts and Accounts[acc_id].is_active()

# #------------------------------------------------------------------------
# #ErrorMsg

# class DuplicateAccountError(Exception):
#     pass

# class AccountNotFoundError(Exception):
#     pass

# class InvalidAmountError(Exception):
#     pass

# class InsufficientBalanceError(Exception):
#     pass

# #----------------------------------------------------------------------
# #Main Code

# if __name__ == "__main__":
#     Accounts={}
#     FirstData=True
#     Last_Interest={}

#     while True:
#         Input=input()
#         if Input=="q":
#             break
        
#         #input
#         List_Data=Input.split(" ")      #[2023-11-30,OPEN,P1,1000]
#         Date=List_Data[0].split("-")      #[2023,11,30]
#         Operation=List_Data[1]
#         Year=int(Date[0])
#         Month=int(Date[1])

#         if FirstData==True:
#             Current_Year=int(Date[0])
#             Current_Month=int(Date[1])
#             FirstData=False
        
#         for Acc_ID,Acc in Accounts.items():
#             if Acc.is_active(): 
#                 Last_Year,Last_Month=Last_Interest.get(Acc_ID,(Current_Year,Current_Month))
#                 New_Year,New_Month=Acc.apply_interest(Last_Year,Last_Month,Year,Month)
#                 Last_Interest[Acc_ID]=(New_Year,New_Month)

#         Current_Year=Year
#         Current_Month=Month

#         if Operation=="OPEN":
#             Account = List_Data[2]
#             Amount = int(List_Data[3])
#             s=open_accounts(Account,Amount)
#             #s.is_active=True
#             #s=Accounts[Account]

#         elif Operation in ["DEPOSIT","WITHDRAW"]:
#             Account=List_Data[2]
#             Amount=int(List_Data[3])
#             #if Account in Accounts:   #
#             s=Accounts[Account]
#             #s=BankAccount(Account,Amount)

#             if Operation=="DEPOSIT":
#                 s.deposit(Amount)

#             if Operation=="WITHDRAW":
#                 s.withdraw(Amount)
                
#         elif Operation=="TRANSFER":
#             From_Account=List_Data[2]
#             To_Account=List_Data[3]
#             Amount=int(List_Data[4])
#             transfer(Accounts[From_Account],Accounts[To_Account],Amount)
#             # Accounts[From_Account]=Accounts[From_Account]
#             # Accounts[To_Account]=Accounts[To_Account]

#         elif Operation=="BALANCE":
#             Account=List_Data[2]
#             s=Accounts[Account]
#             print(Account,s.get_balance())
#             # if acc_active(Account):
#             #     print(Account,s.get_balance())
        
#         elif Operation=="CLOSE":
#             Account=List_Data[2]
#             s=Accounts[Account]
#             s.close()
            
#             # Accounts[Account]=s   #



#-------------------------------------------------

# while True:
#     List_Data=input().split(" ")
#     Operation=List_Data[1]
#     Date=List_Data[0].split("-")

    # if Date[2]=="01":
    #     for Month in range(1,13):
    #         if Monthly_Interest==False:
    #             s.apply_interest
    #             Monthly_Interest=True
    