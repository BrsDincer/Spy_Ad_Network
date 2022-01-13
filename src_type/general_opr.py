class CONTROLLING_OPS():
    def TOP_TRACKER_OPS(target_url=str):
        analyze_site,toptracker_site,advertising_site = GET_PARAMETERS.GENERAL_COOKIES_JSON()
        domain_list,_,_ = GET_PARAMETERS.TRACKER_DOMAIN_JSON()
        tracker_domain_list,_,_ = GET_PARAMETERS.TRACKER_MAIN_JSON()
        try:
            _,src_clean_list = PARSING_WEB.GET_SRC(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            content_list,_ = PARSING_WEB.CONTENT_SECURITY(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC SESSION")))
        try:
            for x_src in src_clean_list:
                if x_src in analyze_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"ANALYSIS SITE"))
                elif x_src in toptracker_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER SITE"))
                elif x_src in advertising_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"ADVERTISING SITE"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT SESSION")))
        try:
            for x_src in content_list:
                if x_src in analyze_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s . %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"ANALYSIS SITE"))
                elif x_src in toptracker_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER SITE"))
                elif x_src in advertising_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"ADVERTISING SITE"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC - DOMAIN SESSION")))
        try:
            for x_src in src_clean_list:
                if x_src in domain_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER DOMAIN"))
                else:
                    pass
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT - DOMAIN SESSION")))
            for x_src in content_list:
                if x_src in domain_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER DOMAIN"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC - OTHER TRACKER SESSION")))
        try:
            for x_src in src_clean_list:
                if x_src in tracker_domain_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER DOMAIN"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT - OTHER TRACKER SESSION")))
        try:
            for x_src in content_list:
                if x_src in tracker_domain_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER DOMAIN"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
    
    def HUGE_DOMAIN_OPS(target_url=str):
        try:
            _,src_clean_list = PARSING_WEB.GET_SRC(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            content_list,_ = PARSING_WEB.CONTENT_SECURITY(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        sub_list,main_list = GET_PARAMETERS.HUGE_TRACKER_DOMAIN_JSON()
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC MAIN - HUGE TRACKING SESSION")))
        try:
            for x_m in main_list:
                if x_m in src_clean_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_m)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m),"FOUND"))
                else:
                    pass
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC SUB - HUGE TRACKING SESSION")))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            for x_m in sub_list:
                if x_m in src_clean_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_m)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m),"FOUND"))
                else:
                    pass
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT MAIN - HUGE TRACKING SESSION")))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            for x_m in main_list:
                if x_m in content_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_m)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m),"FOUND"))
                else:
                    pass
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT SUB - HUGE TRACKING SESSION")))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            for x_m in sub_list:
                if x_m in content_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_m)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m),"FOUND"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))

        
