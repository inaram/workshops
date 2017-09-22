def banking():
    balance = 0
    totalDeposits = 0
    totalWithdrawals = 0
    print("Welcome to your personal banking.")
    transactionType = input("If this is a deposit, enter d. If this is a withdrawal, enter w: ")
    amount = int(input("How much? "))
    if transactionType == "d":
        totalDeposits = totalDeposits + amount
        balance = balance + amount
    elif transactionType == "w":
        totalWithdrawals = totalWithdrawals + amount
        balance = balance - amount
    else:
        print("Sorry, you have entered non-existing transaction type")

    print("Your current balance is", balance)
    print("Your total deposits so far: %d. Your total withdrawals so far: %d." % ( totalDeposits, totalWithdrawals))

def main():
    banking()

if __name__ == "__main__":
	main()
	
