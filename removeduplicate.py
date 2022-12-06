from operator import index


def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous_num = 0
        index_value = 0
        unique_value = 0

        for i, num in enumerate(nums):
            if i == 0:
                unique_value += 1
                previous_num = num
                index_value += 1
            
            elif previous_num < num:
                nums[index_value] = num
                previous_num = num
                index_value += 1
                unique_value += 1

        return unique_value, nums

        # numOfUniques = 0
        # replacementIndex = 0
        # prevNumber = 0
        
        # for i,num in enumerate(nums):
        #     if i == 0:
        #         replacementIndex += 1 
        #         numOfUniques += 1
        #         prevNumber = num
        #     elif prevNumber < num:
        #         nums[replacementIndex] = num
        #         replacementIndex += 1
        #         numOfUniques += 1
        #         prevNumber = num
                
        # return numOfUniques
    
                
nums = [1,1,2]

print(removeDuplicates(nums))
# print("----------------------")
# print("Expected Output: 2, nums = [0,1,2,3,4,_,_,_,_,_]")
