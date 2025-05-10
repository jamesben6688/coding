import heapq

class RentalRecord:
    def __init__(self, id, pick, ret):
        self.id = id
        self.pick = pick
        self.ret = ret

def assign_cars(records):
    # 按 pick time 排序
    records.sort(key=lambda r: r.pick)

    heap = []  # [(return_time, car_id)]
    car_id_counter = 0
    assignment = {}

    for r in records:
        if heap and heap[0][0] <= r.pick:
            # 可复用车辆
            ret_time, car_id = heapq.heappop(heap)
        else:
            # 分配新车
            car_id = car_id_counter
            car_id_counter += 1

        assignment[r.id] = car_id
        heapq.heappush(heap, (r.ret, car_id))

    return car_id_counter, assignment


records = [
    RentalRecord('A', 1, 4),
    RentalRecord('B', 2, 5),
    RentalRecord('C', 6, 7),
    RentalRecord('D', 3, 6),
    RentalRecord('E', 8, 9)
]

cars_needed, assignments = assign_cars(records)

print("Min cars needed:", cars_needed)
print("Assignments:")
for rid in sorted(assignments):
    print(f"Record {rid} → Car {assignments[rid]}")
