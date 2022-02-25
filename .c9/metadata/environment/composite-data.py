{"filter":false,"title":"composite-data.py","tooltip":"/composite-data.py","undoManager":{"mark":43,"position":42,"stack":[[{"start":{"row":0,"column":0},"end":{"row":1,"column":19},"action":"insert","lines":["        import csv","        import copy"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":8},"action":"remove","lines":["        "],"id":2}],[{"start":{"row":1,"column":4},"end":{"row":1,"column":8},"action":"remove","lines":["    "],"id":3}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":4},"action":"remove","lines":["    "],"id":4}],[{"start":{"row":1,"column":11},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":12,"column":9},"action":"insert","lines":["        myVehicle = {","          \"vin\" : \"<empty>\",","          \"make\" : \"<empty>\" ,","          \"model\" : \"<empty>\" ,","          \"year\" : 0,","          \"range\" : 0,","          \"topSpeed\" : 0,","          \"zeroSixty\" : 0.0,","          \"mileage\" : 0","        }"],"id":6}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":8},"action":"remove","lines":["    "],"id":9},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":11}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":12}],[{"start":{"row":5,"column":4},"end":{"row":5,"column":8},"action":"remove","lines":["    "],"id":14},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":8},"action":"remove","lines":["    "],"id":15},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":8},"action":"remove","lines":["    "],"id":20},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"remove","lines":["    "],"id":21},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"remove","lines":["    "],"id":22},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "],"id":23},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":8},"action":"remove","lines":["    "],"id":24},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":25},{"start":{"row":11,"column":15},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":19},"end":{"row":13,"column":0},"action":"insert","lines":["","    ",""],"id":26}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":27},{"start":{"row":11,"column":19},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":12,"column":1},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":28},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":44},"action":"insert","lines":["        for key, value in myVehicle.items():","          print(\"{} : {}\".format(key,value))"],"id":29}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":8},"action":"remove","lines":["    "],"id":30},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"remove","lines":["    "],"id":31},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"remove","lines":[" "],"id":32},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "],"id":33}],[{"start":{"row":15,"column":38},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":17,"column":0},"action":"insert","lines":["",""]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":35}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":21},"action":"insert","lines":["myInventoryList = [ ]"],"id":36}],[{"start":{"row":17,"column":21},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":37}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":38}],[{"start":{"row":19,"column":0},"end":{"row":39,"column":46},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:  ","      csvReader = csv.reader(csvFile, delimiter=',')  ","      lineCount = 0  ","      for row in csvReader:  ","        if lineCount == 0:  ","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","      print(f'Processed {lineCount} lines.')  "],"id":39}],[{"start":{"row":25,"column":28},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":40},{"start":{"row":26,"column":0},"end":{"row":26,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["#"],"id":42}],[{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"insert","lines":["#"],"id":43}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["#"],"id":44}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":15},"action":"remove","lines":["lineCount"],"id":45},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["l"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["i"]},{"start":{"row":21,"column":8},"end":{"row":21,"column":9},"action":"insert","lines":["n"]}],[{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["#"],"id":46}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":9},"action":"remove","lines":["lin"],"id":47},{"start":{"row":21,"column":6},"end":{"row":21,"column":7},"action":"insert","lines":["l"]},{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["i"]}],[{"start":{"row":21,"column":6},"end":{"row":21,"column":8},"action":"remove","lines":["li"],"id":48},{"start":{"row":21,"column":6},"end":{"row":21,"column":15},"action":"insert","lines":["lineCount"]}],[{"start":{"row":23,"column":8},"end":{"row":23,"column":9},"action":"remove","lines":["#"],"id":49}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"remove","lines":["#"],"id":50}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"remove","lines":["#"],"id":51}],[{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"remove","lines":["#"],"id":52}],[{"start":{"row":28,"column":18},"end":{"row":28,"column":19},"action":"remove","lines":["f"],"id":55}]]},"ace":{"folds":[],"scrolltop":136.58571289062508,"scrollleft":0,"selection":{"start":{"row":40,"column":46},"end":{"row":40,"column":46},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":8,"state":"start","mode":"ace/mode/python"}},"timestamp":1645691414501,"hash":"134d8135d80c43edca90b1ec518da99ac102a52b"}