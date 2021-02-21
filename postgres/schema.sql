CREATE TABLE IF NOT EXISTS public."Datos" (
    id SERIAL PRIMARY KEY,
    concepto VARCHAR(255) NOT NULL,
    dia DATETIME NOT NULL,
    dinero FLOAT NOT NULL,
    idtransaction VARCHAR(3) NOT NULL
);

CREATE TABLE IF NOT EXISTS public."Cuentas" (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    inicial FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS public."Gastos" (
    id SERIAL PRIMARY KEY,
    concepto VARCHAR(255) NOT NULL,
    mes DATETIME NOT NULL
);