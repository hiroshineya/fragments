#!/usr/bin/python
# -*- coding: utf-8 -*-
# 元利均等返済

# 元利均等返済方式(毎月返済, 端数切捨て)
# @param debt           借入金
# @param bonus          借入金の内、ボーナス返済の割合(未実装)
# @param period_y       返済期間年
# @param period_m       返済期間月
# @param intrst         金利(当初金利)
# @return [[支払い額, 元金充当,利息], ・・・]
def calc_loan_level_payment(debt, bonus, period_y, period_m, intrst):
    result = []
    pay_times = period_y * 12 + period_m
    # 月利にする
    calc_intrst = intrst / 100.0 / 12.0
    
    src_num = debt * calc_intrst * ((1+calc_intrst) ** pay_times)
    div_num = ((1+calc_intrst) ** pay_times) - 1
    a_pay = int(src_num / div_num)
    a_intrst = 0
    a_appropriation = 0
    principal = debt
    for i in range(0, pay_times):
        a_intrst = int(principal * calc_intrst)
        a_appropriation = a_pay - a_intrst
        principal = principal - a_appropriation
        if principal < 0:
            a_pay = a_pay + principal
            principal = 0
        result.append([a_pay, a_appropriation, a_intrst])
    
    return result


if __name__ == "__main__":
    result = calc_loan_level_payment(10000000, 0, 10, 0, 2)
    print result

