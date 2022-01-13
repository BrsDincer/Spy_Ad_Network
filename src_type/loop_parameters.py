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
        clean_list = list(dict.fromkeys(ops_list))
        return clean_list
    
    def CLEANING_URL(target_site=str):
        new_site = target_site.replace("http://","").replace("https://","").replace("www.","")
        split_site = new_site.split("/")
        return split_site[0]
    
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
    
    def HUGE_TRACKER_DOMAIN_JSON(): #tracker_main
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
    
    def COMMON_SITE_JSON():
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
    
    def VERIZON_SITE_JSON():
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
    
    def FACEBOOK_SITE_JSON():
        facebook_site_list = []
        open_doc = open("tracker_main.json",errors="replace")
        load_doc = json.loads(open_doc.read())
        facebook_domain = load_doc["entities"]["Facebook, Inc."]["domains"]
        for i_v in facebook_domain:
            facebook_site_list.append(i_v)
        return facebook_site_list
    
    def AKAMAI_SITE_JSON():
        akamai_site_list = []
        open_doc = open("tracker_main.json",errors="replace")
        load_doc = json.loads(open_doc.read())
        akamai_domain = load_doc["entities"]["Akamai Technologies"]["domains"]
        for i_v in akamai_domain:
            akamai_site_list.append(i_v)
        return akamai_site_list
        
    
    def SOCIAL_COOKIES_JSON(): #cookies_tracker
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
    
    def TRACKER_DOMAIN_JSON(): #tracker_blocking
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
    
    def FACEBOOK_JS_JSON(): #social_ctp
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
    
    def TRACKER_MAIN_JSON(): #tracker_point
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