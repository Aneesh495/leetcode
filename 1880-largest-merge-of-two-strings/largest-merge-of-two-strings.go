func largestMerge(word1 string, word2 string) string {
 ans:=make([]byte,0,len(word1)+len(word2));i,j:=0,0
 for i<len(word1) && j<len(word2) {if word1[i:]>word2[j:] {ans=append(ans,word1[i]);i++} else {ans=append(ans,word2[j]);j++}}
 ans=append(ans,word1[i:]...);ans=append(ans,word2[j:]...);return string(ans)
}