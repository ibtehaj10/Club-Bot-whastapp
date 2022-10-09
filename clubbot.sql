-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 09, 2022 at 08:20 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clubbot`
--

-- --------------------------------------------------------

--
-- Table structure for table `club`
--

CREATE TABLE `club` (
  `id` int(11) NOT NULL,
  `number` varchar(13) NOT NULL,
  `name` varchar(100) NOT NULL,
  `seat` int(11) NOT NULL,
  `song` varchar(100) NOT NULL,
  `time` datetime NOT NULL,
  `status` int(11) NOT NULL,
  `ques1` int(11) NOT NULL,
  `ques2` int(11) NOT NULL,
  `alldone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `club`
--

INSERT INTO `club` (`id`, `number`, `name`, `seat`, `song`, `time`, `status`, `ques1`, `ques2`, `alldone`) VALUES
(1, '0313', 'ibtehaj', 4, 'jazba junoon by ali azmat', '2022-10-02 10:02:07', 0, 0, 1, 0),
(3, '0313', 'bilal', 5, 'waka waka', '2022-10-02 10:07:22', 0, 0, 1, 1),
(17, '923237655474', 'Ibtehaj', 7, 'Waka waka by shakira', '2022-10-02 16:20:36', 0, 1, 1, 1),
(18, '923101062596', 'Ibtehaj Khan', 7, 'eminem loose yourself', '2022-10-02 16:38:31', 0, 1, 1, 1),
(19, '923237655474', 'Ibtehaj', 5, 'Gangasta paradise by big e', '2022-10-02 16:39:28', 0, 1, 1, 1),
(20, '923237655474', 'Ibtehaj', 4, 'Mujhe tum nazar se gira to rahe ho by mehdi hasan', '2022-10-02 19:57:02', 0, 1, 1, 1),
(21, '923237655474', 'Ibtehaj', 8, 'Love me like you do remix', '2022-10-02 22:32:26', 0, 1, 1, 1),
(23, '923237655474', 'Ibtehaj', 5, 'Afreen afreen by rfak', '2022-10-02 23:04:21', 0, 1, 1, 1),
(25, '923213277510', 'Dua Jan M', 5, 'Aaj ki Raat', '2022-10-02 23:10:37', 0, 1, 1, 1),
(27, '923101062596', 'Ibtehaj Khan', 8, 'waka waka by shakira', '2022-10-03 11:33:43', 0, 1, 1, 1),
(28, '923101062596', 'Ibtehaj Khan', 22, 'pasoori', '2022-10-03 11:51:24', 0, 1, 1, 1),
(31, '923213277510', 'Dua Jan M', 0, '', '2022-10-03 22:14:44', 0, 1, 0, 0),
(32, '923237655474', 'Ibtehaj', 5, 'Hhhh by ssss', '2022-10-07 19:25:24', 0, 1, 1, 1),
(33, '923237655474', 'Ibtehaj', 6, 'Ggg', '2022-10-07 19:31:17', 0, 1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `clubbo`
--

CREATE TABLE `clubbo` (
  `id` int(11) NOT NULL,
  `number` varchar(14) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `seat` int(11) DEFAULT NULL,
  `song` varchar(100) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `ques1` int(11) DEFAULT NULL,
  `ques2` int(11) DEFAULT NULL,
  `alldone` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `club`
--
ALTER TABLE `club`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `clubbo`
--
ALTER TABLE `clubbo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `club`
--
ALTER TABLE `club`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `clubbo`
--
ALTER TABLE `clubbo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
