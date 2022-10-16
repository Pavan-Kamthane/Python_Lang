# validate an array is subsequence of other array
def validateSubsequence(mainArray,seqArray):
     check=0
     for ele in mainArray:
         if(seqArray[check]==ele):
             check+=1
             if (check==len(seqArray)):
                 break
     return check==len(seqArray)
respose = validateSubsequence([3,1,2],[2,1])
print(respose)
