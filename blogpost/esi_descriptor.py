#モジュールの用意
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

#ログイン用の設定
connection_config = {
    'user': 'postgres',
    'password':  'kuma_aso_3',
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'test.ESI'
}

#データベースへ接続
engine = create_engine('postgresql://{user}:{password}\
@{host}:{port}/{database}'.format(**connection_config))

def Edescriptor():
    xyz = pd.read_csv('esi/smiles.csv')#ここでの位置はファイルのある場所から見た相対位置ではないので注意
    asd=xyz.iloc[:,1]
    smiles=[]
    for i in range(len(asd)):
        B=xyz.iloc[i, 1]
        smiles.append(B)
    data2 = pd.DataFrame()
    for x in range (len(asd)):
        query="select * from blogpost_esi_descriptor_model WHERE smiles="+"'"+smiles[x]+"';"
        data1 = pd.read_sql(sql = query, con=engine )
        data2 = pd.concat([data2, data1], ignore_index=True)
    esi=pd.merge(xyz, data2, on='smiles', how='left')

    esi=esi.drop('id', axis=1)

    esi.to_csv('ESI_to_user/esi_descriptor.csv', index=False)#ここでの位置はファイルのある場所から見た相対位置ではないので注意
    
    return esi

    


