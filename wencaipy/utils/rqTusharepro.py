import tushare as ts 

try:
    token = "2f8fd6706d131778c82e15d4231d2776aa13c6e4234d5496b3ebe7b2"
    #ts.set_token(token)
    pro = ts.pro_api(token)
    #print('tushare token set ok , can use pro as api!')
except Exception as e:
    print(e)
    


