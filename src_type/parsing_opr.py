class PARSING_WEB():
    def GET_SRC(target_url=str):
        src_list=[]
        src_clean_list = []
        text_set,content_set,\
            header_set,cookies_set,\
            elapsed_set = REQUESTS_OPS.REQUESTS_INFO(target_url,
                                                     return_parser=True)
        src_parameters = re.findall(r'http.*',text_set)
        for x_src in src_parameters:
            split_one = x_src.split('"')
            clean_url = GET_PARAMETERS.CLEANING_URL(split_one[0])
            src_list.append(split_one[0])
            src_clean_list.append(clean_url)
        src_list = GET_PARAMETERS.CLEANING_DUBLICATES(src_list)
        src_clean_list = GET_PARAMETERS.CLEANING_DUBLICATES(src_clean_list)
        return src_list,src_clean_list
    
    def CONTENT_SECURITY(target_url=str):
        try:
            content_sc_list = []
            main_set_url = []
            _,_,header_x,_,_ = REQUESTS_OPS.REQUESTS_INFO(target_url,return_parser=True)
            try:
                cs_parameters = re.findall(r'http.*',header_x["Content-Security-Policy"])
                for x_cs in cs_parameters:
                    split_cs = x_cs.split(" ")
                    for x_split in split_cs:
                        if ".com" in x_split:
                            clean_url = GET_PARAMETERS.CLEANING_URL(x_split)
                            main_set_url.append(x_split)
                            content_sc_list.append(clean_url)
                sc_clean_list = GET_PARAMETERS.CLEANING_DUBLICATES(content_sc_list)
                sc_full_list = GET_PARAMETERS.CLEANING_DUBLICATES(main_set_url)
                return sc_clean_list,sc_full_list
            except:
                print("%s" % (PRINT_OPTIONS.YELLOW_PRINTING("NOT FOUND - SECURITY CONTENT")))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("GETTING INFO FAILED, CHECK CONNECTION")))
            
    def SCRIPT_SOURCE(target_url=str):
        try:
            script_list = []
            text_source,_,_,_,_ = REQUESTS_OPS.REQUESTS_INFO(target_url,return_parser=True)
            try:
                script_parameters = re.findall(r'<script.*',text_source)
                for x_scrpt in script_parameters:
                    x_sx = x_scrpt.replace("<script>","").replace("<script","")\
                        .replace("script","").replace("</script>","").replace("></>","")\
                            .replace(">","").replace("<","").replace(" ","").replace("src=","")\
                                .replace('"',"").replace('\r',"")
                    if x_sx != None and len(x_sx) != 0:
                        script_list.append(x_sx)
                    else:
                        pass
                return script_list
            except:
                print("%s" % (PRINT_OPTIONS.YELLOW_PRINTING("NOT FOUND - SCRIPT")))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("GETTING INFO FAILED, CHECK CONNECTION")))