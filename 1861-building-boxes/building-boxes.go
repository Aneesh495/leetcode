func minimumBoxes(n int) int {
 floor, total, layer:=0,0,0
 for { next:=layer+1; nf:=floor+next; if total+nf>n {break}; layer=next;floor=nf;total+=floor }
 extra:=0
 for total<n {extra++; floor++; total+=extra}
 return floor
}