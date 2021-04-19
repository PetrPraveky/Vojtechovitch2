#Hlavní render
import os
import sys

sys.path.insert(0, os.path.join('functions', 'render'))

import main_render as m_rend

if __name__ == '__main__':
    m_rend.MyApp().run()