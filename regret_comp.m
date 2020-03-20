% Computing regret with non-additive costs

No_Expt=100;
T=1000;
regret_sum=zeros(1,T);
for expt=1:No_Expt
    ch1=binornd(1,0.5,1,T);
    ch2=1-ch1;
    h1=ones(1,T);
    h2=ones(1,T);
    regret=zeros(1,T);
    best_AoI=ones(1,T);
    for t=1:T-1
        % computing the best AoI with fixed policy
        if(ch1(t+1)==1)
            h1(t+1)=1;
        else
            h1(t+1)=h1(t)+1;
        end
        
        if(ch2(t+1)==1)
            h2(t+1)=1;
        else
            h2(t+1)=h2(t)+1;
        end
        best_AoI(t)=min(sum(h1(1:t)), sum(h2(1:t)));
        
    end
    
    h1=ones(1,T);
    h2=ones(1,T);
    avg_AoI=ones(1,T);
    for t=1:T-1
       % computing the performance in terms of Avg_AoI for max-age policy
       [max_val, ind]= max([sum(h1(1:t)), sum(h2(1:t))]);
       %[max_val, ind]=max([h1(t), h2(t)]);
       if(ind==1)
          h2(t+1)=h2(t)+1;
          if(ch1(t+1)==1)
              h1(t+1)=1;
          else
              h1(t+1)=h1(t)+1;
          end
           
       end
       
       
       if(ind==2)
          h1(t+1)=h1(t)+1;
          if(ch2(t+1)==1)
              h2(t+1)=1;
          else
              h2(t+1)=h2(t)+1;
          end
           
       end
       h_sum=h1+h2;
       avg_AoI(t)= sum(h_sum(1:t))/2;
       
    end
    regret=avg_AoI-best_AoI;
    regret_sum=regret_sum+regret;
    
end

regret=regret_sum/No_Expt;


