import pandas as pd
from config import df_coord


def load_datasets():
    #Confirmed cases dataset before 2020-05-12
    url_test1="https://www.data.gouv.fr/fr/datasets/r/b4ea7b4b-b7d1-4885-a099-71852291ff20"
    dtype={'dep': str,'clage_covid':str,'nb_test':int,'nb_pos':int}
    df_test1=pd.read_csv(url_test1,sep = ';',dtype=dtype)
    df_test1=df_test1.drop(["nb_test_h","nb_test_f","nb_pos_h","nb_pos_f"],axis=1)
    df_test1=df_test1.drop(df_test1[(df_test1["jour"]<"2020-03-18") | (df_test1["jour"]>"2020-05-12")].index)
    df_test1=df_test1.drop(df_test1[df_test1["clage_covid"] != "0"].index)
    df_test1=df_test1.drop("clage_covid",axis=1)

    #Confirmed cases dataset after 2020-05-12
    url_test2="https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675"
    dtype={'dep': str,'P':int,'T':int,'cl_age':int}
    df_test2=pd.read_csv(url_test2,sep = ';',dtype=dtype)
    df_test2=df_test2.rename(columns={'P':'nb_pos','T':'nb_test'})
    df_test2=df_test2.drop("cl_age90",axis=1)
    df_test2=df_test2.groupby(["dep","jour"]).tail(1)

    #Merge confirmed cases
    df_test = pd.concat([df_test1,df_test2],ignore_index=True)
    df_test['nb_test_cum']=df_test.groupby("dep")['nb_test'].cumsum()
    df_test['nb_pos_cum']=df_test.groupby("dep")['nb_pos'].cumsum()

    #Hospital dataset
    url2="https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7"
    df_hospital = pd.read_csv(url2,sep=';')
    df_hospital = df_hospital.drop(df_hospital[(df_hospital["sexe"]==1) | (df_hospital["sexe"]==2 ) ].index).reset_index(drop=True)
    df_hospital = df_hospital.drop(["sexe"],axis=1)

    #Merge confirmed cases and hospital cases
    df_dep = pd.merge(df_hospital,df_test,on=['dep','jour'])
    df_dep = pd.merge(df_dep,df_coord,on=['dep'])
    df_dep=df_dep.sort_values(['dep','jour'])
    df_dep["scaled"] = df_dep["nb_pos_cum"] ** 0.77
    df_dep['death_rate']=round(df_dep['dc']/df_dep['nb_pos_cum']*100,2)
    df_dep["new_death_rate"]=df_dep.groupby("dep")["death_rate"].apply(lambda row: row-(row.shift(1)))
    df_dep["new_death_rate"].fillna(df_dep["death_rate"], inplace = True) # first date, new_death_rate = death rate
    df_dep["new_dc"]=df_dep.groupby("dep")["dc"].apply(lambda row: row-(row.shift(1)))
    df_dep["new_dc"].fillna(df_dep["dc"], inplace = True) # first date, new_dc = dc

    #France dataset
    df_france=df_dep.groupby("jour").sum().reset_index()
    df_france['death_rate']=round(df_france['dc']/df_france['nb_pos_cum']*100,2)
    df_france['new_death_rate']=df_france.death_rate-df_france.death_rate.shift(1)
    df_france["new_death_rate"].fillna(df_france["death_rate"], inplace = True) # first date, new_death_rate = death rate
    df_france["lat"]=46.40
    df_france["long"]=0.5
    df_france["zoom"]=3.5
    
    #
    df_last_update=df_dep.groupby("dep").tail(1).reset_index(drop=True)

    all_df={"departments":df_dep,"country":df_france,"last_update":df_last_update}

    return all_df
                
DATAFRAMES=load_datasets()
DF_DEPARTMENTS=DATAFRAMES["departments"]
DF_FRANCE=DATAFRAMES["country"]
DF_LAST_UPDATE=DATAFRAMES["last_update"]