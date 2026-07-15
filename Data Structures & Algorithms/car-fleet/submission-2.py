class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        s = []
        for i in range(len(position)):
            rem = (target - position[i]) / speed[i]
            cars.append((position[i], speed[i], rem))
        
        cars.sort(key=lambda x: x[0], reverse=True)
        print(cars)
        for p, sp, r in cars:
            if s and s[-1] >= r:
                print(s)
                continue
            s.append(r)
        
        print(s)


        return len(s)