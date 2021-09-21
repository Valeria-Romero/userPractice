from User import User

markAccount = User("Mark Simmons", 100)
lilyAccount = User("Lily Addams", 250)
oscarAccount = User("Oscar Martinez", 123)


# Have the first user make 3 deposits and 1 withdrawal and then display their balance
markAccount.deposit(156)
markAccount.deposit(223)
markAccount.deposit(150)

markAccount.make_withdrawal(285)

markAccount.display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance
lilyAccount.deposit(1600)
lilyAccount.deposit(235)

lilyAccount.make_withdrawal(150)
lilyAccount.make_withdrawal(80)

lilyAccount.display_user_balance()

#Have the third user make 1 deposits and 3 withdrawals and then display their balance
oscarAccount.deposit(2500)

oscarAccount.make_withdrawal(135)
oscarAccount.make_withdrawal(58)
oscarAccount.make_withdrawal(650)

oscarAccount.display_user_balance()

#Have the first user transfer money to the third user and then print both users' balances
markAccount.transfer_money(10,oscarAccount)