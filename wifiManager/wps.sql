-- phpMyAdmin SQL Dump
-- version phpStudy 2014
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2019 年 04 月 12 日 03:25
-- 服务器版本: 5.5.53
-- PHP 版本: 5.4.45

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `wps`
--

-- --------------------------------------------------------

--
-- 表的结构 `wifi`
--

CREATE TABLE IF NOT EXISTS `wifi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mac` varchar(100) DEFAULT NULL,
  `router` varchar(100) DEFAULT NULL,
  `routerPwd` varchar(100) DEFAULT NULL,
  `pin` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `ssid` varchar(100) DEFAULT NULL,
  `remarks` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=25 ;

--
-- 转存表中的数据 `wifi`
--

INSERT INTO `wifi` (`id`, `mac`, `router`, `routerPwd`, `pin`, `pwd`, `ssid`, `remarks`) VALUES
(1, '0', '0', '0', '0', '0', '0', '0'),
(2, '0', '0', '0', '0', '0', '0', '0');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
