
def money_calc (summ):
    umeshaetsa_tis = 0
    umeshaetsa_patsot = 0
    umeshaetsa_sot = 0
    umeshaetsa_patdes = 0
    umeshaetsa_des = 0
    umeshaetsa_pat = 0
    umeshaetsa_ed = 0
    
    umeshaetsa_tis = summ // 1000
    promeshut =  summ - umeshaetsa_tis*1000
    umeshaetsa_patsot = promeshut // 500
    promeshut_2 = promeshut - umeshaetsa_patsot*500
    umeshaetsa_sot = promeshut_2 // 100
    promeshut_3 = promeshut_2 - umeshaetsa_sot*100
    umeshaetsa_patdes = promeshut_3 // 50
    promeshut_4 = promeshut_3 - umeshaetsa_patdes*50
    umeshaetsa_des = promeshut_4 // 10
    promeshut_5 = promeshut_4 - umeshaetsa_des*10
    umeshaetsa_pat = promeshut_5 // 5
    promeshut_6 = promeshut_5 - umeshaetsa_pat*5
    umeshaetsa_ed = promeshut_6 // 1
    nominal = {'тысяча': umeshaetsa_tis, 'пятьсот': umeshaetsa_patsot,'сто': umeshaetsa_sot, 'пятьдесят': umeshaetsa_patdes, 'десять': umeshaetsa_des, 'пять': umeshaetsa_pat, 'рубль': umeshaetsa_ed }


    return nominal

print(money_calc(1738))
