# coding=utf-8
__author__ = 'songqi'
import xlrd
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json_dicts

def get_json(json_type):
    case_excel = "data_excel\\" + json_type + ".xlsx"
    print "case_excel:" + case_excel
    json_keys = json_dicts.get_json_dicts(json_type)
    xlrd.Book.encoding = "gbk"
    workbook = xlrd.open_workbook(case_excel)
    sheet0 = workbook.sheet_by_index(0)
    rows_num = sheet0.nrows
    col_num = sheet0.ncols
    if rows_num > 1:
        for i in range(1, rows_num):
            print "="*200
            # Build JSON dict
            tmp_dict = {}
            case_param = {}
            for j in range(0, col_num):
                param_key = str(sheet0.cell_value(0, int(j)))
                if param_key in json_keys:
                    a = sheet0.cell_value(int(i), int(j))
                    b = str(a)
                    tmp_dict[sheet0.cell_value(0, int(j))] = b.rstrip('0').strip('.') if '.' in b else b
                elif param_key == 'ex_result':
                    try:
                        b = str(sheet0.cell_value(int(i), int(j)))
                        case_param["ex_result"] = b.rstrip('0').strip('.') if '.' in b else b
                    except KeyError:
                        case_param["eex_result"] = "No ex_result,please check your case"
                elif str(sheet0.cell_value(0, int(j))) == 'key_result':
                    try:
                        case_param["key_result"] = str(sheet0.cell_value(int(i), int(j)))
                    except KeyError:
                        case_param["key_result"] = "No ex_result,No key_result,please check your case!!!"
                elif str(sheet0.cell_value(0, int(j))) == 'topic':
                    try:
                        case_param["topic"] = str(sheet0.cell_value(int(i), int(j)))
                        print case_param["topic"]
                    except KeyError:
                        case_param["key_result"] = "No ex_result,No key_result,please check your case!!!"
            # After building JSON dict,run Json post
            data_json = str(json.dumps(tmp_dict, ensure_ascii=False))
            case_param["data_json"] = data_json
    return case_param

def get_response(json_type, url):
    data_json = get_json(json_type)["data_json"]
    headers = {'Content-Type': 'application/json'}
    request = urllib2.Request(url=url, headers=headers, data=data_json)
    response = urllib2.urlopen(request)
    return response
