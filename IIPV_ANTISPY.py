import requests,socket,json,random,re
import pandas as pd
from optparse import OptionParser as OPTp
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class COLOR_PICKING():
    try:
        END_COLOR = "\x1b[0m"
        GREEN_COLOR = "\033[1;32m"
        RED_COLOR = "\033[1;31m"
        YELLOW_COLOR = "\033[1;33m"
        INFO_COLOR = "\033[1;36m"
    except:
        pass
    

class PRINT_OPTIONS():
    def GREEN_PRINTING(echo_string=str):
        return COLOR_PICKING.GREEN_COLOR+echo_string+COLOR_PICKING.END_COLOR
    
    def RED_PRINTING(echo_string=str):
        return COLOR_PICKING.RED_COLOR+echo_string+COLOR_PICKING.END_COLOR
    
    def YELLOW_PRINTING(echo_string=str):
        return COLOR_PICKING.YELLOW_COLOR+echo_string+COLOR_PICKING.END_COLOR
    
    def INFO_PRINTING(echo_string=str):
        return COLOR_PICKING.INFO_COLOR+echo_string+COLOR_PICKING.END_COLOR


class SIMPLE_LOOP():
    def FOR_LOOP_ADD(x_e,list_app=list):
        for x_s in x_e:
            try:
                list_app.append(x_s)
            except:
                pass
    def CX_FOR_LOOP_ADD(x_e,main_e,list_app=list,params=str):
        for x_s in x_e:
            try:
                list_app.append(main_e[x_s][params])
            except:
                pass
    def RANGE_FOR_LOOP_ADD(x_e,x_loop,list_app=list,x_list=list,params=str):
        for x_s in x_e:
            try:
                list_app.append(x_loop[x_list[x_s]][params])
            except:
                pass
    def TARGET_FOR_LOOP_ADD(x_e,x_loop,
                            list_app=list,
                            x_list=list,
                            params=str,
                            target=str):
        for x_s in x_e:
            try:
                list_app.append(x_loop[x_list[x_s]][params][target])
            except:
                pass


