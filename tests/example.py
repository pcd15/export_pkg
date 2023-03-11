from exportsgalore.comtrade import Comtrade     # importing the Comtrade class
from exportsgalore.imf import IMF     # importing the IMF class

comtrade_obj = Comtrade()     # creating a Comtrade object so that we can use the methods of the class we imported
imf_obj = IMF()     # creating an IMF object so that we can use the methods of the class we imported

# see above documentation
comtrade_obj.get_all_exports()
comtrade_obj.get_total_exports()

imf_obj.get_reporter_exports()
imf_obj.get_total_exports()
