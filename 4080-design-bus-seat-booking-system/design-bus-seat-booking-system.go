import "strconv"

type BusBooking struct {
    costs []int
    total int
    booked int
}

func Constructor(n int) BusBooking {
    return BusBooking{costs: make([]int, 4*n)}
}

func (b *BusBooking) Toggle(seat string) {
    row, _ := strconv.Atoi(seat[1:])
    letter := int(seat[0]-'A')
    position := 4*(row-1) + letter
    if b.costs[position] != 0 {
        b.total -= b.costs[position]
        b.costs[position] = 0
        b.booked--
        return
    }
    cost := 1
    if (letter == 0 || letter == 3) && b.costs[4*(row-1) + (letter^1)] != 0 {
        cost = 3
    }
    // Store the cost when booked. Later seat toggles never change it.
    b.costs[position] = cost
    b.total += cost
    b.booked++
}

func (b *BusBooking) GetTotalTime() int { return b.total }

func (b *BusBooking) GetMinTime() int {
    // Booking all window seats first avoids every additional delay.
    return b.booked
}