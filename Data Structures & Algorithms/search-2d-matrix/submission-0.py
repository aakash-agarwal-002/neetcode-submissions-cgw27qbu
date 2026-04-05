class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows,columns = len(matrix), len(matrix[0])

        l = 0
        r = rows-1

        while l<=r:
            midr = (l+r)//2

            if matrix[midr][0] <= target <= matrix[midr][-1]:
                lc = 0
                rc = columns-1

                while lc<=rc:
                    midc = (lc+rc)//2
                    if matrix[midr][midc] == target:
                        return True
                    elif matrix[midr][midc] > target:
                        rc = midc-1
                    else:
                        lc = midc+1

                return False
            elif matrix[midr][0] > target:
                r = midr-1
            
            else:
                l = midr+1

        return False
