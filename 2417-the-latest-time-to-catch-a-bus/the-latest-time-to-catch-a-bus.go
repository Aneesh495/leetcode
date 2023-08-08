import "sort"

func latestTimeCatchTheBus(buses []int, passengers []int, capacity int) int {
    sort.Ints(buses)
    sort.Ints(passengers)
    boarded := 0
    lastBusCount := 0
    for _, departure := range buses {
        count := 0
        for boarded < len(passengers) && count < capacity && passengers[boarded] <= departure {
            boarded++
            count++
        }
        lastBusCount = count
    }
    latest := buses[len(buses)-1]
    if lastBusCount == capacity {
        latest = passengers[boarded-1] - 1
    }
    occupied := make(map[int]bool, len(passengers))
    for _, arrival := range passengers { occupied[arrival] = true }
    for occupied[latest] { latest-- }
    return latest
}