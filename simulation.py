from pylab import *

#No. of nodes
Nodes = [2,5,10,30]
Niter_total = sum(Nodes)*10000
TotalAoi_MA = zeros(shape = (4,1))
TotalAoi_MW = zeros(shape = (4,1))
TotalAoi_PF = zeros(shape = (4,1))
TotalAoi_Rand = zeros(shape = (4,1))
TotalAoi_MATP = zeros(shape = (4,1))

AverageMaxAoI_MA = zeros(shape = (4,1))
AverageMaxAoI_MW = zeros(shape = (4,1))
AverageMaxAoI_PF = zeros(shape = (4,1))
AverageMaxAoI_Rand = zeros(shape = (4,1))
AverageMaxAoI_MATP = zeros(shape = (4,1))

for simulations in range(1):
    for j in range(4):
        #No. of nodes
        if(j == 0):
            N = Nodes[0]
        if(j == 1):
            N = Nodes[1]
        if(j == 2):
            N = Nodes[2]
        if(j == 3):
            N = Nodes[3]

        #No. of time slots
        Niter = N*10000
        ############# Max Age Policy Starts #############

        

#AoI vector which will change as the timeslot changes
        AoI_MA = ones(shape = (N,1))
        maxAoI_MA = zeros(shape = (Niter,1))
        AverageAoI_MA = zeros(shape = (Niter,1))
        AverageThroughput_MA = zeros(shape = (Niter,1))
        ExpectedAoI_MA = zeros(shape = (4,1))
        ExpectedMaxAoI_MA = zeros(shape = (4,1))
        

        #Probabilities assigned for each node
        p_i = rand(N,1)


        node2sendvector = ones(shape = (Niter,1))

        i = 0
        iter = 0
        AoI_sum = 0

        #For loop which mimics time
        for iter in range(Niter):
            node2send = max(AoI_MA)
            node2sendvector[iter] = node2send
            ### For loop to choose which node is to be sent ###
            for i in range(N):
                if(AoI_MA[i] == node2send):
                    node2send_iter = i
                    break
            ### For loop ends ###
            ExpectedMaxAoI_MA[j] += max(AoI_MA)
            margin = rand(1,1)
            if(margin <= p_i[node2send_iter]):
                AoI_MA = AoI_MA + 1
                AoI_MA[node2send_iter] = 1
                if(iter > 0):
                    AverageThroughput_MA[iter] = (AverageThroughput_MA[iter - 1]*(iter - 1) + 1)/iter
            else:
                AoI_MA = AoI_MA + 1
                if(iter > 0):
                    AverageThroughput_MA[iter] = (AverageThroughput_MA[iter - 1]*(iter - 1))/iter
            maxAoI_MA[iter] = max(AoI_MA)
            AverageAoI_MA[iter] = sum(AoI_MA)/N
            ExpectedAoI_MA[j] += AverageAoI_MA[iter]
             
        #plot(range(Niter),node2sendvector,"ro")
        #show()
        ExpectedAoI_MA[j] = ExpectedAoI_MA[j]/(N*Niter)
        TotalAoi_MA[j] += ExpectedAoI_MA[j]
        ExpectedMaxAoI_MA[j] = ExpectedMaxAoI_MA[j]/Niter
        AverageMaxAoI_MA[j] += ExpectedMaxAoI_MA[j]
            
        #######################  Proportionally Fair Algorithm ############################

        ## We define the throughput y, maximum possible throughput gamma and the decision variable x
        R = zeros(shape = (N,Niter,1)) + 0.00001
        AoI_PF = ones(shape = (N,1))
        maxAoI_PF = zeros(shape = (Niter,1))
        AverageAoI_PF = zeros(shape = (Niter,1))
        AverageThroughput_PF = zeros(shape = (Niter,1))
        ExpectedAoI_PF = zeros(shape = (4,1))
        ExpectedMaxAoI_PF = zeros(shape = (4,1))

        iter = 0
        beta = 0.1

        ### For loop which mimics time ###
        for iter in range(1,Niter):
            i = 0
            y = zeros(shape = (N,1))
            node2send_pf = max(p_i/R[:,iter - 1])
            
            ### For loop to choose node ###
            for i in range(0,N):
                if(p_i[i][0]/R[i][iter - 1][0] == node2send_pf):
                    node2send_pf_iter = i
                    break
            ### For loop ends ###
            ExpectedMaxAoI_PF[j] += max(AoI_PF)
            margin = rand(1,1)
            if(margin <= p_i[node2send_pf_iter]):
                y[i] = 1
                AoI_PF = AoI_PF + 1
                AoI_PF[node2send_pf_iter] = 1
                if(iter > 0):
                    AverageThroughput_PF[iter] = (AverageThroughput_PF[iter - 1]*(iter - 1) + 1)/iter
            else:
                y[i] = 0
                AoI_PF = AoI_PF + 1
                if(iter > 0):
                    AverageThroughput_PF[iter] = (AverageThroughput_PF[iter - 1]*(iter - 1))/iter
            maxAoI_PF[iter] = max(AoI_PF)
            AverageAoI_PF[iter] = sum(AoI_PF)/N
            R[:,iter] = (1 - beta)*R[:,iter - 1] + (beta)*y
            ExpectedAoI_PF[j] += AverageAoI_PF[iter]
        ExpectedMaxAoI_PF[j] = ExpectedMaxAoI_PF[j]/Niter
        AverageMaxAoI_PF[j] += ExpectedMaxAoI_PF[j]
        ### For loop ends ###
        ExpectedAoI_PF[j] = ExpectedAoI_PF[j]/(N*Niter)
        TotalAoi_PF[j] += ExpectedAoI_PF[j]
        
        
        
        ############## Randomized Algorithm Starts ################

        iter = 0
        AoI_Rand = ones(shape = (N,1))
        maxAoI_Rand = zeros(shape = (Niter,1))
        AverageAoI_Rand = zeros(shape = (Niter,1))
        AverageThroughput_Rand = zeros(shape = (Niter,1))
        ExpectedAoI_Rand = zeros(shape = (4,1))
        ExpectedMaxAoI_Rand = zeros(shape = (4,1))
        
        ### For loop which mimics time ###
        for iter in range(0,Niter):
            node2send_rand = randint(0,N)
            ExpectedMaxAoI_Rand[j] += max(AoI_PF)
            margin = rand(1,1)
            if(margin <= p_i[node2send_rand]):
                AoI_Rand = AoI_Rand + 1
                AoI_Rand[node2send_rand] = 1
                if(iter > 0):
                    AverageThroughput_Rand[iter] = (AverageThroughput_Rand[iter - 1]*(iter - 1) + 1)/iter
            else:
                AoI_Rand = AoI_Rand + 1
                if(iter > 0):
                    AverageThroughput_Rand[iter] = (AverageThroughput_Rand[iter - 1]*(iter - 1))/iter
            maxAoI_Rand[iter] = max(AoI_Rand)
            AverageAoI_Rand[iter] = sum(AoI_Rand)/N
            ExpectedAoI_Rand[j] += AverageAoI_Rand[iter]
        ExpectedAoI_Rand[j] = ExpectedAoI_Rand[j]/(N*Niter)
        TotalAoi_Rand[j] += ExpectedAoI_Rand[j]
        ExpectedMaxAoI_Rand[j] = ExpectedMaxAoI_Rand[j]/Niter
        AverageMaxAoI_Rand[j] += ExpectedMaxAoI_Rand[j]
        
        ############# MW Algorithm starts ###############
        AoI_MW = rand(N,1)
        maxAoI_MW = zeros(shape = (Niter,1))
        AverageAoI_MW = zeros(shape = (Niter,1))
        AverageThroughput_MW = zeros(shape = (Niter,1))
        ExpectedAoI_MW = zeros(shape = (4,1))
        ExpectedMaxAoI_MW = zeros(shape = (4,1))

        ### For loop which mimics time ###
        for iter in range(0,Niter):
            node2send_MW_iter = argmax(p_i*AoI_MW*(AoI_MW + 2))
            ExpectedMaxAoI_MW[j] += max(AoI_MW)
            margin = rand(1,1)
            if(margin <= p_i[node2send_MW_iter]):
                AoI_MW = AoI_MW + 1
                AoI_MW[node2send_MW_iter] = 1
                if(iter > 0):
                    AverageThroughput_MW[iter] = (AverageThroughput_MW[iter - 1]*(iter - 1) + 1)/iter
            else:
                AoI_MW = AoI_MW + 1
                if(iter > 0):
                    AverageThroughput_MW[iter] = (AverageThroughput_MW[iter - 1]*(iter - 1))/iter
            maxAoI_MW[iter] = max(AoI_MW)
            AverageAoI_MW[iter] = sum(AoI_MW)/N
            ExpectedAoI_MW[j] += AverageAoI_MW[iter]
        ### For loop ends ###
        ExpectedAoI_MW[j] = ExpectedAoI_MW[j]/(N*Niter)
        TotalAoi_MW[j] += ExpectedAoI_MW[j]
        ExpectedMaxAoI_MW[j] = ExpectedMaxAoI_MW[j]/Niter
        AverageMaxAoI_MW[j] += ExpectedMaxAoI_MW[j]
        
        
        ############# Max age plus throughput constraints starts ###############
        #AoI vector which will change as the timeslot changes
        AoI_MATP = ones(shape = (N,1))
        maxAoI_MATP = zeros(shape = (Niter,1))
        AverageAoI_MATP = zeros(shape = (Niter,1))
        AverageThroughput_MATP = zeros(shape = (Niter,1))
        ExpectedAoI_MATP = zeros(shape = (4,1))
        ExpectedMaxAoI_MATP = zeros(shape = (4,1))

        node2send_MATP = zeros(shape = (N,1))

        i = 0
        iter = 0
        AoI_sum = 0
        beta = 100
        throughput1 = 0.0

        #For loop which mimics time
        for iter in range(Niter):
            ### Choosing the node to send ###
            node2send_MATP = AoI_MATP - beta
            node2send_MATP[1] = AoI_MATP[1] - beta*(1 - p_i[1])
            node2send_MATP_iter = argmax(node2send_MATP)
            
            ### Sending to the node ###
            ExpectedMaxAoI_MATP[j] += max(AoI_MATP)
            margin = rand(1,1)
            if(margin <= p_i[node2send_MATP_iter]):
                AoI_MATP = AoI_MATP + 1
                AoI_MATP[node2send_MATP_iter] = 1
                if(iter > 0):
                    AverageThroughput_MATP[iter] = (AverageThroughput_MATP[iter - 1]*(iter - 1) + 1)/iter
            else:
                AoI_MATP = AoI_MATP + 1
                if(node2send_MATP_iter == 1):
                    throughput1 += 1
                
                if(iter > 0):
                    AverageThroughput_MATP[iter] = (AverageThroughput_MATP[iter - 1]*(iter - 1))/iter
            maxAoI_MATP[iter] = max(AoI_MATP)
            AverageAoI_MATP[iter] = sum(AoI_MATP)/N
            ExpectedAoI_MATP[j] += AverageAoI_MATP[iter]
             
        #plot(range(Niter),node2sendvector,"ro")
        #show()
        ExpectedAoI_MATP[j] = ExpectedAoI_MATP[j]/(N*Niter)
        TotalAoi_MATP[j] += ExpectedAoI_MATP[j]
        ExpectedMaxAoI_MATP[j] = ExpectedMaxAoI_MATP[j]/Niter
        AverageMaxAoI_MATP[j] += ExpectedMaxAoI_MATP[j]

        
        print(j)
    print(simulations)
    
    
    
