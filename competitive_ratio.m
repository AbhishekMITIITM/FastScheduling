% Rate of growth of competitive ratio for N users

T=10^4;


N=20;



ratio=ones(1,N);

for n=2:N
    
h_MA= ones(1,n);
h_OPT=ones(1,n);
MA_cost=0;
OPT_cost=0;
NExpt=20;
   
for k=1:NExpt
   
for t=1:T
    channel=zeros(1,N);
   act_channel=randsample(N,1); 
   channel(act_channel)=1;
   % Simulating the MA policy
   [max_val, schedUE]=max(h_MA);
   h_MA=h_MA+1;
   if(channel(schedUE)==1)
       h_MA(schedUE)=1;
   end
   MA_cost=MA_cost+sum(h_MA);
   
   %Simulating the OPT policy
   h_OPT=h_OPT+1;
   h_OPT(act_channel)=1;
   
   OPT_cost=OPT_cost+sum(h_OPT);
   
end
ratio(n)=max(ratio(n), MA_cost/OPT_cost);
end
end
plot(ratio(2:N))
hold on
lb=(1:N)/2;
plot(lb)


