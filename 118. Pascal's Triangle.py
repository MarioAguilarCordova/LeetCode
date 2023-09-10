class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # list to store triangle
        triangle = []
        
        # add first row which is always 1
        triangle.append([1])
        
        # run for loop for numRows - 1
        for i in range(numRows - 1):
            # list to store row with 1 as 1st element is always 1
            new = [1]
            for j in range(0,i):
                # run for loop to add 2 numbers of previous rows
                new.append(triangle[i][j] + triangle[i][j + 1])
            # add last element of row
            new.append(1)
            # add row in a triangle
            triangle.append(new)
            
        return triangle
        
        