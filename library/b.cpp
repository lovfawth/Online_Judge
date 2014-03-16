//20131012  codejam1
#include<cstdio>
#include<string>

const long maxn=1000+1;

long a[maxn+1][maxn+1],i,i1,i2,i3,t,n,flag[maxn+1];


void init(){
     freopen("A-large.in","r",stdin);
     freopen("out.txt","w",stdout);
     }


long judge(){
     long i1,i2,i3,i4;
     
     for (i1=1;i1<=n*n;i1++){
         memset(flag,0,sizeof(flag));
         for (i2=1;i2<=n*n;i2++){
             if (flag[a[i1][i2]])
                return 0;
             if (a[i1][i2]>n*n)
                return 0;
             flag[a[i1][i2]]=1;
             }
         }
     
     for (i1=1;i1<=n*n;i1++){
         memset(flag,0,sizeof(flag));
         for (i2=1;i2<=n*n;i2++){
             if (flag[a[i2][i1]])return 0;
             if (a[i2][i1]>n*n)return 0;
             flag[a[i2][i1]]=1;
             }
         }
         
     for (i1=1;i1<=n;i1++)
         for (i2=1;i2<=n;i2++){
             memset(flag,0,sizeof(flag));
             for (i3=n*(i1-1)+1;i3<=i1*n;i3++)
                 for (i4=n*(i2-1)+1;i4<=i2*n;i4++){
                     if (flag[a[i3][i4]])return 0;
                     if (a[i3][i4]>n*n)return 0;
                     flag[a[i3][i4]]=1;
                     }
             }
     return 1;
     }


main(){
       init();
       scanf("%ld",&t);
       for (i=1;i<=t;i++){
           scanf("%ld",&n);
           for (i1=1;i1<=n*n;i1++)
               for (i2=1;i2<=n*n;i2++)
                   scanf("%ld",&a[i1][i2]);
           if (judge()) printf("Case #%ld: Yes\n",i);
              else printf("Case #%ld: No\n",i);
           }
       return (0);
}
