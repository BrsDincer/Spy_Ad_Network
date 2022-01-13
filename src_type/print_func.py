class COLOR_PICKING():
    END_COLOR = "\x1b[0m"
    GREEN_COLOR = "\033[1;32m"
    RED_COLOR = "\033[1;31m"
    YELLOW_COLOR = "\033[1;33m"
    INFO_COLOR = "\033[1;36m"
    

class PRINT_OPTIONS():
    def GREEN_PRINTING(echo_string=str):
        return COLOR_PICKING.GREEN_COLOR+echo_string+COLOR_PICKING.END_COLOR
    
    def RED_PRINTING(echo_string=str):
        return COLOR_PICKING.RED_COLOR+echo_string+COLOR_PICKING.END_COLOR
    
    def YELLOW_PRINTING(echo_string=str):
        return COLOR_PICKING.YELLOW_COLOR+echo_string+COLOR_PICKING.END_COLOR
    
    def INFO_PRINTING(echo_string=str):
        return COLOR_PICKING.INFO_COLOR+echo_string+COLOR_PICKING.END_COLOR