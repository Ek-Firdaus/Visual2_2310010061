-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 20, 2025 at 11:58 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_mahasiswa`
--

-- --------------------------------------------------------

--
-- Table structure for table `mhs`
--

CREATE TABLE `mhs` (
  `npm` varchar(20) NOT NULL,
  `nama_lengkap` varchar(100) DEFAULT NULL,
  `nama_panggilan` varchar(50) DEFAULT NULL,
  `telepon` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `kelas` varchar(50) DEFAULT NULL,
  `matkul` varchar(100) DEFAULT NULL,
  `lokasi_kampus` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mhs`
--

INSERT INTO `mhs` (`npm`, `nama_lengkap`, `nama_panggilan`, `telepon`, `email`, `kelas`, `matkul`, `lokasi_kampus`) VALUES
('0001', 'Eko Setio', 'Eko', '123890', 'eko@gmail.com', 'TI-A', 'Pemrograman Visual 2', 'Kampus A'),
('0002', 'Gina Damayanti', 'Gina', '890567', 'gina@gmail.com', 'TI-B', 'Jaringan Komputer', 'Kampus A'),
('0003', 'Nabil Rahma', 'Nabil', '456123', 'nabil@gmail.com', 'TI-C', 'Pemrograman Berbasis Objek', 'Kampus B'),
('0004', 'Muhammad Zidan', 'Zidan', '654123', 'zidan@gmail.com', 'TI-D', 'Jaringan Komputer', 'Kampus B'),
('0005', 'Sabana Ilham', 'Ilham', '089312', 'ilham@gmail.com', 'TI-E', 'Pemrograman Visual 2', 'Kampus A');

-- --------------------------------------------------------

--
-- Table structure for table `nilai`
--

CREATE TABLE `nilai` (
  `id` int(11) NOT NULL,
  `id_mahasiswa` varchar(20) DEFAULT NULL,
  `nilai_harian` int(11) DEFAULT NULL,
  `nilai_tugas` int(11) DEFAULT NULL,
  `nilai_uts` int(11) DEFAULT NULL,
  `nilai_uas` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nilai`
--

INSERT INTO `nilai` (`id`, `id_mahasiswa`, `nilai_harian`, `nilai_tugas`, `nilai_uts`, `nilai_uas`) VALUES
(10, '0001', 80, 89, 92, 90),
(11, '0002', 89, 80, 87, 88),
(12, '0003', 90, 91, 92, 90),
(13, '0004', 85, 80, 89, 90),
(14, '0005', 90, 92, 90, 94);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mhs`
--
ALTER TABLE `mhs`
  ADD PRIMARY KEY (`npm`);

--
-- Indexes for table `nilai`
--
ALTER TABLE `nilai`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `nilai`
--
ALTER TABLE `nilai`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
