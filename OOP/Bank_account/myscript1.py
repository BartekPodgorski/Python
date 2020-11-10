from bank_account import MinimumBalanceAccount


accountMin = MinimumBalanceAccount(1500)

result = accountMin.try_withdraw(300)

if(result.is_ok()):
    print(result.message)
