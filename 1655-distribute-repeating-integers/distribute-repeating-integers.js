var canDistribute = function(nums, quantity) {
 const f=new Map(); for(const x of nums) f.set(x,(f.get(x)||0)+1);
 const counts=[...f.values()].sort((a,b)=>b-a).slice(0,quantity.length), N=1<<quantity.length, sums=Array(N).fill(0);
 for(let mask=1;mask<N;mask++){let bit=mask&-mask; sums[mask]=sums[mask^bit]+quantity[Math.log2(bit)];}
 let dp=Array(N).fill(false); dp[0]=true;
 for(const c of counts){let next=dp.slice(); for(let mask=0;mask<N;mask++) if(dp[mask]) {let rem=(N-1)^mask; for(let s=rem;s;s=(s-1)&rem) if(sums[s]<=c) next[mask|s]=true;} dp=next; if(dp[N-1]) return true;} return false;
};