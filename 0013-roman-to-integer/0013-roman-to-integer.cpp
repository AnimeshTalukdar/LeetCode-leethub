class Solution {
public:
    int romanToInt(string s) {
        int l = s.length();
        int sum=0;
        for(int i=0;i<l;i++)
        {
            if(s[i]=='M')
            {
                sum+=1000;
            }
            else if(s[i]=='D')
            {
                if(s[i+1]=='M')
                {
                    sum-=500;
                }
                else
                    sum+=500;
            }
            else if(s[i]=='C')
            {                
                if(s[i+1]=='D'||s[i+1]=='M')
                {
                    sum-=100;
                }
                else
                    sum+=100;
                
            }
            else if(s[i]=='L')
            {                
                if(s[i+1]=='C'||s[i+1]=='D'||s[i+1]=='M')
                {
                    sum-=50;
                }
                else
                    sum+=50;
                
            }
            
            else if(s[i]=='X')
            {                
                if(s[i+1]=='L'||s[i+1]=='C'||s[i+1]=='D'||s[i+1]=='M')
                {
                    sum-=10;
                }
                else
                    sum+=10;
                
            }
            
            else if(s[i]=='V')
            {                
                if(s[i+1]=='X'||s[i+1]=='L'||s[i+1]=='C'||s[i+1]=='D'||s[i+1]=='M')
                {
                    sum-=5;
                }
                else
                    sum+=5;
                
            }
            
            else if(s[i]=='I')
            {                
                if(s[i+1]=='V'||s[i+1]=='X'||s[i+1]=='L'||s[i+1]=='C'||s[i+1]=='D'||s[i+1]=='M')
                {
                    sum-=1;
                }
                else
                    sum+=1;
                
            }
            
            
        }
        return sum;
    }
};