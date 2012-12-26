#!/usr/bin/python
# -*- coding: utf-8 -*-
# ローン、アドオン方式算出
# 小数点以下利息に関しては切り捨てする。

# アドオン率での算出
# @param debt 借入金
# @param times 返済回数
# @param rate アドオン率
# @return [[元金充当, 利息], ・・・]
def calc_loan_addon(debt, times, rate):
    payments = []
    hrate = rate / 100.0
    print "total interest:%d" % (debt*hrate)
    a_interest = int( round(debt * hrate, 0) / times )
    a_principal = int( debt / times )
    rest_p = debt - (a_principal*times)
    for i in range(0, times):
        payments.append([a_principal, a_interest])
    payments[0][0] = payments[0][0] + rest_p
    
    return payments

# 実質年率での算出
# @param debt 借入金
# @param times 返済回数
# @param rate 実質年率
# @return [[元金充当, 利息], ・・・]
def calc_loan_addon_w_annual_rate(debt, times, rate):
    payments = []
    hrate = round(rate / 12.0 / 100.0, 8)
    principal = debt
    standard_payment = 0
    total_intrst = 0
    for i in range(times, 0, -1):
        calc_intrst = round(principal * hrate, 0)
        kn = 1 - ( (1+hrate) ** (i*-1.0) )
        if i == times:
            standard_payment = round(calc_intrst / kn, 0)
        pay_principal = standard_payment - calc_intrst
        principal = principal - pay_principal
        total_intrst = total_intrst + calc_intrst
    
    a_principal = int( round(debt / times, 0) )
    a_intrst = int( round(total_intrst / times, 0) )
    rest_p = debt - (a_principal * times)
    for i in range(0, times):
        payments.append([a_principal, a_intrst])
    payments[0][0] = payments[0][0] + rest_p
    
    return payments


if __name__ == "__main__":
    print 'add-on'
    result = calc_loan_addon(550000, 24, 2)
    print result
    print ''
    print 'w_annual_rate'
    result = calc_loan_addon_w_annual_rate(550000, 24, 1.908)
    print result