class GET_PARAMETERS():
    def READING_FILE(file_name=str):
        try:
            with open(file_name,"r",errors="replace") as file_tar:
                x_file = []
                for line_x in file_tar:
                    try:
                        ext_tar = line_x.strip()
                        x_file.append(ext_tar)
                    except:
                        pass
            return x_file
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("GETTING INFO FAILED, TRY AGAIN")))
            pass
        
    def CLEANING_DUBLICATES(ops_list=list):
        try:
            clean_list = list(dict.fromkeys(ops_list))
            return clean_list
        except:
            pass
    
    def CLEANING_URL(target_site=str):
        try:
            new_site = target_site.replace("http://","").replace("https://","").replace("www.","")
            split_site = new_site.split("/")
            return split_site[0]
        except:
            pass
    
    def GET_SITE_INFO(target_site=str):
        try:
            new_site = target_site.replace("http://","").replace("https://","").replace("www.","")
            ip_found = socket.gethostbyname(new_site)
            return ip_found
        except:
            pass
    
    def USER_AGENT_LIST(target_doc=str):
        try:
            f_op = open(target_doc)
            j_op = json.loads(f_op.read())
            list_agent = []
            for x_value in j_op["user_agents"]:
                for ix_values in j_op["user_agents"][x_value]:
                    for ixl_values in j_op["user_agents"][x_value][ix_values]:
                        for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                            list_agent.append(ixlp_values)
            return list_agent
        except:
            print("%s" % (PRINT_OPTIONS.RED_PRINTING("GETTING INFO FAILED, CHECK FILE")))
            
    def GENERAL_COOKIES_JSON(): #cookies_tracker
        try:
            analyze_site=[]
            toptracker_site=[]
            advertising_site=[]
            open_doc = open("cookies_tracker.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            tt_domains = load_doc["TopTrackerDomains"]
            add_domains = load_doc["Advertising"]
            analy_domains = load_doc["Analytics"]
            SIMPLE_LOOP.FOR_LOOP_ADD(tt_domains,toptracker_site)
            SIMPLE_LOOP.FOR_LOOP_ADD(add_domains,advertising_site)
            SIMPLE_LOOP.FOR_LOOP_ADD(analy_domains,analyze_site)
            return analyze_site,toptracker_site,advertising_site
        except:
            pass
    
    def HUGE_TRACKER_DOMAIN_JSON(): #tracker_main
        try:
            domain_main_list = []
            domain_sub_list = []
            entities_all_list = []
            entities_main_list = []
            main_entities = []
            open_doc = open("tracker_main.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            trackers_all = load_doc["trackers"]
            entities_all = load_doc["entities"]
            SIMPLE_LOOP.FOR_LOOP_ADD(trackers_all,domain_main_list)
            SIMPLE_LOOP.FOR_LOOP_ADD(entities_all,entities_all_list)
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(domain_main_list,
                                        trackers_all,
                                        domain_sub_list,
                                        "domain")
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(entities_all_list,
                                        entities_all,
                                        entities_main_list,
                                        "domains")
            for x_in in entities_main_list:
                for x_sub in x_in:
                    main_entities.append(x_sub)
            return domain_sub_list,main_entities
        except:
            pass
    
    def COMMON_SITE_JSON():
        try:
            common_site_list = []
            COMMON_NAME = GET_PARAMETERS.READING_FILE("name_all.txt")
            open_doc = open("tracker_main.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            for x_tc in COMMON_NAME:
                entities_domain = load_doc["entities"][x_tc]["domains"]
                common_site_list.append(entities_domain)
            single_list = []
            for x_in in common_site_list:
                for x_sub in x_in:
                    single_list.append(x_sub)
            return single_list
        except:
            pass
    
    def VERIZON_SITE_JSON():
        try:
            verizon_site_list = []
            open_doc = open("tracker_main.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            ver_media_domain = load_doc["entities"]["Verizon Media"]["domains"]
            ver_domain = load_doc["entities"]["Verizon"]["domains"]
            for i_v in ver_media_domain:
                verizon_site_list.append(i_v)
            for i_v in ver_domain:
                verizon_site_list.append(i_v)
            return verizon_site_list
        except:
            pass
    
    def FACEBOOK_SITE_JSON():
        try:
            facebook_site_list = []
            open_doc = open("tracker_main.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            facebook_domain = load_doc["entities"]["Facebook, Inc."]["domains"]
            for i_v in facebook_domain:
                facebook_site_list.append(i_v)
            return facebook_site_list
        except:
            pass
    
    def AKAMAI_SITE_JSON():
        try:
            akamai_site_list = []
            open_doc = open("tracker_main.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            akamai_domain = load_doc["entities"]["Akamai Technologies"]["domains"]
            for i_v in akamai_domain:
                akamai_site_list.append(i_v)
            return akamai_site_list
        except:
            pass
        
    
    def SOCIAL_COOKIES_JSON(): #cookies_tracker
        try:
            facebook_site=[]
            facebook_connect=[]
            twitter_site=[]
            linkedin_site=[]
            open_doc = open("cookies_tracker.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            facebook_domains = load_doc["Social"]["facebook.com"]["rules"]
            facebook_net_domains = load_doc["Social"]["facebook.net"]["rules"]
            twitter_domains = load_doc["Social"]["twitter.com"]["rules"]
            linkedin_domains = load_doc["Social"]["linkedin.com"]["rules"]
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(range(len(facebook_domains)),
                                        facebook_domains,
                                        facebook_site,
                                        "rule")
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(range(len(facebook_net_domains)),
                                        facebook_net_domains,
                                        facebook_connect,
                                        "rule")
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(range(len(twitter_domains)),
                                        twitter_domains,
                                        twitter_site,
                                        "rule")
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(range(len(linkedin_domains)),
                                        linkedin_domains,
                                        linkedin_site,
                                        "rule")
            return facebook_site,facebook_connect,twitter_site,linkedin_site
        except:
            pass
    
    def TRACKER_DOMAIN_JSON(): #tracker_blocking
        try:
            domain_list = []
            categories_list = []
            name_list = []
            open_doc = open("tracker_blocking.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            domain_name = load_doc["trackers"]
            SIMPLE_LOOP.FOR_LOOP_ADD(domain_name,domain_list)
            SIMPLE_LOOP.RANGE_FOR_LOOP_ADD(range(len(domain_list)),
                                            domain_name,
                                            categories_list,
                                            domain_list,
                                            "categories")
            SIMPLE_LOOP.TARGET_FOR_LOOP_ADD(range(len(domain_list)),
                                            domain_name,
                                            name_list,
                                            domain_list,
                                            "owner",
                                            "name")
            return domain_list,categories_list,name_list
        except:
            pass
    
    def FACEBOOK_JS_JSON(): #social_ctp
        try:
            rule_list = []
            surrogate_list = []
            x_ray_list = []
            selectors_list = []
            simple_list = []
            open_doc = open("social_ctp.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            face_name = load_doc["Facebook"]
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(range(len(face_name["surrogates"])),
                                        face_name["surrogates"],
                                        rule_list,
                                        "rule")
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(range(len(face_name["surrogates"])),
                                        face_name["surrogates"],
                                        surrogate_list,
                                        "surrogate")
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(range(len(face_name["surrogates"])),
                                        face_name["surrogates"],
                                        x_ray_list,
                                        "xray")
            SIMPLE_LOOP.CX_FOR_LOOP_ADD(face_name["elementData"],
                                        face_name["elementData"],
                                        simple_list,
                                        "selectors")
            for x_range in range(len(simple_list)):
                for x_line in range(len(simple_list[x_range])):
                    selectors_list.append(simple_list[x_range][x_line])
            return rule_list,surrogate_list,x_ray_list,selectors_list
        except:
            pass
    
    def TRACKER_MAIN_JSON(): #tracker_point
        try:
            tracker_domain_list = []
            score_list = []
            open_doc = open("tracker_point.json",errors="replace")
            load_doc = json.loads(open_doc.read())
            SIMPLE_LOOP.FOR_LOOP_ADD(load_doc,tracker_domain_list)
            SIMPLE_LOOP.RANGE_FOR_LOOP_ADD(range(len(load_doc)),
                                        load_doc,
                                        score_list,
                                        tracker_domain_list,
                                        "score")
            zip_domain_score = zip(tracker_domain_list,score_list)
            return tracker_domain_list,score_list,zip_domain_score
        except:
            pass
        
class REQUESTS_OPS():
    def REQUESTS_SESSION(target_site=str):
        try:
            u_a_list = GET_PARAMETERS.USER_AGENT_LIST("user_agent_all.json")
            u_a_head = {"User-Agent":f"{random.choice(u_a_list)}"}
            if "https://" in target_site or "http://" in target_site:
                req_session = requests.Session()
                get_req = req_session.get(target_site,
                                          verify=False,
                                          stream=True,
                                          timeout=7,
                                          headers=u_a_head)
                status_req = get_req.status_code
                text_req = get_req.text
                content_req = get_req.content
                headers_req = get_req.headers
                cookies_req = get_req.cookies.get_dict()
                link_req = get_req.links
                history_req = get_req.history
                elapsed_req = get_req.elapsed
                encoding_req = get_req.encoding
                permanent_req = get_req.is_permanent_redirect
                url_req = get_req.url
                req_session.close()
            else:
                req_session = requests.Session()
                get_req = req_session.get("http://"+target_site,
                                          verify=False,
                                          stream=True,
                                          timeout=7,
                                          headers=u_a_head)
                status_req = get_req.status_code
                text_req = get_req.text
                content_req = get_req.content
                headers_req = get_req.headers
                cookies_req = get_req.cookies.get_dict()
                link_req = get_req.links
                history_req = get_req.history
                elapsed_req = get_req.elapsed
                encoding_req = get_req.encoding
                permanent_req = get_req.is_permanent_redirect
                url_req = get_req.url
                req_session.close()
            return status_req,text_req,content_req,\
                headers_req,cookies_req,link_req,\
                    history_req,elapsed_req,encoding_req,\
                        permanent_req,url_req
        except:
            pass
    
    def REQUESTS_INFO(target_site=str,
                                    text_online=False,
                                    content_online=False,
                                    cookies_online=False,
                                    headers_online=False,
                                    return_parser=False):
        try:
            s_r,t_r,c_r,h_r,co_r,\
                l_r,hs_r,el_r,en_r,per_r,url_r = REQUESTS_OPS.REQUESTS_SESSION(target_site)
            if content_online==True and\
                cookies_online==False and text_online==False and headers_online==False:
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("IS PERMANENT"),per_r))
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("ENCODING"),en_r))
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("ELAPSED"),el_r))
                print(c_r)
            elif content_online==False and\
                cookies_online==True and text_online==False and headers_online==False:
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("IS PERMANENT"),per_r))
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("ENCODING"),en_r))
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("ELAPSED"),el_r))
                for head_x in co_r:
                    print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING(head_x),co_r[head_x]))
            elif content_online==False and\
                cookies_online==False and text_online==True and headers_online==False:
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("IS PERMANENT"),per_r))
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("ENCODING"),en_r))
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("ELAPSED"),el_r))
                print(t_r)
            elif content_online==False and\
                cookies_online==False and text_online==False and headers_online==True:
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("IS PERMANENT"),per_r))
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("ENCODING"),en_r))
                print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING("ELAPSED"),el_r))
                for head_x in h_r:
                    print("%s : %s"%(PRINT_OPTIONS.GREEN_PRINTING(head_x),h_r[head_x]))
            else:
                pass
            if return_parser == True:
                return t_r,c_r,h_r,co_r,el_r
            else:
                pass
        except:
            pass

            
