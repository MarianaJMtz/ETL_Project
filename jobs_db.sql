DROP DATABASE IF EXISTS public_jobs_db;

CREATE DATABASE public_jobs_db;

USE public_jobs_db;

/*table_1 in Concursos_ET_Process.ipynb*/
CREATE TABLE job_applications(
    ejercicio INT,
    id_ramo INT,
    nivel_salarial VARCHAR(50),
    estatus VARCHAR(30),
    solicitudes_total INT,
    porcentaje_aceptacion FLOAT
);

/*table_2 in Concursos_ET_Process.ipynb*/
CREATE TABLE salaries(
    ejercicio INT,
    id_ramo INT,
    nivel_salarial VARCHAR(50),
    remuneracion_bruta FLOAT
);

/*mean_satisfaction in ECCO_PROM_TABLA.ipynb*/
CREATE TABLE mean_satisfaccion(
    ramo INT,
    anyo INT,
    promedio_ecco FLOAT
);

/*auditorias_sanciones in AUDITORIAS-SANCIONES_TABLA.ipynb*/
CREATE TABLE autitorias_sanciones(
    ramo INT,
    ejercicio INT,
    auditorias INT,
    sanciones INT,
    aud_san_ratio FLOAT
);

/*ramo_description in DESCRIPCIONES_TABLA.ipynb*/
CREATE TABLE ramo_description(
    ramo INT,
    ramo_descripcion VARCHAR(30)
);






