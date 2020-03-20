T=10^7;
p=ones(1,T);
sum1=0;
for t=1:T-1
   p(t+1)= 1+0.5*p(t)+sqrt(p(t));
   sum1= sum1+2*sqrt(p(t));
end

sum1/T