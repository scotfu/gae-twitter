#-*-coding:utf-8-*-
import os
import sys

sys.path.append(os.path.join(os.path.abspath('.'), 'lib'))

import application
if __name__=='__main__':
    
    application.app.run(debug=True)
