from datetime import datetime
import requests
import json
import mysql.connector
import argparse
import schedule
import logging
from xlwt import Workbook
from models.product import Product
import bootstrap

def get_currency_rate(name_currency):

    try:
        url_template = "http://api.nbp.pl/api/exchangerates/rates/a/"+str(name_currency)
        result = (json.loads(requests.get(url_template).text))["rates"][0]["mid"]

    except BaseException as e:
        print(get_time_now() + " Problem with get_currency_rate function."+ str(e))
        logging.error(get_time_now() + " Problem with get_currency_rate function."+ str(e))

    return(result)

def get_time_now():

    now = datetime.now()
    datetime_now = now.strftime("%d%m%Y %H:%M:%S")

    return(datetime_now)

def update_prices():

    try:
        product = Product()
        product.update_prices("UnitPriceEuro", get_currency_rate("eur"))
        product.update_prices("UnitPriceUSD", get_currency_rate("usd"))
        bootstrap.commit()

        print(get_time_now() + " Prices updated successfully!")
        logging.info(get_time_now() + " Prices updated successfully!")

    except BaseException as e:
        print(get_time_now() + " Problem with update_price function." + str(e))
        logging.error(get_time_now() + " Problem with update_price function." + str(e))

def generate_report():

    try:
        product = Product()
        myresult = product.get_inf_report()

        wb = Workbook()
        headers = ["ProductID", "DepartmentID", "Category", "IDSKU", "ProductName", "Quantity", "UnitPrice",
                   "UnitPriceUSD", "UnitPriceEuro", "Ranking", "ProductDesc", "UnitsInStock", "UnitsInOrder"]

        sheet1 = wb.add_sheet("Report")
        for i in range(len(headers)):
            sheet1.write(0, i, headers[i])

        counter = 0
        for x in myresult:
            counter += 1
            for i in range(len(headers)):
                sheet1.write(counter, i, x[i])

        now = datetime.now()
        datetime_now = now.strftime("%d%m%Y_%H%M%S")
        wb.save("report_"+str(datetime_now)+".xls")

        print(get_time_now() + " Report generated successfully!")
        logging.info(get_time_now() + " Report generated successfully!")

    except BaseException as e:
        print(get_time_now() + " Problem with generate_report function." + str(e))
        logging.error(get_time_now() + " Problem with generate_report function." + str(e))

def main():
    logging.basicConfig(filename="logfile.log", level=logging.INFO)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-upd", "--updateprice", nargs='?', help="update_unit_price", const="")
    parser.add_argument("-gen", "--generatereport", nargs='?', help="generate_product_report", const="")
    args = parser.parse_args()

    if args.updateprice == '':
        update_prices()

    elif args.updateprice != None:
        schedule.every().day.at(args.updateprice).do(update_prices)
        while True:
            schedule.run_pending()

    if args.generatereport != None:
        generate_report()

if __name__ == "__main__":
    bootstrap.init()
    main()
    bootstrap.close()