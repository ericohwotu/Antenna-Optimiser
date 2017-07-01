""" def run all the different actions that can be performed """
import stringactions as sa
from os import system
import calculations as of
import optimisefuncs as opt
import math
from multiprocessing.pool import ThreadPool
from heapq import heappush
from random import randint
import threading


TARGET_S11 = [-1,-1,-1,-2.5,-6,-15,-6,-2.5,-1,-1,-1]
INIT_DIF = 0.005
INIT_INCR = 0.05
_blank = " "*30
_exit = False
class Optimiser:
    def __init__(self, x = [1,21.005,44.1715,40.6144,8.84086,-21.9248],y=[1,43.7363,78.2919,110.0315,139.4120,151.7835],_name = "_original"):
        print("***", "------initialising",_name+"------")
        print("***", "number of sides:", len(x)-1)
        print("***", "x:", x)
        print("***", "y:", y)
        print("***", "verbose mode off")
        self.x = x
        self.y = y
        self.name = _name
        self.dif = INIT_DIF
        self.incr = INIT_INCR
        self.allActions = []
        self.curXs = []
        self.curYs = []
        self.curObjs = []
        self.maxObjs = []
        self.h = []
        print("***", "initial alteration difference:", self.dif)
        print("***", "initial increment:", self.incr)
        #for i in range(0,10):
        #    self.run()
        print("***", "------initialisation completed------")

    def run(self):
        of.write_input_file(self.x,self.y,self.name)
        of.run_nec_command(self.name)
        self.rs = of.read_output_file(self.name)
        self.ts11, self.s11 = of.calc_s11(self.rs)
        self.obj, self.pe = of.calc_obj_value(self.ts11,self.s11)
        
        print(">>>", self.name + ": " + str(self.obj) + '\n', end="")
        #print("-------->>>performing checks-----------")
        self.objs, self.xs, self.ys, self.actions = self.build_array(self.x, self.y)
        self.check_results()
        self.end()

        return self.obj
        
    def check_results(self):
        max_objs = max(self.objs)
        
        print('>>>', '***checking results',_blank)
        print('>>>', 'max objs:',max_objs)
        if max_objs <= self.obj:
            print('>>>', "no solution found at:", self.dif, "altering the difference")
            self.dif +=self.incr
            for xs in self.curXs:
                for k in range(0,len(self.xs)):
                    heappush(self.h,(self.objs[k], k))

                choseni = self.h[-100:]

                for i in choseni:
                    _exit=False
                    self.objs, self.xs, self.ys, self.actions = self.build_array(self.xs[i[1]], self.ys[i[1]])
                    self.curXs.append(self.xs)
                    self.curYs.append(self.ys)
                    self.curObjs.append(self.objs)
                    print('>>>', 'max objs:',max(self.objs))
                    if max(self.objs) > self.obj:
                        _exit = True
                        break
                if _exit:
                    _exit = False
                    break
                self.check_results()
        else:
            self.dif = INIT_DIF
            self.curXs.clear()
            self.curYs.clear()
            self.curObjs.clear()
            self.curXs.append(self.xs)
            self.curYs.append(self.ys)
            self.curObjs.append(self.curObjs)
            self.write_to_file()

        max_i = self.objs.index(max(self.objs))
        self.x = self.xs[max_i]
        self.y = self.ys[max_i]
        self.obj= max(self.objs)
        self.maxObjs.append(max_objs)
        self.lastAction = self.actions[max_i]
        self.allActions.append(self.lastAction)

    def write_to_file(self):
        f = open(self.name+"_results.txt","a")
        f2 = open(self.name+"_final.txt","w")
        n = " "*50
        f.write(n+"\n")
        f.write("Objective value: "+str(self.obj)+"\n")
        f.write("X value: "+str(self.x)+"\n")
        f.write("Y value: "+str(self.y)+"\n")
        f.write("Actions Taken: "+str(self.allActions)+"\n")
        f.write("All Objectives: "+str(self.maxObjs)+"\n")
        f.write(n+"\n")
        f2.write("Objective value: "+str(self.obj)+"\n")
        f2.write("X value: "+str(self.x)+"\n")
        f2.write("Y value: "+str(self.y)+"\n")
        f2.write("Actions Taken: "+str(self.allActions)+"\n")
        f2.write("All Objectives: "+str(self.maxObjs)+"\n")
        f.close()
        f2.close()

    def build_array(self, x,y):
        print('>>>', '***building array')
        func_array =[]
        func_array.append(opt.shift_x_all_left)
        func_array.append(opt.shift_x_all_right)
        func_array.append(opt.shift_y_all_up)
        func_array.append(opt.shift_y_all_down)
        func_array.append(opt.shift_x_first_right)
        func_array.append(opt.shift_x_first_second_right)
        func_array.append(opt.shift_x_first_second_third_right)
        func_array.append(opt.shift_x_first_second_third_fourth_right)
        func_array.append(opt.shift_x_first_second_third_fourth_fifth_right)
        func_array.append(opt.shift_x_first_second_third_fourth_sixth_right)
        func_array.append(opt.shift_x_first_second_third_fifth_right)
        func_array.append(opt.shift_x_first_second_third_fifth_sixth_right)
        func_array.append(opt.shift_x_first_second_third_sixth_right)
        func_array.append(opt.shift_x_first_second_fourth_right)
        func_array.append(opt.shift_x_first_second_fourth_fifth_right)
        func_array.append(opt.shift_x_first_second_fourth_fifth_sixth_right)
        func_array.append(opt.shift_x_first_second_fourth_sixth_right)
        func_array.append(opt.shift_x_first_second_fifth_right)
        func_array.append(opt.shift_x_first_second_fifth_sixth_right)
        func_array.append(opt.shift_x_first_second_sixth_right)
        func_array.append(opt.shift_x_first_third_right)
        func_array.append(opt.shift_x_first_third_fourth_right)
        func_array.append(opt.shift_x_first_third_fourth_fifth_right)
        func_array.append(opt.shift_x_first_third_fourth_fifth_sixth_right)
        func_array.append(opt.shift_x_first_third_fourth_sixth_right)
        func_array.append(opt.shift_x_first_third_fifth_right)
        func_array.append(opt.shift_x_first_third_fifth_sixth_right)
        func_array.append(opt.shift_x_first_third_sixth_right)
        func_array.append(opt.shift_x_first_fourth_right)
        func_array.append(opt.shift_x_first_fourth_fifth_right)
        func_array.append(opt.shift_x_first_fourth_fifth_sixth_right)
        func_array.append(opt.shift_x_first_fourth_sixth_right)
        func_array.append(opt.shift_x_first_fifth_right)
        func_array.append(opt.shift_x_first_fifth_sixth_right)
        func_array.append(opt.shift_x_first_sixth_right)
        func_array.append(opt.shift_x_second_right)
        func_array.append(opt.shift_x_second_third_right)
        func_array.append(opt.shift_x_second_third_fourth_right)
        func_array.append(opt.shift_x_second_third_fourth_fifth_right)
        func_array.append(opt.shift_x_second_third_fourth_fifth_sixth_right)
        func_array.append(opt.shift_x_second_third_fourth_sixth_right)
        func_array.append(opt.shift_x_second_third_fifth_right)
        func_array.append(opt.shift_x_second_third_fifth_sixth_right)
        func_array.append(opt.shift_x_second_third_sixth_right)
        func_array.append(opt.shift_x_second_fourth_right)
        func_array.append(opt.shift_x_second_fourth_fifth_right)
        func_array.append(opt.shift_x_second_fourth_fifth_sixth_right)
        func_array.append(opt.shift_x_second_fourth_sixth_right)
        func_array.append(opt.shift_x_second_fifth_right)
        func_array.append(opt.shift_x_second_fifth_sixth_right)
        func_array.append(opt.shift_x_second_sixth_right)
        func_array.append(opt.shift_x_third_right)
        func_array.append(opt.shift_x_third_fourth_right)
        func_array.append(opt.shift_x_third_fourth_fifth_right)
        func_array.append(opt.shift_x_third_fourth_fifth_sixth_right)
        func_array.append(opt.shift_x_third_fourth_sixth_right)
        func_array.append(opt.shift_x_third_fifth_right)
        func_array.append(opt.shift_x_third_fifth_sixth_right)
        func_array.append(opt.shift_x_third_sixth_right)
        func_array.append(opt.shift_x_fourth_right)
        func_array.append(opt.shift_x_fourth_fifth_right)
        func_array.append(opt.shift_x_fourth_fifth_sixth_right)
        func_array.append(opt.shift_x_fourth_sixth_right)
        func_array.append(opt.shift_x_fifth_right)
        func_array.append(opt.shift_x_fifth_sixth_right)
        func_array.append(opt.shift_x_sixth_right)
        #################################################################################
        func_array.append(opt.shift_x_first_left)
        func_array.append(opt.shift_x_first_second_left)
        func_array.append(opt.shift_x_first_second_third_left)
        func_array.append(opt.shift_x_first_second_third_fourth_left)
        func_array.append(opt.shift_x_first_second_third_fourth_fifth_left)
        func_array.append(opt.shift_x_first_second_third_fourth_sixth_left)
        func_array.append(opt.shift_x_first_second_third_fifth_left)
        func_array.append(opt.shift_x_first_second_third_fifth_sixth_left)
        func_array.append(opt.shift_x_first_second_third_sixth_left)
        func_array.append(opt.shift_x_first_second_fourth_left)
        func_array.append(opt.shift_x_first_second_fourth_fifth_left)
        func_array.append(opt.shift_x_first_second_fourth_fifth_sixth_left)
        func_array.append(opt.shift_x_first_second_fourth_sixth_left)
        func_array.append(opt.shift_x_first_second_fifth_left)
        func_array.append(opt.shift_x_first_second_fifth_sixth_left)
        func_array.append(opt.shift_x_first_second_sixth_left)
        func_array.append(opt.shift_x_first_third_left)
        func_array.append(opt.shift_x_first_third_fourth_left)
        func_array.append(opt.shift_x_first_third_fourth_fifth_left)
        func_array.append(opt.shift_x_first_third_fourth_fifth_sixth_left)
        func_array.append(opt.shift_x_first_third_fourth_sixth_left)
        func_array.append(opt.shift_x_first_third_fifth_left)
        func_array.append(opt.shift_x_first_third_fifth_sixth_left)
        func_array.append(opt.shift_x_first_third_sixth_left)
        func_array.append(opt.shift_x_first_fourth_left)
        func_array.append(opt.shift_x_first_fourth_fifth_left)
        func_array.append(opt.shift_x_first_fourth_fifth_sixth_left)
        func_array.append(opt.shift_x_first_fourth_sixth_left)
        func_array.append(opt.shift_x_first_fifth_left)
        func_array.append(opt.shift_x_first_fifth_sixth_left)
        func_array.append(opt.shift_x_first_sixth_left)
        func_array.append(opt.shift_x_second_left)
        func_array.append(opt.shift_x_second_third_left)
        func_array.append(opt.shift_x_second_third_fourth_left)
        func_array.append(opt.shift_x_second_third_fourth_fifth_left)
        func_array.append(opt.shift_x_second_third_fourth_fifth_sixth_left)
        func_array.append(opt.shift_x_second_third_fourth_sixth_left)
        func_array.append(opt.shift_x_second_third_fifth_left)
        func_array.append(opt.shift_x_second_third_fifth_sixth_left)
        func_array.append(opt.shift_x_second_third_sixth_left)
        func_array.append(opt.shift_x_second_fourth_left)
        func_array.append(opt.shift_x_second_fourth_fifth_left)
        func_array.append(opt.shift_x_second_fourth_fifth_sixth_left)
        func_array.append(opt.shift_x_second_fourth_sixth_left)
        func_array.append(opt.shift_x_second_fifth_left)
        func_array.append(opt.shift_x_second_fifth_sixth_left)
        func_array.append(opt.shift_x_second_sixth_left)
        func_array.append(opt.shift_x_third_left)
        func_array.append(opt.shift_x_third_fourth_left)
        func_array.append(opt.shift_x_third_fourth_fifth_left)
        func_array.append(opt.shift_x_third_fourth_fifth_sixth_left)
        func_array.append(opt.shift_x_third_fourth_sixth_left)
        func_array.append(opt.shift_x_third_fifth_left)
        func_array.append(opt.shift_x_third_fifth_sixth_left)
        func_array.append(opt.shift_x_third_sixth_left)
        func_array.append(opt.shift_x_fourth_left)
        func_array.append(opt.shift_x_fourth_fifth_left)
        func_array.append(opt.shift_x_fourth_fifth_sixth_left)
        func_array.append(opt.shift_x_fourth_sixth_left)
        func_array.append(opt.shift_x_fifth_left)
        func_array.append(opt.shift_x_fifth_sixth_left)
        func_array.append(opt.shift_x_sixth_left)
        #################################################################################
        func_array.append(opt.shift_y_first_up)
        func_array.append(opt.shift_y_first_second_up)
        func_array.append(opt.shift_y_first_second_third_up)
        func_array.append(opt.shift_y_first_second_third_fourth_up)
        func_array.append(opt.shift_y_first_second_third_fourth_fifth_up)
        func_array.append(opt.shift_y_first_second_third_fourth_sixth_up)
        func_array.append(opt.shift_y_first_second_third_fifth_up)
        func_array.append(opt.shift_y_first_second_third_fifth_sixth_up)
        func_array.append(opt.shift_y_first_second_third_sixth_up)
        func_array.append(opt.shift_y_first_second_fourth_up)
        func_array.append(opt.shift_y_first_second_fourth_fifth_up)
        func_array.append(opt.shift_y_first_second_fourth_fifth_sixth_up)
        func_array.append(opt.shift_y_first_second_fourth_sixth_up)
        func_array.append(opt.shift_y_first_second_fifth_up)
        func_array.append(opt.shift_y_first_second_fifth_sixth_up)
        func_array.append(opt.shift_y_first_second_sixth_up)
        func_array.append(opt.shift_y_first_third_up)
        func_array.append(opt.shift_y_first_third_fourth_up)
        func_array.append(opt.shift_y_first_third_fourth_fifth_up)
        func_array.append(opt.shift_y_first_third_fourth_fifth_sixth_up)
        func_array.append(opt.shift_y_first_third_fourth_sixth_up)
        func_array.append(opt.shift_y_first_third_fifth_up)
        func_array.append(opt.shift_y_first_third_fifth_sixth_up)
        func_array.append(opt.shift_y_first_third_sixth_up)
        func_array.append(opt.shift_y_first_fourth_up)
        func_array.append(opt.shift_y_first_fourth_fifth_up)
        func_array.append(opt.shift_y_first_fourth_fifth_sixth_up)
        func_array.append(opt.shift_y_first_fourth_sixth_up)
        func_array.append(opt.shift_y_first_fifth_up)
        func_array.append(opt.shift_y_first_fifth_sixth_up)
        func_array.append(opt.shift_y_first_sixth_up)
        func_array.append(opt.shift_y_second_up)
        func_array.append(opt.shift_y_second_third_up)
        func_array.append(opt.shift_y_second_third_fourth_up)
        func_array.append(opt.shift_y_second_third_fourth_fifth_up)
        func_array.append(opt.shift_y_second_third_fourth_fifth_sixth_up)
        func_array.append(opt.shift_y_second_third_fourth_sixth_up)
        func_array.append(opt.shift_y_second_third_fifth_up)
        func_array.append(opt.shift_y_second_third_fifth_sixth_up)
        func_array.append(opt.shift_y_second_third_sixth_up)
        func_array.append(opt.shift_y_second_fourth_up)
        func_array.append(opt.shift_y_second_fourth_fifth_up)
        func_array.append(opt.shift_y_second_fourth_fifth_sixth_up)
        func_array.append(opt.shift_y_second_fourth_sixth_up)
        func_array.append(opt.shift_y_second_fifth_up)
        func_array.append(opt.shift_y_second_fifth_sixth_up)
        func_array.append(opt.shift_y_second_sixth_up)
        func_array.append(opt.shift_y_third_up)
        func_array.append(opt.shift_y_third_fourth_up)
        func_array.append(opt.shift_y_third_fourth_fifth_up)
        func_array.append(opt.shift_y_third_fourth_fifth_sixth_up)
        func_array.append(opt.shift_y_third_fourth_sixth_up)
        func_array.append(opt.shift_y_third_fifth_up)
        func_array.append(opt.shift_y_third_fifth_sixth_up)
        func_array.append(opt.shift_y_third_sixth_up)
        func_array.append(opt.shift_y_fourth_up)
        func_array.append(opt.shift_y_fourth_fifth_up)
        func_array.append(opt.shift_y_fourth_fifth_sixth_up)
        func_array.append(opt.shift_y_fourth_sixth_up)
        func_array.append(opt.shift_y_fifth_up)
        func_array.append(opt.shift_y_fifth_sixth_up)
        func_array.append(opt.shift_y_sixth_up)
        #################################################################################
        func_array.append(opt.shift_y_first_down)
        func_array.append(opt.shift_y_first_second_down)
        func_array.append(opt.shift_y_first_second_third_down)
        func_array.append(opt.shift_y_first_second_third_fourth_down)
        func_array.append(opt.shift_y_first_second_third_fourth_fifth_down)
        func_array.append(opt.shift_y_first_second_third_fourth_sixth_down)
        func_array.append(opt.shift_y_first_second_third_fifth_down)
        func_array.append(opt.shift_y_first_second_third_fifth_sixth_down)
        func_array.append(opt.shift_y_first_second_third_sixth_down)
        func_array.append(opt.shift_y_first_second_fourth_down)
        func_array.append(opt.shift_y_first_second_fourth_fifth_down)
        func_array.append(opt.shift_y_first_second_fourth_fifth_sixth_down)
        func_array.append(opt.shift_y_first_second_fourth_sixth_down)
        func_array.append(opt.shift_y_first_second_fifth_down)
        func_array.append(opt.shift_y_first_second_fifth_sixth_down)
        func_array.append(opt.shift_y_first_second_sixth_down)
        func_array.append(opt.shift_y_first_third_down)
        func_array.append(opt.shift_y_first_third_fourth_down)
        func_array.append(opt.shift_y_first_third_fourth_fifth_down)
        func_array.append(opt.shift_y_first_third_fourth_fifth_sixth_down)
        func_array.append(opt.shift_y_first_third_fourth_sixth_down)
        func_array.append(opt.shift_y_first_third_fifth_down)
        func_array.append(opt.shift_y_first_third_fifth_sixth_down)
        func_array.append(opt.shift_y_first_third_sixth_down)
        func_array.append(opt.shift_y_first_fourth_down)
        func_array.append(opt.shift_y_first_fourth_fifth_down)
        func_array.append(opt.shift_y_first_fourth_fifth_sixth_down)
        func_array.append(opt.shift_y_first_fourth_sixth_down)
        func_array.append(opt.shift_y_first_fifth_down)
        func_array.append(opt.shift_y_first_fifth_sixth_down)
        func_array.append(opt.shift_y_first_sixth_down)
        func_array.append(opt.shift_y_second_down)
        func_array.append(opt.shift_y_second_third_down)
        func_array.append(opt.shift_y_second_third_fourth_down)
        func_array.append(opt.shift_y_second_third_fourth_fifth_down)
        func_array.append(opt.shift_y_second_third_fourth_fifth_sixth_down)
        func_array.append(opt.shift_y_second_third_fourth_sixth_down)
        func_array.append(opt.shift_y_second_third_fifth_down)
        func_array.append(opt.shift_y_second_third_fifth_sixth_down)
        func_array.append(opt.shift_y_second_third_sixth_down)
        func_array.append(opt.shift_y_second_fourth_down)
        func_array.append(opt.shift_y_second_fourth_fifth_down)
        func_array.append(opt.shift_y_second_fourth_fifth_sixth_down)
        func_array.append(opt.shift_y_second_fourth_sixth_down)
        func_array.append(opt.shift_y_second_fifth_down)
        func_array.append(opt.shift_y_second_fifth_sixth_down)
        func_array.append(opt.shift_y_second_sixth_down)
        func_array.append(opt.shift_y_third_down)
        func_array.append(opt.shift_y_third_fourth_down)
        func_array.append(opt.shift_y_third_fourth_fifth_down)
        func_array.append(opt.shift_y_third_fourth_fifth_sixth_down)
        func_array.append(opt.shift_y_third_fourth_sixth_down)
        func_array.append(opt.shift_y_third_fifth_down)
        func_array.append(opt.shift_y_third_fifth_sixth_down)
        func_array.append(opt.shift_y_third_sixth_down)
        func_array.append(opt.shift_y_fourth_down)
        func_array.append(opt.shift_y_fourth_fifth_down)
        func_array.append(opt.shift_y_fourth_fifth_sixth_down)
        func_array.append(opt.shift_y_fourth_sixth_down)
        func_array.append(opt.shift_y_fifth_down)
        func_array.append(opt.shift_y_fifth_sixth_down)
        func_array.append(opt.shift_y_sixth_down)

        O,X,Y,A = perf_test(x,y, func_array, self.dif)
    
        return(O,X,Y,A)
    
    def end(self):
        None
        #print("********actions completed*********")


    
def perf_test(x,y, func_array, dif):
    #print('-->>> perf_test')
    objs = []
    xs = []
    ys = []
    actions = []
    ox = list(x)
    oy = list(y)
    responses = []
        
    for func in func_array:
        x = list(ox)
        y = list(oy)
        OBJ,X,Y,A = func(x,y, dif)
        objs.append(OBJ)
        xs.append(X)
        ys.append(Y)
        actions.append(A)
        
    return (objs,xs,ys,actions)

if __name__ == '__main__':
    r = Optimiser()

    for i in range(1000):
        print(">>>", "***Currently entering run number",str(i))
        result = r.run()
        if result >= 100:
            break


    
