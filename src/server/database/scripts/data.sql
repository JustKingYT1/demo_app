 INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (0, "Guest", 0);
 INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (1, "User", 1);
 INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (2, "Manager", 2);
 INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (3, "Admin", 3);

 INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (1, 0, "Pismenskiy V. S.", "89377028077", "2004-02-07");
 INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (2, 1, "Pismenskciy V. S.", "89377028277", "2004-01-07");
 INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (3, 2, "Pismefnskiy V. S.", "89377028377", "2004-03-07");
 INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (4, 3, "Pismefdfdnskiy V. S.", "89377048377", "2004-06-07");

 INSERT INTO Products(ID, title, cost) VALUES (1, "Apple", 35);
 INSERT INTO Products(ID, title, cost) VALUES (2, "Pen", 12);
 INSERT INTO Products(ID, title, cost) VALUES (3, "Pencil", 4);

 INSERT INTO Products(ID, title, cost) VALUES (4, "Grape", 15);
 INSERT INTO Products(ID, title, cost) VALUES (5, "Book", 120);
 INSERT INTO Products(ID, title, cost) VALUES (6, "Note", 45);

 INSERT INTO Warehouses(name, locationID, phone) VALUES ('One', 1, '89377028077');
 INSERT INTO Warehouses(name, locationID, phone) VALUES ('Two', 2, '89377038077');
 INSERT INTO Warehouses(name, locationID, phone) VALUES ('Three', 3, '89377048077');

INSERT INTO Orders(ID, accountID, trackNumber, totalCost) VALUES (4, 1, '125-4-33456', 25000);
INSERT INTO Orders(ID, accountID, trackNumber, totalCost) VALUES (5, 65, '5-765-33457', 35000);
INSERT INTO Orders(ID, accountID, trackNumber, totalCost) VALUES (6, 3, '125-765-8', 2000);