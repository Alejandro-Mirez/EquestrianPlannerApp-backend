CREATE TABLE horse
(
    id   int         NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE exercise
(
    id       int         NOT NULL AUTO_INCREMENT,
    exercise varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO exercise (exercise)
VALUES ('flatwork'),('polework'), ('jumping'), ('hack'), ('lunging'), ('outing'), ('day off');

CREATE TABLE treatment
(
    id        int         NOT NULL AUTO_INCREMENT,
    treatment varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO treatment (treatment)
VALUES ('farrier'), ('vet'), ('physiotherapy');

CREATE TABLE plan
(
    id           int NOT NULL AUTO_INCREMENT,
    for_day      date,
    id_horse     int NOT NULL,
    id_exercise  int DEFAULT NULL,
    id_treatment int DEFAULT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_horse) REFERENCES horse(id),
    FOREIGN KEY (id_exercise) REFERENCES exercise(id),
    FOREIGN KEY (id_treatment) REFERENCES treatment(id),
    CONSTRAINT plan_uq_horse_day UNIQUE(id_horse, for_day)
);