class DETAILS_OPS():
    def TOP_TRACKER_DETAILS(target_url=str):
        analyze_site,toptracker_site,advertising_site = GET_PARAMETERS.GENERAL_COOKIES_JSON()
        domain_list,_,_ = GET_PARAMETERS.TRACKER_DOMAIN_JSON()
        tracker_domain_list,_,_ = GET_PARAMETERS.TRACKER_MAIN_JSON()
        try:
            src_all,_ = PARSING_WEB.GET_SRC(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            _,content_all = PARSING_WEB.CONTENT_SECURITY(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC SESSION")))
        try:
            for x_src in src_all:
                if x_src in analyze_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"ANALYSIS SITE"))
                elif x_src in toptracker_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER SITE"))
                elif x_src in advertising_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"ADVERTISING SITE"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT SESSION")))
            for x_src in content_all:
                if x_src in analyze_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s . %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"ANALYSIS SITE"))
                elif x_src in toptracker_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER SITE"))
                elif x_src in advertising_site:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"ADVERTISING SITE"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC - DOMAIN SESSION")))
            for x_src in src_all:
                if x_src in domain_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER DOMAIN"))
                else:
                    pass
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT - DOMAIN SESSION")))
            for x_src in content_all:
                if x_src in domain_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER DOMAIN"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC - OTHER TRACKER SESSION")))
            for x_src in src_all:
                if x_src in tracker_domain_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER DOMAIN"))
                else:
                    pass
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT - OTHER TRACKER SESSION")))
            for x_src in content_all:
                if x_src in tracker_domain_list:
                    try:
                        get_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                        print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                    except:
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                    print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),"TRACKER DOMAIN"))
                else:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
    
    def HUGE_DOMAIN_DETAILS(target_url=str):
        sub_list,main_list = GET_PARAMETERS.HUGE_TRACKER_DOMAIN_JSON()
        try:
            src_all,_ = PARSING_WEB.GET_SRC(target_url)
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC MAIN - HUGE TRACKING SESSION")))
            for x_m in main_list:
                for x_num,x_m_c in enumerate(src_all):
                    if x_m in x_m_c:
                        try:
                            get_ip = GET_PARAMETERS.GET_SITE_INFO(src_all[x_num])
                            print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                        except:
                            print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                        print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m),"FOUND"))
                        print("%s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m_c)))
                        print("\n")
                    else:
                        pass
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SRC SUB - HUGE TRACKING SESSION")))
            for x_m in sub_list:
                for x_num,x_m_c in enumerate(src_all):
                    if x_m in x_m_c:
                        try:
                            get_ip = GET_PARAMETERS.GET_SITE_INFO(src_all[x_num])
                            print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                        except:
                            print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                        print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m),"FOUND"))
                        print("%s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m_c)))
                        print("\n")
                    else:
                        pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            _,content_all = PARSING_WEB.CONTENT_SECURITY(target_url)
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT MAIN - HUGE TRACKING SESSION")))
            for x_m in main_list:
                for x_num,x_m_c in enumerate(content_all):
                    if x_m in x_m_c:
                        try:
                            get_ip = GET_PARAMETERS.GET_SITE_INFO(content_all[x_num])
                            print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                        except:
                            print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                        print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m),"FOUND"))
                        print("%s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m_c)))
                        print("\n")
                    else:
                        pass
            print("\n")
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]CONTENT SUB - HUGE TRACKING SESSION")))
            for x_m in sub_list:
                for x_num,x_m_c in enumerate(content_all):
                    if x_m in x_m_c:
                        try:
                            get_ip = GET_PARAMETERS.GET_SITE_INFO(content_all[x_num])
                            print("%s : %s" % ("IP",PRINT_OPTIONS.YELLOW_PRINTING(get_ip)))
                        except:
                            print("%s" % (PRINT_OPTIONS.INFO_PRINTING("NOT FOUND - IP")))
                        print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m),"FOUND"))
                        print("%s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_m_c)))
                        print("\n")
                    else:
                        pass 
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        

class FACEBOOK_SCRIPT_OPS():
    def CHECK_JS_AND_OPERATIONS(target_url=str):
        try:
            script_list = PARSING_WEB.SCRIPT_SOURCE(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("NOTHING FOUND")))
        _,surrogate_list,x_ray_list,selectors_list = GET_PARAMETERS.FACEBOOK_JS_JSON()
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SURROGATE SESSION")))
        try:
            for x_surr in surrogate_list:
                for x_sc in script_list:
                    if x_surr in x_sc:
                        print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_surr),"FOUND"))
                        print("%s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_sc)))
                        print("\n")
                    else:
                        pass
        except:
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]XRAY SESSION")))
        try:
            for x_surr in x_ray_list:
                for x_sc in script_list:
                    if x_surr in x_sc:
                        print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_surr),"FOUND"))
                        print("%s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_sc)))
                        print("\n")
                    else:
                        pass
        except:
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]SELECTORS SESSION")))
        try:
            for x_surr in selectors_list:
                for x_sc in script_list:
                    if x_surr in x_sc:
                        print("%s - %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_surr),"FOUND"))
                        print("%s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_sc)))
                        print("\n")
                    else:
                        pass
        except:
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("NOTHING FOUND")))
                
