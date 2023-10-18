 INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (0, "Guest", 0);
 INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (1, "User", 1);
 INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (2, "Manager", 2);
 INSERT INTO TypesOfUsers(ID, type, accessLevel) VALUES (3, "Admin", 3);

 INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (65, 0, "Pismenskiy V. S.", "89377028077", "2004-02-07");
 INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (2, 1, "Pismenskciy V. S.", "89377028277", "2004-01-07");
 INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (3, 2, "Pismefnskiy V. S.", "89377028377", "2004-03-07");
 INSERT INTO Users(ID, typeID, FIO, phone, dateBirth) VALUES (635, 3, "Pismefdfdnskiy V. S.", "89377048377", "2004-06-07");

 INSERT INTO Product(ID, title, cost) VALUES (1, "Apple", 35);
 INSERT INTO Product(ID, title, cost) VALUES (2, "Pen", 12);
 INSERT INTO Product(ID, title, cost) VALUES (3, "Pencil", 4);

 INSERT INTO Product(ID, title, cost) VALUES (4, "Grape", 15);
 INSERT INTO Product(ID, title, cost) VALUES (5, "Book", 120);
 INSERT INTO Product(ID, title, cost) VALUES (6, "Note", 45);

INSERT INTO Orders(ID, accountID, trackNumber, totalCost, completed) VALUES (4, 3, '125-4-33456', 25000, FALSE);
INSERT INTO Orders(ID, accountID, trackNumber, totalCost, completed) VALUES (5, 65, '5-765-33457', 35000, FALSE);
INSERT INTO Orders(ID, accountID, trackNumber, totalCost, completed) VALUES (6, 3, '125-765-8', 2000, FALSE);