bal_let = [0]
list_per = []
Vote = []
Candidates_per = []
win = []

# code below introduces the program itself 
print ("VOTING BALLOT SYSTEM")
print ("")
print ("Follow the instructions ")
print 


# Code below the votes of the candidates and votes
def Candidates_voter(bal_let,list_per ,Vote):
    while bal_let != []:
        Vote.append(bal_let.count(bal_let[0]))
        list_per.append(bal_let[0])
        for Votes_per_Candidates in range(Vote[-1]):
            bal_let.pop(0)
    return Vote
    return Candidates_list
    

# code below finds the winner
def Winners(Candidates_per, list_per, win):
    highest_percent = max(Candidates_per)
    
# Code below shows the candidate system in which it records it in list
def Vote_ses(bal_let):
    while bal_let[-1] != "0" :
            bal_let.append(input("enter candidate name: "))
            print("")
            print ("Enter: (0) to return results")
            print("")
            if bal_let[-1] == "" :
                print ("")
                print ("enter candidate name")
                print ("")
                bal_let.pop("")
            
    bal_let.pop(-1)
    bal_let.pop(0)
    bal_let.sort()
    return bal_let
    
# calculates the percentage of the candidates
def Candidates_size(Candidates_list, Vote, Candidates_per):
    Total_voters = sum(Vote) * 1.00
    for i in range(len(Vote)):
        Candidates_per.append((Vote[i]/Total_voters)*100)
    return Candidates_per


#Code bellow uses all the functions previously made and runs/executes them
Vote_ses(bal_let)
Candidates_voter(bal_let,list_per ,Vote)
Candidates_size(list_per , Vote, Candidates_per)
Winners(Candidates_per, list_per, win)
print ("Candidates Names: " + str(list_per))
print ("Number of votes on each person: " + str(Vote))
print ("Voting Percentage of each Candidate: " + str(Candidates_per))
print("")
