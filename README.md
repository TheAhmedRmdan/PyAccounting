# PyAccounting

PyAccounting is a Python library for managing accounting-related tasks and calculations. It provides a set of classes and methods that can be used to handle various financial aspects, such as assets, liabilities, income statements, trial balances, and more.

## Features

- **Account:** The `account` module contains classes and methods for managing individual accounts, such as assets, liabilities, and owner's equity.
- **Financial Position:** The `financial_position` module provides functionality to calculate the financial position of a business by combining the balances of assets, liabilities, and owner's equity.
- **Income Statement:** The `income_statement` module allows users to generate income statements, summarizing revenues, expenses, and net income.
- **Journal Entry:** The `journal_entry` module enables recording and managing journal entries, which are used to track and record financial transactions.
- **Trial Balance:** The `trial_balance` module facilitates the creation and management of trial balances, which verify the accuracy of accounting records by comparing debits and credits.

## Installation

To use PyAccounting, you need to have Python 3.x installed. 

```shell
git clone https://github.com/AhmedRmdan/PyAccounting.git
```

## Usage
The user interface is coming soon.

Here's a simple example demonstrating the usage of PyAccounting classes (in code, not UI):

```python
# Create a new asset account
cash = Asset(name='Cash',5000)

# Record a transaction
cash.debit(1000, 'Initial deposit')

# Print the account balance
print(cash.get_balance())  # Output: 6000
```

For more detailed documentation and examples, please refer to the [Documentation](https://github.com/AhmedRmdan/PyAccounting/wiki) provided.

## Contributing

Contributions to PyAccounting are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the [GitHub repository](https://github.com/AhmedRmdan/PyAccounting).

## License

PyAccounting is licensed under the [MIT License](https://github.com/AhmedRmdan/PyAccounting/blob/main/LICENSE). Feel free to use, modify, and distribute this library as per the terms of the license.

## Credits

PyAccounting is developed and maintained by [@TheAhmedRmdan](https://github.com/TheAhmedRmdan). 

We hope you find PyAccounting useful for your accounting learning! If you have any questions or need further assistance, please don't hesitate to reach out.

Happy accounting!
