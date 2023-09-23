import numpy as np 
def get_bowling_pitch(target_line,target_length,accuracy):
    """
    return the line and length of a delivery
    """
    #convert metric to standard deviations 
    reference_line = (0.2286*5)/20.0
    reference_length =12/25.0
    
    #0 is the worst , 100 the best 
    #68% falls within sigma . 
    #95% falls within 2 sigma
    #99.7 within 3 sigma
    #so 100 accuracy would want 3sigma to be the reference line/length as this is how we've split the grid

    #what would happen for 0? 3sigma= width of cut square? so 99.7% of the time it lands 

    #m = dy/dx
    m_line = (reference_line - reference_line*20.0)/100.0
    c_line = reference_line - m_line*100
    sigma_line = ( m_line*accuracy +c_line )/3.0

    m_length = (reference_length - reference_length*25.0)/100.0
    c_length = reference_length - m_length*100
    sigma_length = ( m_length*accuracy +c_length )/3.0
    #print(sigma_line,sigma_length)
    del_line =np.random.normal(0, sigma_line) 
    
    del_length =np.random.normal(0, sigma_length) 
    #print(del_line,del_length)
    return target_line +del_line,target_length +del_length

if __name__ =="__main__":
    print(get_bowling_pitch(0.1,1.5,100))