############# Plots Start ##############
plot(arange(0,Niter,1000), maxAoI_MA[::1000],  'r-', arange(0,Niter,1000), maxAoI_MW[::1000],'b-', arange(0,Niter,1000), maxAoI_PF[::1000],'g-', arange(0,Niter,1000), maxAoI_Rand[::1000],'y-',arange(0,Niter,1000), maxAoI_MATP[::1000],'c-')
xlabel("Time")
ylabel("Maximum AoI per Slot")
legend(("MA","MW","PF","Rand","MATP"),loc = 0)
show()
plot(arange(0,Niter,1000), AverageAoI_MA[::1000],  'r-', arange(0,Niter,1000), AverageAoI_MW[::1000],'b-', arange(0,Niter,1000), AverageAoI_PF[::1000],'g-', arange(0,Niter,1000), AverageAoI_Rand[::1000],'y-', arange(0,Niter,1000), AverageAoI_MATP[::1000],'c-')
xlabel("Time")
ylabel("Average AoI in the slot")
legend(("MA","MW","PF","Rand","MATP"),loc = 0)
show()
plot(arange(0,Niter,1000), AverageThroughput_MA[::1000],  'r-', arange(0,Niter,1000), AverageThroughput_MW[::1000],'b-', arange(0,Niter,1000), AverageThroughput_PF[::1000],'g-', arange(0,Niter,1000), AverageThroughput_Rand[::1000],'y-', arange(0,Niter,1000), AverageThroughput_MATP[::1000],'c-')
xlabel("Time")
ylabel("Average Throughput per Slot")
legend(("MA","MW","PF","Rand","MATP"),loc = 0)
show()
plot(Nodes, TotalAoi_MA/10,'ro', Nodes, TotalAoi_MW/10,'bo', Nodes, TotalAoi_PF/10,'go', Nodes, TotalAoi_Rand/10,'yo', Nodes, TotalAoi_MATP/10,'co')
xlabel("Number of Users")
ylabel("Expected Average AoI")
legend(("MA","MW","PF","Rand","MATP"),loc = 0)
show()
plot(Nodes, AverageMaxAoI_MA/10,'ro', Nodes, AverageMaxAoI_MW/10,'bo', Nodes, AverageMaxAoI_PF/10,'go', Nodes, AverageMaxAoI_Rand/10,'yo', Nodes, AverageMaxAoI_MATP/10,'co')
xlabel("Number of Users")
ylabel("Average Maximum AoI")
legend(("MA","MW","PF","Rand","MATP"),loc = 0)
show()
    
throughput1 = throughput1/(Niter)
print(throughput1)
    






