class SOCIAL_SITE_OPS():
    def ALL_SITE_CHECKING(target_site=str):
        COMMON_NAME = GET_PARAMETERS.READING_FILE("social_names.txt")
        try:
            text_set,content_set,\
                header_set,cookies_set,\
                elapsed_set = REQUESTS_OPS.REQUESTS_INFO(target_site,
                                                         return_parser=True)
        except:
            print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]IN TEXT SEARCH")))
        try:
            for x_in in COMMON_NAME:
                script_parameters = re.findall(fr'{x_in}.*',text_set.lower())
                if script_parameters != None and len(script_parameters) > 0:
                    for x_sc in script_parameters:
                        print("%s - %s" % ("TYPE",PRINT_OPTIONS.YELLOW_PRINTING(x_in)))
                        print("%s" % (PRINT_OPTIONS.INFO_PRINTING(x_sc)))
                        print("\n")
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]IN HEADER SEARCH")))
        try:
            for x_in in COMMON_NAME:
                script_parameters = re.findall(fr'{x_in}.*',header_set["Content-Security-Policy"])
                if script_parameters != None and len(script_parameters) > 0:
                    for x_sc in script_parameters:
                        print("%s - IN CONTENT POLICY [!]" % (PRINT_OPTIONS.YELLOW_PRINTING(x_in)))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
            
