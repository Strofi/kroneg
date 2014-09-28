class board:

    def __init__(self,num_of_disks_for_first_tower):
        def initialize_tower(num_disks = 0):
            disks = []
            for i in range(num_disks,0,-1):
                disks.append(i)
            return disks
        self.tower1 = initialize_tower(num_of_disks_for_first_tower)
        self.tower2 = initialize_tower()
        self.tower3 = initialize_tower()
        self.towers = (self.tower1,self.tower2,self.tower3)

    def print_me(self):
        max_levels = 0;
        for i in self.towers:
            max_levels = max(max_levels,len(i))
        for i in range(max_levels,0,-1):
            print " %s:\t|\t"%i,
            for ii in self.towers:
                if i <= len(ii):
                   print "|%s|"%ii[i-1],
                print "\t",
                
            print
        for i in range(0,30):
            print ".",
        print

        print "\t|\t",
        for i in range(0,len(self.towers)):
            print"%s(%s)\t"%(i,len(self.towers[i])),
        print
        for i in range(0,30):
            print "_",
        print
        print


    def move(self,num_from,num_to):
        if not self.towers[num_from]: return#raise Exception("NUM FROM EMPTY")
        if self.towers[num_to] and self.towers[num_from][-1] > self.towers[num_to][-1]:
            print "num from val: "+str(self.towers[num_from])+" ; numto: "+str(self.towers[num_to])
            print "EXCEPTION NO"
            self.print_me()
            raise Exception("NUM FROM IS BIGGER THATN NUM TO, num_from: "+str(num_from) +", num_to: "+str(num_to)+" ; ")
        element = self.towers[num_from].pop()
        self.towers[num_to].append(element)

    def move_tower(self,from_i,to_i,disks):
        if not (self.towers[from_i]): return
        proxy_i = 3-(from_i+to_i)
        self.print_me()
        if disks>0:
            self.move_tower(from_i,proxy_i,disks-1)
        self.move(from_i,to_i)
        if disks>0:
            self.move_tower(proxy_i,to_i,disks-1)


def main():
    disks = 15
    myboard = board(disks)
 #   myboard.print_me()
    myboard.move_tower(0,2,disks)
    print "RESULT"
    myboard.print_me()

if __name__ == "__main__":
   main()
