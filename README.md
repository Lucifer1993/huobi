# huobi
参考火币网API写的wrapper

# 操作系统
linux/mac

# 运行环境
python2.7

# 模块
termcolor

# 使用说明
1.首先在火币网申请API KEY，编辑Utils.py将API KEY依次填入.
2.查看资产详情
 eg. python mainhuobi.py -v
3.查询历史订单
 eg. python mainhuobi.py -o btc(ltc)           btc=比特币  ltc=莱特币 下同
4.查询正在进行的委托
 eg. python mainhuobi.py -e btc(ltc)
5.取消委托
 eg. python mainhuobi.py -c btc(ltc) 委托id
6.限价交易
 eg. python mainhuobi.py -l btc(ltc) -b(-s) 限价 数量   -b=买  -s=卖
7.市价交易
 eg. python mainhuobi.py -m btc(ltc) -b(-s) 数量 
 
 
