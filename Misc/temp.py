def breakPalindrome(palindromeStr):
    
    # counts string score
    def countScore(string):
        total = 0
        for letter in string:
            total += ord(letter)
        return total
    
    # find if its a pallindrome 
    def isPallindrome(string):
        return string[::-1] == string
        
    # first
    iniScore = countScore(palindromeStr)
    curMin = iniScore    
    minStr = palindromeStr
    
    # convert to numbers
    numList = [ord(l) for l in palindromeStr]
    max_values = sorted(set(numList))
    max_values = max_values[::-1]
    print(max_values)
    tmp = numList.copy()
    
    def convert2String(inList):
        string = ''.join(chr(i) for i in inList)
        return string
    
    # if only a
    if max_values[0] == 97:
        return 'IMPOSSIBLE'
    
    for max_value in max_values:
        print(max_value)
        for idx, value in enumerate(numList):
            if value == max_value:
                for newVal in range(97,ord('z') + 1):
                    tmp = numList.copy()
                    tmp[idx] = newVal
                    if isPallindrome(tmp):
                        continue
                    else:
                        return convert2String(tmp)
        
    return 'IMPOSSIBLE'


print(breakPalindrome('acca')) # aaca