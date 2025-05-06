class Solution:
    def removeDuplicateHouses(self, neighborhoods, colors):
        # Get the total number of neighborhoods
        m = len(neighborhoods)
        # Get the total number of houses in a neighborhood
        n = len(neighborhoods[0])

        # List to store houses in sorted order
        sorted_list = []

        # For each neighborhood in neighborhoods
        for neighborhood in range(m):
            # For each house in the neighborhood
            for house in range(n):
                # Push houses to sorted_list along with colors
                sorted_list.append((neighborhoods[neighborhood][house], colors[neighborhood][house]))

        # Sort the list by house number
        sorted_list.sort()

        # List of lists to store the answer
        ans = [[] for _ in range(m)]

        # For each neighborhood
        for neighborhood in range(m):
            # For each house in neighborhood
            for house in range(n):
                # Update the answer by assigning the house and its color
                ans[house].append(sorted_list[neighborhood * n + house])

        return ans

# Helper function to print the answer
def printer(neighborhoods):
    for neighborhood in neighborhoods:
        for house in neighborhood:
            # Print the House No and House Color
            print(f"{house[0]}{house[1]}", end=" ")
        print()

# Main code to test
if __name__ == "__main__":
    # All houses are painted with colors
    neighborhoods = [[8, 2, 9], [4, 6, 4], [4, 5, 1]]
    colors = [['r', 'g', 'b'], ['w', 'c', 'b'], ['x', 'y', 'b']]

    # Create the Solution object
    s = Solution()

    # Call the removeDuplicateHouses function and store the answer
    ans = s.removeDuplicateHouses(neighborhoods, colors)

    # Call the helper to print the answer
    printer(ans)
