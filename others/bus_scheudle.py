def latest_arrival(shuttles, capacity, arrivals):
    arrivals.sort()
    idx = 0  # pointer to next waiting passenger

    for i, shuttle_time in enumerate(shuttles):
        count = 0
        # simulate boarding for this shuttle
        while idx < len(arrivals) and arrivals[idx] <= shuttle_time and count < capacity:
            idx += 1
            count += 1

        # For the last shuttle, decide the latest time
        if i == len(shuttles) - 1:
            if count < capacity:
                return shuttle_time
            else:
                # The last person who got on this shuttle
                return arrivals[idx - 1] - 1
