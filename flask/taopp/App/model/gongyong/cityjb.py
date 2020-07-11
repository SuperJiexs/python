import json,pymysql


def run_data():
    with open('city.json','r') as f:
        city_json=json.loads(f.read())
    return city_json

def ins_city(data):

    models=pymysql.Connect(host='localhost',port=3306,user='SuperJie',password='Zxj6593955.0',database='Flask_taopp',charset='utf8')

    cursor=models.cursor()

    city=data.get('returnValue')
    keys=city.keys()
    for k in keys:
        print(k)


        cursor.execute("INSERT INTO let_szm(let_szm) VALUES ('%s');" % k)

        models.commit()

        cursor.execute("SELECT let_szm.id FROM let_szm WHERE let_szm = '%s';" %k)


        let_szm_id=cursor.fetchone()[0]

        print(let_szm_id)

        city_let=city.get(k)
        for let in city_let:
            print(let)
            c_id=let.get('id')
            c_parent_id = let.get('parentId')
            c_name = let.get('regionName')
            c_sitycode = let.get('cityCode')
            c_py = let.get('pinYin')
            cursor.execute("INSERT INTO city_model(let_szm_id, c_id, c_parent_id, c_name, c_sitycode, c_py) VALUES ( %d,%d,%d,'%s',%d,'%s')"%(let_szm_id,c_id,c_parent_id,c_name,c_sitycode,c_py))
            models.commit()

if __name__ == '__main__':
    city_json=run_data()
    ins_city(city_json)