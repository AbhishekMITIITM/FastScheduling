% Computing regret with non-additive costs

%No_Expt=1000;
T=10000;
M=100; % Number of probability values
No_Expt=200;
%CR=linspace(0.001,0.002,M);
pmin=0.001;
pmax=1-pmin;
CR=linspace(pmin,pmax,M);
tight=linspace(pmin,pmax,M);

for k=1:M
    p=CR(k);
    LB=0.5*(1/sqrt(p)+1/sqrt(1-p))^2;
    best_AoI=0;
    MA_AoI=0;
for expt=1:No_Expt
    ch1=binornd(1,p,1,T);
    ch2=1-ch1;
    h1=zeros(1,T);
    h2=zeros(1,T);
    m1=zeros(1,T); % Age for MA policy
    m2=zeros(1,T); 
    
    for t=1:T-1
        % computing the best AoI for OPT
        if(ch1(t+1)==1)
            h1(t+1)=1;
            h2(t+1)=h2(t)+1;
        else
            h1(t+1)=h1(t)+1;
            h2(t+1)=1;
        end
        
        % computing ages for MW
        if (p*m1(t)^2>(1-p)*m2(t)^2)
        %if (m1(t)>m2(t))
           if(ch1(t+1)==1)
               m1(t+1)=1;
               m2(t+1)=m2(t)+1;
           else
               m1(t+1)=m1(t)+1;
               m2(t+1)=m2(t)+1;
           end
        else
            if(ch2(t+1)==1)
                m2(t+1)=1;
                m1(t+1)=m1(t)+1;
            else
                m2(t+1)=m2(t)+1;
                m1(t+1)=m1(t)+1;
            end
        end
        
    end
    best_AoI=best_AoI+(sum(h1)+sum(h2))/T;
    MA_AoI= MA_AoI+ (sum(m1)+sum(m2))/T;
end
    
    best_AoI=best_AoI/No_Expt;
    MA_AoI= MA_AoI/No_Expt;
    
    CR(k)=LB/best_AoI;
    tight(k)= MA_AoI/LB;
%end
end

%plot(CR)
plot(tight)

