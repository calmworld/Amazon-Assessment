def countDecreasingRatings(ratings):
    if not ratings:
        return 0
    count = 0
    currentSubseqLength = 0
    currentSubseqTail = float('-inf')
    for rating in ratings:
        if rating < currentSubseqTail: # Does decreasing include "=="?
            currentSubseqTail = rating
            currentSubseqLength += 1
        else:
            # You're starting a new subsequence at this spot
            count += (currentSubseqLength * (currentSubseqLength + 1) // 2)
            currentSubseqTail = rating
            currentSubseqLength = 1
    count += (currentSubseqLength * (currentSubseqLength + 1 ) // 2)
    return count

def test():
    ratings = [2, 1, 3]
    result = countDecreasingRatings(ratings)
    expected = 4
    print(result, result == expected)
test()
