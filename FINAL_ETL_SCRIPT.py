# coding: utf-8

#Import dependencies
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import pymysql 
pymysql.install_as_MySQLdb()

#Import CSV file and read with Pandas
Concursos_df = pd.read_csv("Concursos.csv", encoding="ISO-8859-1")

#Manipulate data frame to obtain desired tables
Concursos_df = Concursos_df.drop(['Semestre', 'RAMO', 'ID_UR','UR', 'PUESTO', 'FOLIO_CONCURSO', 'FECHA_PUBLICACION',                                 'MES_PUBLICACION','AÑO_PUBLICACION','FECHA_RESOLUCION'], axis=1)
Concursos_df = Concursos_df.drop(Concursos_df.columns[7], axis=1)

#Add a column containing the total of applications received
Concursos_df['SOLICITUDES_TOTAL'] = Concursos_df['SOLICITUDES_ACEPTADAS'] + Concursos_df['SOLICITUDES_RECHAZADAS']

#Create table_1 using information from Concursos_df
table_1 = pd.pivot_table(Concursos_df,index=["Ejercicio","ID_RAMO", 'NIVEL_SALARIAL','ESTATUS'],                         values=['SOLICITUDES_TOTAL',"SOLICITUDES_ACEPTADAS"],aggfunc=np.sum)
table_1['%_ACEPTACION'] = (table_1['SOLICITUDES_ACEPTADAS'] / table_1['SOLICITUDES_TOTAL'])*100
table_1 = table_1.drop(['SOLICITUDES_ACEPTADAS'], axis = 1)

#Rename columns and indexes
table_1 = table_1.rename(columns={'SOLICITUDES_TOTAL': 'solicitudes_total', '%_ACEPTACION':'porcentaje_aceptacion'})

table_1.index.names = ['ejercicio', 'id_ramo', 'nivel_salarial', 'estatus']

#Save table with the name used in MySQL
job_applications = table_1

#Create table_2 using information from Concursos_df
table_2 = Concursos_df.drop(["ESTATUS", "SOLICITUDES_ACEPTADAS", "SOLICITUDES_RECHAZADAS", "SOLICITUDES_TOTAL"], axis = 1)

table_2['REMUNERACION_BRUTA'] = table_2['REMUNERACION_BRUTA'].str.replace(',','')

table_2['REMUNERACION_BRUTA'] = table_2['REMUNERACION_BRUTA'].apply(pd.to_numeric, errors='coerce')

table_2 = pd.pivot_table(table_2,index=["Ejercicio","ID_RAMO", 'NIVEL_SALARIAL'],                         values=['REMUNERACION_BRUTA'],aggfunc=np.mean)

#Rename columns and indexes
table_2 = table_2.rename(columns={'REMUNERACION_BRUTA': 'remuneracion_bruta'})
table_2.index.names = ['ejercicio', 'id_ramo', 'nivel_salarial']

#Save table with the name used in MySQL
salaries = table_2

#Upload data from Auditorias.csv
auditorias_df = pd.read_csv('Auditorias.csv', encoding='iso-8859-1')

#Manipulate data to create table_3
auditorias_df_ext = auditorias_df[['RAMO', 'EJERCICIO', 'AUDITORÍAS_REALIZADAS', 'OBSERVACIONES_DETERMINADAS']].copy()
table_3 = auditorias_df_ext.groupby(['RAMO', 'EJERCICIO']).sum()
table_3 = table_3.rename(columns={'AUDITORÍAS_REALIZADAS':'AUDITORIAS', 'OBSERVACIONES_DETERMINADAS':'SANCIONES'})
table_3['AUD/SUM'] = table_3['AUDITORIAS'] / table_3['SANCIONES']

#Rename columns and indexes
table_3 = table_3.rename(columns={'AUDITORIAS': 'auditorias', 'SANCIONES':'sanciones', 'AUD/SUM': 'aud/sum'})
table_3.index.names = ['id_ramo', 'ejercicio']

#Save table with the name used in MySQL
auditorias_sanciones = table_3

#Upload data from ECCO.csv
ecco_df = pd.read_csv('ECCO.csv', encoding='iso-8859-1')

#Manipulate data to create table_4
ecco_df_extract = ecco_df[['RAMO', 'AÑO', 'INDICE DE SATISFACCIÓN LABORAL']].copy()
table_4 = ecco_df_extract.groupby(['RAMO', 'AÑO']).mean()
table_4 = ecco_df_extract.rename(columns={'INDICE DE SATISFACCIÓN LABORAL':'PROMEDIO ECCO'})

#Rename columns 
table_4 = table_4.rename(columns={'RAMO': 'id_ramo', 'AÑO':'anio', 'PROMEDIO ECCO' : 'promedio_ecco'})

#Save table with the name used in MySQL
mean_satisfaction = table_4

#Create table_5 using data from ecco_df
table_5 = ecco_df[['RAMO', 'RAMO DESCRIPCION']].copy()
table_5 = table_5.drop_duplicates()

#Rename columns
table_5 = table_5.rename(columns={'RAMO': 'id_ramo', 'RAMO DESCRIPCION':'ramo_descripcion'})

#Save table with the name used in MySQL
ramo_description = table_5

password = input("Enter MySQL password: ")
engine = create_engine(f"mysql://root:{password}@localhost/icecream_db")

job_applications.to_sql(job_applications, engine)    
salaries.to_sql(salaries, engine)    
mean_satisfaction.to_sql(mean_satisfaction, engine)    
auditorias_sanciones.to_sql(auditorias_sanciones, engine)    
ramo_description.to_sql(ramo_description, engine)    
