DROP TABLE IF EXISTS `booking`;
DROP TABLE IF EXISTS `room`;
DROP TABLE IF EXISTS `worker`;


CREATE TABLE `booking` (
    `id` INTEGER PRIMARY KEY NOT NULL ,
    `worker` int(11) NOT NULL,
    `room` int(11) NOT NULL,
    `date` int(11) NOT NULL,
    `time` int(11) NOT NULL
);

CREATE TABLE `room` (
    `id` INTEGER PRIMARY KEY NOT NULL,
    `name` varchar(10) NOT NULL
);



INSERT INTO `room` (`id`, `name`) VALUES
(0, 'EG_0_1'),
(1, 'EG_0_2'),
(2, 'OG_1_1'),
(3, 'OG_1_2'),
(4, 'OG_2_1');



CREATE TABLE `worker` (
    `id` INTEGER PRIMARY KEY NOT NULL,
    `firstname` varchar(50) NOT NULL,
    `lastname` varchar(50) NOT NULL
);



INSERT INTO `worker` (`id`, `firstname`, `lastname`) VALUES
(0, 'Jonas', 'Johannsons von Johannisgrams');
