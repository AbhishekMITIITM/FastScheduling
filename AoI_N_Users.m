%N user case

clc;
clear all;
%close all;

block_size=2;
no_of_blocks=100;

N=5; %no of users
no_good_channels=1;
ratio_max=0;

%T=block_size*no_of_blocks;
T=1000;
ratio_sum=zeros(1,T);

No_Expt=10;

for expt=1:No_Expt
    
    channels=zeros(N,T);
    %channels(1,:)=binornd(1,0.5,1,T);
    %channels(2,:)=1-channels(1,:);
    for t=1:T
        channels(randperm(N,no_good_channels),t)=1;
    end
    
    h_opt=ones(N,T);
    h_algo=ones(N,T);
    best_AoI=ones(1,T);
    avg_AoI=ones(1,T);
    
    for t=1:T-1
        
        %optimal policy
        h_opt(:,t+1)=h_opt(:,t)+1;
        pos=find(channels(:,t+1)==1); %assuming there is only 1 good channel
        h_opt(pos,t+1)=1;
        
        %max_wt policy
        [max_val,ind]=max(h_algo(:,t));
        h_algo(:,t+1)=h_algo(:,t)+1;
        if(channels(ind,t+1)==1)
            h_algo(ind,t+1)=1;
        end
        
        best_AoI(t)=sum(h_opt(:,1:t))/N;
        avg_AoI(t)=sum(h_algo(:,1:t))/N;
        
    end
    
    best_AoI(T)=sum(h_opt(:,1:T))/N;
    avg_AoI(T)=sum(h_algo(:,1:T))/N;
    
    ratio=avg_AoI./best_AoI;
    ratio_max=max(ratio_max, ratio);
end

%ratio_avg=ratio_sum/No_Expt;

ratio_max




