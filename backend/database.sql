CREATE TABLE horse
(
    id   int         NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE activity
(
    id       int         NOT NULL AUTO_INCREMENT,
    activity varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO activity (activity)
VALUES ('flatwork'),('polework'), ('jumping'), ('hack'), ('lunging'), ('outing'), ('farrier'), ('vet'), ('physiotherapy');

CREATE TABLE plan
(
    id           int NOT NULL AUTO_INCREMENT,
    for_day      date,
    id_horse     int NOT NULL,
    id_activity  varchar(50) DEFAULT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_horse) REFERENCES horse(id) ON DELETE CASCADE,
    CONSTRAINT plan_uq_horse_day UNIQUE(id_horse, for_day)
);
