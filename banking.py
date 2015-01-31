#Banking Module - needed by Bank Accounts

class BankAccount:
	def __init__(self):
		self.balance = float(0)
	
	def deposit(self, depositAmount):
		self.balance = float(self.balance + depositAmount)

	def withdraw(self, withdrawAmount):
		if self.balance >= withdrawAmount:
			self.balance = float(self.balance - withdrawAmount)
		else:
			print("Insufficient funds! Please withdraw a smaller amount or make a deposit")

	def transfer(self, transferAmount, transferAccount):
		if self.balance >= transferAmount:
			self.balance = float(self.balance - transferAmount)
			transferAccount.balance = float(transferAccount.balance + transferAmount)
		else:
			print("Insufficient funds! Please transfer a smaller amount or make a deposit")

