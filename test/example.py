from export_ease.comtrade import Comtrade     # importing the Comtrade class
from export_ease.imf import IMF     # importing the IMF class

Comtrade.set_key(...)

Comtrade.get_all_exports("B", 2021)
Comtrade.get_total_exports("B", 2021)

Comtrade.get_all_imports("B", 2021)
Comtrade.get_total_imports("B", 2021)

IMF.get_reporter_exports("France", "B", 2021)
IMF.get_total_exports("B", 2021)
