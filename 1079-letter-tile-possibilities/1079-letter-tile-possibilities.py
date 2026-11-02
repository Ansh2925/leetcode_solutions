class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        used = [False] * len(tiles)
        def backtrack(subset):
            count = 0
            for i in range(len(tiles)):
                
                if used[i]:
                    continue

                if i > 0 and tiles[i] == tiles[i-1] and not used[i-1]:
                    continue
                subset.append(tiles[i])
                used[i] = True

                count += 1

                count += backtrack(subset)

                subset.pop()

                used[i] = False

            return count

        return backtrack([])