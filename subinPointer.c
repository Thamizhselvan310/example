#include<stdio.h>
#include<conio.h>
void main()
{
 int *p1,*p2,a,b,sub;

 printf("\n Enter Any Two Numbers To Subtract : ");
 scanf("%d%d",&a,&b);

 p1=&a;
 p2=&b;

 sub = *p1 - *p2;

 printf("\n Subtraction = %d",sub);
}
