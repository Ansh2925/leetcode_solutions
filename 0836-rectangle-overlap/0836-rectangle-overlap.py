class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left1_x = rec1[0]
        left1_y = rec1[1]
        right1_x = rec1[2]
        right1_y = rec1[3]

        left2_x = rec2[0]
        left2_y = rec2[1]
        right2_x = rec2[2]
        right2_y = rec2[3]

        if left2_x >= right1_x: return False
        if left1_x >= right2_x: return False
        
        if left2_y >= right1_y: return False
        if left1_y >= right2_y: return False

        return True
