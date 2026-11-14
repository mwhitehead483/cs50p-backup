class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be greater than or equal to 0")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n
        print(f"\n[Deposit {n}] Current jar: {self}") # <-- Prints contents

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies to withdraw")
        self._size -= n
        print(f"\n[Withdraw {n}] Current jar: {self}") # <-- Prints contents

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    print("--- Starting Manual Jar Test ---")

    # Initialize jar
    jar = Jar(5)  # initialize capacity to 5
    print(f"Initial jar capacity: {jar.capacity}, size: {jar.size}")

    # Test deposits
    jar.deposit(3)
    jar.deposit(2)  #  total

    # Test withdrawals
    jar.withdraw(1)
    jar.withdraw(3)  #  total now 1
    jar.deposit(2)  # total 5 again
    jar.withdraw(2)

    print("--- Manual Test Complete ---")

if __name__ == "__main__":
    main()
