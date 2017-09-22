# coding=utf-8
__author__ = 'songqi'
import xlrd
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json_dicts

import logging
import logging.handlers
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='interface_test.log',
                    filemode='w')

#################################################################################################
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
reload(sys)
sys.setdefaultencoding('utf-8')


def read_excel(json_type, interface_type, url):
    logging.info("="*30 + json_type + "_test" + "="*30)
    case_excel = "data_excel\\" + json_type + ".xlsx"
    json_keys = json_dicts.get_json_dicts(json_type)
    logging.info("json_keys is :")
    logging.info(json_keys)
    xlrd.Book.encoding = "gbk"
    workbook = xlrd.open_workbook(case_excel)
    sheet0 = workbook.sheet_by_index(0)
    rows_num = sheet0.nrows
    col_num = sheet0.ncols
    if rows_num > 1:
        for i in range(1, rows_num):
            logging.info("="*200)
            # Build JSON dict
            tmp_dict = {}
            for j in range(0, col_num):
                if str(sheet0.cell_value(0, int(j))) in json_keys:
                    a = sheet0.cell_value(int(i), int(j))
                    b = str(a)
                    tmp = b.rstrip('0').strip('.') if '.' in b else b
                    if tmp:
                        tmp_dict[sheet0.cell_value(0, int(j))] = tmp
                    else:
                        tmp_dict[sheet0.cell_value(0, int(j))] = "-1"
                elif str(sheet0.cell_value(0, int(j))) == 'ex_result':
                    try:
                        b = str(sheet0.cell_value(int(i), int(j)))
                        ex_result = b.rstrip('0').strip('.') if '.' in b else b
                    except KeyError:
                        ex_result = "No ex_result,please check your case"
                elif str(sheet0.cell_value(0, int(j))) == 'key_result':
                    try:
                        key_result = str(sheet0.cell_value(int(i), int(j)))
                    except KeyError:
                        key_result = "No ex_result,No key_result,please check your case!!!"
                elif str(sheet0.cell_value(0, int(j))) == 'topic':
                    try:
                        topic = str(sheet0.cell_value(int(i), int(j)))
                        logging.info("topic is:"+ str(topic))
                    except KeyError:
                        key_result = "No ex_result,No key_result,please check your case!!!"
            # After building JSON dict,run Json post
            data_json = str(json.dumps(tmp_dict, ensure_ascii=False))
            logging.info(data_json)
            headers = {'Content-Type': 'application/json'}
            request = urllib2.Request(url=url, headers=headers, data=data_json)
            response = urllib2.urlopen(request)
            # Response Analysis
            for j in response:
                flag_key_result = 0
                k = json.loads(j)
                if interface_type == 'doAccess':
                    re_result_list = k['data']['data']
                    for annotations_dict in re_result_list['annotations']:
                        main_rule_id = annotations_dict['ruleId']
                        main_rule_name = annotations_dict['ruleName']
                        main_rule_result_code = annotations_dict['ruleResultCode']
                        sub_rules_list = annotations_dict['subRules']  # 通过subRules找到对应的待测返回报文
                        for sub_rules_dict in sub_rules_list:
                            rule_name = sub_rules_dict['remark']
                            if rule_name.__eq__(key_result):
                                logging.info(u"找到待测规则：" + str(sub_rules_dict['remark']) + "。检查ruleResultCode")
                                logging.info('rule_id = ' + str(sub_rules_dict['ruleId']))
                                re_result = sub_rules_dict['ruleResultCode']
                                logging.info("re_result: " + str(re_result))
                                logging.info('*'*30)
                                logging.info('main_ruleId:' + str(main_rule_id))
                                logging.info('main_ruleName:' + str(main_rule_name))
                                logging.info('main_ruleResultCode:' + str(main_rule_result_code))
                                logging.info('*'*30)
                                flag_key_result = 1
                elif interface_type == 'doScore':
                    if k['data'][key_result]:
                        re_result = k['data'][key_result]
                    else:
                        logging.info(key_result.join(' is null'))
                        re_result = 'null'
                    msg = u"找到待测规则：" + str(key_result) + "。检查ruleResultCode"
                    logging.info(msg)
                    msg = "re_result: " + str(re_result)
                    logging.info(msg)
                else:
                    logging.info('Unknown Interface')
                    break
                ########
                if flag_key_result == 1:
                    pass
                else:
                    logging.info(u'没有找到待测规则:"' + str(key_result) + u'"')
                if re_result:
                    if re_result.__eq__(ex_result):
                        logging.info(u"和预期结果一致")
                        pass
                    else:
                        logging.info("*" * 100)
                        logging.info(u"和预期结果不一致")
                        logging.info(i)
                        logging.info(topic)
                        logging.info("jason=")
                        logging.info(data_json)
                        logging.info("返回值：")
                        logging.info(k['data']['data'])
                        logging.info("预期值：")
                        logging.info(ex_result)
                        logging.info("=" * 100)
                else:
                    logging.info(u"无法找到待测字段，请检查用例")
                    logging.info(re_result)


def run_rule_test(env, interface_type, *args):
    url = "http://rule." + env + ".com/rule-app/ruleapi/" + interface_type
    for i in args:
        read_excel(i, interface_type,  url)


if __name__ == '__main__':
    run_rule_test('stb', 'doAccess', 'BLD0831AJ')
    run_rule_test('stb', 'doAccess', 'ML', 'MS', 'NLB', 'NLW', 'NSB', 'NSW', 'FOCUS', 'RLC', 'RSD', 'RSR')
    run_rule_test('stb', 'doScore', 'BLD')
"""
    read_excel('BLD0831AJ', url)

    read_excel('ML', url)

    read_excel('MS', url)

    read_excel('NLB', url)

    read_excel('NLW', url)

    read_excel('NSB', url)

    read_excel('NSW', url)

    read_excel('FOCUS', url)

    read_excel('RLC', url)

    read_excel('RSD', url)

    read_excel('RSR', url)
"""