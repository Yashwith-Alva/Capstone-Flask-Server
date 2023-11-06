-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 19, 2023 at 11:12 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `arfoodmenu`
--

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `menuId` int(11) NOT NULL,
  `rid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `menu_items`
--

CREATE TABLE `menu_items` (
  `menuId` int(11) NOT NULL,
  `itemId` int(11) NOT NULL,
  `itemName` varchar(50) NOT NULL,
  `category` varchar(15) DEFAULT NULL,
  `nutrituionId` int(11) DEFAULT NULL,
  `ingredient_info` text DEFAULT NULL,
  `dish_model` varchar(510) DEFAULT NULL,
  `verified` enum('verified','inprogress','rejected') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `nutrition`
--

CREATE TABLE `nutrition` (
  `nutrituionId` int(11) NOT NULL,
  `Energy` int(11) DEFAULT NULL,
  `Protein` int(11) DEFAULT NULL,
  `Carbohydrate` int(11) DEFAULT NULL,
  `Fat` int(11) DEFAULT NULL,
  `Veg` enum('VEG','NON-VEG') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `restaurant`
--

CREATE TABLE `restaurant` (
  `rid` int(11) NOT NULL,
  `resName` varchar(255) NOT NULL,
  `about` text DEFAULT NULL,
  `qr` varchar(510) DEFAULT NULL,
  `address` text NOT NULL,
  `locationLink` varchar(510) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `restaurant`
--

INSERT INTO `restaurant` (`rid`, `resName`, `about`, `qr`, `address`, `locationLink`) VALUES
(1, 'abc', 'a test restaurant', NULL, 'bangalore', 'https://goo.gl/maps/sv6b9JfdKQUyXbuX7');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `usrId` char(10) NOT NULL,
  `usrpassword` char(8) NOT NULL,
  `rid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`usrId`, `usrpassword`, `rid`) VALUES
('abc100', 'pass', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`menuId`),
  ADD KEY `rid` (`rid`);

--
-- Indexes for table `menu_items`
--
ALTER TABLE `menu_items`
  ADD PRIMARY KEY (`itemId`),
  ADD KEY `menuId` (`menuId`),
  ADD KEY `nutrituionId` (`nutrituionId`);

--
-- Indexes for table `nutrition`
--
ALTER TABLE `nutrition`
  ADD PRIMARY KEY (`nutrituionId`);

--
-- Indexes for table `restaurant`
--
ALTER TABLE `restaurant`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`usrId`),
  ADD KEY `rid` (`rid`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `menu`
--
ALTER TABLE `menu`
  ADD CONSTRAINT `menu_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `restaurant` (`rid`);

--
-- Constraints for table `menu_items`
--
ALTER TABLE `menu_items`
  ADD CONSTRAINT `menu_items_ibfk_1` FOREIGN KEY (`menuId`) REFERENCES `menu` (`menuId`),
  ADD CONSTRAINT `menu_items_ibfk_2` FOREIGN KEY (`nutrituionId`) REFERENCES `nutrition` (`nutrituionId`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `restaurant` (`rid`);
COMMIT;