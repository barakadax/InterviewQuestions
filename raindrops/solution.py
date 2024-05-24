import random

class unit_count:
    def __init__(self, min_value: float, max_value: float) -> None:
        self.min: float = min_value
        self.max: float = max_value
        self.filled_lower: float = max_value
        self.filled_upper: float = min_value
    

    def get_is_full(self) -> bool:
        return self.filled_lower <= self.min and self.filled_upper >= self.max
    

class axis:
    def __init__(self, size: float) -> None:
        self.__size: float = size


    def __get_meter(self) -> dict[int, unit_count]:
        units_dict = {}

        for i in range (0, int(self.__size)):
            units_dict[i] = unit_count(float(i), i + 1.0)

        return units_dict


    def __get_raindrop(self) -> float:
        return random.uniform(0, self.__size)
    

    def __upper(self, units_dict: dict[int, unit_count], point: float) -> None:
        upper = point + 0.5

        if int(point) in units_dict and units_dict[int(point)].filled_upper < upper:
            units_dict[int(point)].filled_upper = upper
        
        if int(upper) > int(point) and int(upper) in units_dict and units_dict[int(upper)].min < upper:
            units_dict[int(upper)].min = upper
            if units_dict[int(upper)].get_is_full():
                del units_dict[int(upper)]


    def __lower(self, units_dict: dict[int, unit_count], point: float) -> None:
        lower = point - 0.5

        if int(point) in units_dict and units_dict[int(point)].filled_lower > lower:
            units_dict[int(point)].filled_lower = lower

        if int(lower) < int(point) and int(lower) in units_dict and units_dict[int(lower)].max > lower:
            units_dict[int(lower)].max = lower
            if units_dict[int(lower)].get_is_full():
                del units_dict[int(lower)]


    def run(self) -> int:
        counter = 0
        units_dict = self.__get_meter()

        while bool(units_dict):
            counter -= -1
            point = self.__get_raindrop()
            self.__upper(units_dict, point)
            self.__lower(units_dict, point)

            if int(point) in units_dict and units_dict[int(point)].get_is_full():
                del units_dict[int(point)]

        return counter


if __name__ == '__main__':
    x = axis(5.0)
    res = x.run()
    print(res)
