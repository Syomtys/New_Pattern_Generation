
def Create_Pats_html(lang_opt):
    import json
    with open('../script/language_all_list.json','r') as file_json:
        full_list = json.load(file_json)[lang_opt]["html_lang"]
    list_html_files = {}
    for file_name in full_list:
        html_pat = '<html>\n<head>\n\t<meta charset="utf-8"/>\n\t<title>T1T1TL3</title>\n\t<style>\n\tbody, html{\n\tmin-height: 100%;\n\tmargin:0px;\n\tpadding: 0px;\n\t}\n\tbody{\n\t\tpadding-top: 40px;\n\t\tpadding-bottom: 40px;\n\t\tbackground:#bebebe\n\t}\n\tdiv{\n\t\tmax-width: 800px;\n\t\tfont-size:19px;\n\t\tbackground:#ebebeb;\n\t\tmargin: 0px auto;\n\t\tbackground: #fff;\n\t\tpadding: 20px 40px 40px 40px;\n\t\tborder: 5px solid #989898;\n\t\tline-height: 20px;\n\t}\n\tdiv h1{\n\t\tcolor: #3B6A7C;\n\t\tmargin-bottom: 30px;\n\t\ttext-align: center;\n\t}\n\t@media screen and (max-width: 540px){\n\tdiv{\n\t\tpadding:0 10px;\n\t}\n\tbody{\n\t\tpadding-bottom:40px;\n\t}\n\tdiv h1{\n\t\tfont-size: 27px;\n\t}\n\t</style>\n</head>\n<body>\n<div>\n<h1>HI1H</h1>\n<p>PA11P</p>\n</div>\n</body>\n</html>'
        # print(file_name)
        for tags in full_list[file_name]:
            html_pat = html_pat.replace(tags, full_list[file_name][tags])
            # print(tags + ' - '+ full_list[file_name][tags])
        list_html_files[f'{file_name}.html'] = html_pat
    return list_html_files
        # for file in list_html_files:
        #     with open(file, 'w') as file_html:
        #         file_html.write(list_html_files[file])
# Create_Pats_html()

