var decrypt = function(code, k) {
 const n=code.length, ans=Array(n).fill(0);
 for(let i=0;i<n;i++) for(let j=1;j<=Math.abs(k);j++) ans[i]+=code[(i+(k>0?j:-j)+n)%n];
 return ans;
};