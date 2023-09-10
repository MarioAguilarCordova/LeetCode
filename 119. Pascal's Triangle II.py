class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
       
        if rowIndex == 0:
            return [1]
    
        # list to store triangle
        triangle = []
        
        # Initialize first row since pascals always starts with 1
        triangle.append([1])
        
        # run for loop for rowIndex
        for i in range(rowIndex):
            # make new list to get values then append to pascal triangle list
            new = [1]
            for j in range(0,i):
                # Run for loop to add 2 numbers to previous rows
                new.append(triangle[i][j] + triangle[i][j + 1])
            # add last element of row
            new.append(1)
            # add row to triangle list
            triangle.append(new)
            # Get rowIndex from pascals triangle
            print(i)
            if i + 1 == rowIndex:
                return triangle[rowIndex]
                
        