class IP_PROCESS():
    def MATCHED_IP(target_domain = str):
        ip_reading = pd.read_csv("source_and_ip.csv")
        ip_reading = ip_reading.dropna()
        site_target = GET_PARAMETERS.GET_SITE_INFO(target_domain)
        print("TARGET %s" % (PRINT_OPTIONS.YELLOW_PRINTING(site_target)))
        print("\n")
        for x_ip,x_src in zip(ip_reading["IP"].values,ip_reading["SRC"].values):
            if x_ip == site_target:
                print("[!] MATCHED %s TO %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),site_target))
                print("[>] REFERER %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_ip)))
                print("\n")
            else:
                pass
    
    def CATCH_IP(target_domain=str):
        try:
            _,src_clean_list = PARSING_WEB.GET_SRC(target_domain)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            content_list,_ = PARSING_WEB.CONTENT_SECURITY(target_domain)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        ip_reading = pd.read_csv("source_and_ip.csv")
        ip_reading = ip_reading.dropna()
        site_target = GET_PARAMETERS.GET_SITE_INFO(target_domain)
        print("TARGET %s" % (PRINT_OPTIONS.YELLOW_PRINTING(site_target)))
        print("\n")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]IN SRC SEARCH")))
        print("\n")
        try:
            for x_in_all_src in src_clean_list:
                try:
                    src_ip = GET_PARAMETERS.GET_SITE_INFO(x_in_all_src)
                    for x_ip,x_src in zip(ip_reading["IP"].values,ip_reading["SRC"].values):
                        try:
                            if x_ip == src_ip:
                                print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_in_all_src)))
                                print("[!] MATCHED %s TO %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),src_ip))
                                print("[>] REFERER %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_ip)))
                                print("\n")
                            else:
                                pass
                        except:
                            pass
                except:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]IN CONTENT SEARCH")))
        print("\n")
        try:
            for x_in_all_src in content_list:
                try:
                    src_ip = GET_PARAMETERS.GET_SITE_INFO(x_in_all_src)
                    for x_ip,x_src in zip(ip_reading["IP"].values,ip_reading["SRC"].values):
                        try:
                            if x_ip == src_ip:
                                print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_in_all_src)))
                                print("[!] MATCHED %s TO %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src),src_ip))
                                print("[>] REFERER %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_ip)))
                                print("\n")
                            else:
                                pass
                        except:
                            pass
                except:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
    
    def MALWARE_AND_ABUSE_IP(target_url=str):
        try:
            _,src_clean_list = PARSING_WEB.GET_SRC(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            content_list,_ = PARSING_WEB.CONTENT_SECURITY(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        
        IP_ALL_A_M = GET_PARAMETERS.READING_FILE("total_ip.txt")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]IN SRC SEARCH")))
        print("\n")
        try:
            for x_src in src_clean_list:
                try:
                    src_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                    for x_a_m in IP_ALL_A_M:
                        try:
                            if x_a_m == src_ip:
                                print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src)))
                                print("[!] MATCHED %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_a_m)))
                                print("[>] REFERER %s" % (PRINT_OPTIONS.YELLOW_PRINTING(src_ip)))
                                print("\n")
                            else:
                                print("[SEARCH FOR] %s [IP] %s" % (PRINT_OPTIONS.INFO_PRINTING(x_src),
                                                                   PRINT_OPTIONS.INFO_PRINTING(src_ip)))
                                print("[X] NOT MATCHED %s" % (PRINT_OPTIONS.INFO_PRINTING(x_a_m)))
                        except:
                            pass
                except:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]IN CONTENT SEARCH")))
        print("\n")    
        try:
            for x_src in content_list:
                try:
                    src_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                    for x_a_m in IP_ALL_A_M:
                        try:
                            if x_a_m == src_ip:
                                print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src)))
                                print("[!] MATCHED %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_a_m)))
                                print("[>] REFERER %s" % (PRINT_OPTIONS.YELLOW_PRINTING(src_ip)))
                                print("\n")
                            else:
                                print("[SEARCH FOR] %s [IP] %s" % (PRINT_OPTIONS.INFO_PRINTING(x_src),
                                                                   PRINT_OPTIONS.INFO_PRINTING(src_ip)))
                                print("[X] NOT MATCHED %s" % (PRINT_OPTIONS.INFO_PRINTING(x_a_m)))
                        except:
                            pass
                except:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
    
    def ADD_LIST_CATCH(target_url=str):
        try:
            _,src_clean_list = PARSING_WEB.GET_SRC(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        try:
            content_list,_ = PARSING_WEB.CONTENT_SECURITY(target_url)
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        
        ALL_LIST = GET_PARAMETERS.READING_FILE("all_list_in.txt")
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]IN SRC SEARCH")))
        print("\n")
        try:
            for x_src in src_clean_list:
                try:
                    src_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                    for x_a_m in ALL_LIST:
                        add_ip_am = GET_PARAMETERS.GET_SITE_INFO(x_a_m)
                        try:
                            if add_ip_am == src_ip:
                                print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src)))
                                print("[!] MATCHED %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_a_m)))
                                print("[>] REFERER %s" % (PRINT_OPTIONS.YELLOW_PRINTING(src_ip)))
                                print("\n")
                            else:
                                print("[X] NOT MATCHED %s" % (PRINT_OPTIONS.INFO_PRINTING(x_a_m)))
                        except:
                            pass
                except:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("[>>]IN CONTENT SEARCH")))
        print("\n")    
        try:
            for x_src in content_list:
                try:
                    src_ip = GET_PARAMETERS.GET_SITE_INFO(x_src)
                    for x_a_m in ALL_LIST:
                        add_ip_am = GET_PARAMETERS.GET_SITE_INFO(x_a_m)
                        try:
                            if add_ip_am == src_ip:
                                print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_src)))
                                print("[!] MATCHED %s" % (PRINT_OPTIONS.YELLOW_PRINTING(add_ip_am)))
                                print("[>] REFERER %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_a_m)))
                                print("\n")
                            else:
                                print("[X] NOT MATCHED %s" % (PRINT_OPTIONS.INFO_PRINTING(x_a_m)))
                        except:
                            pass
                except:
                    pass
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
                            

class CONNECT_TREE():
    def JUMP_TO_CONTENT_TO_CONTENT(target_url=str,verbose_on=True):
        new_content_tree = []
        if verbose_on == True:
            try:
                content_list,_ = PARSING_WEB.CONTENT_SECURITY(target_url)
            except:
                print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
                
            try:
                for x_content in content_list:
                    try:
                        print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_content)))
                        new_content_site,_ = PARSING_WEB.CONTENT_SECURITY(x_content)
                        for x_in_n in new_content_site:
                            try:
                                new_content_tree.append(x_in_n)
                            except:
                                pass
                        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("DONE")))
                        new_content_tree = GET_PARAMETERS.CLEANING_DUBLICATES(new_content_tree)
                    except:
                        pass
                return new_content_tree
            except:
                pass
        else:
            try:
                content_list,_ = PARSING_WEB.CONTENT_SECURITY(target_url)
            except:
                print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
                
            try:
                for x_content in content_list:
                    try:
                        new_content_site,_ = PARSING_WEB.CONTENT_SECURITY(x_content)
                        for x_in_n in new_content_site:
                            try:
                                new_content_tree.append(x_in_n)
                            except:
                                pass
                        new_content_tree = GET_PARAMETERS.CLEANING_DUBLICATES(new_content_tree)
                    except:
                        pass
                return new_content_tree
            except:
                pass
        
    def JUMP_TO_SRC_TO_CONTENT(target_url=str,verbose_on=True):
        new_src_tree = []
        if verbose_on == True:
            try:
                _,src_clean_list = PARSING_WEB.GET_SRC(target_url)
            except:
                print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
                
            try:
                for x_content in src_clean_list:
                    try:
                        print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_content)))
                        new_content_site,_ = PARSING_WEB.CONTENT_SECURITY(x_content)
                        for x_in_n in new_content_site:
                            try:
                                new_src_tree.append(x_in_n)
                            except:
                                pass
                        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("DONE")))
                        new_src_tree = GET_PARAMETERS.CLEANING_DUBLICATES(new_src_tree)
                    except:
                        pass
                return new_src_tree
            except:
                pass
        else:
            try:
                _,src_clean_list = PARSING_WEB.GET_SRC(target_url)
            except:
                print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
                
            try:
                for x_content in src_clean_list:
                    try:
                        new_content_site,_ = PARSING_WEB.CONTENT_SECURITY(x_content)
                        for x_in_n in new_content_site:
                            try:
                                new_src_tree.append(x_in_n)
                            except:
                                pass
                        new_src_tree = GET_PARAMETERS.CLEANING_DUBLICATES(new_src_tree)
                    except:
                        pass
                return new_src_tree
            except:
                pass
    
    def JUMP_TO_CONTENT_TO_SRC(target_url=str,verbose_on=True):
        new_content_tree = []
        if verbose_on == True:
            try:
                content_list,_ = PARSING_WEB.CONTENT_SECURITY(target_url)
            except:
                print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
                
            try:
                for x_content in content_list:
                    try:
                        print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_content)))
                        _,src_clean_list = PARSING_WEB.GET_SRC(x_content)
                        for x_in_n in src_clean_list:
                            try:
                                new_content_tree.append(x_in_n)
                            except:
                                pass
                        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("DONE")))
                        new_content_tree = GET_PARAMETERS.CLEANING_DUBLICATES(new_content_tree)
                    except:
                        pass
                return new_content_tree
            except:
                pass
        else:
            try:
                content_list,_ = PARSING_WEB.CONTENT_SECURITY(target_url)
            except:
                print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
                
            try:
                for x_content in content_list:
                    try:
                        _,src_clean_list = PARSING_WEB.GET_SRC(x_content)
                        for x_in_n in src_clean_list:
                            try:
                                new_content_tree.append(x_in_n)
                            except:
                                pass
                        new_content_tree = GET_PARAMETERS.CLEANING_DUBLICATES(new_content_tree)
                    except:
                        pass
                return new_content_tree
            except:
                pass
            
        
    def JUMP_TO_SRC_TO_SRC(target_url=str,verbose_on=True):
        new_src_tree = []
        if verbose_on == True:
            try:
                _,src_clean_list = PARSING_WEB.GET_SRC(target_url)
            except:
                print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
                
            try:
                for x_content in src_clean_list:
                    try:
                        print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_content)))
                        _,src_clean_list = PARSING_WEB.GET_SRC(x_content)
                        for x_in_n in src_clean_list:
                            try:
                                new_src_tree.append(x_in_n)
                            except:
                                pass
                        print("%s" % (PRINT_OPTIONS.GREEN_PRINTING("DONE")))
                        new_src_tree = GET_PARAMETERS.CLEANING_DUBLICATES(new_src_tree)
                    except:
                        pass
                return new_src_tree
            except:
                pass
        else:
            try:
                _,src_clean_list = PARSING_WEB.GET_SRC(target_url)
            except:
                print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND")))
                
            try:
                for x_content in src_clean_list:
                    try:
                        _,src_clean_list = PARSING_WEB.GET_SRC(x_content)
                        for x_in_n in src_clean_list:
                            try:
                                new_src_tree.append(x_in_n)
                            except:
                                pass
                        new_src_tree = GET_PARAMETERS.CLEANING_DUBLICATES(new_src_tree)
                    except:
                        pass
                return new_src_tree
            except:
                pass
        
    def IP_TREE_ALL(target_url=str):
        all_target_att = []
        print("[%s]" % (PRINT_OPTIONS.GREEN_PRINTING("PROCESS HAS BEEN STARTED")))
        print(">> %s" % (PRINT_OPTIONS.GREEN_PRINTING("PLEASE WAIT")))
        print("\n")
        try:
            j_src_t_src = CONNECT_TREE.JUMP_TO_SRC_TO_SRC(target_url,verbose_on=False)
            all_target_att.append(j_src_t_src)
            print("%s" % (PRINT_OPTIONS.INFO_PRINTING("[COLLECTED] - SCR TO SRC")))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND [SCR TO SRC]")))
        try:
            j_cnt_t_src = CONNECT_TREE.JUMP_TO_CONTENT_TO_SRC(target_url,verbose_on=False)
            all_target_att.append(j_cnt_t_src)
            print("%s" % (PRINT_OPTIONS.INFO_PRINTING("[COLLECTED] - CONTENT TO SRC")))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND [CONTENT TO SRC]")))
        try:
            j_src_t_cnt = CONNECT_TREE.JUMP_TO_SRC_TO_CONTENT(target_url,verbose_on=False)
            all_target_att.append(j_src_t_cnt)
            print("%s" % (PRINT_OPTIONS.INFO_PRINTING("[COLLECTED] - SRC TO CONTENT")))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND [SRC TO CONTENT]")))
        try:
            j_cnt_t_cnt = CONNECT_TREE.JUMP_TO_CONTENT_TO_CONTENT(target_url,verbose_on=False)
            all_target_att.append(j_cnt_t_cnt)
            print("%s" % (PRINT_OPTIONS.INFO_PRINTING("[COLLECTED] - CONTENT TO CONTENT")))
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("NOTHING FOUND [CONTENT TO CONTENT]")))
        try:
            ALL_LIST = GET_PARAMETERS.READING_FILE("C:\\Users\\Asus\\Desktop\\bloacklist\\all_list_in.txt")
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("CHECK FILE OR LOCATION")))
        print("\n")    
        if len(all_target_att) > 0:
            for x_att_x in all_target_att:
                try:
                    for x_sub_x in x_att_x:
                        print("[PROCESS FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_sub_x)))
                        try:
                            x_sub_ip = GET_PARAMETERS.GET_SITE_INFO(x_sub_x)
                            for x_ip_in in ALL_LIST:
                                try:
                                    x_ip_add_control = GET_PARAMETERS.GET_SITE_INFO(x_ip_in)
                                    if x_sub_ip == x_ip_add_control:
                                        print("[SEARCH FOR] %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_sub_x)))
                                        print("[!] MATCHED %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_ip_add_control)))
                                        print("[>] REFERER %s" % (PRINT_OPTIONS.YELLOW_PRINTING(x_ip_in)))
                                        print("\n")
                                    else:
                                        print("NOT MATCHED WITH - %s" % (PRINT_OPTIONS.RED_PRINTING(x_ip_add_control)))
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass