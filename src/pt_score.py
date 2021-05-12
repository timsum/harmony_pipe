#!/usr/bin/env python3
#
#  prototype for preset chord sequence

# a score should have a list of states.
import numpy as np
import harmony_state
import pt_utils

class pt_score():
    '''
    prototype for a paradigmatic 'chart'
    
    '''

    def __init__(self, home_key=np.array([0,0,1,4,3])):
        self.tempo_bpm = 60
        self.home_key = home_key
        self.chord_motion_filter = np.array([[0,0,0,0,0], [0,0,1,0,1], [0,0,3,0,0], [0,0,6,0,0]], dtype=np.int16)
        self.melody_contour = None
        self.rhythm_contour = None


    def chord_at_index(self, index):
        return pt_utils.kpdve_add(self.home_key, self.chord_motion_filter[index%len(self.chord_motion_filter)])

if __name__ == '__main__':
    sc = pt_score()
    print(sc.chord_at_index(2))



    
