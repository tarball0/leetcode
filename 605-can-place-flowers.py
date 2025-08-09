class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        plantable = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            if len(flowerbed) == 1:
                return True

            if i == 0 and flowerbed[i+1] == 0:
                plantable += 1
                flowerbed[i] = 1
            elif i == (len(flowerbed) - 1) and flowerbed[i-1] == 0:
                plantable += 1
                flowerbed[i] = 1
            elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                plantable += 1
                flowerbed[i] = 1
            else:
                continue

        print(plantable)
        if plantable >= n:
            return True
        else:
            return False