class PARSING_WEB():
    def GET_SRC(target_url=str):
        try:
            src_list=[]
            src_clean_list = []
            text_set,content_set,\
                header_set,cookies_set,\
                elapsed_set = REQUESTS_OPS.REQUESTS_INFO(target_url,
                                                         return_parser=True)
            src_parameters = re.findall(r'http.*',text_set)
            for x_src in src_parameters:
                try:
                    split_one = x_src.split('"')
                    clean_url = GET_PARAMETERS.CLEANING_URL(split_one[0])
                    src_list.append(split_one[0])
                    src_clean_list.append(clean_url)
                except:
                    pass
            src_list = GET_PARAMETERS.CLEANING_DUBLICATES(src_list)
            src_clean_list = GET_PARAMETERS.CLEANING_DUBLICATES(src_clean_list)
            return src_list,src_clean_list
        except:
            pass
    
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
        print("! %s" % (PRINT_OPTIONS.GREEN_PRINTING("IGNORE WARNINGS")))
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


class USER_OPS():
    def SHOW_INFO():
        try:
            print("""
                  
                  
             IIIIIIIIIIIIIIIIIIII        PPPPPPPPPPPPPPPPP        VVVVVVVV           VVVVVVVV
             I::::::::II::::::::I        P::::::::::::::::P       V::::::V           V::::::V
             I::::::::II::::::::I        P::::::PPPPPP:::::P      V::::::V           V::::::V
             II::::::IIII::::::II        PP:::::P     P:::::P     V::::::V           V::::::V
               I::::I    I::::I            P::::P     P:::::P      V:::::V           V:::::V 
               I::::I    I::::I            P::::P     P:::::P       V:::::V         V:::::V  
               I::::I    I::::I            P::::PPPPPP:::::P         V:::::V       V:::::V   
               I::::I    I::::I            P:::::::::::::PP           V:::::V     V:::::V    
               I::::I    I::::I            P::::PPPPPPPPP              V:::::V   V:::::V     
               I::::I    I::::I            P::::P                       V:::::V V:::::V      
               I::::I    I::::I            P::::P                        V:::::V:::::V       
               I::::I    I::::I            P::::P                         V:::::::::V        
             II::::::IIII::::::II        PP::::::PP                        V:::::::V         
             I::::::::II::::::::I ...... P::::::::P                         V:::::V          
             I01000110II00110100I .::::. P01000110P                          V:::V     --> CREATED FOR FREE NET
             IIIIIIIIIIIIIIIIIIII ...... PPPPPPPPPP                           VVV      --> open-source culture
                                                                                       --> ANTI-SPY
                  
                 -------------------------------------------------------------------------------------
                 ############################################################################################################
                 ############################################################################################################
                  
                 python IIPV_ANTISPY.py -<type_short_parameter> [target_site]
                 python IIPV_ANTISPY.py --<type_long_parameter> [target_site]
                  
                  ####   -h    --help             how to use   ####
                  
                  [ -S ]  --source                        -> GET SOURCE
                  [ -C ]  --content                       -> GET CONTENT
                  [ -s ]  --script                        -> GET SCRIPT 
                  [ -H ]  --header                        -> GET HEADER
                  [ -c ]  --cookies                       -> GET COOKIES
                  -------------------------------------------------------------------------------------
                  -------------------------------------------------------------------------------------
                  [ -M ]  --matchedip                     -> SEARCH FOR MATCHING
                  [ -m ]  --searchip                      -> SEARCH IN IP LISTS
                  [ -a ]  --malandab                      -> SEARCH IN MALWARE AND ABUSE LIST 
                  [ -P ]  --searchinall                   -> SEARCH IN ALL
                  -------------------------------------------------------------------------------------
                  -------------------------------------------------------------------------------------
                  [ -t ]  --toptracker                    -> TOP TRACKER CHECKING
                  [ -u ]  --hugesearch                    -> HUGE SEARCHING FOR TOP TRACKERS
                  [ -d ]  --detailsearch                  -> DETAIL SEARCHING 
                  [ -D ]  --searchdomainall               -> SEARCH IN DOMAIN LIST
                  -------------------------------------------------------------------------------------
                  -------------------------------------------------------------------------------------
                  [ -n ]  --allsocialchecking             -> SEARCH FOR SOCIAL SITE TRACKING
                  [ -F ]  --facebookjs                    -> SEARCH FOR FACEBOOK JS
                  -------------------------------------------------------------------------------------
                  -------------------------------------------------------------------------------------
                  
                  [It jumps from content to content to try to expose the entire network of connections]
                  
                  [ -T ]  --contenttocontent              -> CONTENT TO CONTENT SPY-CONNECTIONS
                  [ -R ]  --contenttosrc                  -> CONTENT TO SOURCE SPY-CONNECTIONS
                  [ -L ]  --srctocontent                  -> SOURCE TO CONTENT SPY-CONNECTIONS
                  [ -K ]  --srctosrc                      -> SOURCE TO SOURCE SPY-CONNECTIONS
                  [ -Z ]  --alltree                       -> FOR ALL SPY-CONNECTIONS
                  
                  
                  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                  -------------------------------------------------------------------------------------
                  [NOTED - IMPORTANT]
                  + CHECK YOUR AUTHORIZATION SETTINGS FOR BROWSERS
                  + USE VPN AND PROXIES
                  + THE SITE MAY ALSO BE PROHIBITED IN THE COUNTRIES
                  -------------------------------------------------------------------------------------
                  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                  
                  
                  """)
        except:
            pass

