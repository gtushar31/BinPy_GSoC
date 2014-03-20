class IC_7441(Base_16pin):
## This is a 16 pin IC 7441. it has ground pin on 5and power pin as 12
## It has 4 input pins 3,4,6 and 7 while the rest are output pins.
        def __init__(self):
                self.pins = [None, None, 0, 0, 0, 0, 0, None, None, None, None, 0, None, None, None, None]
        def run(self):
                output={}
                inputlist=[]
                inputpinslist = [3,4,6,7]
                for i in inputpinslist:
                        a = input("Enter 1 or 0 for " + str(i) + "\n")
                        self.pins[i] = a
                        inputlist.append(self.pins[i])

                invalidlist = [[1,0,1,0], [1,0,1,1], [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]]



                output[16] = AND(NOT(self.pins[3]).output(), NOT(self.pins[4]).output(), NOT(self.pins[6]).output(), NOT(self.pins[7]).output()).output()
                output[15] = AND(NOT(self.pins[3]).output(), NOT(self.pins[4]).output(), NOT(self.pins[6]).output(), self.pins[7]).output()
                output[8] = AND(NOT(self.pins[3]).output(), NOT(self.pins[4]).output(), self.pins[6], NOT(self.pins[7]).output()).output()
                output[9] = AND(NOT(self.pins[3]).output(), NOT(self.pins[4]).output(), self.pins[6], self.pins[7]).output()
                output[13] = AND(NOT(self.pins[3]).output(), self.pins[4], NOT(self.pins[6]).output(), NOT(self.pins[7]).output()).output()
                output[14] = AND(NOT(self.pins[3]).output(), self.pins[4], NOT(self.pins[6]).output(), self.pins[7]).output()
                output[11] = AND(NOT(self.pins[3]).output(), self.pins[4], self.pins[6], NOT(self.pins[7]).output()).output()
                output[10] = AND(NOT(self.pins[3]).output(), self.pins[4], self.pins[6], self.pins[7]).output()
                output[1] = AND(self.pins[3], NOT(self.pins[4]).output(), NOT(self.pins[6]).output(), NOT(self.pins[7]).output()).output()
                output[2] = AND(self.pins[3], NOT(self.pins[4]).output(), NOT(self.pins[6]).output(), self.pins[7]).output()

                self.pins[5] = input("enter ground=")
                self.pins[12] =input ("enter VCC=")

                if self.pins[5] == 0 and self.pins[12]==1:
                        if inputlist in invalidlist:
                                print "Over Range"
                        else:
                                print output
                else:
                        print ("Ground and VCC points have not been configured correctly.")


