#include<stdio.h>
 
void main()
{
    int i,j,n,burst_t[40],p[40],waiting_t[40],turn_around_t[40],total=0,pos,temp;
    float avg_waitingt,avg_turnaroundt;
    printf("Enter number of process:");
    scanf("%d",&n);
 
    printf("\nEnter Burst Time:\n");
    for(i=0;i<n;i++)
    {
        printf("p%d:",i+1);
        scanf("%d",&burst_t[i]);
        p[i]=i+1;         
    }
 
   
    for(i=0;i<n;i++)
    {
        pos=i;
        for(j=i+1;j<n;j++)
        {
            if(burst_t[j]<burst_t[pos])
                pos=j;
        }
 
        temp=burst_t[i];
        burst_t[i]=burst_t[pos];
        burst_t[pos]=temp;
 
        temp=p[i];
        p[i]=p[pos];
        p[pos]=temp;
    }
 
    waiting_t[0]=0;      
 
   
    for(i=1;i<n;i++)
    {
        waiting_t[i]=0;
        for(j=0;j<i;j++)
            waiting_t[i]+=burst_t[j];
 
        total+=waiting_t[i];
    }
 
    avg_waitingt=(float)total/n;      
 
    printf("\nProcess\t    Burst Time    \tWaiting Time\tTurnaround Time");
    for(i=0;i<n;i++)
    {
        turn_around_t[i]=burst_t[i]+waiting_t[i];     
        total+=turn_around_t[i];
        printf("\np%d\t\t  %d\t\t    %d\t\t\t%d",p[i],burst_t[i],waiting_t[i],turn_around_t[i]);
    }
 
    avg_turnaroundt=(float)total/n;    
    printf("\n\nAverage Waiting Time=%f",avg_waitingt);
    printf("\nAverage Turnaround Time=%f\n",avg_turnaroundt);
}
