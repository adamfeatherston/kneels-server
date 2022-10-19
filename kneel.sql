CREATE TABLE `Metal`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Size`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `size` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Style`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Order`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `timestamp` NUMERIC(15) NOT NULL,
    [metal_id] INTEGER NOT NULL,
    [size_id] INTEGER NOT NULL,
    [style_id] INTEGER NOT NULL,
    FOREIGN KEY (`metal_id`) REFERENCES `Metal`(`id`),
    FOREIGN KEY (`size_id`) REFERENCES `Size`(`id`),
    FOREIGN KEY (`style_id`) REFERENCES `Style`(`id`)
);

INSERT INTO `Metal` VALUES (null, "Sterling Silver", 12.42);
INSERT INTO `Metal` VALUES (null, "14K Gold", 736.4);
INSERT INTO `Metal` VALUES (null, "24K Gold", 1258.9);
INSERT INTO `Metal` VALUES (null, "Platinum", 795.45);
INSERT INTO `Metal` VALUES (null, "Palladium", 1241);

INSERT INTO `Size` VALUES (null, 0.5, 405);
INSERT INTO `Size` VALUES (null, 0.75, 782);
INSERT INTO `Size` VALUES (null, 1, 1470);
INSERT INTO `Size` VALUES (null, 1.5, 1997);
INSERT INTO `Size` VALUES (null, 2, 3638);

INSERT INTO `Style` VALUES (null, "Classic", 500);
INSERT INTO `Style` VALUES (null, "Modern", 710);
INSERT INTO `Style` VALUES (null, "Vintage", 965);

INSERT INTO `Order` VALUES (null, 1614659931693, 3, 2, 3);
INSERT INTO `Order` VALUES (null, 1614659931895, 1, 3, 2);
INSERT INTO `Order` VALUES (null, 1614659931998, 2, 1, 1);

INSERT INTO [Order]
            ( timestamp, metal_id, size_id, style_id )
        VALUES
            ( 12345678910, 1, 2, 3 );