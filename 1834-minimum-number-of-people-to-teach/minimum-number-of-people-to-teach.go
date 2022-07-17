func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
 m:=len(languages); known:=make([][]bool,m)
 for i,ls:=range languages { known[i]=make([]bool,n+1); for _,x:=range ls {known[i][x]=true} }
 bad:=make([]bool,m)
 for _,f:=range friendships {a,b:=f[0]-1,f[1]-1; common:=false; for _,x:=range languages[a] {if known[b][x] {common=true;break}}; if !common {bad[a]=true;bad[b]=true}}
 count:=0; freq:=make([]int,n+1); best:=0
 for i,v:=range bad {if v {count++;for _,x:=range languages[i] {freq[x]++;if freq[x]>best {best=freq[x]}}}}
 return count-best
}