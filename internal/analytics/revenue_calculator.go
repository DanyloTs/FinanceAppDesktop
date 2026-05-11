package analytics

// Transaction represents a single financial transaction.
type Transaction struct {
    ID     string
    Amount float64
}

// RevenueCalculator computes revenue from a list of transactions.
type RevenueCalculator struct{}

// New returns a new RevenueCalculator.
func New() *RevenueCalculator {
    return &RevenueCalculator{}
}

// Calculate sums the Amount fields of all provided transactions.
func (r *RevenueCalculator) Calculate(txs []Transaction) float64 {
    total := 0.0
    for _, t := range txs {
        total += t.Amount
    }
    return total
}
