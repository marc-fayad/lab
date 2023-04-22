class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up account object.
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to deposit money to account.
        :param amount: Amount of money to add
        :return: Boolean value based on success of deposit
        """
        if amount > 0:
            self.__account_balance += amount
            return True

        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to withdraw money from account.
        :param amount: Amount of money to remove
        :return: Boolean value based on success of withdrawal
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True

        else:
            return False

    def get_balance(self) -> float:
        """
        Function to return account balance.
        :return: Amount of money in account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to return account name.
        :return: Name of account
        """
        return self.__account_name
