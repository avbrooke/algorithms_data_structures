class PouleSheet:
    def __init__(self, number, size):
        self._number = number
        self._size = size
        self._competitors = [None] * size
        self._results = [[None] * size for _ in range(size)]

    def add_competitor(self, name):
        if name in self._competitors or name is None:
            return False
        else:
            for i in range(self._size):
                if self._competitors[i] is None:
                    self._competitors[i] = name
                    return True
                else:
                    return False

    def record_bout(self, fencer1, fencer2, h1, h2):
        self._results[fencer1][fencer2] = h1
        self._results[fencer2][fencer1] = h2

    def get_winners(self):
        if any(cell is None for row in self._results for cell in row):
            return None
        victories = [0] * self._size
        hit_difference = [0] * self._size
        total_hits = [0] * self._size

        for x in range(self._size):
            for y in range(self._size):
                if self._results[x][y] is not None:
                    if self._results[x][y] > self._results[y][x]:
                        victories[x] += 1
                    total_hits[x] += self._results[x][y] if self._results[x][y] is not None else 0
                    total_hits[y] += self._results[y][x] if self._results[y][x] is not None else 0

        for x in range(self._size):
            hit_difference[x] = total_hits[x] - sum(self._results[x])

        competitors = list(range(self._size))
        competitors.sort(key=lambda x: (victories[x], hit_difference[x], total_hits[x]), reverse=True)
        max_victories = victories[competitors[0]]
        winners = {self._competitors[x] for x in competitors if victories[x] == max_victories}

        return winners




