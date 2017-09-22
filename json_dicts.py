# coding=utf-8
"""
@author = 'songqi'
"""

def get_json_dicts(json_type):
    json_dicts = {}
    # 评分评级卡
    json_dicts['Level'] = ['studentEducation', 'schoolType', 'mobileMoxieDuration', 'tongdunFinalScore', 'zhiMaScore']
    json_dicts['Level_Result'] = ['level']
    # 大准入大额借
    json_dicts['ML'] = ["idHitOurBlackList", "mobileHitOurBlackList", "idHitTongDunLoanBlackList",
                           "mobileHitTongDunLoanBlackList", "idNameHitTongDunFuzzyLoanBlackList",
                           "idHitTongDunCourtBlackList", "idNameHitTongDunFuzzyCourtBlackList",
                           "idHitTongDunCrimeBlackList", "idHitTongDunCourtExecuteList",
                           "idNameHitTongDunFuzzyCourtExecuteList", "idHitTongDunLegalPersonBlackList",
                           "mobileHitTongDunLegalPersonBlackList",
                           "mobileHitTongDunLoanBlackIntermediary",
                           "userAge", "idHitTongDunLoanBlackList",
                            "hitTongDunRepeateLoanOneWeekend",
                            "hitTongDunRepeateLoanOneMonth",
                            "hitTongDunRepeateLoanThreeMonth",
                            "tongDunRepeateLoanOneWeekendDivOneMonth",
                            "type"]
    json_dicts['ML_Result'] = ['annotations']
    # 大准入闪电借
    json_dicts['MS'] = ["idHitOurBlackList", "mobileHitOurBlackList", "idHitTongDunLoanBlackList",
                        "mobileHitTongDunLoanBlackList", "idNameHitTongDunFuzzyLoanBlackList",
                        "idHitTongDunCourtBlackList", "idNameHitTongDunFuzzyCourtBlackList",
                        "idHitTongDunCrimeBlackList", "idHitTongDunCourtExecuteList",
                        "idNameHitTongDunFuzzyCourtExecuteList", "idHitTongDunLegalPersonBlackList",
                        "mobileHitTongDunLegalPersonBlackList",
                        "mobileHitTongDunLoanBlackIntermediary",
                        "userAge", "idHitTongDunLoanBlackList",
                        "hitTongDunRepeateLoanOneWeekend",
                        "hitTongDunRepeateLoanOneMonth",
                        "hitTongDunRepeateLoanThreeMonth",
                        "tongDunRepeateLoanOneWeekendDivOneMonth",
                        "hitZhongzhichengBlackListCount",
                        "hitZhongzhichengTenantCount",
                        "hitBaiqishiRiskUserDecisionReject",
                        "type"]
    json_dicts['MS_Result'] = ['annotations']
    # 小准入大额蓝领
    json_dicts['NLB'] = [
        "userAge", "zhiMaScore", "zhiMaIvsScore", "hitTongDunRepeateLoanOneWeekend", "hitTongDunRepeateLoanOneMonth",
        "hitTongDunRepeateLoanThreeMonth", "tongdunFinalScore", "mobileMoxieDuration", "tianXingDuration",
        "type"
    ]
    json_dicts['NLB_Result'] = ['annotations']
    # 小准入大额白领
    json_dicts['NLW'] = [
        "userAge", "zhiMaScore", "zhiMaIvsScore", "hitTongDunRepeateLoanOneWeekend", "hitTongDunRepeateLoanOneMonth",
        "hitTongDunRepeateLoanThreeMonth", "tongdunFinalScore", "mobileMoxieDuration", "graduateYears", "tianXingDuration",
        "type"
    ]
    json_dicts['NLW_Result'] = ['annotations']
    # 小准入小额白领
    json_dicts['NSW'] = [
        "userAge", "zhiMaScore", "zhiMaIvsScore", "hitTongDunRepeateLoanOneWeekend", "hitTongDunRepeateLoanOneMonth",
        "hitTongDunRepeateLoanThreeMonth", "tongdunFinalScore", "mobileMoxieDuration", "graduateYears", "tianXingDuration",
        "type"
    ]
    json_dicts['NSW_Result'] = ['annotations']
    # 小准入小额蓝领
    json_dicts['NSB'] = [
        "userAge", "zhiMaScore", "zhiMaIvsScore", "hitTongDunRepeateLoanOneWeekend", "hitTongDunRepeateLoanOneMonth",
        "hitTongDunRepeateLoanThreeMonth", "tongdunFinalScore", "mobileMoxieDuration", "graduateYears", "tianXingDuration",
        "type"
    ]
    json_dicts['NSB_Result'] = ['annotations']
    # 芝麻IVS
    json_dicts['ZMIVS'] = [
        "zhiMaIvsScore",
        "type"
    ]
    json_dicts['ZMIVS_Result'] = ['annotations']
    # 芝麻行业关注
    json_dicts['FOCUS'] = [
        "hitZhiMaFocus",
        "type"
    ]
    json_dicts['FOCUS_Result'] = ['annotations']
    # RLC
    json_dicts['RLC'] = [
        "faceSimilarPercent", "loanStatusOverdue", "maxOverDueDays", "isRetainedUser",
        "rejectIn30Days", "userContactCount", "userContactHighDangerCount",	"userContactHighDangerRate",
        "type"
    ]
    json_dicts['RLC_Result'] = ['annotations']

    # RSD
    json_dicts['RSD'] = [
        "faceSimilarPercent", "loanStatusOverdue", "maxOverDueDays", "isRetainedUser",
        "rejectIn30Days", "userContactCount", "userContactHighDangerCount",	"userContactHighDangerRate",
        "type"
    ]
    json_dicts['RSD_Result'] = ['annotations']
    # RSR
    json_dicts['RSR'] = [
        "countInLBSCodeOneDay", "borrowTimeShortInDevice", "moveDistanceExceptionInDevice", "oneHourManyAccountInDevice",
        "oneDayManyAccountInDevice", "oneHourMuchAccountInDevice", "oneDayMuchAccountInDevice",	"sevenDayMuchAccountInDevice",
        "oneHourMuchAccountAll", "oneDayMuchAccountAll", "sevenDayMuchAccountAll", "lbsCodeNotPeerNumTopThree3m",
        "lbsCodeNotPeerNumTopThree6m", "faceSimilarPercent", "emayIsBlack", "baiduBlackLevel", "baiduBlackReason",
        "type"
    ]
    json_dicts['RSR_Result'] = ['annotations']
    # BLD
    json_dicts['BLD'] = [
        "bizCode", "hasSuccessLoan", "hitTongDunRepeateLoansixMonth", "badDebtFriends", "maxOverDueDays", "zhiMaScore",
        "userGender", "eduDegree"
    ]
    # MZJK
    json_dicts['MZJK'] = [
        "bizCode", "hasSuccessLoan", "hitTongDunRepeateLoansixMonth", "badDebtFriends", "maxOverDueDays", "zhiMaScore",
        "userGender", "eduDegree"
    ]
    # BLD0831AJ
    json_dicts['BLD0831AJ'] = [
        "type", "isRetainedUser", "maxOverDueDays", "idHitOurBlackList", "mobileHitOurBlackList", "idHitTongDunLoanBlackList", "mobileHitTongDunLoanBlackList",
        "idNameHitTongDunFuzzyLoanBlackList", "idHitTongDunCourtBlackList", "idNameHitTongDunFuzzyCourtBlackList", "idHitTongDunCrimeBlackList", "idHitTongDunCourtExecuteList",
        "idNameHitTongDunFuzzyCourtExecuteList", "idHitTongDunLegalPersonBlackList", "mobileHitTongDunLegalPersonBlackList", "mobileHitTongDunLoanBlackIntermediary",
        "hitZhongzhichengBlackListCount", "hitZhongzhichengTenantCount", "hitBaiqishiRiskUserDecisionReject", "faceSimilarPercent",
        "userAge", "hitTongDunRepeateLoanOneMonth", "zhiMaScore"
    ]
    return json_dicts[json_type]
