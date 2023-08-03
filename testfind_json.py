# python find data in json

import json   
e = "台南"
f = u"我"
g = e.encode('unicode_escape')
uni_city_name = e.encode('unicode_escape').decode('utf-8')




with open("./search.json") as all_script:
        script = json.load(all_script)
        # print(data)

        data = script['search']['areaData']['zh-tw']['continents']
        id = data[0]['countries'][0]['cities'][24]['id']
        name = data[0]['countries'][0]['cities'][24]['name']
        N = len(data) #計算有多少洲:8
        # print(data)
        print(id,name)
        print(N)
        cityList =[]
        # 將每個城市的id and name 抓出來
        for i in range(0,N-1):
            countries = data[i]['countries']
            J = len(countries) # 計算每一洲(區域)有幾個國家:27
            # print("J :",J)
            for j in range(0,J-1):
              cities = countries[j]['cities']
              K = len(cities) # 計算每個國家的城市有幾個
              # print("K:",K)
              for k in range(0,K-1):
               id = data[i]['countries'][j]['cities'][k]['id']
               name = data[i]['countries'][j]['cities'][k]['name']

               if e == name:
                 print(i,j,k)
                 print(id)
               
              
               cityList.append([id,name])

        # print(cityList)

        # 如果城市名 等於 cityList當中的城市，可以得知其城市的 i,j,k
        #返回 id 給網址

                 

        print(uni_city_name)
        #判斷cityname
        if uni_city_name in data:
          print(uni_city_name)
          print("ok")


        