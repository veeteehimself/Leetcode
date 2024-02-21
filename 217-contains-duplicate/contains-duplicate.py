class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict={} # intialize the dictionary
        for element in nums :
            if element in nums_dict :
                return True
            else :
                nums_dict[element]=1
        return False