class MAIN_PROCESS():
    def RUN_INFO():
        run_args = OPTp(add_help_option=False,epilog="SITE INFO")
        run_args.add_option("-h",
                            "--help",
                            action="store_true",
                            dest="x_help",
                            help="HELP")
        run_args.add_option("-S",
                            "--source",
                            type="string",
                            dest="x_source",
                            help="GET MAIN SOURCE INFO")
        run_args.add_option("-C",
                            "--content",
                            type="string",
                            dest="x_content",
                            help="GET MAIN CONTENT INFO")
        run_args.add_option("-s",
                            "--script",
                            type="string",
                            dest="x_script",
                            help="GET MAIN SCRIPT INFO")
        run_args.add_option("-H",
                            "--header",
                            type="string",
                            dest="x_header",
                            help="GET HEADER INFO")
        run_args.add_option("-c",
                            "--cookies",
                            type="string",
                            dest="x_cookies",
                            help="GET COOKIES INFO")
        run_args.add_option("-M",
                            "--matchedip",
                            type="string",
                            dest="x_matchedip",
                            help="SEARCH IP IN SIMPLE TRACKING LIST")
        run_args.add_option("-m",
                            "--searchip",
                            type="string",
                            dest="x_searchip",
                            help="SEARCH IP WITH ALL SOURCE AND CONTENT")
        run_args.add_option("-a",
                            "--malandab",
                            type="string",
                            dest="x_malandab",
                            help="SEARCH IP IN MALWARE AND ABUSE LIST")
        run_args.add_option("-P",
                            "--searchinall",
                            type="string",
                            dest="x_searchinall",
                            help="SEARCH IP WITH ALL TARGETS")
        run_args.add_option("-t",
                            "--toptracker",
                            type="string",
                            dest="x_toptracker",
                            help="SEARCH IN TOP-TRACKER LIST")
        run_args.add_option("-u",
                            "--hugesearch",
                            type="string",
                            dest="x_hugesearch",
                            help="SEARCH IN HUGE LIST FOR TRACKING")
        run_args.add_option("-d",
                            "--detailsearch",
                            type="string",
                            dest="x_detailsearch",
                            help="SEARCH FOR TOP-TRACKER DETAILS")
        run_args.add_option("-D",
                            "--searchdomainall",
                            type="string",
                            dest="x_domainall",
                            help="SEARCH IN TRACKER DOMAIN LIST")
        run_args.add_option("-n",
                            "--allsocialchecking",
                            type="string",
                            dest="x_allsocial",
                            help="SEARCH FOR ALL SOCIAL TRACKING")
        run_args.add_option("-F",
                            "--facebookjs",
                            type="string",
                            dest="x_facejs",
                            help="SEARCH FOR FACEBOOK JS")
        run_args.add_option("-T",
                            "--contenttocontent",
                            type="string",
                            dest="x_ctc",
                            help="SEARCH CONTENT TO CONTENT")
        run_args.add_option("-R",
                            "--contenttosrc",
                            type="string",
                            dest="x_cts",
                            help="SEARCH CONTENT TO SOURCE")
        run_args.add_option("-L",
                            "--srctocontent",
                            type="string",
                            dest="x_srctocontent",
                            help="SEARCH SOURCE TO CONTENT")
        run_args.add_option("-K",
                            "--srctosrc",
                            type="string",
                            dest="x_srctosrc",
                            help="SEARCH SOURCE TO SOURCE")
        run_args.add_option("-Z",
                            "--alltree",
                            type="string",
                            dest="x_alltree",
                            help="SEARCH FOR ALL CONNECTIONS")
        run_ops,arq_ops = run_args.parse_args()
        if run_ops.x_source:
            site_target = str(run_ops.x_source).replace(" ","")
            src_all,src_clean = PARSING_WEB.GET_SRC(site_target)
            print("\n")
            print("[ALL] %s" % (PRINT_OPTIONS.GREEN_PRINTING("SOURCE")))
            print("\n")
            print(src_all)
            print("\n")
            print("[ALL - CLEAN] %s" % (PRINT_OPTIONS.GREEN_PRINTING("SOURCE")))
            print("\n")
            print(src_clean)
        elif run_ops.x_help:
            print("\n")
            USER_OPS.SHOW_INFO()
            pass
        elif run_ops.x_content:
            site_target = str(run_ops.x_content).replace(" ","")
            con_clean,con_all = PARSING_WEB.CONTENT_SECURITY(site_target)
            print("\n")
            print("[ALL] %s" % (PRINT_OPTIONS.GREEN_PRINTING("CONTENT")))
            print("\n")
            print(con_all)
            print("\n")
            print("[ALL - CLEAN] %s" % (PRINT_OPTIONS.GREEN_PRINTING("CONTENT")))
            print("\n")
            print(con_clean)
        elif run_ops.x_script:
            site_target = str(run_ops.x_script).replace(" ","")
            script_all = PARSING_WEB.SCRIPT_SOURCE(site_target)
            print("\n")
            print("[ALL] %s" % (PRINT_OPTIONS.GREEN_PRINTING("SCRIPT")))
            print("\n")
            print(script_all)
        elif run_ops.x_header:
            site_target = str(run_ops.x_header).replace(" ","")
            print("\n")
            REQUESTS_OPS.REQUESTS_INFO(site_target,headers_online=True)
            print("\n")
        elif run_ops.x_cookies:
            site_target = str(run_ops.x_cookies).replace(" ","")
            print("\n")
            REQUESTS_OPS.REQUESTS_INFO(site_target,cookies_online=True)
            print("\n")
        elif run_ops.x_matchedip:
            site_target = str(run_ops.x_matchedip).replace(" ","")
            print("\n")
            IP_PROCESS.MATCHED_IP(site_target)
            print("\n")
        elif run_ops.x_searchip:
            site_target = str(run_ops.x_searchip).replace(" ","")
            print("\n")
            IP_PROCESS.CATCH_IP(site_target)
            print("\n")
        elif run_ops.x_malandab:
            site_target = str(run_ops.x_malandab).replace(" ","")
            print("\n")
            IP_PROCESS.MALWARE_AND_ABUSE_IP(site_target)
            print("\n")
        elif run_ops.x_searchinall:
            site_target = str(run_ops.x_searchinall).replace(" ","")
            print("\n")
            IP_PROCESS.ADD_LIST_CATCH(site_target)
            print("\n")
        elif run_ops.x_toptracker:
            site_target = str(run_ops.x_toptracker).replace(" ","")
            print("\n")
            CONTROLLING_OPS.TOP_TRACKER_OPS(site_target)
            print("\n")
        elif run_ops.x_hugesearch:
            site_target = str(run_ops.x_hugesearch).replace(" ","")
            print("\n")
            CONTROLLING_OPS.HUGE_DOMAIN_OPS(site_target)
            print("\n")
        elif run_ops.x_detailsearch:
            site_target = str(run_ops.x_detailsearch).replace(" ","")
            print("\n")
            DETAILS_OPS.TOP_TRACKER_DETAILS(site_target)
            print("\n")
        elif run_ops.x_domainall:
            site_target = str(run_ops.x_domainall).replace(" ","")
            print("\n")
            DETAILS_OPS.HUGE_DOMAIN_DETAILS(site_target)
            print("\n")
        elif run_ops.x_allsocial:
            site_target = str(run_ops.x_allsocial).replace(" ","")
            print("\n")
            SOCIAL_SITE_OPS.ALL_SITE_CHECKING(site_target)
            print("\n")
        elif run_ops.x_facejs:
            site_target = str(run_ops.x_facejs).replace(" ","")
            print("\n")
            FACEBOOK_SCRIPT_OPS.CHECK_JS_AND_OPERATIONS(site_target)
            print("\n")
        elif run_ops.x_ctc:
            site_target = str(run_ops.x_ctc).replace(" ","")
            print("\n")
            ctc_list = CONNECT_TREE.JUMP_TO_CONTENT_TO_CONTENT(site_target)
            print(ctc_list)
            print("\n")
        elif run_ops.x_cts:
            site_target = str(run_ops.x_cts).replace(" ","")
            print("\n")
            cts_list = CONNECT_TREE.JUMP_TO_CONTENT_TO_SRC(site_target)
            print(cts_list)
            print("\n")
        elif run_ops.x_srctocontent:
            site_target = str(run_ops.x_srctocontent).replace(" ","")
            print("\n")
            stc_list = CONNECT_TREE.JUMP_TO_SRC_TO_CONTENT(site_target)
            print(stc_list)
            print("\n")
        elif run_ops.x_srctosrc:
            site_target = str(run_ops.x_srctosrc).replace(" ","")
            print("\n")
            sts_list = CONNECT_TREE.JUMP_TO_SRC_TO_SRC(site_target)
            print(sts_list)
            print("\n")
        elif run_ops.x_alltree:
            site_target = str(run_ops.x_alltree).replace(" ","")
            print("\n")
            CONNECT_TREE.IP_TREE_ALL(site_target)
            print("\n")
        else:
            USER_OPS.SHOW_INFO()
            pass
        

if __name__ == "__main__":
    try:
        MAIN_PROCESS.RUN_INFO()
    except:
        USER_OPS.SHOW_INFO()
        pass        

