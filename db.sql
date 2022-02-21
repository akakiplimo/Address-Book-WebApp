-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Feb 21, 2022 at 11:12 AM

--SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO"; mySQL
--SET time_zone = "+03:00"; mySQL


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: postgresql
--

-- --------------------------------------------------------

--
-- Table structure for table customers
--

CREATE TABLE contacts (
  id serial NOT NULL,
  first_name varchar(255) NOT NULL,
  last_name varchar(255) NOT NULL,
  phone varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  address varchar(255) NOT NULL
);

--
-- Dumping data for table customers
--

INSERT INTO contacts (id, first_name, last_name, phone, email, address) VALUES
(1, 'Abu', 'Kip', '715-455-503', 'ak@gmail.com', '10 Ndalat Rd'),
(2, 'Joy', 'Chem', '100-522-105', 'jc@test.com', '20 Ndovu Rd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table customers
--
ALTER TABLE contacts
  ADD PRIMARY KEY (id);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table customers
--
--ALTER TABLE contacts mySQL
--  MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3; mySQL
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;