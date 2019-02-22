DROP DATABASE IF EXISTS public_jobs_db;
CREATE DATABASE public_jobs_db;
USE public_jobs_db;

/*table_1 in Concursos_ET_Process.ipynb*/
DROP TABLE IF EXISTS job_applications;
CREATE TABLE job_applications(
    ejercicio INT,
    id_ramo INT,
    nivel_salarial VARCHAR,
    estatus VARCHAR,
    solicitudes_total INT,
    porcentaje_aceptacion FLOAT
);

/*table_2 in Concursos_ET_Process.ipynb*/
DROP TABLE IF EXISTS salaries;
CREATE TABLE salaries(
    ejercicio INT,
    id_ramo INT,
    nivel_salarial VARCHAR,
    remuneracion_bruta FLOAT
);

/*mean_satisfaction in ECCO_PROM_TABLA.ipynb*/
DROP TABLE IF EXISTS mean_satisfaction;
CREATE TABLE mean_satisfaction(
    id_ramo INT,
    anyo INT,
    promedio_ecco FLOAT
);

/*auditorias_sanciones in AUDITORIAS-SANCIONES_TABLA.ipynb*/
DROP TABLE IF EXISTS auditorias_sanciones;
CREATE TABLE autitorias_sanciones(
    id_ramo INT,
    ejercicio INT,
    auditorias INT,
    sanciones INT,
    aud_san_ratio FLOAT
);

/*ramo_description in DESCRIPCIONES_TABLA.ipynb*/
DROP TABLE IF EXISTS ramo_description;
CREATE TABLE ramo_description(
    id_ramo INT,
    ramo_descripcion VARCHAR
);






