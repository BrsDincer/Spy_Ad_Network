class REQUESTS_OPS():
    def REQUESTS_SESSION(target_site=str):
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
    
    def REQUESTS_INFO(target_site=str,
                                    text_online=False,
                                    content_online=False,
                                    cookies_online=False,
                                    headers_online=False,
                                    return_parser=False):
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