var getMaxGridHappiness = function(m,n,introvertsCount,extrovertsCount) {
 if(n>m)[m,n]=[n,m]; const pow=3**n, top=3**(n-1), pair=[[0,0,0],[0,-60,-10],[0,-10,40]], memo=new Map();
 function dfs(pos,a,b,mask){ if(pos===m*n || (!a&&!b))return 0; const key=(((pos*7+a)*7+b)*pow+mask); if(memo.has(key))return memo.get(key); let next=mask*3%pow, up=Math.floor(mask/top), left=pos%n?mask%3:0; let best=dfs(pos+1,a,b,next); if(a)best=Math.max(best,120+pair[1][up]+pair[1][left]+dfs(pos+1,a-1,b,next+1)); if(b)best=Math.max(best,40+pair[2][up]+pair[2][left]+dfs(pos+1,a,b-1,next+2)); memo.set(key,best); return best; }
 return dfs(0,introvertsCount,extrovertsCount,0);
};