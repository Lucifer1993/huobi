#coding=utf-8
'''
@prog: huobi.com interface wrapper
@author: Lucifer
@date: 2017-7-8
@version: v1.0
@bugs: hanmengzi1993@gmail.com       
'''

import sys
import time
from termcolor import cprint
from Util import *
import HuobiService

reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == "__main__":
    if sys.argv[1] == "-v":
        accountdic = dict(HuobiService.getAccountInfo(ACCOUNT_INFO))
        cprint("[*] 可用比特币: "+accountdic['available_btc_display'], "green")
        cprint("[*] 可用莱特币: "+accountdic['available_ltc_display'], "green")
        cprint("[*] 可用人民币: "+accountdic['available_cny_display'], "green")
        cprint("[*] 借贷人民币: "+accountdic['loan_cny_display'], "yellow")
        cprint("[*] 借贷比特币: "+accountdic['loan_btc_display'], "yellow")
        cprint("[*] 借贷莱特币: "+accountdic['loan_ltc_display'], "yellow")
        cprint("[*] 冻结人民币: "+accountdic['frozen_cny_display'], "red")
        cprint("[*] 冻结比特币: "+accountdic['frozen_btc_display'], "red")
        cprint("[*] 冻结莱特币: "+accountdic['frozen_ltc_display'], "red")
        cprint("[*] 资产总值: "+accountdic['total'], "white")

    elif sys.argv[1] == "-o":
        if sys.argv[2] == "btc":
            cprint("[*] 查询比特币历史订单: ", "cyan")
            count = 0
            orders = HuobiService.getNewDealOrders(1,NEW_DEAL_ORDERS)
            if len(orders) == 0:
                cprint("[!] 比特币订单为空")
            for order in orders:
                count += 1
                if order['type'] == 1:
                    otype = "限价买"
                elif order['type'] == 2:
                    otype = "限价卖"
                elif order['type'] == 3:
                    otype = "市价买"
                else:
                    otype = "市价卖"
                if order['status'] == 0:
                    status = "未成交"
                elif order['status'] == 1:
                    status = "部分成交"
                elif order['status'] == 2:
                    status = "已完成"
                else:
                    status = "已取消"
                print "第" + str(count) + "条订单信息"
                print "---------------------------------------"
                cprint("[*] 委托订单id: " + str(order['id']), "white")
                cprint("[*] 委托时间: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(order['order_time'])), "white")
                cprint("[*] 最后成交时间: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(order['last_processed_time'])), "white")
                cprint("[*] 委托类型: " + otype, "white")
                cprint("[*] 委托价格: " + order['order_price'], "white")
                cprint("[*] 委托数量: " + order['order_amount'], "white")
                cprint("[*] 已经完成的数量: " + order['processed_amount'], "white")
                cprint("[*] 订单状态: " + status, "white")
                print "---------------------------------------"
                print
                print

        if sys.argv[2] == "ltc":
            cprint("[*] 查询莱特币历史订单: ", "cyan")
            count = 0
            orders = HuobiService.getNewDealOrders(2,NEW_DEAL_ORDERS)
            if len(orders) == 0:
                cprint("[!] 莱特币订单为空")
            for order in orders:
                count += 1
                if order['type'] == 1:
                    otype = "限价买"
                elif order['type'] == 2:
                    otype = "限价卖"
                elif order['type'] == 3:
                    otype = "市价买"
                else:
                    otype = "市价卖"
                if order['status'] == 0:
                    status = "未成交"
                elif order['status'] == 1:
                    status = "部分成交"
                elif order['status'] == 2:
                    status = "已完成"
                else:
                    status = "已取消"
                print "第" + str(count) + "条订单信息"
                print "---------------------------------------"
                cprint("[*] 委托订单id: " + str(order['id']), "white")
                cprint("[*] 委托时间: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(order['order_time'])), "white")
                cprint("[*] 最后成交时间: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(order['last_processed_time'])), "white")
                cprint("[*] 委托类型: " + otype, "white")
                cprint("[*] 委托价格: " + order['order_price'], "white")
                cprint("[*] 委托数量: " + order['order_amount'], "white")
                cprint("[*] 已经完成的数量: " + order['processed_amount'], "white")
                cprint("[*] 订单状态: " + status, "white")

                print "---------------------------------------"
                print
                print

    elif sys.argv[1] == "-e":
        if sys.argv[2] == "ltc":
            cprint("[*] 正在进行的莱特币委托: ", "cyan")
            count = 0
            entrusts = HuobiService.getOrders(2,GET_ORDERS)
            if len(entrusts) == 0:
                cprint("[!] 莱特币委托为空", "red")
            for entrust in entrusts:
                count += 1
                if entrust['type'] == 1:
                    etype = "买"
                else:
                    etype = "卖"
                print "第" + str(count) + "条委托信息"
                print "---------------------------------------"
                cprint("[*] 委托id: " + str(entrust['id']), "white")
                cprint("[*] 委托时间: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(entrust['order_time'])), "white")
                cprint("[*] 委托类型: " + etype, "white")
                cprint("[*] 委托价格: " + entrust['order_price'], "white")
                cprint("[*] 委托数量: "+ entrust['order_amount'], "white")
                cprint("[*] 已经完成的数量: " + entrust['processed_amount'], "white")
                print "---------------------------------------"
                print
                print
        if sys.argv[2] == "btc":
            cprint("[*] 正在进行的比特币委托: ", "cyan")
            count = 0
            entrusts = HuobiService.getOrders(1,GET_ORDERS)
            if len(entrusts) == 0:
                cprint("[!] 比特币委托为空", "red")
            for entrust in entrusts:
                count += 1
                if entrust['type'] == 1:
                    etype = "买"
                else:
                    etype = "卖"
                print "第" + str(count) + "条委托信息"
                print "---------------------------------------"
                cprint("[*] 委托id: " + str(entrust['id']), "white")
                cprint("[*] 委托时间: " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(entrust['order_time'])), "white")
                cprint("[*] 委托类型: " + etype, "white")
                cprint("[*] 委托价格: " + entrust['order_price'], "white")
                cprint("[*] 委托数量: "+ entrust['order_amount'], "white")
                cprint("[*] 已经完成的数量: " + entrust['processed_amount'], "white")
                print "---------------------------------------"
                print
                print

    elif sys.argv[1] == "-c":
        if sys.argv[2] == "btc":
            results = HuobiService.cancelOrder(1,sys.argv[3].strip(),CANCEL_ORDER)
            if results.has_key('msg'):
                cprint("[!] "+results['msg'], "red")
            elif results.has_key('result') and results['result'] == "success":
                cprint("[+] 比特币委托取消成功", "green")
            else:
                pass
        if sys.argv[2] == "ltc":
            results = HuobiService.cancelOrder(2,sys.argv[3].strip(),CANCEL_ORDER)
            if results.has_key('msg'):
                cprint("[!] "+results['msg'], "red")
            elif results.has_key('result') and results['result'] == "success":
                cprint("[+] 莱特币委托取消成功", "green")
            else:
                pass

    elif sys.argv[1] == "-l":
        if sys.argv[2] == "btc":
            if sys.argv[3] == "-b":
                limitprice = HuobiService.buy(1,sys.argv[4].strip(),sys.argv[5].strip(),None,None,BUY)
                if limitprice.has_key('msg'):
                    cprint("[!] 现价买入比特币失败,"+limitprice['msg'], "red")
                if limitprice.has_key('result') and limitprice['result'] == "success":
                    cprint("[+] 现价买入比特币成功,委托id: " + str(limitprice['id']), "green")

            if sys.argv[3] == "-s":
                limitprice = HuobiService.sell(1,sys.argv[4].strip(),sys.argv[5].strip(),None,None,SELL)
                if limitprice.has_key('msg'):
                    cprint("[!] 现价卖出比特币失败,"+limitprice['msg'], "red")
                if limitprice.has_key('result') and limitprice['result'] == "success":
                    cprint("[+] 现价卖出比特币成功,委托id: " + str(limitprice['id']), "green")
        if sys.argv[2] == "ltc":
            if sys.argv[3] == "-b":
                limitprice = HuobiService.buy(2,sys.argv[4].strip(),sys.argv[5].strip(),None,None,BUY)
                if limitprice.has_key('msg'):
                    cprint("[!] 现价买入莱特币失败,"+limitprice['msg'], "red")
                if limitprice.has_key('result') and limitprice['result'] == "success":
                    cprint("[+] 现价买入莱特币成功,委托id: " + str(limitprice['id']), "green")

            if sys.argv[3] == "-s":
                limitprice = HuobiService.sell(2,sys.argv[4].strip(),sys.argv[5].strip(),None,None,SELL)
                if limitprice.has_key('msg'):
                    cprint("[!] 现价卖出莱特币失败,"+limitprice['msg'], "red")
                if limitprice.has_key('result') and limitprice['result'] == "success":
                    cprint("[+] 现价卖出莱特币成功,委托id: " + str(limitprice['id']), "green")

    elif sys.argv[1] == "-m":
        if sys.argv[2] == "btc":
            if sys.argv[3] == "-b":
                marketprice = HuobiService.buyMarket(1,sys.argv[4].strip(),None,None,BUY_MARKET)
                if marketprice.has_key('msg'):
                    cprint("[!] 市价买入比特币失败,"+marketprice['msg'], "red")
                if marketprice.has_key('result'):
                    cprint("[+] 市价买入比特币成功,委托id: " + str(marketprice['id']), "green")

            if sys.argv[3] == "-s":
                marketprice = HuobiService.sellMarket(1,sys.argv[4].strip(),None,None,SELL_MARKET)
                if marketprice.has_key('msg'):
                    cprint("[!] 市价卖出比特币失败,"+marketprice['msg'], "red")
                if marketprice.has_key('result'):
                    cprint("[+] 市价卖出比特币成功,委托id: " + str(marketprice['id']), "green")

        if sys.argv[2] == "ltc":
            if sys.argv[3] == "-b":
                marketprice = HuobiService.buyMarket(2,sys.argv[4].strip(),None,None,BUY_MARKET)
                if marketprice.has_key('msg'):
                    cprint("[!] 市价买入莱特币失败,"+marketprice['msg'], "red")
                if marketprice.has_key('result'):
                    cprint("[+] 市价买入莱特币成功,委托id: " + str(marketprice['id']), "green")

            if sys.argv[3] == "-s":
                marketprice = HuobiService.sellMarket(2,sys.argv[4].strip(),None,None,SELL_MARKET)
                if marketprice.has_key('msg'):
                    cprint("[!] 市价卖出莱特币失败,"+marketprice['msg'], "red")
                if marketprice.has_key('result'):
                    cprint("[+] 市价卖出莱特币成功,委托id: " + str(marketprice['id']), "green")
    else:
        pass

