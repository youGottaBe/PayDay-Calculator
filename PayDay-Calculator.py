# calculate 2 week work check 


fwkhrs = input('Enter Total Work Hours for Week 1: ')
swkhrs = input('Enter Total Work Hours for Week 2: ')
rt = input('Enter hourly pay rate: ')


try:
    fhr = float(fwkhrs)
    shr = float(swkhrs)
    frt = float(rt)
except:
    print('Error! Please enter a number: ')
    quit()


if fhr <= 40 and shr <= 40:
    fregular = fhr * frt
    sregular = shr * frt
    regaftax1 = fregular * .79
    regaftax2 = sregular * .79
    afregftaxgross = regaftax1 + regaftax2
    print("Gross Pay Week 1:" , fregular)
    print("After Tax Week 1:", regaftax1)
    print("Gross Pay Week 2:" , sregular)
    print("After Tax Week 2:", regaftax2)
    print('TOTAL GROSS:', fregular + sregular)
    print('AFTER TAX GROSS:', afregftaxgross)
   

elif fhr > 40 or shr > 40 :
    fot = (fhr - 40) * (frt * 1.5)
    sot = (shr - 40) * (frt * 1.5)
    freg = (40 * frt)
    ftot = fot + freg
    sreg = (40 * frt)
    stot = sot + sreg
    aftax1 = ftot * .79
    aftax2 = stot * .79
    totgross = ftot + stot
    aftaxgross = aftax1 + aftax2
    print("Regular Pay:", freg)
    print("Overtime Pay Week 1:", fot)
    print("Gross Pay Week 1:", ftot)
    print("After Tax Week 1:", aftax1)
    print("Regular Pay:", sreg)
    print("Overtime Pay Week 2:", sot)
    print("Gross Pay Week 2:", stot)
    print("After Tax Week 2:", aftax2)
    print("TOTAL GROSS PAY", totgross)
    print("TOTAL AFTER TAX:", aftaxgross)