class LoanCalculator:
    def __init__(self, principal, annual_rate, years):
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
    
    def monthly_payment(self):
        monthly_rate = self.annual_rate / 100 / 12
        num_payments = self.years * 12
        
        if monthly_rate == 0:
            return self.principal / num_payments
        
        payment = self.principal * (monthly_rate * (1 + monthly_rate) ** num_payments) / \
                  ((1 + monthly_rate) ** num_payments - 1)
        return payment
    
    def total_interest(self):
        return (self.monthly_payment() * self.years * 12) - self.principal


# Example usage
loan = LoanCalculator(principal=200000, annual_rate=5.5, years=30)
print(f"Monthly Payment: ${loan.monthly_payment():.2f}")
print(f"Total Interest: ${loan.total_interest():.2f}")