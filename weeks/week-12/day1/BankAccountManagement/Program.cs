using System;
using System.Runtime.InteropServices.Marshalling;
using System.Security.Cryptography.X509Certificates;

public enum AccoutTypeModel
{
    Saving,
    Checking,
    Business
}

public class BankAccount
{

    // fields
    private int _accoutNumber;
    private string _ownerName;
    private double _balance;
    private AccoutTypeModel _accountType;
    private bool _isActic;
    private List<string> _transactionHistory = [];
    private const double _interestForSavingAccounts = 1.02;

    // Properties
    public int AccountNumber { get => _accoutNumber; }
    public string OwnerName
    {
        get => _ownerName;
        set
        {
            if (string.IsNullOrWhiteSpace(value)) _ownerName = "UnKnown";
            else _ownerName = value;
        }
    }

    public double Balance
    {
        get => _balance;
        set
        {
            if (value < 0) _balance = 0;
            else _balance = value;
        }
    }

    public string AccountType
    {
        get => _accountType.ToString();
        set
        {
            AccoutTypeModel type;
            if (!Enum.TryParse(value, ignoreCase: true, out type) || !Enum.IsDefined(type)) _accountType = AccoutTypeModel.Checking;
            else _accountType = type;
        }
    }

    public bool IsActive { get => _isActic; private set { _isActic = value; } }

    // constructors

    public BankAccount(int accountNumber, string ownerName, double balance, string accountType)
    {
        _accoutNumber = accountNumber;
        OwnerName = ownerName;
        Balance = balance;
        AccountType = accountType;
        IsActive = true;

    }

    public BankAccount(int accountNumber, string ownerName) :
        this(accountNumber, ownerName, 0.0, "Checking")
    { }

    public BankAccount(int accountNumber, string ownerName, double initialDeposit) :
        this(accountNumber, ownerName, initialDeposit, "Checking")
    { }

    //methods

    public override string ToString()
    {
        return $"Account #{AccountNumber} | Owner: {OwnerName} | Balance: ${Balance} | Type: {AccountType}";
    }

    public void Deposit(double amount)
    {
        if (!IsActive)
        {
            Console.WriteLine($"Error: {AccountNumber} => Inactive");
        }
        else if (amount > 0)
        {
            Balance += amount;
            _transactionHistory.Add($"Depositing ${amount} to account #{AccountNumber}");
        }
    }

    public bool Withdraw(double amount)
    {
        if (!IsActive) { Console.WriteLine($"Error: {AccountNumber} => Inactive"); return false; }
        if (amount < 0) { Console.WriteLine("Error: withdrow must be positive "); return false; }
        if (amount < Balance) { Console.WriteLine("Error: withdrow must be higher then balance."); return false; }
        Balance -= amount;
        _transactionHistory.Add($"Withdrawing ${amount} from account #{AccountNumber}");
        return true;
    }
    public void ApplyInterest()
    {
        if (_accountType == AccoutTypeModel.Saving) Balance *= _interestForSavingAccounts;
    }
    public void PrintTransactionHistory()
    {
        Console.WriteLine(string.Join("\n", _transactionHistory));
    }

    public void Activate() { IsActive = true; }

    public void Deativate() { IsActive = false; }

    public static bool Transfer(BankAccount from, BankAccount to, double amount)
    {
        if (!from.IsActive) { Console.WriteLine("Error: source account inactive."); return false; }
        if (amount < 0) { Console.WriteLine("Error: amount must be positive"); return false; }
        
        if (!from.Withdraw(amount)) return false;

        to.Deposit(amount);
        return true;
    
    }


    




}

class Projrem()
{
    static void Main()
    {
        List<BankAccount> accounts = new();

        accounts.Add(new BankAccount(1, "Liri"));
        accounts.Add(new BankAccount(2, "David", 1500));
        accounts.Add(new BankAccount(3, "Mery", 5000, "saving"));
        accounts.Add(new BankAccount(4, "Mara", 1600, "bla bala"));
        accounts.Add(new BankAccount(5, "", -800, "business"));

        Console.WriteLine(string.Join("\n", accounts));

        accounts[0].Withdraw(500);
        accounts[1].Withdraw(800);
        accounts[2].Deposit(400);

        foreach (BankAccount account in accounts) {Console.WriteLine($"account {account.AccountNumber}"); account.PrintTransactionHistory();Console.WriteLine($"status: {account.ToString()}"); }
        Console.WriteLine(string.Join("\n", accounts));



    }

}
