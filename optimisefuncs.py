""" define all the different operations to optimise the antenna """
import stringactions as sa
import calculations as of
_blank = ' '*100

def execute(x,y,n):
    of.write_input_file(x,y,n)
    of.run_nec_command(n)
    rs = of.read_output_file(n)
    ts11, s11 = of.calc_s11(rs)
    obj, pe = of.calc_obj_value(ts11,s11)
    print('>>>',_blank,end="\r")
    print('>>>', n + ': ' + str(obj)+'\r', end="\r")
    return (obj, pe)
    
""" shift the x's to the right
this set perform all the right shifts of the x axis"""
def shift_x_all_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._ALL_ + sa._RIGHT_
    X=[]
    for i in range(0,len(x)):
        X.append(x[i] + DIF_INIT)
        
        
    obj, pe = execute(X,y,_name)
    return(obj, X, y, _name)
"""


"""
def shift_x_first_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._RIGHT_
    
    x[0] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[2] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fourth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fourth_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fourth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fourth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fourth_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fourth_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fourth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[3] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[1] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[2] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fourth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fourth_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fourth_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fourth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[2] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[2] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[2] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fourth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fourth_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fourth_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fourth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[3] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[0] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_x_second_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._RIGHT_
    
    x[1] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[2] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fourth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fourth_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fourth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fourth_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[2] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fourth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fourth_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fourth_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fourth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[3] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[1] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_x_third_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._RIGHT_
    
    x[2] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fourth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._RIGHT_
    
    x[2] += DIF_INIT
    x[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fourth_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fourth_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fourth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[2] += DIF_INIT
    x[3] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[2] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[2] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[2] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_x_fourth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FOURTH_ + sa._RIGHT_
    
    x[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_fourth_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._RIGHT_
    
    x[3] += DIF_INIT
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_fourth_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[3] += DIF_INIT
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_fourth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[3] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)
"""


"""
def shift_x_fifth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIFTH_ + sa._RIGHT_
    
    x[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_fifth_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._RIGHT_
    
    x[4] += DIF_INIT
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""


"""
def shift_x_sixth_right(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SIXTH_ + sa._RIGHT_
    
    x[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

""" shift the x's to the left
this set perform all the left shifts of the x axis"""
def shift_x_all_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._ALL_ + sa._LEFT_
    X=[]
    for i in range(0,len(x)):
        X.append(x[i] - DIF_INIT)
        
        
    obj, pe = execute(X,y,_name)
    return(obj, X, y, _name)
"""


"""
def shift_x_first_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._LEFT_
    
    x[0] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fourth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fourth_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fourth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_third_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fourth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fourth_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fourth_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fourth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[3] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_second_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[1] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[2] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fourth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fourth_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fourth_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fourth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[2] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[2] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_third_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[2] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fourth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fourth_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fourth_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fourth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[3] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_first_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIRST_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[0] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_x_second_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._LEFT_
    
    x[1] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fourth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fourth_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fourth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fourth_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_third_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[2] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fourth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fourth_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fourth_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fourth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[3] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_second_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SECOND_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[1] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_x_third_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._LEFT_
    
    x[2] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fourth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._LEFT_
    
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fourth_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fourth_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fourth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[2] -= DIF_INIT
    x[3] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[2] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[2] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_third_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[2] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_x_fourth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FOURTH_ + sa._LEFT_
    
    x[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_fourth_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._LEFT_
    
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_fourth_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[3] -= DIF_INIT
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_fourth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[3] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)
"""


"""
def shift_x_fifth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIFTH_ + sa._LEFT_
    
    x[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_x_fifth_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._LEFT_
    
    x[4] -= DIF_INIT
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""


"""
def shift_x_sixth_left(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._X_ + sa._SIXTH_ + sa._LEFT_
    
    x[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

""" shift the y's to the top
this set perform all the left shifts of the x axis"""
def shift_y_all_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._ALL_ + sa._UP_
    Y=[]
    for i in range(0,len(x)):
        Y.append(y[i] + DIF_INIT)
        
        
    obj, pe = execute(x,Y,_name)
    return(obj, x, Y, _name)
"""


"""
def shift_y_first_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._UP_
    
    y[0] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[2] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fourth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fourth_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fourth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fourth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fourth_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fourth_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fourth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[3] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[1] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._UP_
    
    y[0] += DIF_INIT
    y[2] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fourth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fourth_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fourth_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fourth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[2] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[2] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[2] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fourth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fourth_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fourth_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fourth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[3] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[0] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_y_second_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._UP_
    
    y[1] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._UP_
    
    y[1] += DIF_INIT
    y[2] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fourth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fourth_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fourth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fourth_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[2] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fourth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fourth_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fourth_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fourth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[3] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[1] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_y_third_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._UP_
    
    y[2] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fourth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._UP_
    
    y[2] += DIF_INIT
    y[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fourth_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fourth_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fourth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[2] += DIF_INIT
    y[3] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[2] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[2] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[2] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_y_fourth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FOURTH_ + sa._UP_
    
    y[3] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_fourth_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._UP_
    
    y[3] += DIF_INIT
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_fourth_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[3] += DIF_INIT
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_fourth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[3] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)
"""


"""
def shift_y_fifth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIFTH_ + sa._UP_
    
    y[4] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_fifth_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._UP_
    
    y[4] += DIF_INIT
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""


"""
def shift_y_sixth_up(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SIXTH_ + sa._UP_
    
    y[5] += DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

""" shift the y's to the bottom
this set perform all the left shifts of the x axis"""
def shift_y_all_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._ALL_ + sa._DOWN_
    Y=[]
    for i in range(0,len(x)):
        Y.append(y[i] - DIF_INIT)
        
        
    obj, pe = execute(x,Y,_name)
    return(obj, x, Y, _name)
"""


"""
def shift_y_first_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._DOWN_
    
    y[0] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fourth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fourth_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fourth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_third_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fourth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fourth_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fourth_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fourth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[3] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_second_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SECOND_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[1] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[2] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fourth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fourth_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fourth_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fourth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[2] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[2] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_third_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[2] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fourth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fourth_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fourth_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fourth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[3] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_first_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIRST_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[0] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_y_second_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._DOWN_
    
    y[1] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fourth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fourth_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fourth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fourth_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_third_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[2] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fourth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fourth_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fourth_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fourth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[3] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_second_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SECOND_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[1] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_y_third_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._DOWN_
    
    y[2] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fourth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._DOWN_
    
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fourth_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fourth_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fourth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[2] -= DIF_INIT
    y[3] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[2] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[2] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_third_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._THIRD_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[2] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""



"""
def shift_y_fourth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FOURTH_ + sa._DOWN_
    
    y[3] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_fourth_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._DOWN_
    
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_fourth_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FOURTH_ + sa._AND_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[3] -= DIF_INIT
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_fourth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FOURTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[3] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)
"""


"""
def shift_y_fifth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIFTH_ + sa._DOWN_
    
    y[4] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

def shift_y_fifth_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._FIFTH_ + sa._AND_ + sa._SIXTH_ + sa._DOWN_
    
    y[4] -= DIF_INIT
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)

"""


"""
def shift_y_sixth_down(x,y,DIF_INIT=0.05):
    _name = sa._SHIFT_ + sa._Y_ + sa._SIXTH_ + sa._DOWN_
    
    y[5] -= DIF_INIT
        
    obj, pe = execute(x,y,_name)
    return (obj, x, y, _name)
