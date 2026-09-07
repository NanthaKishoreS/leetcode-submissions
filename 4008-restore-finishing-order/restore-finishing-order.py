class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # 1. Manually build a lookup table (hash set) using a standard loop
        friends_set = set()
        for friend in friends:
            friends_set.add(friend)
            
        # 2. Initialize an empty array for the results
        result = []
        
        # 3. Use an explicit index loop to find matching participants
        for i in range(len(order)):
            current_racer = order[i]
            
            # Check if current racer is in our friends lookup table
            if current_racer in friends_set:
                result.append(current_racer)
                
        return result
