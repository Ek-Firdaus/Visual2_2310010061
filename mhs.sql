-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 15, 2025 at 06:41 PM
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
('220001', 'Ahmad Rizky Ramadhan', 'Rizky', '081234567890', 'rizky.ahmad@email.com', 'TI-1A', 'Pemrograman Dasar', 'Kampus A'),
('220002', 'Siti Nurhaliza', 'Siti', '082345678901', 'siti.nurhaliza@email.com', 'TI-1B', 'Sistem Operasi', 'Kampus B'),
('220003', 'Dewi Anggraini', 'Dewi', '083456789012', 'dewi.anggraini@email.com', 'TI-1A', 'Jaringan Komputer', 'Kampus A'),
('220004', 'Budi Santoso', 'Budi', '084567890123', 'budi.santoso@email.com', 'TI-1C', 'Struktur Data', 'Kampus C'),
('220005', 'Fitri Handayani', 'Fitri', '085678901234', 'fitri.handayani@email.com', 'TI-1B', 'Basis Data', 'Kampus A'),
('220006', 'Fajar Nugroho', 'Fajar', '086789012345', 'fajar.nugroho@email.com', 'TI-1A', 'Pemrograman Web', 'Kampus A'),
('220007', 'Lestari Wulandari', 'Tari', '087890123456', 'lestari.w@email.com', 'TI-1C', 'Desain UI/UX', 'Kampus B'),
('220008', 'Agus Wijaya', 'Agus', '088901234567', 'agus.wijaya@email.com', 'TI-1A', 'Jaringan Komputer', 'Kampus A'),
('220009', 'Dian Puspita', 'Dian', '089012345678', 'dian.puspita@email.com', 'TI-1B', 'Pemrograman Dasar', 'Kampus B'),
('220010', 'Hendra Gunawan', 'Hendra', '081223344556', 'hendra.gunawan@email.com', 'TI-1C', 'Basis Data', 'Kampus C');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mhs`
--
ALTER TABLE `mhs`
  ADD PRIMARY KEY (`npm`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
