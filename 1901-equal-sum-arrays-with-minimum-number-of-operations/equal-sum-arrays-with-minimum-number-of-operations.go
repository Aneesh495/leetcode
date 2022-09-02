func minOperations(nums1 []int, nums2 []int) int {
 a,b:=0,0;for _,x:=range nums1 {a+=x};for _,x:=range nums2 {b+=x};if a>b {a,b=b,a;nums1,nums2=nums2,nums1};diff:=b-a;var gain [6]int
 for _,x:=range nums1 {gain[6-x]++};for _,x:=range nums2 {gain[x-1]++}
 ops:=0;for d:=5;d>=1 && diff>0;d-- {for gain[d]>0 && diff>0 {gain[d]--;diff-=d;ops++}};if diff>0{return -1};return ops
}