#import data
with open('input6.txt', 'r') as input:
    data = input.read()

characters = list(data)

#function to show all characters (be careful, too many characters)
def DisplayChars():
    for character in characters:
        print(characters)

#test if all characters is different the others
def TestChars(i, n):
    for j in range(i, i + n):
        for k in range(j + 1, i + n):
            if characters[j] == characters[k]:
                return False
    return True
            
#find the marker after the 'n' different characters.
def FindMarker(n):
    for i in range(len(characters)-n):
        if TestChars(i, n):
            print('\nThe marker for a', n,'characters is: ', i + n, '\n')
            break
                    
# ---- part 1 ----
FindMarker(4)

# ---- part 2 ----
FindMarker(14)