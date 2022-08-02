func minCharacters(a string, b string) int {
 var ca,cb [26]int
 for _,c:=range a {ca[c-'a']++}; for _,c:=range b {cb[c-'a']++}
 best:=len(a)+len(b); pa,pb:=0,0
 for i:=0;i<26;i++ {
  same:=len(a)+len(b)-ca[i]-cb[i]; if same<best {best=same}
  pa+=ca[i]; pb+=cb[i]
  if i<25 {x:=len(a)-pa+pb; y:=len(b)-pb+pa; if x<best {best=x};if y<best {best=y}}
 }
 return best
}