-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2021 at 06:30 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `movies_list`
--

CREATE TABLE `movies_list` (
  `m_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `movie_title` varchar(100) NOT NULL,
  `year_released` varchar(50) NOT NULL,
  `actors` varchar(200) NOT NULL,
  `awards` varchar(200) NOT NULL,
  `box_office` varchar(100) NOT NULL,
  `country` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movies_list`
--

INSERT INTO `movies_list` (`m_id`, `user_id`, `movie_title`, `year_released`, `actors`, `awards`, `box_office`, `country`) VALUES
(13, 4, 'Intruder', '1989', 'Elizabeth Cox, Renée Estevez, Dan Hicks', 'N/A', 'N/A', 'United States'),
(15, 4, 'Kong: Skull Island', '2017', 'Tom Hiddleston, Samuel L. Jackson, Brie Larson', 'Nominated for 1 Oscar. 1 win & 21 nominations total', '$168,052,812', 'United States, China'),
(16, 11, 'Black Widow', '2021', 'Scarlett Johansson, Florence Pugh, David Harbour', 'N/A', '$179,377,043', 'United States'),
(17, 10, 'Mulan', '1998', 'Ming-Na Wen, Eddie Murphy, BD Wong', 'Nominated for 1 Oscar. 17 wins & 21 nominations total', '$120,620,254', 'United States, China'),
(18, 10, 'The Witches', '1990', 'Anjelica Huston, Mai Zetterling, Jasen Fisher', '3 wins & 8 nominations total', '$10,360,553', 'United Kingdom, United States'),
(19, 11, 'Titanic', '1997', 'Leonardo DiCaprio, Kate Winslet, Billy Zane', 'Won 11 Oscars. 125 wins & 83 nominations total', '$659,363,944', 'United States, Mexico, Australia'),
(20, 12, 'Scream', '1996', 'Neve Campbell, Courteney Cox, David Arquette', '11 wins & 11 nominations', '$103,046,663', 'United States');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `u_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`u_id`, `username`, `password`) VALUES
(4, 'Sameer123', '1234'),
(10, 'sam123', '12345'),
(11, 'arfan123', '12345'),
(12, 'Ifty123', 'ifty1234');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `movies_list`
--
ALTER TABLE `movies_list`
  ADD PRIMARY KEY (`m_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`u_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `movies_list`
--
ALTER TABLE `movies_list`
  MODIFY `m_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `movies_list`
--
ALTER TABLE `movies_list`
  ADD CONSTRAINT `movies_list_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`u_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
