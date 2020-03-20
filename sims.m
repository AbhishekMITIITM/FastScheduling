% Simulation Script to Simulate different scheduling policies
% N denotes the number of users

N=10;
T=10^6;
%p=rand(N,1);
p=ones(N,1)*(1/N);
% m denotes the number of policies 
m=1;
H=zeros(m,T);
H_avg=zeros(m,T);

% Simulating the max-age policy
%---------------------------------------------------------
h=ones(N,1);

sum_age=0;

for t=1:T
    [val, ind]=max(h);
    H(1,t)=max(h);
    sum_age=sum_age+val;
    for i=1:N
        h(i)=h(i)+1;
    end
    r=binornd(1, p(ind));
    if(r==1)
      h(ind)= 1;
    end
    
    H_avg(1,t)=sum_age/t;
    
end


avg_age_MA=sum_age/T

% Simulating the PF Policy
%-------------------------------------------------
h=ones(N,1);
R=ones(N,1);
epsilon=0.1; % exponential smoothing parameter for PF
sum_age=0;

for t=1:T
    [val, ind]=max(p./R);
    H(2,t)=max(h);
    sum_age=sum_age+ max(h);
    for i=1:N
        h(i)=h(i)+1;
    end
    r=binornd(1, p(ind));
    if(r==1)
      h(ind)= 1;
      R(ind)=R(ind)+epsilon;
    end
    
    H_avg(2,t)=sum_age/t;
end

avg_age_PF=sum_age/T


% Simulating the MW Policy
%-------------------------------------------------
h=ones(N,1);

sum_age=0;

for t=1:T
    [val, ind]=max(p.*h.^2);
    H(3,t)=max(h);
    sum_age=sum_age+ max(h);
    for i=1:N
        h(i)=h(i)+1;
    end
    r=binornd(1, p(ind));
    if(r==1)
      h(ind)= 1;
      R(ind)=R(ind)+epsilon;
    end
    
    H_avg(3,t)=sum_age/t;
    
end

avg_age_MW=sum_age/T


% Simulating the Randomized Policy
%-------------------------------------------------
h=ones(N,1);

sum_age=0;

for t=1:T
    ind=randi(N);
    H(4,t)=max(h);
    sum_age=sum_age+ max(h);
    for i=1:N
        h(i)=h(i)+1;
    end
    r=binornd(1, p(ind));
    if(r==1)
      h(ind)= 1;
    end
   H_avg(4,t)=sum_age/t; 
    
end

avg_age_RAND=sum_age/T


plot(1:T, H_avg(1,:), 1:T, H_avg(2,:), 1:T, H_avg(3,:), 1:T, H_avg(4,:));

%plot(1:T, H(1,:), 1:T, H(2,:), 1:T, H(3,:), 1:T, H(4,:));

%bar([avg_age_MA, avg_age_MW, avg_age_PF, avg_age_RAND]);

