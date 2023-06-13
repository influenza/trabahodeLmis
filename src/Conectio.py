import mysql.connector
import json as jso
import pandas as pd
def my_connetion():
    cxn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="gabrielben07",
         database="lmis"
        )
    
    if cxn.is_connected():
         print("Conexão estabelecida com sucesso!")
         cursor = cxn.cursor()
         cursor.execute(f"INSERT INTO `lmis`.`numeros` (`lfjkals`) VALUES ('a');")
         cursor.execute(f"select Max(Numero) from lmis.numeros order by Numero;")
         resultados = cursor.fetchall()
         print(resultados)
         cursor.close()
    cxn.commit()
    cxn.close()
    return resultados

def json_to_data_arr(number):
     arr=[]
     df = pd.read_csv("Spotify_final_dataset.csv")
     json,json2,json3 = df["Position"].to_json(),df["Artist Name"].to_json(),df["Song Name"].to_json()
     data= jso.loads(json)
     data2 = jso.loads(json2)
     data3 = jso.loads(json3)
     for i in range(number):
          datas=[data[f"{i}"],data2[f"{i}"],data3[f"{i}"]]
          arr.append(datas)
     return arr

