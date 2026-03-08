import random

# Time O(N) | Space O(N)
class SidewalkSimulation:
    def __init__(self, size: float):
        self.size = size

    def run(self) -> int:
        gaps: list[list[float]] = [[0.0, self.size]]
        drops: int = 0

        while gaps:
            drops += 1
            center: float = random.uniform(0, self.size)
            drop_start: float = max(0.0, center - 0.5)
            drop_end: float = min(self.size, center + 0.5)

            new_gaps: list[list[float]] = []
            for g_start, g_end in gaps:
                if drop_start < g_end and drop_end > g_start:
                    if drop_start > g_start:
                        new_gaps.append([g_start, drop_start])
                    if drop_end < g_end:
                        new_gaps.append([drop_end, g_end])
                else:
                    new_gaps.append([g_start, g_end])
            gaps = new_gaps

        return drops

sim: SidewalkSimulation = SidewalkSimulation(5.0)
print(sim.run())
