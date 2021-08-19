#include<stdio.h>
char brd[]= {49,50,51,52,53,54,55,56,57};
int mv=0;
void board()
{
    printf("    ============================\n");
    printf("            MAN  VS  A.I.\n");
    printf("    ============================\n\n");
    printf("         |   |   |   |\n");
    printf("         | %c | %c | %c |\n",brd[0],brd[1],brd[2]);
    printf("         |   |   |   |\n");
    printf("         ×---×---×---×\n");
    printf("         |   |   |   |\n");
    printf("         | %c | %c | %c |\n",brd[3],brd[4],brd[5]);
    printf("         |   |   |   |\n");
    printf("         ×---×---×---×\n");
    printf("         |   |   |   |\n");
    printf("         | %c | %c | %c |\n",brd[6],brd[7],brd[8]);
    printf("         |   |   |   |\n\n");
}
int iswin(char le,char ar[])
{
    int cr,h,v;
    cr= ar[0]==le && ar[4]==le && ar[8]==le || ar[2]==le && ar[4]==le && ar[6]==le;
    h= ar[0]==le && ar[1]==le && ar[2]==le || ar[3]==le && ar[4]==le && ar[5]==le || ar[6]==le && ar[7]==le && ar[8]==le ;
    v= ar[0]==le && ar[3]==le && ar[6]==le || ar[1]==le && ar[4]==le && ar[7]==le || ar[2]==le && ar[5]==le && ar[8]==le ;
    return (cr||h||v);

}
int draw()
{
    int i,j;
    for(i=0; i<9; i++)
    {
        if(brd[i]!='X'&& brd[i]!='O')
            return 0;
    }
    return 1;
}
int cheak(char le)
{
    if(iswin(le,brd))
        return 1;
    return 0;
}
void player()
{
    int p;
st:
    printf("position 1-9: ");
    scanf("%d",&p);
    if(brd[p-1]!='X'&& brd[p-1]!='O')
        brd[p-1]='X';
    else
    {
        printf("Already  filled:\n");
        goto st;
    }
}
void cmp()
{
    int bestscore=-1000,score,move,k,i;
    for(i=0; i<=8; i++)
    {
        if(brd[i]!='X'&& brd[i]!='O')
        {
            k=brd[i];
            brd[i]='O';
            score=minimax(brd,0);
            brd[i]=k;
            if(score>bestscore)
            {
                move=i;
                bestscore=score;
            }
        }
    }
    brd[move]='O';
}

int minimax(char cb[],int max)
{
    int i,bestscore,score,k;
    if(iswin('O',cb))
        return 100;
    if(iswin('X',cb))
        return -100;
    if(draw())
        return 0;
    if(max)
    {
        bestscore=-1000;
        for(i=0; i<=8; i++)
        {
            if(cb[i]!='X'&& cb[i]!='O')
            {
                k=cb[i];
                cb[i]='O';
                score=minimax(cb,0);
                cb[i]=k;
                if(score>bestscore)
                    bestscore=score;
            }
        }
        return bestscore;

    }
    else
    {
        bestscore=800;
        for(i=0; i<=8; i++)
        {
            if(brd[i]!='X'&& brd[i]!='O')
            {
                k=cb[i];
                cb[i]='X';
                score=minimax(cb,1);
                cb[i]=k;
                if(score<bestscore)
                    bestscore=score;
            }
        }
        return bestscore;

    }
}

int main()
{
    int run=0,rn;
    while(!run)
    {
        board();
        player();
        board();
        rn=cheak('X');
        if(rn==1)
        {
            printf("player win");
            return 1;
        }
        if(draw())
        {
            printf("draw");
            return 1;
        }

        cmp();
        rn=cheak('O');
        if(rn==1)
        {
            printf("A.I. win");
            return 1;
        }
        if(draw())
        {
            printf("draw");
            return 1;
        }


    }
    return 0;
}
