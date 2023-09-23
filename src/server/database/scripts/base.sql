CREATE TABLE Countries
(
    ID INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Regions
(
    ID INT NOT NULL PRIMARY KEY,
    countryID INT NOT NULL,
    name VARCHAR(50) NOT NULL UNIQUE,
    FOREIGN KEY (countryID) 
        REFERENCES Countries(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE Locations
(
    ID INT NOT NULL PRIMARY KEY,
    regionID INT NOT NULL,
    locale VARCHAR(100) NOT NULL UNIQUE,
    coordinates VARCHAR(40) NOT NULL UNIQUE,
    FOREIGN KEY (regionID) 
        REFERENCES Regions(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE Structures
(
    ID INT NOT NULL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Facilities
(
    ID INT NOT NULL PRIMARY KEY,
    structureID INT NOT NULL,
    locationID INT NOT NULL UNIQUE,
    phone VARCHAR(18) NOT NULL UNIQUE,
    FOREIGN KEY (structureID) 
        REFERENCES Structures(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (locationID) 
        REFERENCES Locations(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE TypesOfUsers
(
    ID INT NOT NULL PRIMARY KEY,
    type VARCHAR(35) NOT NULL UNIQUE,
    accessLevel INT NOT NULL
);

CREATE TABLE Users
(
    ID INT NOT NULL PRIMARY KEY,
    typeID INT NOT NULL,
    FIO VARCHAR(50) NOT NULL,
    phone VARCHAR(18) NOT NULL UNIQUE,
    dateBirth DATE NOT NULL,
    FOREIGN KEY (typeID)
        REFERENCES TypesOfUsers(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE Accounts
(
    ID INT NOT NULL PRIMARY KEY,
    userID INT NOT NULL UNIQUE,
    login VARCHAR(25) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    FOREIGN KEY (userID)
        REFERENCES Users(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE Orders
(
    ID INT NOT NULL PRIMARY KEY,
    accountID INT NOT NULL,
    trackNumber VARCHAR(15) NOT NULL UNIQUE,
    totalCost INT NOT NULL,
    completed BOOLEAN NOT NULL,
    FOREIGN KEY (accountID)
        REFERENCES Accounts(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE Product
(
    ID INT NOT NULL PRIMARY KEY,
    title VARCHAR(50) UNIQUE NOT NULL,
    cost INT NOT NULL
);

CREATE TABLE ListOfProducts
(
    ID INT NOT NULL PRIMARY KEY,
    orderID INT NOT NULL,
    productID INT NOT NULL,
    count INT NOT NULL,
    FOREIGN KEY (orderID) 
        REFERENCES Orders(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (productID)
        REFERENCES Products(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE RemnantsOfProducts
(
    ID INT NOT NULL PRIMARY KEY,
    warehouseID INT NOT NULL,
    productID INT NOT NULL,
    count INT NOT NULL,
    FOREIGN KEY (warehouseID)
        REFERENCES Facilities(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (productID)
        REFERENCES Products(ID)
        ON DELETE CASCADE ON UPDATE NO ACTION
);

INSERT INTO Countries(ID, name) VALUES (1, 'Россия');
INSERT INTO Countries(ID, name) VALUES (2, 'Америка');
INSERT INTO Countries(ID, name) VALUES (3, 'Франция');
INSERT INTO Countries(ID, name) VALUES (4, 'Германия');

INSERT INTO Regions(ID, countryID, name) VALUES (1, 1, 'Город Москва');
INSERT INTO Regions(ID, countryID, name) VALUES (2, 2, 'Северо-восток');
INSERT INTO Regions(ID, countryID, name) VALUES (3, 3, 'Аквитания');
INSERT INTO Regions(ID, countryID, name) VALUES (4, 4, 'Бавария');

INSERT INTO Locations(ID, regionID, locale, coordinates) VALUES (1, 1, 'Красная площадь', 'Широта: -71.36980, долгота: 110.98373');
INSERT INTO Locations(ID, regionID, locale, coordinates) VALUES (2, 2, 'Статуя свободы', 'Широта: 58.00203, долгота: -47.57092');
INSERT INTO Locations(ID, regionID, locale, coordinates) VALUES (3, 3, 'Эйфелева башня', 'Широта: 53.06230, долгота: -5.78470');
INSERT INTO Locations(ID, regionID, locale, coordinates) VALUES (4, 4, 'Нойшванштайн', 'Широта: 1.70418, долгота: -61.87414');

INSERT INTO Structures(ID, name) VALUES (1, 'Склад');
INSERT INTO Structures(ID, name) VALUES (2, 'Филиал');

INSERT INTO Facilities(ID, structureID, locationID, phone) VALUES (1, 1, 1, '79564367244');
INSERT INTO Facilities(ID, structureID, locationID, phone) VALUES (2, 1, 3, '79556367269');
INSERT INTO Facilities(ID, structureID, locationID, phone) VALUES (3, 2, 4, '79454363962');

INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (1, 'Guest', 0);
INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (2, 'User', 1);
INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (3, 'Manager', 2);
INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (4, 'Admin', 3);

INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (1, 1, 'Зайкин Иван Иванович', '794541253', '2004.01.07');
INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (2, 2, 'Степанов Антон Александрович', '7954754732', '2002.12.05');
INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (3, 3, 'Коломин Никита Вячеславович', '7976937665', '2003.25.02');
INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (4, 4, 'Гордеев Вадим Сергеевич', '7956824355', '2001.08.11');

INSERT INTO Products(ID, title, cost) VALUES (1, 'Карандаш', 15);
INSERT INTO Products(ID, title, cost) VALUES (2, 'Ручка', 25);
INSERT INTO Products(ID, title, cost) VALUES (3, 'Линейка', 45);
INSERT INTO Products(ID, title, cost) VALUES (4, 'Ластик', 23);

