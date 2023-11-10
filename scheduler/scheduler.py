import pandas as pd
import numpy as np
import glob2 as glob
from pathlib import Path

from .models import teacher, student


# Scheduler
class Scheduler():
    teachers = list()
    error = ""
    
    def __init__(self):
        pass
    
    
    def fetch_teacher_details(self):
        try:
            self.teachers = teacher.get_objects()
        except:
            self.error = "Unable to fetch teachers details."
    
    
    def make_tt(self):
        self.fetch_teacher_details()
        
        if not self.teacher:
            return False, self.error