
from bowling.bowling_mechanics import get_bowling_pitch
from bowling.trajectory import hit_target_pitch,create_traj,interpolate_to_loc
from batting.shot_plotter import CoverDrive,Leave

import numpy as np
if __name__=="__main__":
    #target pitch
    line = float(input('Choose line to target: (in metres) '))
    length = float(input('Choose length to target: (in metres) '))

    #real pitch
    real_line,real_length = get_bowling_pitch(line,length,80)
    print(f'pitches at line : {real_line:.2f}m and length: {real_length:.2f}m')

    #get trajectory
    velocity = 35
    angle = hit_target_pitch(line, length, velocity)
    rp = (-20.12, line, 2.0)
    phi = 0  # angle between y and x

    rv = (velocity * np.cos(angle), 0.0, velocity * np.sin(angle))
    ra = (0, 0, 0)
    x, y, z = create_traj(rp, rv, ra)

    #find position at batting plane
    height = interpolate_to_loc(x,y,z,'x','z',-1.22)[0]

    print(f'arrives to batter at line of {real_line:.2f}m and height of {height:.2f}m')

    #choose shot
    p_cover = CoverDrive().probability(real_line,height)
    if p_cover <0.05:
        shot='Leave'
        p = 1.0
    else:
        shot ='Cover Drive'
        p = p_cover
    #fielding

    #report outcome
    print(f'Batter plays {shot} with {p:.2f} probability of success ')